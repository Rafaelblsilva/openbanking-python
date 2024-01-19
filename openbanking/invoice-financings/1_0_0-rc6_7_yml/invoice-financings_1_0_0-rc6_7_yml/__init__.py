# coding: utf-8

# flake8: noqa

"""
    API Invoice-financings - Open Banking Brasil

    API de informações de operações de antecipação de recebíveis do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo antecipação de recebíveis – direitos creditórios descontados - mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Invoice-financings  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}`   - permissions:      - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **INVOICE_FINANCINGS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **INVOICE_FINANCINGS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.7
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from invoice-financings_1_0_0-rc6_7_yml.api.invoice_financings_api import InvoiceFinancingsApi
# import ApiClient
from invoice-financings_1_0_0-rc6_7_yml.api_client import ApiClient
from invoice-financings_1_0_0-rc6_7_yml.configuration import Configuration
# import models into sdk package
from invoice-financings_1_0_0-rc6_7_yml.models.enum_contract_amortization_scheduled import EnumContractAmortizationScheduled
from invoice-financings_1_0_0-rc6_7_yml.models.enum_contract_calculation import EnumContractCalculation
from invoice-financings_1_0_0-rc6_7_yml.models.enum_contract_fee_charge import EnumContractFeeCharge
from invoice-financings_1_0_0-rc6_7_yml.models.enum_contract_fee_charge_type import EnumContractFeeChargeType
from invoice-financings_1_0_0-rc6_7_yml.models.enum_contract_finance_charge_type import EnumContractFinanceChargeType
from invoice-financings_1_0_0-rc6_7_yml.models.enum_contract_instalment_periodicity import EnumContractInstalmentPeriodicity
from invoice-financings_1_0_0-rc6_7_yml.models.enum_contract_interest_rate_type import EnumContractInterestRateType
from invoice-financings_1_0_0-rc6_7_yml.models.enum_contract_product_sub_type_invoice_financings import EnumContractProductSubTypeInvoiceFinancings
from invoice-financings_1_0_0-rc6_7_yml.models.enum_contract_product_type_invoice_financings import EnumContractProductTypeInvoiceFinancings
from invoice-financings_1_0_0-rc6_7_yml.models.enum_contract_referential_rate_indexer_sub_type import EnumContractReferentialRateIndexerSubType
from invoice-financings_1_0_0-rc6_7_yml.models.enum_contract_referential_rate_indexer_type import EnumContractReferentialRateIndexerType
from invoice-financings_1_0_0-rc6_7_yml.models.enum_contract_tax_periodicity import EnumContractTaxPeriodicity
from invoice-financings_1_0_0-rc6_7_yml.models.enum_warranty_sub_type import EnumWarrantySubType
from invoice-financings_1_0_0-rc6_7_yml.models.enum_warranty_type_yaml import EnumWarrantyTypeYaml
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_balloon_payment import InvoiceFinancingsBalloonPayment
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_charge_over_parcel import InvoiceFinancingsChargeOverParcel
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_contract import InvoiceFinancingsContract
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_contract_data import InvoiceFinancingsContractData
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_contract_interest_rate import InvoiceFinancingsContractInterestRate
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_contracted_fee import InvoiceFinancingsContractedFee
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_contracted_warranty import InvoiceFinancingsContractedWarranty
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_fee_over_parcel import InvoiceFinancingsFeeOverParcel
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_finance_charge import InvoiceFinancingsFinanceCharge
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_instalments import InvoiceFinancingsInstalments
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_payments import InvoiceFinancingsPayments
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_releases import InvoiceFinancingsReleases
from invoice-financings_1_0_0-rc6_7_yml.models.invoice_financings_releases_over_parcel import InvoiceFinancingsReleasesOverParcel
from invoice-financings_1_0_0-rc6_7_yml.models.links import Links
from invoice-financings_1_0_0-rc6_7_yml.models.meta import Meta
from invoice-financings_1_0_0-rc6_7_yml.models.response_error import ResponseError
from invoice-financings_1_0_0-rc6_7_yml.models.response_error_errors import ResponseErrorErrors
from invoice-financings_1_0_0-rc6_7_yml.models.response_invoice_financings_contract import ResponseInvoiceFinancingsContract
from invoice-financings_1_0_0-rc6_7_yml.models.response_invoice_financings_contract_list import ResponseInvoiceFinancingsContractList
from invoice-financings_1_0_0-rc6_7_yml.models.response_invoice_financings_instalments import ResponseInvoiceFinancingsInstalments
from invoice-financings_1_0_0-rc6_7_yml.models.response_invoice_financings_payments import ResponseInvoiceFinancingsPayments
from invoice-financings_1_0_0-rc6_7_yml.models.response_invoice_financings_warranties import ResponseInvoiceFinancingsWarranties
