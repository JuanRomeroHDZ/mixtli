# MIXTlI

## Puntos a configurar

	1. Direccionamiento IPv4
	2. Configuración básica de seguridad
	3. VLANs
	4. Troncales y puertos de acceso
	5. Inter-VLAN Routing
	6. DHCP
	7. OSPFv2 single-area
	8. Ruta por defecto e inyección de ruta en OSPF
	9. NAT/PAT para salida a Internet
	10. ACLs
	11. Servidor TACACS+ para gestión mediante SSH
	12. NTP
	13. Syslog o logging básico
	14. Verificación y documentación de evidencias

---

## Tabla de enrutamiento

| Device		| Name		| Interface		| IP			| Submask		| Wildcard		| VLAN		| DHCP		| Note		|
|-----------------------|---------------|-----------------------|-----------------------|-----------------------|-----------------------|---------------|---------------|---------------|
| Router 2901		| MasterRouter	| G0/0			| N/A			| N/A			| N/A			| N/A		| N/A		| Conexión a internet mediante NAT/PAT	|
|			| MasterRouter	| G0/1			| N/A			| N/A			| N/A			| N/A		| N/A		| Encender interfaz	|
| 			| MasterRouter	| G0/1.10		| 192.168.10.250	|			|			|		|		|			|
