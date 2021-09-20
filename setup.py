from setuptools import setup, find_namespace_packages

PKG = "ABrowser"
AUTHOR = "HorusElohim"
VERSION = "0.1"
LICENSE = "GPLv3"
DESCRIPTION = """
Soft wrapper around selenium to accelerate the usage 
"""

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name=PKG,
    author=AUTHOR,
    url='https://github.com/HorusElohim/ABrowser',
    version=VERSION,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    packages=find_namespace_packages(include=[PKG, f'{PKG}.*']),
    entry_points={'console_scripts': [f'{PKG}_console = {PKG}.scripts:ABrowser_console']},
    install_requires=requirements,
    include_package_data=True,
    python_requires='>=3.7'
)
