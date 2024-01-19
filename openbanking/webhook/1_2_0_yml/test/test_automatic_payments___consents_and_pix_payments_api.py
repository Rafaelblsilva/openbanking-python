# coding: utf-8

"""
    API Webhook - Open Finance Brasil

    API de Webhook é responsável por notificar eventos definidos em cada uma das APIs que possuem a funcionalidade no Open Finance Brasil.    Informações sobre endpoints suportados e funcionamento podem ser encontrados na página <a href=\"https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/105021661/Conven+o+de+Webhook\">Convenção de Webhook</a>, disponível no portal do desenvolvedor do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import webhook_1_2_0_yml
from webhook_1_2_0_yml.api.automatic_payments___consents_and_pix_payments_api import AutomaticPaymentsConsentsAndPixPaymentsApi  # noqa: E501
from webhook_1_2_0_yml.rest import ApiException


class TestAutomaticPaymentsConsentsAndPixPaymentsApi(unittest.TestCase):
    """AutomaticPaymentsConsentsAndPixPaymentsApi unit test stubs"""

    def setUp(self):
        self.api = AutomaticPaymentsConsentsAndPixPaymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_recurring_consent_id_notification(self):
        """Test case for recurring_consent_id_notification

        Notificações de mudanças da entidade de consentimentos da API de Pagamentos automáticos.  # noqa: E501
        """
        pass

    def test_recurring_payment_id_notification(self):
        """Test case for recurring_payment_id_notification

        Notificações de mudanças da entidade de pagamentos da API de Pagamentos automáticos.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()