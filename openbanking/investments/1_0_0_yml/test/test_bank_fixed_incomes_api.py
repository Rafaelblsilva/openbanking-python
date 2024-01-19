# coding: utf-8

"""
    API Investments - Open Finance Brasil

    Estas APIs visam o compartilhamento de dados sobre Investimentos e suas características entre as Instituições Financeiras participantes do Open Finance Brasil   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import investments_1_0_0_yml
from investments_1_0_0_yml.api.bank_fixed_incomes_api import BankFixedIncomesApi  # noqa: E501
from investments_1_0_0_yml.rest import ApiException


class TestBankFixedIncomesApi(unittest.TestCase):
    """BankFixedIncomesApi unit test stubs"""

    def setUp(self):
        self.api = BankFixedIncomesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_investments_get_fixed_income_bank(self):
        """Test case for investments_get_fixed_income_bank

        Conjunto de informações de produtos de Renda Fixa Bancária (CDB, RDB, LCI e LCA)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
