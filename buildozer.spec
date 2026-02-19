[app]

# (str) Uygulamanın adı
title = Pro Hesap Makinesi

# (str) Paket adı (Türkçe karakter ve boşluk içermez)
package.name = prohesap

# (str) Paket alanı
package.domain = org.ybs

# (str) Kodun bulunduğu dizin
source.dir = .

# (list) Dahil edilecek dosya uzantıları
source.include_exts = py,png,jpg,kv,atlas

# (str) Uygulama sürümü
version = 0.1

# (list) Gereksinimler (Virgülden sonra boşluk bırakma!)
requirements = python3,kivy

# (list) Desteklenen yön
orientation = portrait

# (bool) Tam ekran modu
fullscreen = 0

# (int) Hedef Android API (En stabil olanı 33'tür)
android.api = 33

# (int) Minimum desteklenen API
android.minapi = 21

# (str) Android SDK build tools versiyonu
android.sdk_build_tools_version = 33.0.0

# (bool) Lisansları otomatik kabul et (GitHub Actions için ŞART!)
android.accept_sdk_license = True

# (list) Desteklenen mimariler (Çoğu telefon için yeterli)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Yedeklemeye izin ver
android.allow_backup = True

[buildozer]

# (int) Log seviyesi (Hataları görmek için 2 yapıldı)
log_level = 2

# (int) Root uyarısını göster
warn_on_root = 1
