# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import common_1_0_0-rc5_yml
from common_1_0_0-rc5_yml.api.discovery_api import DiscoveryApi  # noqa: E501
from common_1_0_0-rc5_yml.rest import ApiException


class TestDiscoveryApi(unittest.TestCase):
    """DiscoveryApi unit test stubs"""

    def setUp(self):
        self.api = DiscoveryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_outage(self):
        """Test case for get_outage

        a descrição referente ao código de status retornado pelas APIs  # noqa: E501
        """
        pass

    def test_get_status(self):
        """Test case for get_status

        a descrição referente ao código de status retornado pelas APIs  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
