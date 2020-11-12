# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in venpep/__init__.py
from venpep import __version__ as version

setup(
	name='venpep',
	version=version,
	description='Venture for People',
	author='Venpep',
	author_email='dhamodaran.p@venpep.net',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
