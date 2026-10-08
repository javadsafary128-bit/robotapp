[app]

# (str) Title of your application
title = Robot App

# (str) Package name
package.name = robotapp

# (str) Package domain
package.domain = org.robotapp

# (str) Source code where main.py is located
source.dir = .

# (str) Main entry point
source.main = main.py

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Orientation
orientation = portrait

# (list) Supported orientations
fullscreen = 0

# (str) Android API target
android.api = 35

# (str) Android minimum API
android.minapi = 21

# (str) Android architecture
android.arch = arm64-v8a

# (bool) Copy Python files
source.include_exts = py,png,jpg,jpeg,kv

# (str) Presplash
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon
# icon.filename = %(source.dir)s/data/icon.png


[buildozer]

# (str) Log level
log_level = 2

# (str) Warning if running as root
warn_on_root = 1
