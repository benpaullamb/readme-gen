from setuptools import setup

setup(
  name='readme-gen',
  version='0.1.0',
  py_modules=['app'],
  install_requires=[
    'Click',
  ],
  entry_points={
    'console_scripts': [
      'readme-gen = app:cli',
    ],
  },
)