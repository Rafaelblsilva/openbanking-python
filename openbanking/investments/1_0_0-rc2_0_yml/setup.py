# coding: utf-8

"""
    API Investments - Open Finance Brasil

    Estas APIs visam o compartilhamento de dados sobre Investimentos e suas características entre as Instituições Financeiras participantes do Open Finance Brasil   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "investments-1-0-0-rc2-0-yml"
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
    description="API Investments - Open Finance Brasil",
    author_email="gt-interfaces@openbankingbr.org",
    url="",
    keywords=["Swagger", "API Investments - Open Finance Brasil"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Estas APIs visam o compartilhamento de dados sobre Investimentos e suas características entre as Instituições Financeiras participantes do Open Finance Brasil   # noqa: E501
    """
)
