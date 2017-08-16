
import sys, os
from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist --formats=zip,gztar')
    os.system('python setup.py bdist_wheel')
    print('You probably sync to git with tag of version by:')
    print('    git tag -a $(VERSION)  -m "New version * released" ')
    print('    git push --tags')
    sys.exit()


setup(name = 'ColorBash',
      version = '1.0',
      description = 'Make your output in bash colorful',
      author = 'Hankso',
      author_email = '3080863354@qq.com',
      url = 'www.baidu.com/s?wd=python%20colorful%20output',
      license = 'GPL',
      package_dir = {'colorbash':'src'},
      packages = ['colorbash'],
#==============================================================================
#       package_data = {},
#       data_files = [(),],
#==============================================================================
#==============================================================================
#       requires = [],
#       provides = [],
#==============================================================================
)
