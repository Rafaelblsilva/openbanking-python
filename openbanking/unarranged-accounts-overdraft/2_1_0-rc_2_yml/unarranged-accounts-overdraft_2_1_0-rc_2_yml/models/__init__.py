# coding: utf-8

# flake8: noqa
"""
    API Unarranged-accounts-overdraft - Open Finance Brasil

    API de informações de operações de adiantamento a depositantes do Open Finance Brasil –Fase 2.  API que retorna informações de operações de crédito do tipo adiantamento a depositantes, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos (ao menos para os últimos 12 meses), amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ### Observação   - No endpoint `/contracts/{contratId}/payments` a paginação ocorrerá sob os dados contidos no campo `releases` do tipo lista.  ## Permissions necessárias para a API Unarranged-accounts-overdraft  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **UNARRANGED_ACCOUNTS_OVERDRAFT_READ** ### `/contracts/{contractId}`   - permissions: **UNARRANGED_ACCOUNTS_OVERDRAFT_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **UNARRANGED_ACCOUNTS_OVERDRAFT_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **UNARRANGED_ACCOUNTS_OVERDRAFT_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **UNARRANGED_ACCOUNTS_OVERDRAFT_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 2.1.0-rc.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.charge_type import ChargeType
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.enum_contract_fee_charge import EnumContractFeeCharge
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.enum_contract_fee_charge_type import EnumContractFeeChargeType
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.enum_contract_instalment_periodicity import EnumContractInstalmentPeriodicity
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.enum_contract_interest_rate_type import EnumContractInterestRateType
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.enum_contract_referential_rate_indexer_sub_type import EnumContractReferentialRateIndexerSubType
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.enum_contract_referential_rate_indexer_type import EnumContractReferentialRateIndexerType
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.enum_contract_tax_periodicity import EnumContractTaxPeriodicity
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.enum_contract_tax_type import EnumContractTaxType
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.enum_type_number_of_instalments import EnumTypeNumberOfInstalments
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.enum_warranty_sub_type import EnumWarrantySubType
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.enum_warranty_type import EnumWarrantyType
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.links import Links
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.meta import Meta
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.product_sub_type import ProductSubType
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.product_type import ProductType
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.response_error import ResponseError
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.response_error_meta import ResponseErrorMeta
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.response_error_with_able_additional_properties import ResponseErrorWithAbleAdditionalProperties
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.response_error_with_able_additional_properties_errors import ResponseErrorWithAbleAdditionalPropertiesErrors
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.response_unarranged_account_overdraft_contract import ResponseUnarrangedAccountOverdraftContract
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.response_unarranged_account_overdraft_contract_list import ResponseUnarrangedAccountOverdraftContractList
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.response_unarranged_account_overdraft_instalments import ResponseUnarrangedAccountOverdraftInstalments
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.response_unarranged_account_overdraft_payments import ResponseUnarrangedAccountOverdraftPayments
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.response_unarranged_account_overdraft_warranties import ResponseUnarrangedAccountOverdraftWarranties
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_balloon_payment import UnarrangedAccountOverdraftBalloonPayment
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_balloon_payment_amount import UnarrangedAccountOverdraftBalloonPaymentAmount
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_charge_over_parcel import UnarrangedAccountOverdraftChargeOverParcel
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_contract_data import UnarrangedAccountOverdraftContractData
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_contract_interest_rate import UnarrangedAccountOverdraftContractInterestRate
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_contract_list_data import UnarrangedAccountOverdraftContractListData
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_contracted_fee import UnarrangedAccountOverdraftContractedFee
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_fee_over_parcel import UnarrangedAccountOverdraftFeeOverParcel
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_finance_charge import UnarrangedAccountOverdraftFinanceCharge
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_instalments_data import UnarrangedAccountOverdraftInstalmentsData
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_payments_data import UnarrangedAccountOverdraftPaymentsData
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_releases import UnarrangedAccountOverdraftReleases
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_account_overdraft_releases_over_parcel import UnarrangedAccountOverdraftReleasesOverParcel
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.unarranged_accounts_overdraft_contracted_warranty import UnarrangedAccountsOverdraftContractedWarranty
from unarranged-accounts-overdraft_2_1_0-rc_2_yml.models.x_fapi_interaction_id import XFapiInteractionId
