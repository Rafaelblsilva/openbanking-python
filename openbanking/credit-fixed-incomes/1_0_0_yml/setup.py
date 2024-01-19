# coding: utf-8

"""
    API Credit Fixed Incomes - Open Finance Brasil

    API de informações de operações de Renda Fixa Crédito do Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Renda Fixa Crédito (Debêntures, CRI/CRA) mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação do produto, rentabilidade, quantidade, prazos, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. A exposição se dará por cada operação de renda fixa contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "credit-fixed-incomes-1-0-0-yml"
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
    description="API Credit Fixed Incomes - Open Finance Brasil",
    author_email="gt-interfaces@openbankingbr.org",
    url="",
    keywords=["Swagger", "API Credit Fixed Incomes - Open Finance Brasil"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    API de informações de operações de Renda Fixa Crédito do Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Renda Fixa Crédito (Debêntures, CRI/CRA) mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação do produto, rentabilidade, quantidade, prazos, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. A exposição se dará por cada operação de renda fixa contratada pelo cliente.   # noqa: E501
    """
)