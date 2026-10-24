# TÜBİTAK 2209-A - Ağ Trafiği Analiz ve Ön Çalışma Prototipi

Bu repository Muhammet Yusuf KÜTÜK tarafından, TÜBİTAK 2209-A araştırma projesi kapsamında geliştirilen ağ trafiği analizi ve paket işleme prototipinin ön çalışma aşamasını içermektedir. Projenin temel amacı, yakalanan ağ paketi dosyalarını (.pcap) harici araçlara bağımlı kalmadan programatik olarak okumak, filtrelemek ve analiz etmek için güvenli bir Python altyapısı sunmaktır.

## Proje İçeriği ve Dosya Yapısı

- pcaptester2209analiz.py: Scapy kütüphanesi kullanılarak .pcap dosyalarını okuyan ve trafik analiz grafiği çıkartan uygulama.

- pcaptester2209softinfo.py: Scapy kütüphanesi kullanılarak .pcap dosyalarını analiz edip  istenilen sayı kadar kaynaktan hedefe giden istekler(İP dahil) ve verileri boyut bilgileri dahil olarak bilgi sunar.

- trafik_analiz.png:dosya içerisindeki pcaptester2209analiz.py dosyasının çalıştırılması sonucu elde edilen çıktının ekran görüntüsü.

- wirepcapsharktester.pcap: Kontrollü test ortamında(kali linux) (kimlik doğrulama gerektirmeyen standart web siteleri üzerinden) yakalanan 80 -90 saniyelik ham ağ trafik veri seti.(kapsam github dosya boyutu sebebiyle daraltıldı)

## Kullanılan Teknolojiler

- Python 3.x
- Scapy (Ağ paketi analizi ve ayrıştırma kütüphanesi)

- wireshark


## Kurulum ve Çalıştırma Adımları

Projeyi kendi bilgisayarınızda veya test ortamınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

1. Depoyu klonlayın veya indirin:
   ```bash
   git clone <repo-linkiniz>
   cd <repo-klasorunuz>

2. Zip olarak indirip kendi studio nuzda yada masaüstünüzde çalıştırabilirsiniz.
