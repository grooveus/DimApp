[INFO]:    Building liblzma for armeabi-v7a
[INFO]:    -> directory context /home/eduardo/testes/.buildozer/android/platform/build-armeabi-v7a/build/other_builds/liblzma/armeabi-v7a__ndk_target_21/liblzma
[INFO]:    -> running autoreconf -vif
           working: autoreconf: autopoint is needed because this package uses Gettext                                              Exception in thread background thread for pid 67097:
Traceback (most recent call last):
  File "/usr/lib/python3.8/threading.py", line 932, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.8/threading.py", line 870, in run
    self._target(*self._args, **self._kwargs)
  File "/usr/local/lib/python3.8/dist-packages/sh-1.14.2-py3.8.egg/sh.py", line 1683, in wrap
    fn(*rgs, **kwargs)
  File "/usr/local/lib/python3.8/dist-packages/sh-1.14.2-py3.8.egg/sh.py", line 2662, in background_thread
    handle_exit_code(exit_code)
  File "/usr/local/lib/python3.8/dist-packages/sh-1.14.2-py3.8.egg/sh.py", line 2349, in fn
    return self.command.handle_command_exit_code(exit_code)
  File "/usr/local/lib/python3.8/dist-packages/sh-1.14.2-py3.8.egg/sh.py", line 905, in handle_command_exit_code
    raise exc
sh.ErrorReturnCode_1: 

  RAN: /usr/bin/autoreconf -vif

  STDOUT:
autoreconf: Entering directory `.'
autoreconf: running: autopoint --force
Can't exec "autopoint": No such file or directory at /usr/share/autoconf/Autom4te/FileUtils.pm line 345.
autoreconf: failed to run autopoint: No such file or directory
autoreconf: autopoint is needed because this package uses Gettext


  STDERR:

Traceback (most recent call last):                                                                                                 
  File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/eduardo/testes/.buildozer/android/platform/python-for-android/pythonforandroid/toolchain.py", line 1260, in <module>
    main()
  File "/home/eduardo/testes/.buildozer/android/platform/python-for-android/pythonforandroid/entrypoints.py", line 18, in main
    ToolchainCL()
  File "/home/eduardo/testes/.buildozer/android/platform/python-for-android/pythonforandroid/toolchain.py", line 709, in __init__
    getattr(self, command)(args)
  File "/home/eduardo/testes/.buildozer/android/platform/python-for-android/pythonforandroid/toolchain.py", line 154, in wrapper_func
    build_dist_from_args(ctx, dist, args)
  File "/home/eduardo/testes/.buildozer/android/platform/python-for-android/pythonforandroid/toolchain.py", line 213, in build_dist_from_args
    build_recipes(build_order, python_modules, ctx,
  File "/home/eduardo/testes/.buildozer/android/platform/python-for-android/pythonforandroid/build.py", line 577, in build_recipes
    recipe.build_arch(arch)
  File "/home/eduardo/testes/.buildozer/android/platform/python-for-android/pythonforandroid/recipes/liblzma/__init__.py", line 24, in build_arch
    shprint(sh.Command('autoreconf'), '-vif', _env=env)
  File "/home/eduardo/testes/.buildozer/android/platform/python-for-android/pythonforandroid/logger.py", line 167, in shprint
    for line in output:
  File "/usr/local/lib/python3.8/dist-packages/sh-1.14.2-py3.8.egg/sh.py", line 953, in next
    self.wait()
  File "/usr/local/lib/python3.8/dist-packages/sh-1.14.2-py3.8.egg/sh.py", line 879, in wait
    self.handle_command_exit_code(exit_code)
  File "/usr/local/lib/python3.8/dist-packages/sh-1.14.2-py3.8.egg/sh.py", line 905, in handle_command_exit_code
    raise exc
sh.ErrorReturnCode_1: 

  RAN: /usr/bin/autoreconf -vif

  STDOUT:
autoreconf: Entering directory `.'
autoreconf: running: autopoint --force
Can't exec "autopoint": No such file or directory at /usr/share/autoconf/Autom4te/FileUtils.pm line 345.
autoreconf: failed to run autopoint: No such file or directory
autoreconf: autopoint is needed because this package uses Gettext


  STDERR:

