# coding: utf-8

"""
    API Treasure Titles - Open Finance Brasil

    API de informações de operações de Títulos do Tesouro Direto Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Títulos do Tesouro Direto mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. Devem ser considerados como escopo de exposição todos os títulos ofertados pelo Tesouro Direto. A exposição se dará por cada operação de títulos do Tesouro Direto contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc3.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import treasure-titles_1_0_0-rc3_0_yml
from treasure-titles_1_0_0-rc3_0_yml.api.product_list_api import ProductListApi  # noqa: E501
from treasure-titles_1_0_0-rc3_0_yml.rest import ApiException


class TestProductListApi(unittest.TestCase):
    """ProductListApi unit test stubs"""

    def setUp(self):
        self.api = ProductListApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_treasure_titles_get_investments(self):
        """Test case for treasure_titles_get_investments

        Obtém a lista de operações de Títulos do Tesouro Direto mantidas pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
