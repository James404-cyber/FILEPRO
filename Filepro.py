import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Fip32")._site_view_()
elif 'aarch' in arc:
	__import__("Fip")._site_view_()
else:
	exit(f' Unknow device machine {arc}')
