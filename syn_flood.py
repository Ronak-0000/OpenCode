from scapy.all import *
target_ip = "127.0.0.1"
target_port = 80

print("[*] Sending 5 SYN packets...")

i = 0

while i < 5:
    ip = IP(dst=target_ip)
    tcp = TCP(dport=target_port, flags="S", sport=RandShort())
    packet = ip / tcp

    send(packet, verbose=False)
    print(f"Sent SYN packet {i+1}")
    i =i + 1

print("[*] Demo finished.")
