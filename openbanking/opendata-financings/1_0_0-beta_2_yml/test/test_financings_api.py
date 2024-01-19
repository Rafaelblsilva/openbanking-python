# coding: utf-8

"""
    API OpenData Financings do Open Finance Brasil

    A API descrita neste documento é referente as API Financings da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-beta.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import opendata-financings_1_0_0-beta_2_yml
from opendata-financings_1_0_0-beta_2_yml.api.financings_api import FinancingsApi  # noqa: E501
from opendata-financings_1_0_0-beta_2_yml.rest import ApiException


class TestFinancingsApi(unittest.TestCase):
    """FinancingsApi unit test stubs"""

    def setUp(self):
        self.api = FinancingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_business_financings(self):
        """Test case for get_business_financings

        Obtém a lista de Financiamentos de Pessoa Jurídica.  # noqa: E501
        """
        pass

    def test_get_personal_financings(self):
        """Test case for get_personal_financings

        Obtém a lista de Financiamentos de Pessoa Natural.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()