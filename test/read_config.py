import os
import configparser

# 获取文件的当前路径（绝对路径) 
cur_path = os.path.dirname(os.path.realpath(__file__))

# 获取config.ini的路径
config_path = os.path.join(cur_path, 'config.ini')

conf = configparser.ConfigParser()
conf.read(config_path)

pause = conf.get('begin', 'make.pause')
stop = conf.get('begin', 'make.stop')
location = conf.get('begin', 'make.location')