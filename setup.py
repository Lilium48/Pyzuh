from setuptools import setup
import configparser
import os 
import sys 

setup(
    name='pyzuh',
    version='1.0.0',
    description='Python Library for the Wazuh API',
    author="@lilium48",
    author_email="austin@liliumsecurity.com",
    project_urls={
        'Source': 'https://github.com/Lilium48/pyzuh',
    },
    install_requires=[
        "requests>=2.31.0",
        "pyjwt>=2.8.0",
        "urllib3>=2.2.0"
    ],
  
    license='MIT',
    packages=['pyzuh'])