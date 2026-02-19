[app]

# (str) Uygulamanın başlığı
title = Pro Hesap Makinesi

# (str) Paket adı (Türkçe karakter ve boşluk içermez)
package.name = prohesap

# (str) Paket alanı (YBS bölümüne özel)
package.domain = org.ybs

# (str) Kaynak kodun olduğu dizin
source.dir = .

# (list) Dahil edilecek dosya uzantıları
source.include_exts = py,png,jpg,kv,atlas

# (str) Uygulama sürümü
version = 0.1

# (list) Gereksinimler
requirements = python3,kivy

# (list) Desteklenen yön (Dikey)
orientation = portrait

# (bool) Tam ekran modu
fullscreen = 0

# (int) Hedef Android API (En stabil sürüm)
android.api = 33

# (int) Minimum desteklenen API
android.minapi = 21

# (str) Android NDK sürümü (HATANIN ÇÖZÜMÜ BURASI!)
android.ndk = 25b

# (str) Android SDK build tools sürümü
android.sdk_build_tools_version = 33.0.0

# (bool) Lisansları otomatik kabul et (GitHub Actions için zorunludur)
android.accept_sdk_license = True

# (list) Desteklenen mimariler
android.archs = arm64-v8a, armeabi-v7a

# (bool) Yedeklemeye izin ver
android.allow_backup = True

[buildozer]

# (int) Log seviyesi (Hata ayıklama için 2 yapıldı)
log_level = 2

# (int) Root uyarısını göster
warn_on_root = 1
