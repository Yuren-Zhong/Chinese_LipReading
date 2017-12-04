
import subprocess

MIN_NUM = 0
MAX_NUM = 2750

for index in range(MIN_NUM, MAX_NUM):
	cmd = 'python video_filter.py --index ' + str(index)
	subprocess.run(cmd, timeout=60)