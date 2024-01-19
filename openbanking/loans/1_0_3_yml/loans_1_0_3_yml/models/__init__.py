# coding: utf-8

# flake8: noqa
"""
    API Loans - Open Banking Brasil

    API de informações de operações de empréstimos do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo empréstimo, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Loans  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **LOANS_READ** ### `/contracts/{contractId}`   - permissions:      - GET **LOANS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **LOANS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **LOANS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **LOANS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.3
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from loans_1_0_3_yml.models.enum_contract_amortization_scheduled import EnumContractAmortizationScheduled
from loans_1_0_3_yml.models.enum_contract_calculation import EnumContractCalculation
from loans_1_0_3_yml.models.enum_contract_fee_charge import EnumContractFeeCharge
from loans_1_0_3_yml.models.enum_contract_fee_charge_type import EnumContractFeeChargeType
from loans_1_0_3_yml.models.enum_contract_finance_charge_type import EnumContractFinanceChargeType
from loans_1_0_3_yml.models.enum_contract_instalment_periodicity import EnumContractInstalmentPeriodicity
from loans_1_0_3_yml.models.enum_contract_interest_rate_type import EnumContractInterestRateType
from loans_1_0_3_yml.models.enum_contract_product_sub_type_loans import EnumContractProductSubTypeLoans
from loans_1_0_3_yml.models.enum_contract_product_type_loans import EnumContractProductTypeLoans
from loans_1_0_3_yml.models.enum_contract_referential_rate_indexer_sub_type import EnumContractReferentialRateIndexerSubType
from loans_1_0_3_yml.models.enum_contract_referential_rate_indexer_type import EnumContractReferentialRateIndexerType
from loans_1_0_3_yml.models.enum_contract_tax_periodicity import EnumContractTaxPeriodicity
from loans_1_0_3_yml.models.enum_contract_tax_type import EnumContractTaxType
from loans_1_0_3_yml.models.enum_warranty_sub_type import EnumWarrantySubType
from loans_1_0_3_yml.models.enum_warranty_type import EnumWarrantyType
from loans_1_0_3_yml.models.links import Links
from loans_1_0_3_yml.models.loans_balloon_payment import LoansBalloonPayment
from loans_1_0_3_yml.models.loans_charge_over_parcel import LoansChargeOverParcel
from loans_1_0_3_yml.models.loans_contract import LoansContract
from loans_1_0_3_yml.models.loans_contract_interest_rate import LoansContractInterestRate
from loans_1_0_3_yml.models.loans_contracted_fee import LoansContractedFee
from loans_1_0_3_yml.models.loans_fee_over_parcel import LoansFeeOverParcel
from loans_1_0_3_yml.models.loans_finance_charge import LoansFinanceCharge
from loans_1_0_3_yml.models.loans_instalments import LoansInstalments
from loans_1_0_3_yml.models.loans_list_contract import LoansListContract
from loans_1_0_3_yml.models.loans_payments import LoansPayments
from loans_1_0_3_yml.models.loans_releases import LoansReleases
from loans_1_0_3_yml.models.loans_releases_over_parcel import LoansReleasesOverParcel
from loans_1_0_3_yml.models.loans_warranties import LoansWarranties
from loans_1_0_3_yml.models.meta import Meta
from loans_1_0_3_yml.models.response_error import ResponseError
from loans_1_0_3_yml.models.response_error_errors import ResponseErrorErrors
from loans_1_0_3_yml.models.response_loans_contract import ResponseLoansContract
from loans_1_0_3_yml.models.response_loans_contract_list import ResponseLoansContractList
from loans_1_0_3_yml.models.response_loans_instalments import ResponseLoansInstalments
from loans_1_0_3_yml.models.response_loans_payments import ResponseLoansPayments
from loans_1_0_3_yml.models.response_loans_warranties import ResponseLoansWarranties
from loans_1_0_3_yml.models.x_fapi_interaction_id import XFapiInteractionId