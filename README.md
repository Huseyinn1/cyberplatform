# Cyber Platform

Cyber Platform, siber güvenlik ve dijital analiz araçlarını bir araya getiren kapsamlı bir web uygulamasıdır.

## Özellikler

### 1. Log Analiz Sistemi
- Apache, Syslog, Application, Firewall ve Windows Event log analizi
- Gerçek zamanlı log izleme
- Anomali tespiti
- Görselleştirme ve raporlama

### 2. OCR (Optik Karakter Tanıma)
- Görüntüden metin çıkarma
- Belge analizi
- Metin dönüştürme

### 3. QR Kod Analizi
- QR kod okuma
- QR kod doğrulama
- Güvenlik kontrolü

### 4. Blog Sistemi
- Kategori ve etiket desteği
- Kullanıcı yorumları
- Medya yönetimi
- Blog abonelik sistemi

### 5. Kullanıcı Yönetimi
- Kayıt ve giriş sistemi
- Profil yönetimi
- Avatar desteği
- Kullanıcı dashboard'u

## Teknik Detaylar

### Kullanılan Teknolojiler
- Django 5.1.6
- Python
- SQLite
- HTML/CSS/JavaScript
- Chart.js (Görselleştirme için)

### Proje Yapısı
- `accounts/`: Kullanıcı yönetimi ve profil işlemleri
- `blogs/`: Blog sistemi ve içerik yönetimi
- `pages/`: Ana sayfa ve genel sayfalar
- `templates/`: HTML şablonları
- `static/`: Statik dosyalar (CSS, JS, resimler)
- `media/`: Kullanıcı yüklemeleri

## Kurulum

1. Sanal ortam oluşturun:
```bash
python -m venv env
```

2. Sanal ortamı aktifleştirin:
```bash
# Windows için
env\Scripts\activate
# Linux/Mac için
source env/bin/activate
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. Veritabanı migrasyonlarını yapın:
```bash
python manage.py migrate
```

5. Geliştirme sunucusunu başlatın:
```bash
python manage.py runserver
```

## Kullanım

1. Ana Sayfa: Platform özelliklerine genel bakış
2. Log Parser: Log dosyalarını analiz etme
3. OCR: Görüntüden metin çıkarma
4. QR Check: QR kod analizi
5. Blog: Makale okuma ve yorum yapma
6. Dashboard: Kullanıcı profili ve ayarları

## Geliştirme

### Gereksinimler
- Python 3.8+
- Django 5.1+
- Pillow (Görüntü işleme için)
- python-decouple (Çevre değişkenleri için)
