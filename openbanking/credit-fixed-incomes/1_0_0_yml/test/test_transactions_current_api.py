# coding: utf-8

"""
    API Credit Fixed Incomes - Open Finance Brasil

    API de informações de operações de Renda Fixa Crédito do Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Renda Fixa Crédito (Debêntures, CRI/CRA) mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação do produto, rentabilidade, quantidade, prazos, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. A exposição se dará por cada operação de renda fixa contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import credit-fixed-incomes_1_0_0_yml
from credit-fixed-incomes_1_0_0_yml.api.transactions_current_api import TransactionsCurrentApi  # noqa: E501
from credit-fixed-incomes_1_0_0_yml.rest import ApiException


class TestTransactionsCurrentApi(unittest.TestCase):
    """TransactionsCurrentApi unit test stubs"""

    def setUp(self):
        self.api = TransactionsCurrentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_credit_fixed_incomes_get_investments_investment_id_transactions_current(self):
        """Test case for credit_fixed_incomes_get_investments_investment_id_transactions_current

        Obtém as movimentações recentes da operação de Renda Fixa Crédito identificada por investmentId. O período a ser considerado para apresentação de movimentações será de até 7 dias - 7 dias anteriores da consulta, incluindo o dia da consulta (D-6).  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
