[app]

# (str) Title of your application
title = PKTWVolumeControl

# (str) Package name
package.name = pktwvolume

# (str) Package domain (unique)
package.domain = org.test

# (str) Source code where main.py is
source.dir = .

# (str) The main entry point
entrypoint = main.py

# (list) Permissions
android.permissions = MODIFY_AUDIO_SETTINGS, ACCESS_NOTIFICATION_POLICY

# (int) Target Android API
android.api = 30

# (int) Minimum API your app will support
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 30

# (str) Android NDK version
android.ndk = 23b

# (str) Android build tools version
android.build_tools = 30.0.3

# (list) Architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (str) Application versioning
version = 1.0

# (str) Orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

# (str) Application icon
icon.filename = %(source.dir)s/icon.png

# (list) Include these file types
source.include_exts = py,png,jpg,kv,atlas

# (str) Supported requirements
requirements = python3,kivy,pyjnius
