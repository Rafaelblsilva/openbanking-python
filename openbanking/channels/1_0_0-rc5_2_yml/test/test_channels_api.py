# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.2
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import channels_1_0_0-rc5_2_yml
from channels_1_0_0-rc5_2_yml.api.channels_api import ChannelsApi  # noqa: E501
from channels_1_0_0-rc5_2_yml.rest import ApiException


class TestChannelsApi(unittest.TestCase):
    """ChannelsApi unit test stubs"""

    def setUp(self):
        self.api = ChannelsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_banking_agents(self):
        """Test case for get_banking_agents

        Obtém a lista de correspondentes bancários da instituição financeira.  # noqa: E501
        """
        pass

    def test_get_branches(self):
        """Test case for get_branches

        Obtém a lista de dependências próprias da instituição financeira.  # noqa: E501
        """
        pass

    def test_get_electronic_channels(self):
        """Test case for get_electronic_channels

        Obtém a lista de canais eletrônicos de atendimento da instituição financeira.  # noqa: E501
        """
        pass

    def test_get_phone_channels(self):
        """Test case for get_phone_channels

        Obtém a lista de canais telefônicos de atendimento da instituição financeira.  # noqa: E501
        """
        pass

    def test_get_shared_automated_teller_machines(self):
        """Test case for get_shared_automated_teller_machines

        Obtém a lista de terminais compartilhados de autoatendimento.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
