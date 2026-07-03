enable
configure terminal

! ============================================================
! ROUTERMEDIFY - Gateway Perimetral
! ============================================================
hostname routermedify

! --- Configuraciones Globales ---
no ip domain-lookup
ip domain-name mixtli.mixtli
username admin_mixtli privilege 15 password admin_mixtli

! --- Criptografia y SSH ---
crypto key generate rsa general-keys modulus 2048
ip ssh version 2

! --- Limpieza de ACL ---
no ip access-list extended ACL_WAN_IN

! --- WAN a la universidad (Recibe DHCP) ---
interface GigabitEthernet0/0
 description WAN hacia Universidad (DHCP)
 ip address dhcp
 ip nat outside
 ip verify unicast source reachable-via rx
 duplex auto
 speed auto
 no shutdown
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

! --- PAT Unificado (Traduccion de red hacia Internet) ---
access-list 1 permit 10.10.1.0 0.0.0.7
access-list 1 permit 10.10.3.0 0.0.0.7
access-list 1 permit 192.168.0.0 0.0.255.255
access-list 1 permit 172.16.0.0 0.15.255.255
ip nat inside source list 1 interface GigabitEthernet0/0 overload

! --- OSPF Proceso 1 ---
router ospf 1
 router-id 5.5.5.5
 network 10.10.1.0 0.0.0.7 area 0
 network 10.10.3.0 0.0.0.7 area 0
 passive-interface GigabitEthernet0/0
 default-information originate
 exit

! --- Consola Limpia ---
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
