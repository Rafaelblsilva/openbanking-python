# coding: utf-8

# flake8: noqa

"""
    API Consents - Open Banking Brasil

    API que trata da criação, consulta e revogação de consentimentos para o Open Banking Brasil Fase 2 - customer-data.   Não possui segregação entre pessoa natural e pessoa jurídica.      # Orientações importantes A API Consents trata dos consentimentos exclusivamente para a fase 2 do Open Banking Brasil. - As informações da instituição receptora não trafegam na API Consents – a autenticação da receptora se dá através do [DCR](https://openbanking-brasil.github.io/specs-seguranca/open-banking-brasil-dynamic-client-registration-1_ID1.html).    - Na chamada para a criação do consentimento deve-se utilizar um token gerado via `client_credentials`. - Após o `POST` de criação do consentimento, o `STATUS` devolvido na resposta deverá ser `AWAITING_AUTHORISATION`. - O `STATUS` será alterado para `AUTHORISED` somente após autenticação e confirmação por parte do usuário na instituição transmissora dos dados. - Todas as datas trafegadas nesta API seguem o padrão da [RFC3339](https://tools.ietf.org/html/rfc3339) e formato \"zulu\". - A descrição do fluxo de consentimento encontra-se disponível no [Portal do desenvolvedor](https://openbanking-brasil.github.io/areadesenvolvedor/#em-revisao-fluxo-de-consentimento). - O arquivo com o mapeamento completo entre `Roles`, `scopes` e `permissions` está disponibilizado no Portal do desenvolvedor, no mesmo item acima - descrição do fluxo de consentimento. - É de responsabilidade da instituição receptora de dados, no pedido de criação do consentimento, o envio de todas as `permissions` correspondentes aos agrupamentos de dados selecionados pelo cliente e necessárias às consultas nos endpoints de cada uma das APIs de dados.        # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.7
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from consents_1_0_0-rc6_7_yml.api.consents_api import ConsentsApi
# import ApiClient
from consents_1_0_0-rc6_7_yml.api_client import ApiClient
from consents_1_0_0-rc6_7_yml.configuration import Configuration
# import models into sdk package
from consents_1_0_0-rc6_7_yml.models.business_entity import BusinessEntity
from consents_1_0_0-rc6_7_yml.models.business_entity_document import BusinessEntityDocument
from consents_1_0_0-rc6_7_yml.models.create_consent import CreateConsent
from consents_1_0_0-rc6_7_yml.models.create_consent_data import CreateConsentData
from consents_1_0_0-rc6_7_yml.models.links import Links
from consents_1_0_0-rc6_7_yml.models.logged_user import LoggedUser
from consents_1_0_0-rc6_7_yml.models.logged_user_document import LoggedUserDocument
from consents_1_0_0-rc6_7_yml.models.meta import Meta
from consents_1_0_0-rc6_7_yml.models.response_consent import ResponseConsent
from consents_1_0_0-rc6_7_yml.models.response_consent_data import ResponseConsentData
from consents_1_0_0-rc6_7_yml.models.response_error import ResponseError
from consents_1_0_0-rc6_7_yml.models.response_error_errors import ResponseErrorErrors
