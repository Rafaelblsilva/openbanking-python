# coding: utf-8

"""
    APIs Admin do Open Finance Brasil

    As API's administrativas são recursos que podem ser consumidos apenas pelo diretório para avaliação e controle da qualidade dos serviços fornecidos pelas instituições financeiras  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "admin-2-0-0-yml"
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
    description="APIs Admin do Open Finance Brasil",
    author_email="",
    url="",
    keywords=["Swagger", "APIs Admin do Open Finance Brasil"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    As API&#x27;s administrativas são recursos que podem ser consumidos apenas pelo diretório para avaliação e controle da qualidade dos serviços fornecidos pelas instituições financeiras  # noqa: E501
    """
)
