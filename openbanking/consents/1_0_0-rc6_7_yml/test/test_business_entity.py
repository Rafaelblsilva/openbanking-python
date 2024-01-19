# coding: utf-8

"""
    API Consents - Open Banking Brasil

    API que trata da criação, consulta e revogação de consentimentos para o Open Banking Brasil Fase 2 - customer-data.   Não possui segregação entre pessoa natural e pessoa jurídica.      # Orientações importantes A API Consents trata dos consentimentos exclusivamente para a fase 2 do Open Banking Brasil. - As informações da instituição receptora não trafegam na API Consents – a autenticação da receptora se dá através do [DCR](https://openbanking-brasil.github.io/specs-seguranca/open-banking-brasil-dynamic-client-registration-1_ID1.html).    - Na chamada para a criação do consentimento deve-se utilizar um token gerado via `client_credentials`. - Após o `POST` de criação do consentimento, o `STATUS` devolvido na resposta deverá ser `AWAITING_AUTHORISATION`. - O `STATUS` será alterado para `AUTHORISED` somente após autenticação e confirmação por parte do usuário na instituição transmissora dos dados. - Todas as datas trafegadas nesta API seguem o padrão da [RFC3339](https://tools.ietf.org/html/rfc3339) e formato \"zulu\". - A descrição do fluxo de consentimento encontra-se disponível no [Portal do desenvolvedor](https://openbanking-brasil.github.io/areadesenvolvedor/#em-revisao-fluxo-de-consentimento). - O arquivo com o mapeamento completo entre `Roles`, `scopes` e `permissions` está disponibilizado no Portal do desenvolvedor, no mesmo item acima - descrição do fluxo de consentimento. - É de responsabilidade da instituição receptora de dados, no pedido de criação do consentimento, o envio de todas as `permissions` correspondentes aos agrupamentos de dados selecionados pelo cliente e necessárias às consultas nos endpoints de cada uma das APIs de dados.        # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.7
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import consents_1_0_0-rc6_7_yml
from consents_1_0_0-rc6_7_yml.models.business_entity import BusinessEntity  # noqa: E501
from consents_1_0_0-rc6_7_yml.rest import ApiException


class TestBusinessEntity(unittest.TestCase):
    """BusinessEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBusinessEntity(self):
        """Test BusinessEntity"""
        # FIXME: construct object with mandatory attributes with example values
        # model = consents_1_0_0-rc6_7_yml.models.business_entity.BusinessEntity()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
