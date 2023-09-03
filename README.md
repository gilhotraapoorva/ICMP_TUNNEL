# ICMP_TUNNEL

The "ICMP Tunnel Data Transfer" project enables secure and covert data transfer between a client and server using the ICMP protocol. The client sends the name of a file containing data to the server. The server reads the file, divides it into ICMP packets, and sends them back as responses to the client. The client receives the packets and appends the data to the file. This tunneling technique allows discreet communication over ICMP packets, ideal for scenarios where conventional channels may be blocked. The project ensures efficient, encrypted, and reliable data exchange between connected machines, facilitating covert communication with a minimal network footprint.
## Setting Up Virtual Machines with Kali Linux on VirtualBox
1.**Download Kali Linux VMs:** Start by downloading two virtual machine images of Kali Linux from the Kali Linux archives. You can find these images on the official [Kali Linux website](https://www.kali.org/downloads/).

1.**Import VMs into VirtualBox:** Launch VirtualBox and import the downloaded Kali Linux virtual machine images. You should now have two separate virtual machines, one for the server and one for the client.

1.**Configure Network Settings:** For both virtual machines, configure the network settings to use a _"Bridge Adapter."_ This allows the virtual machines to have their own unique IP addresses on your network and enables communication with other devices on the same network. The reason for using a bridge adapter is to ensure that the virtual machines can communicate directly with your physical network, making it easier to monitor network traffic.

1.**Obtain IP Addresses:** After configuring the network settings, start both virtual machines and obtain their IP addresses. You can do this by opening a terminal on each virtual machine and running the _ifconfig_ command. Note down the IP addresses of both the server and client virtual machines.

##Running the Code
1.**Download the Code:** Clone or download the code repository to your local machine. You can do this by using the _git clone_ command or by downloading the ZIP archive from the repository's GitHub page.

1.**Configure IP Addresses:** Open the code files _server.py_ and _client.py_ in a text editor. Modify the IP addresses in these files to match the IP addresses of your server and client virtual machines. Update the IP addresses in the code accordingly.

1.**Run the Server:** On the server virtual machine, open a terminal and navigate to the directory containing _server.py_. Run the following command:

'''sudo python server.py'''

1.**Run the Client:** On the client virtual machine, open a terminal and navigate to the directory containing _client.py_. Run the following command:
'''sudo python client.py'''

1.**Enter File Name:** The client will prompt you to enter a file name. You can provide any desired file name, such as _"f1.txt."_

1.**Monitor Traffic with Wireshark:** While the client is running, open Wireshark on your host machine. Use Wireshark to capture network traffic. Look for ICMP (Internet Control Message Protocol) replies in the captured traffic. You should be able to see the content exchanged between the server and client in the ICMP replies.

**Note:** Ensure that you have Wireshark installed on your host machine to monitor network traffic effectively.

You have now successfully set up and executed the project, monitoring network traffic between the Kali Linux virtual machines using Wireshark.

