# coding: utf-8

"""
    API OpenData Accounts do Open Finance Brasil

    A API descrita neste documento é referente as API Accounts da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import opendata-accounts_1_0_0-beta_1_yml
from opendata-accounts_1_0_0-beta_1_yml.api.accounts_api import AccountsApi  # noqa: E501
from opendata-accounts_1_0_0-beta_1_yml.rest import ApiException


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
