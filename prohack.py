import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Filepro").license()
elif 'aarch' in arc:
	__import__("Filepro64").license()
else:
	exit(f' Unknow device machine {arc}')
