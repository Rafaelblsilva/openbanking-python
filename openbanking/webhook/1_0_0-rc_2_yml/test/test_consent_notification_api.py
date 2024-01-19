# coding: utf-8

"""
    API Webhook - Open Finance Brasil

    API de Webhook é responsável por notificar eventos definidos em cada uma das APIs que possuem a funcionalidade no Open Finance Brasil.    Informações sobre endpoints suportados e funcionamento podem ser encontrados na página <a href=\"https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/105021661/Conven+o+de+Webhook\">Convenção de Webhook</a>, disponível no portal do desenvolvedor do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import webhook_1_0_0-rc_2_yml
from webhook_1_0_0-rc_2_yml.api.consent_notification_api import ConsentNotificationApi  # noqa: E501
from webhook_1_0_0-rc_2_yml.rest import ApiException


class TestConsentNotificationApi(unittest.TestCase):
    """ConsentNotificationApi unit test stubs"""

    def setUp(self):
        self.api = ConsentNotificationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_consent_notification(self):
        """Test case for consent_notification

        Notificações de mudanças de estados de consentimentos da API de Iniciação de Pagamentos.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()