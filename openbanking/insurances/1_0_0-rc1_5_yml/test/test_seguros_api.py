# coding: utf-8

"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.5
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import insurances_1_0_0-rc1_5_yml
from insurances_1_0_0-rc1_5_yml.api.seguros_api import SegurosApi  # noqa: E501
from insurances_1_0_0-rc1_5_yml.rest import ApiException


class TestSegurosApi(unittest.TestCase):
    """SegurosApi unit test stubs"""

    def setUp(self):
        self.api = SegurosApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_automotive_insurance(self):
        """Test case for get_automotive_insurance

        Conjunto de informações referentes a seguros automotivos de uma instituição  # noqa: E501
        """
        pass

    def test_get_home_insurance(self):
        """Test case for get_home_insurance

        Conjunto de informações referentes a seguros residenciais de uma instituição  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
