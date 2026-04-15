# Maven Fuzzy Factory E-Ticaret Analizi

Maven Fuzzy Factory e-ticaret veri seti üzerine kurulmuş, iş odaklı bir analiz vaka çalışması. Bu proje, işletmenin Mart 2012 ile Mart 2015 arasında nasıl büyüdüğünü, hangi kanalların ölçek sağladığını ve hangilerinin verimlilik yarattığını, ürün genişlemesinin sepet ekonomisini nasıl etkilediğini ve dönüşüm ile iade sorunlarının performansı nerelerde sınırladığını inceler.

## İş Problemi
Maven Fuzzy Factory, üç yıllık dönemde güçlü bir büyüme yaşadı. Ancak yalnızca büyümek yeterli değildir. Bu projenin amacı şu soruları yanıtlamaktı:

- trafik, sipariş ve gelir zaman içinde nasıl değişti
- hangi pazarlama kanalları ölçek sağladı ve hangileri daha yüksek kaliteli trafik getirdi
- ürün genişlemesi sipariş ekonomisini iyileştirdi mi
- müşteri dönüşümü hangi noktalarda kısıtlandı
- hangi ürünler iade riski yaratarak net gelir kalitesini zayıflattı

## Veri Seti
Zaman kapsamı:
- Mart 2012 ile Mart 2015 arası

Kullanılan ana tablolar:
- `website_sessions`
- `website_pageviews`
- `orders`
- `order_items`
- `order_item_refunds`
- `products`

Yüksek seviyede veri hacmi:
- 472.871 web oturumu
- 1.188.124 sayfa görüntüleme
- 32.313 sipariş
- 40.025 sipariş kalemi
- 1.731 iade edilen sipariş kalemi
- 4 ürün

## Araçlar
- Python
- SQLite
- SQL
- Power BI
- Markdown / DOCX dokümantasyonu

## Proje Akışı
Bu proje, doğrudan dashboard oluşturmaya atlamak yerine pratik bir analitik iş akışı izledi.

1. **Veri yükleme**  
   Ham CSV dosyaları toplandı ve yerel bir SQLite veritabanına aktarıldı.

2. **Doğrulama**  
   Analize başlamadan önce satır sayıları, join yapıları, zaman kapsamı ve toplulaştırma tutarlılığı kontrolleri incelendi.

3. **Dönüştürme**  
   Trend analizi, kanal karşılaştırması, ürün analizi ve iade incelemesi için aylık özet çıktılar oluşturuldu.

4. **Analiz**  
   SQL kullanılarak büyüme, kanal verimliliği, dönüşüm, ürün karması ve iade kalitesiyle ilgili temel iş soruları yanıtlandı.

5. **Görselleştirme**  
   Bulgular, paydaşların kolay anlayabileceği dashboard sayfaları halinde Power BI üzerinde düzenlendi.

6. **Öneri geliştirme**  
   Nihai çıktıların odağı yalnızca grafikler değil, iş aksiyonları oldu.

## Veri Hattı
`CSV dosyaları -> SQLite veritabanı -> SQL analizi -> özet çıktılar -> Power BI dashboard -> iş önerileri`

## Veri Kalitesi Kontrolleri
Sonuçlara geçmeden önce şu kontroller tamamlandı:

- her ham tablonun SQLite'a yüklenmesinden sonra satır sayıları doğrulandı
- oturumlar, sayfa görüntülemeleri, siparişler, sipariş kalemleri, iadeler ve ürünler arasındaki tablo kapsamı teyit edildi
- şu join yapıları test edildi:
  - sessions ve orders
  - orders ve order_items
  - order_items ve refunds
  - order_items ve products
- oturumlar ve siparişler için minimum ve maksimum tarihler doğrulandı
- aylık trend çıktılarının oturumlar, siparişler, dönüşüm ve gelir tarafında yönsel olarak tutarlı olduğu kontrol edildi
- temel KPI değerlerinin toplulaştırma sonrası ticari olarak makul olup olmadığı gözden geçirildi
- BI görselleştirmeleri sırasında metrik ölçekleme sorunları incelendi, gerekli yerlerde sayısal biçimlendirme ve dönüşüm mantığı düzeltildi

