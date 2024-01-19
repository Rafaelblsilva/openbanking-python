# coding: utf-8

"""
    API Webhook - Open Finance Brasil

    API de Webhook é responsável por notificar eventos definidos em cada uma das APIs que possuem a funcionalidade no Open Finance Brasil.  <u>Endpoints que possuem a funcionalidade de Webhook</u> <br/>  Na versão atual, temos os seguintes endpoints:   API Payments v2:   - POST /pix/payments   - POST /consents  # Orientações <u>Todos os endpoints nessa API utilizam-se de mTLS para autenticação, não possuem scopes e permissions específicos de segurança. Toda a segurança é feita via certificado(mTLS – BRCAC).</u>  Dado que as URLs do ecossistema são formadas com a configuração abaixo:   \\<host> / \\<string> / \\<api> / \\<versão> / \\<recurso>  <u>Para a utilização desse recurso é necessário que:</u> - Iniciadoras de pagamentos e/ou Receptora de dados: Precisam cadastrar a sua URI base (\\<host>) no diretório de participantes no campo `<CAMPO_A_DEFINIR>`, - Detentoras de contas e/ou Transmissora de dados: Precisam construir a URI de notificação da seguinte forma:  <u>Exemplo de URI do consentimento:</u> <br/> <br/> <img src=\"./img/image001.png\" alt=\"Image Webhook\"/> <br/> <br/>  <u>Exemplo de URI do pagamento:</u> <br/> <br/> <img src=\"./img/image002.png\" alt=\"Image Webhook\"/>   # noqa: E501

    OpenAPI spec version: 1.0.0-beta1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import webhook_1_0_0-beta1_yml
from webhook_1_0_0-beta1_yml.api.pix_payment_notification_api import PixPaymentNotificationApi  # noqa: E501
from webhook_1_0_0-beta1_yml.rest import ApiException


class TestPixPaymentNotificationApi(unittest.TestCase):
    """PixPaymentNotificationApi unit test stubs"""

    def setUp(self):
        self.api = PixPaymentNotificationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_pix_payment_notification(self):
        """Test case for pix_payment_notification

        Notificações de mudanças de estados do pagamento: Arranjo Pix da API de Iniciação de Pagamentos.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
