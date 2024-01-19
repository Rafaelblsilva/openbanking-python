# coding: utf-8

"""
    API Funds - Open Finance Brasil

    API de informações de operações de Fundos de Investimento Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Fundos de Investimento mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente e movimentações financeiras.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  Devem ser considerados como escopo de exposição todos os fundos de investimento classificados como: Renda Fixa, Ações, Multimercado e Cambial.  Para identificação do produto e posição do cliente, a exposição será de forma consolidada por Fundo de Investimento.  Para movimentações, a exposição se dará pela Ordem do Cliente, por exemplo, uma Ordem de Resgate é compartilhada como uma única movimentação, mesmo que esteja associada a diferentes Certificados (Cautelas).   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import funds_1_0_0-rc1_0_yml
from funds_1_0_0-rc1_0_yml.api.product_list_api import ProductListApi  # noqa: E501
from funds_1_0_0-rc1_0_yml.rest import ApiException


class TestProductListApi(unittest.TestCase):
    """ProductListApi unit test stubs"""

    def setUp(self):
        self.api = ProductListApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_funds_get_investments(self):
        """Test case for funds_get_investments

        Obtém a lista de operações de Fundos de Investimento mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
