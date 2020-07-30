# 4.文件和目录访问的  pathlib   os.path
import os
# 或则from os import Path

print(os.path.abspath('.'))
print(os.path.exists('dir_test.py'))
print(os.path.isdir('/Users'))

# 路径的拼接
os.path.join('/tmp/a', 'b/c')

from pathlib import Path
p = Path('.')
print(p.absolute())
print(p.is_dir())
#创建目录
q = Path('/Desktop/what')
Path.mkdir(q,parents=True)