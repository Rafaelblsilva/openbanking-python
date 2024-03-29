# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    Família de API para permitir o pagamento sem redirecionamento via Open Finance Brasil.   Permite tanto o gerenciamento dos dispositivos vinculados as contas quanto a autorização de consentimentos criados via fluxo sem redirecionamento.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import enrollments_1_0_0_yml
from enrollments_1_0_0_yml.api.vnculo_de_dispositivo_api import VnculoDeDispositivoApi  # noqa: E501
from enrollments_1_0_0_yml.rest import ApiException


class TestVnculoDeDispositivoApi(unittest.TestCase):
    """VnculoDeDispositivoApi unit test stubs"""

    def setUp(self):
        self.api = VnculoDeDispositivoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_enrollment(self):
        """Test case for delete_enrollment

        Revogar ou rejeitar vínculo de conta.  # noqa: E501
        """
        pass

    def test_enrollment_create_fido_registration_options(self):
        """Test case for enrollment_create_fido_registration_options

        Obter parâmetros para criação de credenciais FIDO2.  # noqa: E501
        """
        pass

    def test_enrollment_create_fido_signing_options(self):
        """Test case for enrollment_create_fido_signing_options

        Obter parâmetros para autenticação FIDO2.  # noqa: E501
        """
        pass

    def test_enrollment_register_fido_credential(self):
        """Test case for enrollment_register_fido_credential

        Associação da credencial FIDO2 ao vínculo de conta.  # noqa: E501
        """
        pass

    def test_get_enrollment(self):
        """Test case for get_enrollment

        Consultar vínculo de conta.  # noqa: E501
        """
        pass

    def test_post_enrollments(self):
        """Test case for post_enrollments

        Criar vínculo de conta.  # noqa: E501
        """
        pass

    def test_risk_signals(self):
        """Test case for risk_signals

        Envio de sinais de risco para iniciação do vínculo de dispositivo  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
