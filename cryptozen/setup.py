import pathlib
from os import path
from setuptools import setup

# The directory containing this file
this_directory = pathlib.Path(__file__).parent
# The text of the README file
with open(path.join(this_directory, 'Readme.md'), encoding='utf-8') as f:
    long_description = f.read()


# This call to setup() does all the work
setup(
    name="cryptozen",
    version="0.0.1",
    description="Basic ciphers/Modern Ciphers",
    long_description=long_description,
    url="https://github.com/Darknez07/CyberSec-Ciphers-hashes/cryptozen",
    author="Darknez07",
    author_email="darknez077@gmail.com",
    license="GNU",
    classifiers=[
        "License :: OSI Approved :: GNU License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.9"
    ],
    keywords=["cryptography", "Files"],
    packages=["cryptozen"],
    include_package_data=True,
    install_requires=["sys", "random","math"],
    entry_points={
        "console_scripts": [
            "cryptozen=cryptozen.__main__:main",
        ]
    },
)