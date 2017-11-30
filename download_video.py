from subprocess import *

p = Popen(["C:\\Program Files (x86)\\Xmlbar\\FLV Downloader\\FLVDownloader(xmlbar).exe"], stdin=PIPE)

s = ''
for i in range(17):
	s += '\t'

p.communicate(bytes(s+'http://tv.cctv.com/2017/11/28/VIDETRtb7usiG8XC3Om6ovxg171128.shtml', 'ascii'))

p.kill()