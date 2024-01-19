# coding: utf-8

"""
    API Resources - Open Banking Brasil

    API que trata da consulta do status de recursos para o Open Banking Brasil - Fase 2.\\ Não possui segregação entre pessoa natural e pessoa jurídica.  # Orientações importantes - A API resources lista os recursos vinculados ao consentimento específico, identificado por `consentId` e vinculado ao token enviado no header `Authorization`. - Os `STATUS` dos recursos listados DEVEM considerar não apenas o consentimento vinculado mas também a disponibilidade do recurso na instituição transmissora dos dados. - Na lista de recursos devolvida na API resources somente constará informação no atributo `resourceId` para recursos com o `STATUS` `AVAILABLE`. - Para os demais `STATUS` não é devolvido o identificador do recurso - `resourceId`. - A `permission` específica desta API  - `RESOURCES_READ` - DEVE ser solicitada pela instituição receptora na ocasião do pedido de criação do consentimento. - A consulta à API Resources não é obrigatória por parte das instituições receptoras - esta API foi criada para dar visibilidade da existência de ocorrências que possam impedir o compartilhamento de determinados recursos por parte da instituição transmissora dos dados. - O identificador do recurso devolvido na API Resources - `resourceId` - quando apresentado corresponde ao mesmo identificador designado para o recurso em sua API específica, o seja: o `resourceId` corresponde ao `accountId` da API accounts, ao `creditCardAccountId` da API de conta pós-paga e assim sucessivamente.  ## Status previstos para os recursos listados na API Resources - AVAILABLE: indica que o recurso encontra-se disponível e o(s) consentimento(s) associado(s) possui(em) status `AUTHORISED`. - UNAVAILABLE: indica que o recurso não está mais disponível, por exemplo, em caso de uma conta encerrada. - TEMPORARILY_UNAVAILABLE: indica que o recurso encontra-se temporariamente indisponível, embora o(s) consentimento(s) associado(s) possua(m) status `AUTHORISED`.   Caso de exemplo: conta temporariamente bloqueada por suspeita de fraude. - PENDING_AUTHORISATION: indica a existência de pendências para o compartilhamento do recurso, por exemplo, em caso de alçada dupla, quando é necessário o consentimento de mais de um titular.  ## Permissions necessárias para a API Resources ### `/resources`   - permissions:     - GET: **RESOURCES_READ**   # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "resources-1-0-2-yml"
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
    description="API Resources - Open Banking Brasil",
    author_email="gt-interfaces@openbankingbr.org",
    url="",
    keywords=["Swagger", "API Resources - Open Banking Brasil"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    API que trata da consulta do status de recursos para o Open Banking Brasil - Fase 2.\\ Não possui segregação entre pessoa natural e pessoa jurídica.  # Orientações importantes - A API resources lista os recursos vinculados ao consentimento específico, identificado por &#x60;consentId&#x60; e vinculado ao token enviado no header &#x60;Authorization&#x60;. - Os &#x60;STATUS&#x60; dos recursos listados DEVEM considerar não apenas o consentimento vinculado mas também a disponibilidade do recurso na instituição transmissora dos dados. - Na lista de recursos devolvida na API resources somente constará informação no atributo &#x60;resourceId&#x60; para recursos com o &#x60;STATUS&#x60; &#x60;AVAILABLE&#x60;. - Para os demais &#x60;STATUS&#x60; não é devolvido o identificador do recurso - &#x60;resourceId&#x60;. - A &#x60;permission&#x60; específica desta API  - &#x60;RESOURCES_READ&#x60; - DEVE ser solicitada pela instituição receptora na ocasião do pedido de criação do consentimento. - A consulta à API Resources não é obrigatória por parte das instituições receptoras - esta API foi criada para dar visibilidade da existência de ocorrências que possam impedir o compartilhamento de determinados recursos por parte da instituição transmissora dos dados. - O identificador do recurso devolvido na API Resources - &#x60;resourceId&#x60; - quando apresentado corresponde ao mesmo identificador designado para o recurso em sua API específica, o seja: o &#x60;resourceId&#x60; corresponde ao &#x60;accountId&#x60; da API accounts, ao &#x60;creditCardAccountId&#x60; da API de conta pós-paga e assim sucessivamente.  ## Status previstos para os recursos listados na API Resources - AVAILABLE: indica que o recurso encontra-se disponível e o(s) consentimento(s) associado(s) possui(em) status &#x60;AUTHORISED&#x60;. - UNAVAILABLE: indica que o recurso não está mais disponível, por exemplo, em caso de uma conta encerrada. - TEMPORARILY_UNAVAILABLE: indica que o recurso encontra-se temporariamente indisponível, embora o(s) consentimento(s) associado(s) possua(m) status &#x60;AUTHORISED&#x60;.   Caso de exemplo: conta temporariamente bloqueada por suspeita de fraude. - PENDING_AUTHORISATION: indica a existência de pendências para o compartilhamento do recurso, por exemplo, em caso de alçada dupla, quando é necessário o consentimento de mais de um titular.  ## Permissions necessárias para a API Resources ### &#x60;/resources&#x60;   - permissions:     - GET: **RESOURCES_READ**   # noqa: E501
    """
)
