# Proyecto de Alta Disponibilidad, Seguridad y Monitoreo de Infraestructura

---
## Miembros del equipo
- Romero Hernández Juan José 	 - 0324108222 - [CV](./CVs/Romero_Hernandez_Juan_Jose_English.pdf)
- Aguilar Garcia David Gerardo	 - 0324108223 - [CV](./CVs/Aguilar_Garcia_David_Gerardo_English.pdf)
- Días Benites Jorge Enrique	 - 
- Vargas Juarez Rafael Alejandro - 
- Becerra Garcia Angel Daniel	 - 

---

## 1. Alta disponibilidad por hardware, almacenamiento, DNS, routers y switches

### 1.1 Hardware, almacenamiento y DNS

- Se utilizarán tres servidores físicos para ofrecer alta disponibilidad en las máquinas virtuales o nodos contratados por los usuarios.

- Se utilizarán dos servidores para la alta disponibilidad del almacenamiento, junto con una copia adicional en un proveedor de nube como AWS, Azure u otro similar.

- El almacenamiento contará con redundancia total, replicación y respaldo externo para recuperación ante desastres.

- Se contemplará la configuración de intervalos de respaldo para reducir el riesgo de corrupción de backups ante incidentes como malware o fallos del sistema.

- **Pendiente de revisión:** se evaluará la alta disponibilidad del dominio mediante DNS redundante, certificados SSL y servicios externos de resolución.

### 1.2 Routers y switches

- Se utilizará VRRP para alta disponibilidad entre routers.

- Se utilizará EtherChannel mediante LACP para agrupar enlaces físicos y mejorar la disponibilidad en conexiones críticas.

- **Pendiente de revisión:** se implementarán VLANs adaptadas a la red, por ejemplo:

  - Administración
  - Servicios / Clientes
  - Almacenamiento
  - Seguridad / Monitoreo
  - IoT
  - Otras VLANs según la necesidad del proyecto

- Se integrarán ACLs para controlar la comunicación entre segmentos de red.

- Se implementará NAT/PAT para permitir la conexión con la red.

- Se documentará la topología física y lógica de la red, incluyendo VLANs, enlaces, direccionamiento IP, rutas y reglas aplicadas.

- Se realizarán pruebas de failover para validar la disponibilidad ante fallos de enlaces o dispositivos.

---

## 2. Implementación de Kubernetes como servicio complementario

- **Pendiente de revisión:** se evaluará la implementación de Kubernetes sobre varios nodos para ofrecer despliegue, reinicio automático y balanceo de servicios.

- El almacenamiento utilizado por Kubernetes se integrará con la infraestructura de alta disponibilidad.

> **Nota:** este servicio podrá ofrecerse como un nivel avanzado para usuarios que requieran aplicaciones contenedorizadas.

---

## 3. Firewall, VPN y segmentación de seguridad

- Se utilizará OPNsense o pfSense como firewall principal.

- Se evaluará la implementación de VPN para acceso remoto seguro.

- Se configurarán reglas de filtrado, segmentación por VLANs y control de tráfico entre redes.

- **Pendiente de revisión:** se aplicará hardening básico en servidores y servicios críticos.

---

## 4. Monitoreo de red, rendimiento y seguridad

- Se integrará Netdata para monitoreo de rendimiento en tiempo real.

- Se utilizará Wazuh como SIEM/XDR para centralizar eventos de seguridad.

- Se integrará Suricata como IDS/IPS/NSM para análisis de tráfico, detección de amenazas y generación de alertas.

- Se implementará un dashboard centralizado para visualizar disponibilidad, rendimiento, eventos de seguridad y estado de los servicios.

---

## 5. Alertas y notificaciones

- **Pendiente de revisión:** se configurarán alertas por Telegram o WhatsApp según el nivel del evento.

- Las alertas podrán enviarse al administrador o al usuario final, dependiendo del tipo de servicio contratado.

- Las alertas se clasificarán por prioridad:

  - Informativas
  - Advertencias
  - Críticas

---

## 6. Integración de IoT

- Se implementará control de acceso mediante NFC/RFID para el rack o site.

- Se evaluará la integración de cámaras de videovigilancia.

- Se integrarán sensores de temperatura, humedad y condiciones ambientales.

- Los datos de IoT podrán enviarse al sistema de monitoreo para generar alertas automáticas.

---

## 7. Backups, recuperación y continuidad del servicio

- Se implementarán backups locales y en la nube.

- Se definirán métricas de recuperación como RTO y RPO.

- Se realizarán pruebas periódicas de restauración para validar que los respaldos funcionen correctamente y no se corrompan ante incidentes como malware o fallos del sistema.

- Se documentará un plan básico de recuperación ante desastres.

---

## 8. Documentación, control de cambios y entrega formal

- Se documentarán configuraciones, diagramas, direccionamiento IP, VLANs, reglas de firewall y servicios implementados.

- Se utilizará GitHub para el control de versiones de scripts, configuraciones y documentación técnica.

- Se mantendrá una bitácora de cambios para registrar modificaciones importantes.

> **Nota:** evaluar si la bitácora de cambios se manejará directamente mediante GitHub y su historial de versiones.

- Se preparará documentación formal para presentación, mantenimiento y escalabilidad del proyecto.

---

## 9. Modelo de servicio por niveles

Se ofrecerán diferentes niveles de servicio según las necesidades del usuario.

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
- Kubernetes
- IoT
- Dashboards
- Soporte de recuperación ante amenazas

---

## Recomendaciones

- Definir con claridad qué elementos quedarán como implementación obligatoria y cuáles permanecerán como pendientes de revisión.

- Especificar el alcance real de Kubernetes, ya que para considerarse alta disponibilidad debe ejecutarse sobre varios nodos.

- Definir previamente las VLANs, el direccionamiento IP y las reglas ACL para evitar cambios desordenados durante la implementación.

- Confirmar si se utilizará OPNsense o pfSense como firewall principal para evitar duplicidad en la documentación.

- Investigar y documentar correctamente los conceptos de RTO y RPO antes de definir la estrategia de recuperación.

- Validar si las alertas serán enviadas únicamente a administradores o también a usuarios finales.

- Definir si la bitácora de cambios será un documento separado o si se manejará mediante commits, issues y releases en GitHub.

- Separar claramente el monitoreo de rendimiento, el monitoreo de seguridad y el monitoreo físico mediante IoT para que el proyecto sea más fácil de explicar.

## Diagrama de referencia
![Demo](sources/Diagrama_temporal_1.png)
