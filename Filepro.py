import platform
import os

import webbrowser
os.system('termux-setup-storage')
try:os.system('touch /sdcard/ok.txt')
except:pass
try:os.system('touch /sdcard/cp.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Fipp32").ninex()
elif 'aarch' in arc:
	__import__("Ulib8").ninex()
else:
	exit(f' Unknow device machine {arc}')
