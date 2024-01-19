# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    Família de API para permitir o pagamento sem redirecionamento via Open Finance Brasil.   Permite tanto o gerenciamento dos dispositivos vinculados as contas quanto a autorização de consentimentos criados via fluxo sem redirecionamento.   # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import enrollments_1_1_0_yml
from enrollments_1_1_0_yml.api.consentimento_api import ConsentimentoApi  # noqa: E501
from enrollments_1_1_0_yml.rest import ApiException


class TestConsentimentoApi(unittest.TestCase):
    """ConsentimentoApi unit test stubs"""

    def setUp(self):
        self.api = ConsentimentoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authorize_consent(self):
        """Test case for authorize_consent

        Autorização de um consentimento de pagamentos na jornada sem redirecionamento  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()