import platform
import os

import webbrowser
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir /sdcard/JAMES')
except:pass
try:os.system('mkdir /sdcard/JAMES/OK')
except:pass
try:os.system('mkdir /sdcard/JAMES/CP')
except:pass
try:os.system('mkdir /sdcard/JAMES/TAP-A2F')
except:pass
try:os.system('touch .prox.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Fipp32").ninex()
elif 'aarch' in arc:
	__import__("Fip").ninex()
else:
	exit(f' Unknow device machine {arc}')
