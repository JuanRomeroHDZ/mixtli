from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from proxmoxer import ProxmoxAPI
import urllib3

urllib3.disable_warnings()

PROXMOX_HOST = "ip"
PROXMOX_USER = "root@pam"
PROXMOX_PASS = "password"
PROXMOX_NODE = "node"
TEMPLATE_ID  = #aqui va la vm a clonar cabzeas de rodilla, lo hice rapido para que vieran maso como funciona la clonacion

try:
    px = ProxmoxAPI(
        PROXMOX_HOST,
        user=PROXMOX_USER,
        password=PROXMOX_PASS,
        verify_ssl=False
    )
    print("proxmox conectado")
except Exception as e:
    print(f"error conectando a proxmox: {e}")
    px = None

app = FastAPI(title="mixtli backend api", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class CloneVM(BaseModel):
    nuevo_id: int
    nombre: str
    template_id: int = TEMPLATE_ID

class UpdateSpecs(BaseModel):
    vmid: int
    ram_mb: int
    cores: int

class SnapshotCreate(BaseModel):
    vmid: int
    nombre: str
    descripcion: str = ""

#verificar conexion
def check_proxmox():
    if not px:
        raise HTTPException(status_code=503, detail="si lees esto no vales brg porque no hay conecsion")

#estado del servidor
@app.get("/")
def raiz():
    return {"status": "mixtli backend corriendo", "proxmox": PROXMOX_HOST}

#listar vms
@app.get("/vms")
def listar_vms():
    check_proxmox()
    try:
        vms = px.nodes(PROXMOX_NODE).qemu.get()
        return [
            {
                "vmid":     v["vmid"],
                "nombre":   v["name"],
                "estado":   v["status"],
                "ram_mb":   v.get("maxmem", 0) // 1024 // 1024,
                "cores":    v.get("cpus", 0),
                "disco_gb": round(v.get("maxdisk", 0) / 1024**3, 2)
            }
            for v in vms
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#estado de una vm
@app.get("/vms/{vmid}")
def estado_vm(vmid: int):
    check_proxmox()
    try:
        status = px.nodes(PROXMOX_NODE).qemu(vmid).status.current.get()
        config = px.nodes(PROXMOX_NODE).qemu(vmid).config.get()
        return {
            "vmid":   vmid,
            "nombre": config.get("name"),
            "estado": status.get("status"),
            "ram_mb": config.get("memory"),
            "cores":  config.get("cores"),
            "uptime": status.get("uptime", 0)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#clonar vm
@app.post("/vms/clonar")
def clonar_vm(data: CloneVM):
    check_proxmox()
    try:
        px.nodes(PROXMOX_NODE).qemu(data.template_id).clone.post(
            newid=data.nuevo_id,
            name=data.nombre,
            full=1
        )
        return {"status": "ok", "mensaje": f"vm {data.nuevo_id} clonada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#encender vm
@app.post("/vms/{vmid}/encender")
def encender_vm(vmid: int):
    check_proxmox()
    try:
        px.nodes(PROXMOX_NODE).qemu(vmid).status.start.post()
        return {"status": "ok", "mensaje": f"vm {vmid} encendida"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#apagar vm
@app.post("/vms/{vmid}/apagar")
def apagar_vm(vmid: int):
    check_proxmox()
    try:
        px.nodes(PROXMOX_NODE).qemu(vmid).status.shutdown.post()
        return {"status": "ok", "mensaje": f"vm {vmid} apagandose para mimir"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#reiniciar vm
@app.post("/vms/{vmid}/reiniciar")
def reiniciar_vm(vmid: int):
    check_proxmox()
    try:
        px.nodes(PROXMOX_NODE).qemu(vmid).status.reboot.post()
        return {"status": "ok", "mensaje": f"vm {vmid} reiniciada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#eliminar vm
@app.delete("/vms/{vmid}")
def eliminar_vm(vmid: int):
    check_proxmox()
    try:
        status = px.nodes(PROXMOX_NODE).qemu(vmid).status.current.get()
        if status.get("status") == "running":
            px.nodes(PROXMOX_NODE).qemu(vmid).status.stop.post()
        px.nodes(PROXMOX_NODE).qemu(vmid).delete()
        return {"status": "ok", "mensaje": f"vm {vmid} eliminada como ecuador jaja que geis 2-0"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#actualizar specs
@app.put("/vms/specs")
def actualizar_specs(data: UpdateSpecs):
    check_proxmox()
    try:
        px.nodes(PROXMOX_NODE).qemu(data.vmid).config.post(
            memory=data.ram_mb,
            cores=data.cores
        )
        return {"status": "ok", "mensaje": f"vm {data.vmid} actualizada"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#crear snapshot
@app.post("/vms/snapshot")
def crear_snapshot(data: SnapshotCreate):
    check_proxmox()
    try:
        px.nodes(PROXMOX_NODE).qemu(data.vmid).snapshot.post(
            snapname=data.nombre,
            description=data.descripcion
        )
        return {"status": "ok", "mensaje": f"snapshot '{data.nombre}' creado en vm {data.vmid}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#listar snapshots
@app.get("/vms/{vmid}/snapshots")
def listar_snapshots(vmid: int):
    check_proxmox()
    try:
        snaps = px.nodes(PROXMOX_NODE).qemu(vmid).snapshot.get()
        return [
            {
                "nombre":      s.get("name"),
                "descripcion": s.get("description", ""),
                "fecha":       s.get("snaptime", 0)
            }
            for s in snaps
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#dependencias, instalentas hdlv
#pip install fastapi uvicorn proxmoxer requests --break-system-packages
#uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
