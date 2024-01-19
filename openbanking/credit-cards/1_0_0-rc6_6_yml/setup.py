# coding: utf-8

"""
    API Credit-cards-accounts - Open Banking Brasil

    API de contas de pagamento pós-pagas do Open Banking Brasil – Fase 2. API que retorna informações de contas de pagamento pós-paga mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, produto, bandeira, limites de crédito, informações sobre transações de pagamento efetuadas e faturas.  Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.   # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.    ## Permissions necessárias para a API Credit-cards-accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}/bills`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_READ** ### `/accounts/{creditCardAccountId}/{billId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/limits`           - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_LIMITS_READ** ### `/accounts/{creditCardAccountId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.6
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "credit-cards-1-0-0-rc6-6-yml"
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
    description="API Credit-cards-accounts - Open Banking Brasil",
    author_email="gt-interfaces@openbankingbr.org",
    url="",
    keywords=["Swagger", "API Credit-cards-accounts - Open Banking Brasil"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    API de contas de pagamento pós-pagas do Open Banking Brasil – Fase 2. API que retorna informações de contas de pagamento pós-paga mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, produto, bandeira, limites de crédito, informações sobre transações de pagamento efetuadas e faturas.  Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os &#x60;endpoints&#x60;.   # Orientações A &#x60;Role&#x60;  do diretório de participantes relacionada à presente API é a &#x60;DADOS&#x60;.\\ Para todos os &#x60;endpoints&#x60; desta API é previsto o envio de um &#x60;token&#x60; através do header &#x60;Authorization&#x60;.\\ Este token deverá estar relacionado ao consentimento (&#x60;consentId&#x60;) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao &#x60;consentId&#x60; específico relacionado.\\ Os dados serão devolvidos na consulta desde que o &#x60;consentId&#x60; relacionado corresponda a um consentimento válido e com o status &#x60;AUTHORISED&#x60;.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as &#x60;permissions&#x60; necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (&#x60;consentId&#x60;).\\ Relacionamos a seguir as &#x60;permissions&#x60; necessárias para a consulta de dados em cada &#x60;endpoint&#x60; da presente API.    ## Permissions necessárias para a API Credit-cards-accounts  Para cada um dos paths desta API, além dos escopos (&#x60;scopes&#x60;) indicados existem &#x60;permissions&#x60; que deverão ser observadas:  ### &#x60;/accounts&#x60;   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### &#x60;/accounts/{creditCardAccountId}&#x60;   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### &#x60;/accounts/{creditCardAccountId}/bills&#x60;   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_READ** ### &#x60;/accounts/{creditCardAccountId}/{billId}/transactions&#x60;   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ** ### &#x60;/accounts/{creditCardAccountId}/limits&#x60;           - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_LIMITS_READ** ### &#x60;/accounts/{creditCardAccountId}/transactions&#x60;   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ**   # noqa: E501
    """
)
