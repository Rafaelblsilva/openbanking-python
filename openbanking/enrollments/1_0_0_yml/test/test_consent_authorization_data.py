# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    Família de API para permitir o pagamento sem redirecionamento via Open Finance Brasil.   Permite tanto o gerenciamento dos dispositivos vinculados as contas quanto a autorização de consentimentos criados via fluxo sem redirecionamento.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import enrollments_1_0_0_yml
from enrollments_1_0_0_yml.models.consent_authorization_data import ConsentAuthorizationData  # noqa: E501
from enrollments_1_0_0_yml.rest import ApiException


class TestConsentAuthorizationData(unittest.TestCase):
    """ConsentAuthorizationData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConsentAuthorizationData(self):
        """Test ConsentAuthorizationData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = enrollments_1_0_0_yml.models.consent_authorization_data.ConsentAuthorizationData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
