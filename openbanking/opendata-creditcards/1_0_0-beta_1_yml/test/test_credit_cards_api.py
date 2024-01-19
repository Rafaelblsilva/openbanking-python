# coding: utf-8

"""
    API OpenData Credit Cards do Open Finance Brasil

    A API descrita neste documento é referente as API Credit Cards da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import opendata-creditcards_1_0_0-beta_1_yml
from opendata-creditcards_1_0_0-beta_1_yml.api.credit_cards_api import CreditCardsApi  # noqa: E501
from opendata-creditcards_1_0_0-beta_1_yml.rest import ApiException


class TestCreditCardsApi(unittest.TestCase):
    """CreditCardsApi unit test stubs"""

    def setUp(self):
        self.api = CreditCardsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_business_credit_cards(self):
        """Test case for get_business_credit_cards

        Obtém dados sobre cartões de crédito pessoa jurídica  # noqa: E501
        """
        pass

    def test_get_personal_credit_cards(self):
        """Test case for get_personal_credit_cards

        Obtém dados sobre cartões de crédito pessoa natural  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()