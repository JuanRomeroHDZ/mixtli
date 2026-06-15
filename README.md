<p align="center">
  <img src="./Resources/Logo_proyecto_recortado.png" alt="Logo MIXTLI" width="250">
</p>
<h3 align="center">Alta Disponibilidad, Seguridad y Monitoreo de Infraestructura</h3>

---
## Miembros del equipo
- Romero Hernández Juan José     - 0324108222 - [CV](./CVs/Romero_Hernandez_Juan_Jose_English.pdf)
- Aguilar Garcia David Gerardo   - 0324108223 - [CV](./CVs/Aguilar_Garcia_David_Gerardo_English.pdf)
- Díaz Benitez Jorge Enrique     - 0324108243 - [CV](./CVs/Diaz_Benitez_Jorge_Enrique_English.pdf)
- Becerra Garcia Angel Daniel    - 0324108208 - [CV](./CVs/Becerra_Garcia_Angel_Daniel_English.pdf)

---

## 1. Alta disponibilidad por hardware, almacenamiento, routers y switches

### 1.1 Hardware, almacenamiento

- Se utilizarán tres servidores fisicos para ofrecer alta disponibilidad en las máquinas virtuales o nodos contratados por los usuarios

- El almacenamiento contará con redundancia, replicación y respaldo externo para recuperación ante desastres. En este punto se piensa poner un proveedor externo alojado en la nube.

- Se contemplará la configuración de intervalos de tiempo en los respaldos para reducir el riesgo de corrupción de backups ante desastres.

- **Pendiente de mejora:** evaluar la posibilidad de alta disponibilidad en dominios DNS redundantes, certificados SSL.

### 1.2 Routers y switches

- Se configurará OSPF para tener mejor enrutamiento y lograr mejor adaptabilidad en cuanto a errores

- Se implementará VRRP para alta disponibilidad entre los routers 

- Se implementará EtherChannel mediante LACP para agrupar enlaces fisicos y mejorar la disponibilidad en conexiones criticas

- Implementación de ACLs para controlar la comunicación entre segmentos de red

- Se implementará NAT/PAT para tener conexión a internet

- **Pendiente de revisión #1:** VLANs adaptadas a la red

- **Pendiente de revisión #2:** Reglas a aplicar en las ACLs

- **Pendiente de revisión #3:** Documentación de la topología física y logica, incluyendo tablas de direccionamiento, reglas ACL y VLANs.

- **Pendiente de revisión #4:** Resultado de pruebas de failover para realizar tiempos estimados.

---

## 2. Firewall, VPN y segmentación de seguridad

- Se utilizará OPNsense o pfSense como firewall principal

- Se implementará VPN utilizando algún proveedor por cuestiones de IPs publicas, esto será utiilzado para el uso de las VMs contratadas

- **Pendiente de revisión #5:** Aplicar hardening básico a servidores y servicios críticos.

---

## 3. Monitoreo de red, rendimiento y seguridad

- Integraciónn de Wazuh como SIEM/XDR para centralizar eventos de seguridad

- Integración de Suricada como IDS/IPS/NSM para visualizar disponibilidad, rendimiento, eventos de seguridad y estado de los servicios

- **Revisar #1:**  Integrar Netdata para monitorear el rendimiento de la red en tiempo real. (El tema es que no es un servicio para ofrecer)

---

## 4. Alertas y notificaciones

- Las alertas podrán enviarse al administrador o al usuario final, dependiendo del tipo de servicio contratado

- Las alertas se clasificarán por priodidad (Esto puede ser cambiado en proximas revisiones):
	
	- Informativas
	- Advertencias
	- Críticas

- **Pendiente de revisión #6:** Serán enviadas las alertas por Telegram o WhatsApp según el nivel del evento

---

## 5. Integración de IoT

- **Pendiente de revisión #7:** Se implementará control de acceso mediante NFC/RFID para rack o site (Uso exclusivo por el momento)

- **Pendiente de revisión #8:** Se evaluará la posibilidad de integración de cámaras de videovigilancia con detección automatica con IA utilizando iSpy Agent 

- **Pendiente de revisión #9:** Se podrá implementar sensores de temperatura, humedad y condiciones ambientales. 

- **Pendiente de revisión #10:** Los datos recopilados del IoT podrán enviarse al sistema de monitoreo para generar alertas automaticas.

---

## 6. Backups, recuperación y continuidad del servicio

- Se implementarán backups locales y en la nube

- **Pendiente de revisión #11:** Se definirán metricas de recuperación como RTO (Objetivo de Tiempo de Recuperación)  y RPO (Objetivo de Punto de Recuperación). 

- **Pendiente de revisión #12:** Realizar pruebas

- **Pendiente de revisión #13:** Documento formal para tener un plan de recuperación ante desastres (Aunque sea básico)

---

## 7. Documentación, control de cambios y entrega formal

- Se documentarán las configuraciones, diagramas, direcciones IP, VLANs, reglas del firewall y servicios implementados

- Se utilizará GitHub para el control de versiones de scripts, configuraciones y documentación técnica

- Se mantendrá una bitácora de cambios para registrar modificaciones importantes

- Se preparará documentación formal IEEE, donde saldrá información para presentaciones, mantenimiento y posible escalabilidad del proyecto

---

## 8. Modelo de servicio por niveles

Se ofrecerán diferentes niveles de servicio según las necesidades del usuario

### 9.1 Nivel básico

Incluye:

	- Monitoreo
	- Alertas
	- Backups locales

### 9.2 Nivel intermedio

Incluye:
	
	- Firewall
	- VPN
	- SIEM
	- Backups locales y en la nube

### 9.3 Nivel avanzado

Incluye:

	- Alta disponibilidad
	- Dashboards
	- IoT
	- Soporte para recuperación ante amenazas

--- 

## Notas

Evaluar cada **Pendiente de revisión** para un mejor desarrollo de proyecto, los niveles que se asignarán aún estan por definirse, sin embargo lo anteriormente previsto es una base.

## Diagrama de referencia
![Diagrama](Resources/Diagrama_temporal_1.png)