## Temel Bulgular
### 1. Büyüme hem ölçekten hem verimlilikten geldi
İşletme yalnızca trafik kazanımıyla büyümedi. Oturumlar ciddi şekilde artarken siparişler daha da hızlı arttı. Bu da dönüşüm performansının da iyileştiğini gösterdi.

### 2. Nonbrand paid search büyümeyi ölçekledi, ancak yüksek niyetli trafik daha iyi gelir yarattı
Ücretli nonbrand arama en yüksek hacmi sağladı. Brand, direct ve organic trafik ise daha güçlü dönüşüm ve gelir verimliliği üretti.

### 3. Mobil en net performans açığıydı
Masaüstü dönüşümü, mobil dönüşümden belirgin biçimde daha yüksekti. Bu da mobil deneyimi en büyük optimizasyon fırsatlarından biri haline getirdi.

### 4. Ürün genişlemesi sepet ekonomisini iyileştirdi
Ürün kataloğu genişledikçe ortalama sipariş değeri arttı ve çoklu ürün içeren sepetler daha değerli hale geldi.

### 5. Her ürün büyümesi aynı derecede sağlıklı değildi
Bazı ürünler daha yüksek iade baskısı yarattı. Bu nedenle performansı değerlendirmek için yalnızca brüt satışlara bakmak yeterli değildi.

### 6. Gelir amiral ürün üzerinde yoğunlaşmış durumda kaldı
Original Mr. Fuzzy, ana gelir sürücüsü olmaya devam etti. Bu hem bir güç hem de bir yoğunlaşma riskidir.

## Dashboard Yapısı
### Sayfa 1: Yönetici Özeti / Satış Performansı
- toplam oturum
- toplam sipariş
- dönüşüm oranı
- toplam gelir
- oturum başına gelir
- zaman içindeki büyüme trendleri
- kanal verimliliği öne çıkanları

### Sayfa 2: Müşteri / Ürün İçgörüleri
- cihaz performans farkı
- ürün karması ve ürün geliri
- sepet değeri örüntüleri
- ürün bazında iade davranışı
- aksiyon odaklı iş önerileri

## Öneriler
1. Mobil dönüşüm optimizasyonuna öncelik ver.
2. Çapraz satış ve bundle stratejisini genişlet.
3. Düşük kaliteli edinim kanallarını yeniden değerlendir.
4. Yüksek iade oranına sahip SKU'ları beklenti veya kalite sorunları açısından incele.

## Kısıtlar
- Reklam harcaması verisi bulunmadığı için gerçek ROI ve CPA hesaplanamadı.
- Demografik veya coğrafi müşteri detayı mevcut değildi.
- Kök neden analizi için açık bir iade nedeni alanı bulunmuyordu.
- Ürün lansmanı etkileri kesin nedensellik olarak değil, yönsel olarak yorumlandı.
- Tekrar satın alma analizi, gözlem penceresi nedeniyle sınırlı kaldı.

## Öğrenimler
- İyi SQL tek başına yeterli değildir. Toplulaştırma mantığı ve BI biçimlendirmesi hâlâ hikâyeyi bozabilir.
- Sorgu içinde makul görünen iş metrikleri, dashboard araçlarında sayısal ölçekleme doğrulanmazsa yanlış gösterilebilir.
- Ürün genişlemesi ortalama sipariş değerini artırabilir, ancak bunu başarı olarak adlandırmadan önce iade kalitesi kontrol edilmelidir.
- Kanal hacmi ve kanal kalitesi aynı şey değildir ve ayrı analiz edilmelidir.
- Güçlü bir portföy projesi hem analiz kalitesi hem de sunum disiplini gerektirir.

## Repo Yapısı
```text
toy_store/
├── data/
│   ├── raw/
│   └── toy_store.db
├── sql/
│   ├── 01_growth_trends.sql
│   ├── 02_channel_analysis.sql
│   ├── 03_device_analysis.sql
│   ├── 04_product_analysis.sql
│   └── 05_refund_analysis.sql
├── powerbi/
│   └── toy_store_dashboard.pbix
├── outputs/
│   ├── charts/
│   └── summary_tables/
├── docs/
│   ├── case_study_report.md
│   └── toy_store_findings_summary.docx
└── README.md
```

## Proje Durumu
Temel analiz tamamlandı. Dokümantasyon ve dashboard paketleme süreci, nihai portföy sunumu için iyileştiriliyor.
