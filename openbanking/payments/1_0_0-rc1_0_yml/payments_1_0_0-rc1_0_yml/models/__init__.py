# coding: utf-8

# flake8: noqa
"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, reponsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openId` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from payments_1_0_0-rc1_0_yml.models.create_payment_consent import CreatePaymentConsent
from payments_1_0_0-rc1_0_yml.models.create_payment_consent_data import CreatePaymentConsentData
from payments_1_0_0-rc1_0_yml.models.create_pix_payment import CreatePixPayment
from payments_1_0_0-rc1_0_yml.models.create_pix_payment_data import CreatePixPaymentData
from payments_1_0_0-rc1_0_yml.models.creditor_account import CreditorAccount
from payments_1_0_0-rc1_0_yml.models.debtor_account import DebtorAccount
from payments_1_0_0-rc1_0_yml.models.enum_account_payments_type import EnumAccountPaymentsType
from payments_1_0_0-rc1_0_yml.models.identification import Identification
from payments_1_0_0-rc1_0_yml.models.inline_response422 import InlineResponse422
from payments_1_0_0-rc1_0_yml.models.inline_response4221 import InlineResponse4221
from payments_1_0_0-rc1_0_yml.models.inline_response4221_errors import InlineResponse4221Errors
from payments_1_0_0-rc1_0_yml.models.inline_response422_errors import InlineResponse422Errors
from payments_1_0_0-rc1_0_yml.models.payment_consent import PaymentConsent
from payments_1_0_0-rc1_0_yml.models.payment_pix import PaymentPix
from payments_1_0_0-rc1_0_yml.models.response_error import ResponseError
from payments_1_0_0-rc1_0_yml.models.response_error_errors import ResponseErrorErrors
from payments_1_0_0-rc1_0_yml.models.response_error_meta import ResponseErrorMeta
from payments_1_0_0-rc1_0_yml.models.response_payment_consent import ResponsePaymentConsent
from payments_1_0_0-rc1_0_yml.models.response_payment_consent_data import ResponsePaymentConsentData
from payments_1_0_0-rc1_0_yml.models.response_pix_payment import ResponsePixPayment
from payments_1_0_0-rc1_0_yml.models.response_pix_payment_data import ResponsePixPaymentData
