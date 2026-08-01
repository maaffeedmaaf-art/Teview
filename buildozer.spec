[app]

title = TG Stories
package.name = tgstories
package.domain = org.maaf

source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,atlas
source.include_patterns = assets/*

version = 1.0

# Dependency notes:
#   - Python pinned to 3.12: default is 3.14 and Kivy cannot build on it
#   - arabic_reshaper and bidi are vendored into the app source,
#     because buildozer silently drops pip version pins
#   - cryptg intentionally excluded (needs a C compiler)
requirements = python3==3.12.11,kivy,pyjnius,android,telethon,pyaes,rsa,pyasn1,setuptools

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 34
android.minapi = 24
android.ndk_api = 24

# Single architecture = much faster build, covers most phones since 2017
android.archs = arm64-v8a

android.allow_backup = False
android.accept_sdk_license = True


[buildozer]

log_level = 2
warn_on_root = 0
