# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    API de Dispositivo Vínculado para suportar Iniciação de Pagamentos na Jornada Sem Redirecionamento do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-beta.1
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import enrollments_1_0_0-beta_1_yml
from enrollments_1_0_0-beta_1_yml.api.dispositivo_vinculado_api import DispositivoVinculadoApi  # noqa: E501
from enrollments_1_0_0-beta_1_yml.rest import ApiException


class TestDispositivoVinculadoApi(unittest.TestCase):
    """DispositivoVinculadoApi unit test stubs"""

    def setUp(self):
        self.api = DispositivoVinculadoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authorize_consent(self):
        """Test case for authorize_consent

        Autorização de um consentimento de pagamentos na jornada sem redirecionamento  # noqa: E501
        """
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


if __name__ == '__main__':
    unittest.main()
