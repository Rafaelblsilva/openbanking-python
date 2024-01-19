# coding: utf-8

"""
    API Loans - Open Banking Brasil

    API de informações de operações de empréstimos do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo empréstimo, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Loans  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **LOANS_READ** ### `/contracts/{contractId}`   - permissions:      - GET **LOANS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **LOANS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **LOANS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **LOANS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "loans-1-0-2-yml"
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
    description="API Loans - Open Banking Brasil",
    author_email="gt-interfaces@openbankingbr.org",
    url="",
    keywords=["Swagger", "API Loans - Open Banking Brasil"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    API de informações de operações de empréstimos do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo empréstimo, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os &#x60;endpoints&#x60;.  # Orientações A &#x60;Role&#x60;  do diretório de participantes relacionada à presente API é a &#x60;DADOS&#x60;.\\ Para todos os &#x60;endpoints&#x60; desta API é previsto o envio de um &#x60;token&#x60; através do header &#x60;Authorization&#x60;.\\ Este token deverá estar relacionado ao consentimento (&#x60;consentId&#x60;) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao &#x60;consentId&#x60; específico relacionado.\\ Os dados serão devolvidos na consulta desde que o &#x60;consentId&#x60; relacionado corresponda a um consentimento válido e com o status &#x60;AUTHORISED&#x60;.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as &#x60;permissions&#x60; necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (&#x60;consentId&#x60;).\\ Relacionamos a seguir as &#x60;permissions&#x60; necessárias para a consulta de dados em cada &#x60;endpoint&#x60; da presente API.  ## Permissions necessárias para a API Loans  Para cada um dos paths desta API, além dos escopos (&#x60;scopes&#x60;) indicados existem &#x60;permissions&#x60; que deverão ser observadas:  ### &#x60;/contracts&#x60;   - permissions:     - GET: **LOANS_READ** ### &#x60;/contracts/{contractId}&#x60;   - permissions:      - GET **LOANS_READ** ### &#x60;/contracts/{contractId}/warranties&#x60;   - permissions:     - GET: **LOANS_WARRANTIES_READ** ### &#x60;/contracts/{contractId}/scheduled-instalments&#x60;   - permissions:     - GET: **LOANS_SCHEDULED_INSTALMENTS_READ** ### &#x60;/contracts/{contractId}/payments&#x60;   - permissions:     - GET: **LOANS_PAYMENTS_READ**   # noqa: E501
    """
)
