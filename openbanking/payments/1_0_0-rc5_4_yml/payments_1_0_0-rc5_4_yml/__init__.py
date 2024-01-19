# coding: utf-8

# flake8: noqa

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora  de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:   - Certificados exigidos para assinatura de mensagens:   [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Algoritmos usados para assinatura de mensagens `JWS`:   [Perfil de segurança FAPI - Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-financial-api-1_ID1.md#algorithm-considerations)  - Mensagens assinadas, `JWS` e `JWKS`:   [Guia de usuário (Receptoras e iniciadoras de pagamento)](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/tpp-user-guide.md#143-what-is-a-jwt-jwe-jws-and-jwk)    ## Controle de acesso    O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).    Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.       # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.4
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from payments_1_0_0-rc5_4_yml.api.pagamentos_api import PagamentosApi
# import ApiClient
from payments_1_0_0-rc5_4_yml.api_client import ApiClient
from payments_1_0_0-rc5_4_yml.configuration import Configuration
# import models into sdk package
from payments_1_0_0-rc5_4_yml.models.business_entity import BusinessEntity
from payments_1_0_0-rc5_4_yml.models.business_entity_document import BusinessEntityDocument
from payments_1_0_0-rc5_4_yml.models.create_payment_consent import CreatePaymentConsent
from payments_1_0_0-rc5_4_yml.models.create_payment_consent_data import CreatePaymentConsentData
from payments_1_0_0-rc5_4_yml.models.create_pix_payment import CreatePixPayment
from payments_1_0_0-rc5_4_yml.models.create_pix_payment_data import CreatePixPaymentData
from payments_1_0_0-rc5_4_yml.models.creditor_account import CreditorAccount
from payments_1_0_0-rc5_4_yml.models.debtor_account import DebtorAccount
from payments_1_0_0-rc5_4_yml.models.end_to_end_id import EndToEndId
from payments_1_0_0-rc5_4_yml.models.enum_account_payments_type import EnumAccountPaymentsType
from payments_1_0_0-rc5_4_yml.models.enum_local_instrument import EnumLocalInstrument
from payments_1_0_0-rc5_4_yml.models.identification import Identification
from payments_1_0_0-rc5_4_yml.models.inline_response422 import InlineResponse422
from payments_1_0_0-rc5_4_yml.models.inline_response4221 import InlineResponse4221
from payments_1_0_0-rc5_4_yml.models.inline_response4221_errors import InlineResponse4221Errors
from payments_1_0_0-rc5_4_yml.models.inline_response422_errors import InlineResponse422Errors
from payments_1_0_0-rc5_4_yml.models.links import Links
from payments_1_0_0-rc5_4_yml.models.logged_user import LoggedUser
from payments_1_0_0-rc5_4_yml.models.logged_user_document import LoggedUserDocument
from payments_1_0_0-rc5_4_yml.models.meta import Meta
from payments_1_0_0-rc5_4_yml.models.payment_consent import PaymentConsent
from payments_1_0_0-rc5_4_yml.models.payment_pix import PaymentPix
from payments_1_0_0-rc5_4_yml.models.response_error import ResponseError
from payments_1_0_0-rc5_4_yml.models.response_error_errors import ResponseErrorErrors
from payments_1_0_0-rc5_4_yml.models.response_payment_consent import ResponsePaymentConsent
from payments_1_0_0-rc5_4_yml.models.response_payment_consent_data import ResponsePaymentConsentData
from payments_1_0_0-rc5_4_yml.models.response_pix_payment import ResponsePixPayment
from payments_1_0_0-rc5_4_yml.models.response_pix_payment_data import ResponsePixPaymentData
from payments_1_0_0-rc5_4_yml.models.x_fapi_interaction_id import XFapiInteractionId
