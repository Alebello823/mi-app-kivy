[app]

# (str) Title of your application
title = Mia Isabella Downloader

# (str) Package name
package.name = miadownloader

# (str) Package domain
package.domain = org.alebell

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
# MUY IMPORTANTE: Incluimos yt-dlp y certificados para que funcione el HTTPS
requirements = python3,kivy==2.3.0,yt-dlp,certifi,openssl,requests

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# ==========================================================
# SECCIÓN ANDROID - CONFIGURACIÓN CRÍTICA
# ==========================================================

# (list) Permissions: Internet para descargar y Storage para guardar el video
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# (int) Target Android API (33 es el estándar actual)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (bool) Enable AndroidX support (Necesario para apps modernas)
android.enable_androidx = True

# (list) The Android archs to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) allow backup
android.allow_backup = True

# (str) The format used to package the app for debug mode (apk)
android.debug_artifact = apk

# ==========================================================
# SECCIÓN BUILDOZER GENERAL
# ==========================================================

[buildozer]

# (int) Log level (2 = debug para ver errores si algo falla)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1

