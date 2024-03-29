# coding: utf-8

"""
    API Funds - Open Finance Brasil

    API de informações de operações de Fundos de Investimento Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Fundos de Investimento mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente e movimentações financeiras.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  Devem ser considerados como escopo de exposição todos os fundos de investimento classificados como: Renda Fixa, Ações, Multimercado e Cambial.  Para identificação do produto e posição do cliente, a exposição será de forma consolidada por Fundo de Investimento.  Para movimentações, a exposição se dará pela Ordem do Cliente, por exemplo, uma Ordem de Resgate é compartilhada como uma única movimentação, mesmo que esteja associada a diferentes Certificados (Cautelas).  As instituições podem apresentar cenários distintos no que diz respeito ao sincronismo entre posição `/balances` e movimentação `/transactions` e `/transactions-current` da API:  - Algumas instituições refletem movimentações ainda não convertidas na posição do cliente em seus canais eletrônicos. Isso implica que pode ocorrer compartilhamento de posição atualizada, cujas movimentações relacionadas serão expostas no ecossistema apenas após a conversão das mesmas;  - Outras instituições refletem na posição apenas movimentações convertidas nos seus canais eletrônicos. Isso implica que o compartilhamento da posição em relação às movimentações é feito de forma sincronizada no ecossistema.  Para o identificador do investimento (investmentId) deve ser adotado o seguinte comportamento:  - Após 12 meses sem movimentações e com quantidade de ativos zerada, o resourceId correspondente ao investmentId em questão deve passar ao status UNAVAILABLE (considerando consentimento válido);  - Nas situações em que o cliente compre novamente o ativo após um período de 12 meses sem movimentação e com quantidade de ativos zerada, o mesmo identificador (investmentId) deve ser utilizado. Especificamente para tais produtos, o status do recurso na resources deve passar de UNAVAILABLE para AVAILABLE.   # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import funds_1_0_1_yml
from funds_1_0_1_yml.models.response_funds_balances import ResponseFundsBalances  # noqa: E501
from funds_1_0_1_yml.rest import ApiException


class TestResponseFundsBalances(unittest.TestCase):
    """ResponseFundsBalances unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseFundsBalances(self):
        """Test ResponseFundsBalances"""
        # FIXME: construct object with mandatory attributes with example values
        # model = funds_1_0_1_yml.models.response_funds_balances.ResponseFundsBalances()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
