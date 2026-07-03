enable
configure terminal
hostname SecundaryRouter
no ip domain-lookup
ip domain-name mixtli.mixtli

username admin_mixtli privilege 15 password admin_mixtli

crypto key generate rsa general-keys modulus 2048
ip ssh version 2

interface GigabitEthernet0/0
 description Link directo a MainRouter G0/0
 ip address 10.10.4.2 255.255.255.248
 no shutdown
 exit

interface GigabitEthernet0/1
 description Enlace Trunk a Switch S2
 no shutdown
 exit

interface GigabitEthernet0/1.10
 encapsulation dot1Q 10
 ip address 192.168.1.3 255.255.255.248
 standby 10 ip 192.168.1.1
 standby 10 priority 100
 standby 10 preempt
 exit

interface GigabitEthernet0/1.20
 encapsulation dot1Q 20
 ip address 192.168.20.3 255.255.255.0
 standby 20 ip 192.168.20.1
 standby 20 priority 100
 standby 20 preempt
 exit

interface GigabitEthernet0/1.30
 encapsulation dot1Q 30
 ip address 172.16.0.3 255.255.0.0
 standby 30 ip 172.16.0.1
 standby 30 priority 100
 standby 30 preempt
 exit

interface Serial0/0/0
 description Enlace OSPF hacia MainRouter
 ip address 10.10.2.2 255.255.255.248
 no shutdown
 exit

interface Serial0/0/1
 description Enlace de Respaldo Internet a R-Isaid
 ip address 10.10.3.1 255.255.255.248
 no shutdown
 exit

ip dhcp excluded-address 172.16.0.1 172.16.0.3
ip dhcp pool Public_IP_Pool
 network 172.16.0.0 255.255.0.0
 default-router 172.16.0.1
 exit

router ospf 1
 router-id 2.2.2.2
 network 192.168.1.0 0.0.0.7 area 0
 network 192.168.20.0 0.0.0.255 area 0
 network 172.16.0.0 0.0.255.255 area 0
 network 10.10.2.0 0.0.0.7 area 0
 network 10.10.3.0 0.0.0.7 area 0
 network 10.10.4.0 0.0.0.7 area 0
 exit

ip route 0.0.0.0 0.0.0.0 10.10.3.2
ip route 0.0.0.0 0.0.0.0 10.10.2.1 50

line console 0
 login local
 logging synchronous
 exit
line vty 0 4
 login local
 logging synchronous
 transport input all
 end
write memory