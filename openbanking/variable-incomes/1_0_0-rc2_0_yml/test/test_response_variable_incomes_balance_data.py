# coding: utf-8

"""
    API Variable Incomes - Open Finance Brasil

    API de informações de operações de Renda Variável Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Renda Variável mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente, movimentações financeiras e detalhes da nota de negociação.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  A granularidade de exposição de operações de renda variável se dá por cada ativo (ticker) da carteira do cliente.  Ações escriturais não fazem parte do escopo do Open Finance Brasil.  Operações de day trade devem ser incluídas nos endpoints.  Segue abaixo tabela com o escopo de produtos a ser considerado para compartilhamento:  ```    |----------------------|-------------------------------|----------------------|-----------------------------------|    | CLASSE DE ATIVOS     | PRODUTO                       | SUBPRODUTO           | DENOMINAÇÃO                       |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       |     -                | FIAGRO                            |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | Subscrição           | Bonus / Direito / Recibo          |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       | Fundo imobiliario    | FII                               |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | À vista              | ON / PN / UNIT                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF de Renda Variável             |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF Internacional                 |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF Renda Fixa       | ETF Renda Fixa                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    ```   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import variable-incomes_1_0_0-rc2_0_yml
from variable-incomes_1_0_0-rc2_0_yml.models.response_variable_incomes_balance_data import ResponseVariableIncomesBalanceData  # noqa: E501
from variable-incomes_1_0_0-rc2_0_yml.rest import ApiException


class TestResponseVariableIncomesBalanceData(unittest.TestCase):
    """ResponseVariableIncomesBalanceData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseVariableIncomesBalanceData(self):
        """Test ResponseVariableIncomesBalanceData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = variable-incomes_1_0_0-rc2_0_yml.models.response_variable_incomes_balance_data.ResponseVariableIncomesBalanceData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
