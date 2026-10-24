import logging
# Scapy'nin libpcap uyarısını log seviyesini yükselterek tamamen susturalım
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import rdpcap, IP

def pcap_dosyasini_oku(dosya_yolu):
    print(f"[*] '{dosya_yolu}' dosyası yükleniyor ve okunuyor...")
    
    try:
        # Pcap dosyasını Scapy ile oku
        paketler = rdpcap(dosya_yolu)
        toplam_paket = len(paketler)
        print(f"[*] Toplam yakalanan paket sayısı: {toplam_paket}\n")
        
        # Kullanıcı doğru bir giriş yapana kadar döngüde kal
        limit = None
        while True:
            giris = input("Kaç adetle sınırlayayım? (Tümünü görmek için direkt Enter'a basın): ").strip()
            
            # Sadece Enter'a basıldıysa
            if giris == "":
                limit = None
                print("[*] Tüm paketler listeleniyor...")
                break
            
            try:
                limit = int(giris)
                if limit <= 0:
                    print("[!] Lütfen 0'dan büyük bir sayı girin.")
                    continue
                break # Geçerli bir sayı girildiyse döngüden çık
            except ValueError:
                print("[!] Hatalı giriş! Lütfen bir sayı girin ya da sadece Enter'a basın.")

        print("-" * 65)
        print(f"{'No':<6} | {'Kaynak IP':<15} -> {'Hedef IP':<15} | {'Boyut (Byte)'}")
        print("-" * 65)
        
        sayac = 1
        for paket in paketler:
            # Sadece IP katmanı içeren paketleri filtrele
            if IP in paket:
                kaynak_ip = paket[IP].src
                hedef_ip = paket[IP].dst
                boyut = len(paket)
                
                print(f"{sayac:<6} | {kaynak_ip:<15} -> {hedef_ip:<15} | {boyut}")
                sayac += 1
                
                # Kullanıcının belirlediği limit aşıldıysa döngüyü durdur
                if limit is not None and (sayac - 1) >= limit:
                    print("-" * 65)
                    print(f"[!] Belirttiğiniz sınır ({limit} adet) dolduğu için liste durduruldu.")
                    break
                    
    except FileNotFoundError:
        print(f"[!] Hata: '{dosya_yolu}' adında bir dosya bulunamadı.")
        print("[!] İpucu: Python betiği ile pcap dosyasının aynı klasörde olduğundan emin ol.")
    except Exception as e:
        print(f"[!] Beklenmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    # GitHub'a yükleyeceğin pcap dosyasının tam adı (Aynı klasörde olmalılar)
    pcap_dosyasi = "wirepcapsharktester.pcap"
    pcap_dosyasini_oku(pcap_dosyasi)