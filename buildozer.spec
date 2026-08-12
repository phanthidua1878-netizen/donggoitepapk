[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Version of your application
version = 0.1

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Thêm các thư viện khác vào đây nếu app của bạn cần (ví dụ: requests, pillow...)
requirements = python3,kivy

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (bool) Indicate whether the API should be accepting Android SDK licenses
android.accept_sdk_license = True

# (list) PERMISSIONS
# android.permissions = INTERNET
