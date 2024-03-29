# coding: utf-8

# flake8: noqa
"""
    API Funds - Open Finance Brasil

    API de informações de operações de Fundos de Investimento Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Fundos de Investimento mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente e movimentações financeiras.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  Devem ser considerados como escopo de exposição todos os fundos de investimento classificados como: Renda Fixa, Ações, Multimercado e Cambial.  Para identificação do produto e posição do cliente, a exposição será de forma consolidada por Fundo de Investimento.  Para movimentações, a exposição se dará pela Ordem do Cliente, por exemplo, uma Ordem de Resgate é compartilhada como uma única movimentação, mesmo que esteja associada a diferentes Certificados (Cautelas).  As instituições podem apresentar cenários distintos no que diz respeito ao sincronismo entre posição `/balances` e movimentação `/transactions` e `/transactions-current` da API:  - Algumas instituições refletem movimentações ainda não convertidas na posição do cliente em seus canais eletrônicos. Isso implica que pode ocorrer compartilhamento de posição atualizada, cujas movimentações relacionadas serão expostas no ecossistema apenas após a conversão das mesmas;  - Outras instituições refletem na posição apenas movimentações convertidas nos seus canais eletrônicos. Isso implica que o compartilhamento da posição em relação às movimentações é feito de forma sincronizada no ecossistema.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc3.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from funds_1_0_0-rc3_0_yml.models.enum_funds_transactions_current_transaction_type import EnumFundsTransactionsCurrentTransactionType
from funds_1_0_0-rc3_0_yml.models.enum_funds_transactions_current_type import EnumFundsTransactionsCurrentType
from funds_1_0_0-rc3_0_yml.models.enum_funds_transactions_transaction_type import EnumFundsTransactionsTransactionType
from funds_1_0_0-rc3_0_yml.models.enum_funds_transactions_type import EnumFundsTransactionsType
from funds_1_0_0-rc3_0_yml.models.funds_balances_blocked_amount import FundsBalancesBlockedAmount
from funds_1_0_0-rc3_0_yml.models.funds_balances_financial_transaction_tax_provision import FundsBalancesFinancialTransactionTaxProvision
from funds_1_0_0-rc3_0_yml.models.funds_balances_gross_amount import FundsBalancesGrossAmount
from funds_1_0_0-rc3_0_yml.models.funds_balances_income_tax_provision import FundsBalancesIncomeTaxProvision
from funds_1_0_0-rc3_0_yml.models.funds_balances_net_amount import FundsBalancesNetAmount
from funds_1_0_0-rc3_0_yml.models.funds_balances_quota_gross_price_value import FundsBalancesQuotaGrossPriceValue
from funds_1_0_0-rc3_0_yml.models.funds_links import FundsLinks
from funds_1_0_0-rc3_0_yml.models.funds_meta import FundsMeta
from funds_1_0_0-rc3_0_yml.models.meta_only_request_date_time import MetaOnlyRequestDateTime
from funds_1_0_0-rc3_0_yml.models.meta_single import MetaSingle
from funds_1_0_0-rc3_0_yml.models.meta_with_able_additional_properties import MetaWithAbleAdditionalProperties
from funds_1_0_0-rc3_0_yml.models.response_error_meta_single import ResponseErrorMetaSingle
from funds_1_0_0-rc3_0_yml.models.response_error_meta_single_errors import ResponseErrorMetaSingleErrors
from funds_1_0_0-rc3_0_yml.models.response_error_with_able_additional_properties import ResponseErrorWithAbleAdditionalProperties
from funds_1_0_0-rc3_0_yml.models.response_funds_balance_data import ResponseFundsBalanceData
from funds_1_0_0-rc3_0_yml.models.response_funds_balances import ResponseFundsBalances
from funds_1_0_0-rc3_0_yml.models.response_funds_product_identification import ResponseFundsProductIdentification
from funds_1_0_0-rc3_0_yml.models.response_funds_product_identification_data import ResponseFundsProductIdentificationData
from funds_1_0_0-rc3_0_yml.models.response_funds_product_list import ResponseFundsProductList
from funds_1_0_0-rc3_0_yml.models.response_funds_product_list_data import ResponseFundsProductListData
from funds_1_0_0-rc3_0_yml.models.response_funds_transactions import ResponseFundsTransactions
from funds_1_0_0-rc3_0_yml.models.response_funds_transactions_current import ResponseFundsTransactionsCurrent
from funds_1_0_0-rc3_0_yml.models.response_funds_transactions_current_data import ResponseFundsTransactionsCurrentData
from funds_1_0_0-rc3_0_yml.models.response_funds_transactions_data import ResponseFundsTransactionsData
from funds_1_0_0-rc3_0_yml.models.response_funds_transactions_data_financial_transaction_tax import ResponseFundsTransactionsDataFinancialTransactionTax
from funds_1_0_0-rc3_0_yml.models.response_funds_transactions_data_income_tax import ResponseFundsTransactionsDataIncomeTax
from funds_1_0_0-rc3_0_yml.models.response_funds_transactions_data_transaction_exit_fee import ResponseFundsTransactionsDataTransactionExitFee
from funds_1_0_0-rc3_0_yml.models.response_funds_transactions_data_transaction_gross_value import ResponseFundsTransactionsDataTransactionGrossValue
from funds_1_0_0-rc3_0_yml.models.response_funds_transactions_data_transaction_net_value import ResponseFundsTransactionsDataTransactionNetValue
from funds_1_0_0-rc3_0_yml.models.response_funds_transactions_data_transaction_quota_price import ResponseFundsTransactionsDataTransactionQuotaPrice
from funds_1_0_0-rc3_0_yml.models.response_funds_transactions_data_transaction_value import ResponseFundsTransactionsDataTransactionValue
