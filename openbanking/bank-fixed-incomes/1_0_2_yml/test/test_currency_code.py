# coding: utf-8

"""
    API Bank Fixed Incomes - Open Finance Brasil

    API de informações de operações de Renda Fixa Bancária Open Finance Brasil (Fase 4). API que retorna informações de operações de investimento do tipo Renda Fixa Bancária (CDB/RDB, LCI e LCA) mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação do produto, rentabilidade, quantidade, prazos, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. A exposição se dará por cada operação de renda fixa contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import bank-fixed-incomes_1_0_2_yml
from bank-fixed-incomes_1_0_2_yml.models.currency_code import CurrencyCode  # noqa: E501
from bank-fixed-incomes_1_0_2_yml.rest import ApiException


class TestCurrencyCode(unittest.TestCase):
    """CurrencyCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCurrencyCode(self):
        """Test CurrencyCode"""
        # FIXME: construct object with mandatory attributes with example values
        # model = bank-fixed-incomes_1_0_2_yml.models.currency_code.CurrencyCode()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
