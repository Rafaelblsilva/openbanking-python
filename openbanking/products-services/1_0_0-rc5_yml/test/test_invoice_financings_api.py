# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import products-services_1_0_0-rc5_yml
from products-services_1_0_0-rc5_yml.api.invoice_financings_api import InvoiceFinancingsApi  # noqa: E501
from products-services_1_0_0-rc5_yml.rest import ApiException


class TestInvoiceFinancingsApi(unittest.TestCase):
    """InvoiceFinancingsApi unit test stubs"""

    def setUp(self):
        self.api = InvoiceFinancingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_business_invoice_financings(self):
        """Test case for get_business_invoice_financings

        Obtém a lista de Adiantamento de Recebíveis de Pessoa Jurídica.  # noqa: E501
        """
        pass

    def test_get_personal_invoice_financings(self):
        """Test case for get_personal_invoice_financings

        Obtém a lista de Adiantamento de Recebíveis de Pessoa Natural.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
