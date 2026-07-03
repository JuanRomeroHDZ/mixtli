interface Serial0/0/0
 description Conexión hacia MainRouter S0/0/0
 ip address 10.10.1.2 255.255.255.248
 clock rate 128000
 ip nat inside
 no shutdown
 exit

interface Serial0/0/1
 description Conexión hacia SecundaryRouter S0/0/1
 ip address 10.10.3.2 255.255.255.248
 clock rate 128000
 ip nat inside
 no shutdown
 exit

interface GigabitEthernet0/0
 description Conexión física al puerto de la Universidad (IP por DHCP)
 ip address dhcp
 ip nat outside
 no shutdown
 exit

access-list 1 permit 192.168.1.0 0.0.0.7
access-list 1 permit 192.168.20.0 0.0.0.255
access-list 1 permit 172.16.0.0 0.0.255.255
access-list 1 permit 10.10.0.0 0.0.255.255

ip nat inside source list 1 interface GigabitEthernet0/0 overload

ip route 192.168.1.0 255.255.255.248 10.10.1.1
ip route 192.168.20.0 255.255.255.0 10.10.1.1
ip route 172.16.0.0 255.255.0.0 10.10.1.1

ip route 192.168.1.0 255.255.255.248 10.10.3.1 50
ip route 192.168.20.0 255.255.255.0 10.10.3.1 50
ip route 172.16.0.0 255.255.0.0 10.10.3.1 50

 end
write memory