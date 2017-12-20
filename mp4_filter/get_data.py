
import subprocess
from os.path import isfile, join

MIN_NUM = 0
MAX_NUM = 60000

videodir_path = 'D:\\Chinese_LipReading\\cntv_spider\\tutorial\\new_videos'
scriptdir_path = 'D:\\Chinese_LipReading\\cntv_spider\\tutorial\\new_scripts'


for index in range(MIN_NUM, MAX_NUM):
    video_exist = isfile(join(videodir_path, str(index)+'.mp4'))
    script_exist = isfile(join(scriptdir_path, str(index)+'.txt'))
    if video_exist and script_exist:
        cmd = 'python video_filter.py --index ' + str(index)
        subprocess.run(cmd, timeout=60)