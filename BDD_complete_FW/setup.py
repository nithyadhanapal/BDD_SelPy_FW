# sudo python3 setup.py install in terminal to add the below packages to the python path
# sudo python setup.py develop

from setuptools import setup, find_packages
setup(name='BDD_FW_Practice',
      version='1.0',
      description='Python BDD Practical Examples',
      author='Nithya Praveen',
      author_email='nitydhanapal@gmail.com',
      url='https://www.supersqa.com/',
      packages=find_packages()

     )
