# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, reponsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openId` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import payments_1_0_0-rc2_0_yml
from payments_1_0_0-rc2_0_yml.models.end_to_end_id import EndToEndId  # noqa: E501
from payments_1_0_0-rc2_0_yml.rest import ApiException


class TestEndToEndId(unittest.TestCase):
    """EndToEndId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEndToEndId(self):
        """Test EndToEndId"""
        # FIXME: construct object with mandatory attributes with example values
        # model = payments_1_0_0-rc2_0_yml.models.end_to_end_id.EndToEndId()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
