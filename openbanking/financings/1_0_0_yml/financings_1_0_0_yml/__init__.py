# coding: utf-8

# flake8: noqa

"""
    API Financings - Open Banking Brasil

    API de informações de operações de financiamentos do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo financiamento, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Financings  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **FINANCINGS_READ** ### `/contracts/{contractId}`   - permissions:     - GET **FINANCINGS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **FINANCINGS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **FINANCINGS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **FINANCINGS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from financings_1_0_0_yml.api.financings_api import FinancingsApi
# import ApiClient
from financings_1_0_0_yml.api_client import ApiClient
from financings_1_0_0_yml.configuration import Configuration
# import models into sdk package
from financings_1_0_0_yml.models.enum_product_sub_type import EnumProductSubType
from financings_1_0_0_yml.models.enum_product_type import EnumProductType
from financings_1_0_0_yml.models.financings_balloon_payment import FinancingsBalloonPayment
from financings_1_0_0_yml.models.financings_charge_over_parcel import FinancingsChargeOverParcel
from financings_1_0_0_yml.models.financings_contract import FinancingsContract
from financings_1_0_0_yml.models.financings_contract_fee import FinancingsContractFee
from financings_1_0_0_yml.models.financings_contract_interest_rate import FinancingsContractInterestRate
from financings_1_0_0_yml.models.financings_fee_over_parcel import FinancingsFeeOverParcel
from financings_1_0_0_yml.models.financings_finance_charge import FinancingsFinanceCharge
from financings_1_0_0_yml.models.financings_instalments import FinancingsInstalments
from financings_1_0_0_yml.models.financings_list_contract import FinancingsListContract
from financings_1_0_0_yml.models.financings_over_parcel import FinancingsOverParcel
from financings_1_0_0_yml.models.financings_payments import FinancingsPayments
from financings_1_0_0_yml.models.financings_releases import FinancingsReleases
from financings_1_0_0_yml.models.financings_warranties import FinancingsWarranties
from financings_1_0_0_yml.models.links import Links
from financings_1_0_0_yml.models.meta import Meta
from financings_1_0_0_yml.models.response_error import ResponseError
from financings_1_0_0_yml.models.response_error_errors import ResponseErrorErrors
from financings_1_0_0_yml.models.response_financings_contract import ResponseFinancingsContract
from financings_1_0_0_yml.models.response_financings_contract_list import ResponseFinancingsContractList
from financings_1_0_0_yml.models.response_financings_instalments import ResponseFinancingsInstalments
from financings_1_0_0_yml.models.response_financings_payments import ResponseFinancingsPayments
from financings_1_0_0_yml.models.response_financings_warranties import ResponseFinancingsWarranties
