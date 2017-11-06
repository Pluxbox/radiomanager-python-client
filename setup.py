# coding: utf-8

"""
    RadioManager

    RadioManager

    OpenAPI spec version: 2.0
    Contact: support@pluxbox.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "Pluxbox RadioManager Client"
VERSION = "1.1.4"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="RadioManager",
    author_email="support@pluxbox.com",
    url="http://pluxbox.com",
    keywords=["pluxbox", "radio", "radiomanager", "sdk", "api", "RadioManager"],
    install_requires=REQUIRES,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    RadioManager
    """
)
