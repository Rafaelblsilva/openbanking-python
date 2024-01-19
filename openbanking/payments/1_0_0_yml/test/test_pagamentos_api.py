# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora  de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:   - Certificados exigidos para assinatura de mensagens:   [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Algoritmos usados para assinatura de mensagens `JWS`:   [Perfil de segurança FAPI - Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-financial-api-1_ID1.md#algorithm-considerations)  - Mensagens assinadas, `JWS` e `JWKS`:   [Guia de usuário (Receptoras e iniciadoras de pagamento)](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/tpp-user-guide.md#143-what-is-a-jwt-jwe-jws-and-jwk)    ## Controle de acesso    O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).    Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.       # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import payments_1_0_0_yml
from payments_1_0_0_yml.api.pagamentos_api import PagamentosApi  # noqa: E501
from payments_1_0_0_yml.rest import ApiException


class TestPagamentosApi(unittest.TestCase):
    """PagamentosApi unit test stubs"""

    def setUp(self):
        self.api = PagamentosApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_payments_get_consents_consent_id(self):
        """Test case for payments_get_consents_consent_id

        Consultar consentimento para iniciação de pagamento.  # noqa: E501
        """
        pass

    def test_payments_get_pix_payments_payment_id(self):
        """Test case for payments_get_pix_payments_payment_id

        Consultar iniciação de pagamento.  # noqa: E501
        """
        pass

    def test_payments_post_consents(self):
        """Test case for payments_post_consents

        Criar consentimento para a iniciação de pagamento.  # noqa: E501
        """
        pass

    def test_payments_post_pix_payments(self):
        """Test case for payments_post_pix_payments

        Criar iniciação de pagamento.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
