from scapy.all import *

def handle_icmp_reply(packet):
    print("apu")
    if packet.haslayer(ICMP):
        
        data = packet[ICMP].load.decode('utf-8')
        print(data)
        return data

def receive_icmp_packets():
   
    filter_str = "icmp "

    
    packets = sniff(filter=filter_str, prn=handle_icmp_reply, iface="eth0", timeout=5)

    return packets

def main():
    target_ip = "198.168.18.137" 

    file_name = input("Enter the name of the file to send: ")


   
    icmp_packet = IP(dst=target_ip) / ICMP() / file_name.encode('utf-8')
    send(icmp_packet)

    print("Data sent successfully.")

    
    packets = receive_icmp_packets()

    
    response_data = ''.join([packet[ICMP].load.decode('utf-8') for packet in packets])
    with open(file_name, 'a') as file:
        file.write(response_data)

    print("Response received and written to the file.")

if __name__ == "__main__":
    main()
