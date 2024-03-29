# coding: utf-8

"""
    API's OpenData do Open Finance Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import products-services_3_0_0_yml
from products-services_3_0_0_yml.api.accounts_api import AccountsApi  # noqa: E501
from products-services_3_0_0_yml.rest import ApiException


class TestAccountsApi(unittest.TestCase):
    """AccountsApi unit test stubs"""

    def setUp(self):
        self.api = AccountsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_business_accounts(self):
        """Test case for get_business_accounts

        Obtém dados das contas pessoa jurídica  # noqa: E501
        """
        pass

    def test_get_personal_accounts(self):
        """Test case for get_personal_accounts

        Obtém dados das contas pessoa natural  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
