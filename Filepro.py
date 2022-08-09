import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Fipp32").ninex()
elif 'aarch' in arc:
	__import__("Fip").ninex()
else:
	exit(f' Unknow device machine {arc}')
