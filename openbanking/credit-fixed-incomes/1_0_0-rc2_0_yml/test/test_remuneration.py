# coding: utf-8

"""
    API Credit Fixed Incomes - Open Finance Brasil

    API de informações de operações de Renda Fixa Crédito do Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Renda Fixa Crédito (Debêntures, CRI/CRA) mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação do produto, rentabilidade, quantidade, prazos, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. A exposição se dará por cada operação de renda fixa contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import credit-fixed-incomes_1_0_0-rc2_0_yml
from credit-fixed-incomes_1_0_0-rc2_0_yml.models.remuneration import Remuneration  # noqa: E501
from credit-fixed-incomes_1_0_0-rc2_0_yml.rest import ApiException


class TestRemuneration(unittest.TestCase):
    """Remuneration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRemuneration(self):
        """Test Remuneration"""
        # FIXME: construct object with mandatory attributes with example values
        # model = credit-fixed-incomes_1_0_0-rc2_0_yml.models.remuneration.Remuneration()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
