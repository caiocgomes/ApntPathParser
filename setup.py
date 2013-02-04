import os
from setuptools import setup, find_packages

setup_pth = os.path.dirname(__file__)

setup(
    name='ApntPathParser',
    version="0.0.1",
    packages=find_packages(),
    install_requires=['parse>=1.6.1'],
    author_email='rafael.calsaverini@gmail.com',
    author="Rafael S. Calsaverini",
    url = 'none'
)
