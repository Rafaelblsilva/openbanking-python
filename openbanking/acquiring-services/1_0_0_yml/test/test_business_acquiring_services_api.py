# coding: utf-8

"""
    API Acquiring Services - Open Finance Brasil

    API de Credenciamento do Open Finance Brasil – Fase 4. API que retorna informações de Credenciamento.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import acquiring-services_1_0_0_yml
from acquiring-services_1_0_0_yml.api.business_acquiring_services_api import BusinessAcquiringServicesApi  # noqa: E501
from acquiring-services_1_0_0_yml.rest import ApiException


class TestBusinessAcquiringServicesApi(unittest.TestCase):
    """BusinessAcquiringServicesApi unit test stubs"""

    def setUp(self):
        self.api = BusinessAcquiringServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_business_acquiring_services(self):
        """Test case for get_business_acquiring_services

        Conjunto de informações de Credenciamento para Pessoa Jurídica.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
