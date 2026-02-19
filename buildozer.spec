[app]

# Uygulama Bilgileri
title = Pro Hesap Makinesi
package.name = prohesap
package.domain = org.ybs

# Kaynak klasörü
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Versiyon
version = 0.1

# Gereksinimler (Virgülden sonra boşluk yok!)
requirements = python3,kivy

# Ekran Ayarları
orientation = portrait
fullscreen = 0

# Android Stabil Ayarlar
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.build_tools = 31.0.0

# Mimariler
android.archs = armeabi-v7a, arm64-v8a

# İzinler (şimdilik boş)
android.permissions =

# Log seviyesi (Hata detay için)
log_level = 2

# Debug
android.debug = 1


[buildozer]

# Log seviyesi
log_level = 2

# Uyarı seviyesi
warn_on_root = 1
