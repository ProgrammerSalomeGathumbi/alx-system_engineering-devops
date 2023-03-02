0x08. Networking basics #1  
localhost and 127.0.0.1 are both used to refer to the local machine or the loopback interface. The loopback interface is a virtual network interface that allows a machine to communicate with itself. When you use localhost or 127.0.0.1 as a hostname, your machine will always resolve the address to itself, rather than attempting to communicate with another machine on the network.

0.0.0.0 is a special IP address that represents all possible IP addresses on the local machine. It can be used to bind a network service to all available network interfaces or to listen on all available IP addresses.

/etc/hosts is a file on Unix-like systems (including Linux) that maps hostnames to IP addresses. When you try to connect to a hostname (e.g., google.com) from your machine, your operating system looks up the hostname in the /etc/hosts file to determine the corresponding IP address. If an entry exists for the hostname in the file, the IP address specified in the entry is used for the connection.

To display your machine's active network interfaces, you can use the ifconfig command on Linux/Unix-based systems or ipconfig command on Windows. The output of the command will show you the IP addresses associated with each interface, as well as other network configuration information. 
