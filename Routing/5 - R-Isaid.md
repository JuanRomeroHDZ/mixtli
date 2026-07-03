enable
configure terminal

hostname routermedify
no ip domain-lookup
ip domain-name mixtli.mixtli

! --- Criptografia para SSH ---
crypto key generate rsa general-keys modulus 2048
ip ssh version 2

! --- WAN hacia Universidad (DHCP e Internet) ---
interface GigabitEthernet0/1
 description WAN hacia Universidad (DHCP)
 ip address dhcp
 ip nat outside
 no shutdown
 exit

! --- Interfaz Gigabit0/0 (Apagada/No usada) ---
interface GigabitEthernet0/0
 description No utilizada - Apagada por seguridad
 shutdown
 exit

! --- Serial hacia MainRouter ---
interface Serial0/0/0
 description WAN hacia MainRouter S0/0/0
 ip address 10.10.1.2 255.255.255.248
 clock rate 128000
 ip nat inside
 no shutdown
 exit

! --- Serial hacia SecundaryRouter ---
interface Serial0/0/1
 description WAN hacia SecundaryRouter S0/0/1
 ip address 10.10.3.2 255.255.255.248
 clock rate 128000
 ip nat inside
 no shutdown
 exit

! --- Listas de Acceso y PAT Unificado ---
no access-list 1
access-list 1 permit 10.10.1.0 0.0.0.7
access-list 1 permit 10.10.3.0 0.0.0.7
access-list 1 permit 192.168.0.0 0.0.255.255
access-list 1 permit 172.16.0.0 0.15.255.255
ip nat inside source list 1 interface GigabitEthernet0/1 overload

! --- Proceso de Enrutamiento OSPF ---
router ospf 1
 router-id 5.5.5.5
 network 10.10.1.0 0.0.0.7 area 0
 network 10.10.3.0 0.0.0.7 area 0
 passive-interface GigabitEthernet0/1
 default-information originate
 exit

! --- CONFIGURACIÓN DE USUARIO Y LÍNEAS (AL FINAL) ---
username admin_mixtli privilege 15 password admin_mixtli

line console 0
 login local
 logging synchronous
 exit

line vty 0 15
 login local
 transport input ssh
 exit

end
write memory
