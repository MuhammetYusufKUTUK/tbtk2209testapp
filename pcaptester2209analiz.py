from scapy.all import rdpcap
import matplotlib.pyplot as plt

# 1. Kaydettiğin pcap dosyasını oku
packets = rdpcap("wirepcapsharktester.pcap")

times = []
sizes = []

# İlk paketin zamanını baz alarak relative (göreli) zaman hesapla
start_time = float(packets[0].time) if packets else 0

for pkt in packets:
  times.append(float(pkt.time) - start_time)
  sizes.append(len(pkt))  # Paket boyutu (byte cinsinden)

# 2. Paket Boyutu / Zaman Grafiğini Çiz
plt.figure(figsize=(10, 5))
plt.plot(times, sizes, marker='.', linestyle='-', color='b', alpha=0.6)
plt.title("Ağ Trafiği Paket Boyutu Zaman Grafiği")
plt.xlabel("Zaman (Saniye)")
plt.ylabel("Paket Boyutu (Byte)")
plt.grid(True)
plt.savefig("trafik_analiz.png")  # Grafiği rapora eklemek için kaydet
plt.show()