# coding: utf-8

"""
    API Exchanges - Open Finance Brasil

    API de informações de operações de Câmbio Open Finance Brasil – Fase 4.  API que retorna informações de operações de Câmbio realizadas nas instituições transmissoras por seus clientes, incluindo dados como informações da operação contratada, valor da operação em moeda nacional e moeda estrangeira, classificação da operação, forma de entrega, VET e, quando aplicável, valor a liquidar.  Também serão compartilhados os eventos de alteração da operação, caso existam, com as informações modificadas.  Não possui segregação entre pessoa natural e pessoa jurídica.  Requer consentimento do cliente para todos os endpoints.  __São escopo de compartilhamento as operações de compra e venda de moeda estrangeira de liquidação pronta ou futura, inclusive com adiantamento.  Operações de câmbio anuladas não são escopo de exposição, bem como eventos de vinculação de operações.  A exposição se dará por cada operação de câmbio contratada pelo cliente.__   # noqa: E501

    OpenAPI spec version: 1.0.0-rc.3
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import exchanges_1_0_0-rc_3_yml
from exchanges_1_0_0-rc_3_yml.models.operation_details_foreign_operation_value import OperationDetailsForeignOperationValue  # noqa: E501
from exchanges_1_0_0-rc_3_yml.rest import ApiException


class TestOperationDetailsForeignOperationValue(unittest.TestCase):
    """OperationDetailsForeignOperationValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOperationDetailsForeignOperationValue(self):
        """Test OperationDetailsForeignOperationValue"""
        # FIXME: construct object with mandatory attributes with example values
        # model = exchanges_1_0_0-rc_3_yml.models.operation_details_foreign_operation_value.OperationDetailsForeignOperationValue()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
