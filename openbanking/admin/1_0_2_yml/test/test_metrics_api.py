# coding: utf-8

"""
    APIs Admin do Open Finance Brasil

    As API's administrativas são recursos que podem ser consumidos apenas pelo diretório para avaliação e controle da qualidade dos serviços fornecidos pelas instituições financeiras  # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import admin_1_0_2_yml
from admin_1_0_2_yml.api.metrics_api import MetricsApi  # noqa: E501
from admin_1_0_2_yml.rest import ApiException


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self):
        self.api = MetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_metrics(self):
        """Test case for get_metrics

        Obtém as métricas de disponibilidade das APIs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
