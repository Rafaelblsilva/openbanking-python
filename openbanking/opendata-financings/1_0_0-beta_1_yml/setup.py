# coding: utf-8

"""
    API OpenData Financings do Open Finance Brasil

    A API descrita neste documento é referente as API Financings da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "opendata-financings-1-0-0-beta-1-yml"
VERSION = "1.0.0"
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
    description="API OpenData Financings do Open Finance Brasil",
    author_email="",
    url="",
    keywords=["Swagger", "API OpenData Financings do Open Finance Brasil"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    A API descrita neste documento é referente as API Financings da fase OpenData do Open Finance Brasil.  # noqa: E501
    """
)
