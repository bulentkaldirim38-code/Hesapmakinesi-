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

# Gereksinimler
requirements = python3,kivy

# Ekran
orientation = portrait
fullscreen = 0

# Android Ayarları (STABİL KOMBINASYON)
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 23b
android.build_tools = 31.0.0

# Log seviyesi (hata görürsen detaylı çıkar)
log_level = 2

# İzinler (şimdilik boş)
android.permissions =

# Mimari
android.archs = armeabi-v7a, arm64-v8a

# Debug
android.debug = 1