# Command failed: /usr/bin/python3 -m pythonforandroid.toolchain create --dist_name=myapp --bootstrap=sdl2 --requirements=python3,kivy,kivymd,pandas,math,sympy --arch armeabi-v7a --copy-libs --color=always --storage-dir="/home/eduardo/testes/.buildozer/android/platform/build-armeabi-v7a" --ndk-api=21 --ignore-setup-py
# ENVIRONMENT:
#     SHELL = '/bin/bash'
#     SESSION_MANAGER = 'local/eduardo-VirtualBox:@/tmp/.ICE-unix/1605,unix/eduardo-VirtualBox:/tmp/.ICE-unix/1605'
#     QT_ACCESSIBILITY = '1'
#     COLORTERM = 'truecolor'
#     XDG_CONFIG_DIRS = '/etc/xdg/xdg-ubuntu:/etc/xdg'
#     XDG_MENU_PREFIX = 'gnome-'
#     GNOME_DESKTOP_SESSION_ID = 'this-is-deprecated'
#     LANGUAGE = 'pt_BR:pt:en'
#     GNOME_SHELL_SESSION_MODE = 'ubuntu'
#     SSH_AUTH_SOCK = '/run/user/1000/keyring/ssh'
#     XMODIFIERS = '@im=ibus'
#     DESKTOP_SESSION = 'ubuntu'
#     SSH_AGENT_PID = '1497'
#     GTK_MODULES = 'gail:atk-bridge'
#     DBUS_STARTER_BUS_TYPE = 'session'
#     PWD = '/home/eduardo/testes'
#     LOGNAME = 'eduardo'
#     XDG_SESSION_DESKTOP = 'ubuntu'
#     XDG_SESSION_TYPE = 'x11'
#     GPG_AGENT_INFO = '/run/user/1000/gnupg/S.gpg-agent:0:1'
#     XAUTHORITY = '/run/user/1000/gdm/Xauthority'
#     WINDOWPATH = '2'
#     HOME = '/home/eduardo'
#     USERNAME = 'eduardo'
#     IM_CONFIG_PHASE = '1'
#     LANG = 'pt_BR.UTF-8'
#     LS_COLORS = 'rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:'
#     XDG_CURRENT_DESKTOP = 'ubuntu:GNOME'
#     VTE_VERSION = '6003'
#     GNOME_TERMINAL_SCREEN = '/org/gnome/Terminal/screen/058aa4b9_c4b7_4f58_9eed_21ecdafbcabf'
#     INVOCATION_ID = '52a014c520ae4d8ea0b041c74f263e1d'
#     MANAGERPID = '1316'
#     LESSCLOSE = '/usr/bin/lesspipe %s %s'
#     XDG_SESSION_CLASS = 'user'
#     TERM = 'xterm-256color'
#     LESSOPEN = '| /usr/bin/lesspipe %s'
#     USER = 'eduardo'
#     GNOME_TERMINAL_SERVICE = ':1.115'
#     DISPLAY = ':0'
#     SHLVL = '1'
#     QT_IM_MODULE = 'ibus'
#     DBUS_STARTER_ADDRESS = 'unix:path=/run/user/1000/bus,guid=6e665d477be3a31c031d453660d68799'
#     XDG_RUNTIME_DIR = '/run/user/1000'
#     JOURNAL_STREAM = '8:34851'
#     XDG_DATA_DIRS = '/usr/share/ubuntu:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop'
#     PATH = '/home/eduardo/.buildozer/android/platform/apache-ant-1.9.4/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
#     GDMSESSION = 'ubuntu'
#     DBUS_SESSION_BUS_ADDRESS = 'unix:path=/run/user/1000/bus,guid=6e665d477be3a31c031d453660d68799'
#     _ = '/usr/local/bin/buildozer'
#     PACKAGES_PATH = '/home/eduardo/.buildozer/android/packages'
#     ANDROIDSDK = '/home/eduardo/.buildozer/android/platform/android-sdk'
#     ANDROIDNDK = '/home/eduardo/.buildozer/android/platform/android-ndk-r19c'
#     ANDROIDAPI = '27'
#     ANDROIDMINAPI = '21'
# 
# Buildozer failed to execute the last command
# The error might be hidden in the log above this error
# Please read the full log, and search for it before
# raising an issue with buildozer itself.
# In case of a bug report, please add a full log with log_level = 2
