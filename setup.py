from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='espapp',
      version='0.3',
      description='ESP applicaion',
      author='Karan',
      author_email='karan.rathore@viriminfotech.com',
      license='Virim',
      install_requires=[
          'uuid',
          'python-crontab',
          'requests',
      ],
      )
      
