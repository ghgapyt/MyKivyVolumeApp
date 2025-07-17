[app]
title = PKTWVolumeControl
package.name = pktwvolume
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
orientation = portrait
fullscreen = 0
android.permissions = MODIFY_AUDIO_SETTINGS, ACCESS_NOTIFICATION_POLICY
icon.filename = %(source.dir)s/icon.png
android.minapi = 21
android.api = 33
android.ndk = 23b
android.ndk_api = 21
android.archs = arm64-v8a, armeabi-v7a
requirements = python3,kivy,pyjnius
entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1
