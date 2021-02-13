### Module 6 Networking with Linux
#### TASK 6.1

1. Create virtual machines connection according to figure 1 - Done!

 ![](Screenshots/15.png) 

2. VM2 has one interface (internal), VM1 has 2 interfaces (NAT and internal). Configure all network interfaces in order to make VM2 has an access to the Internet (iptables, forward, masquerade).

Virtual machine settings:

 ![](Screenshots/1.png) 
 
 ![](Screenshots/2.png) 
 
 ![](Screenshots/3.png) 
 
 ![](Screenshots/4.png) 
 
 ![](Screenshots/5.png) 
 
 ![](Screenshots/6.png) 

3. Check the route from VM2 to Host.

![](Screenshots/8.png) 

![](Screenshots/7.png) 

4. Check the access to the Internet, (just ping, for example, 8.8.8.8).

![](Screenshots/9.png)

5. Determine, which resource has an IP address 8.8.8.8.

![](Screenshots/10.png) 

6. Determine, which IP address belongs to resource epam.com.

![](Screenshots/11.png) 

7. Determine the default gateway for your HOST and display routing table.

![](Screenshots/12.png) 

![](Screenshots/13.png) 

8. Trace the route to google.com.

![](Screenshots/14.png) 
