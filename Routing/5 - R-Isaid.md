enable
configure terminal

! ============================================================
! ROUTERMEDIFY - Gateway Perimetral Absoluto
! ============================================================
hostname routermedify

no ip domain-lookup

! --- Activación de SSH Seguro ---
crypto key generate rsa general-keys modulus 2048
ip ssh version 2

! --- Limpieza estricta de cualquier configuración previa ---
no access-list 1
no ip nat inside source list 1 interface GigabitEthernet0/0 overload
no router ospf 10
no router ospf 1
no ip access-list extended ACL_WAN_IN
no ip access-list extended ACL_FROM_RISAID

! --- INTERFAZ DE SALIDA: WAN hacia la Universidad (Internet) ---
interface GigabitEthernet0/0
 description WAN hacia Universidad (DHCP)
 ip address dhcp
 ip nat outside
 ip verify unicast source reachable-via rx
 ip access-group ACL_WAN_IN in
 no shutdown
 exit

! --- INTERFAZ DE ENTRADA: Serial Principal hacia MainRouter ---
interface Serial0/0/0
 description WAN hacia MainRouter S0/0/0
 ip address 10.10.1.2 255.255.255.248
 clock rate 128000
 ip nat inside
 no shutdown
 exit

! --- INTERFAZ DE ENTRADA: Serial de Respaldo hacia SecundaryRouter ---
interface Serial0/0/1
 description WAN hacia SecundaryRouter S0/0/1
 ip address 10.10.3.2 255.255.255.248
 clock rate 128000
 ip nat inside
 no shutdown
 exit

! --- TRÁFICO DE SALIDA (PAT): Permisos de traducción unificados ---
access-list 1 permit 10.10.1.0 0.0.0.7
access-list 1 permit 10.10.3.0 0.0.0.7
access-list 1 permit 192.168.0.0 0.0.255.255
access-list 1 permit 172.16.0.0 0.15.255.255
ip nat inside source list 1 interface GigabitEthernet0/0 overload

! --- ENRUTAMIENTO DINÁMICO: OSPF Proceso 1 (Armonizado) ---
router ospf 1
 router-id 5.5.5.5
 network 10.10.1.0 0.0.0.7 area 0
 network 10.10.3.0 0.0.0.7 area 0
 passive-interface GigabitEthernet0/0
 default-information originate
 exit

! --- SEGURIDAD PERIMETRAL: ACL WAN (Filtrado de entrada de Internet) ---
ip access-list extended ACL_WAN_IN
 remark Anti-spoofing: Evita el ingreso de IPs privadas falsificadas como ORIGEN
 deny   ip 10.0.0.0 0.255.255.255 any
 deny   ip 172.16.0.0 0.15.255.255 any
 deny   ip 192.168.0.0 0.0.255.255 any
 deny   ip 127.0.0.0 0.255.255.255 any
 deny   ip 169.254.0.0 0.0.255.255 any
 deny   ip 224.0.0.0 15.255.255.255 any
 remark Trafico legitimo de retorno (Puertos del servidor externo en el ORIGEN)
 permit tcp any any established
 permit udp any eq domain any
 permit udp any eq ntp any
 permit icmp any any echo-reply
 permit icmp any any unreachable
 permit icmp any any time-exceeded
 permit udp any any eq isakmp
 permit udp any any eq non500-isakmp
 deny   ip any any log
 exit

! --- Configuración de Consola y Terminales Virtuales VTY ---
line console 0
 login local
 logging synchronous
 exit

line vty 0 4
 login local
 logging synchronous
 transport input all
 exit

end
write memory
