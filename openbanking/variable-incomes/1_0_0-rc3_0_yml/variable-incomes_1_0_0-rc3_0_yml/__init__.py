# coding: utf-8

# flake8: noqa

"""
    API Variable Incomes - Open Finance Brasil

    API de informações de operações de Renda Variável Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Renda Variável mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente, movimentações financeiras e detalhes da nota de negociação.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  A granularidade de exposição de operações de renda variável se dá por cada ativo (ticker) da carteira do cliente.  Compartilhamento considera lote padrão e fracionário, entretanto, no Open Finance Brasil, as informações são consolidadas via ticker do lote padrão.  A defasagem em relação ao canal eletrônico da instituição deve ser o fechamento (pregão) do dia anterior (d-1).   Em relação ao aluguel de ações: neste momento não faz parte do escopo de compartilhamento a carteira/posição de aluguel do cliente (ativos alugados e movimentações relacionadas a esses ativos).  Apenas deve ser compartilhado as transações de pagamento ou recebimento de juros oriundos dos contratos de ações alugadas (ou doadas) pelos clientes.  Segue abaixo tabela com o escopo de produtos a ser considerado para compartilhamento:  ```    |----------------------|-------------------------------|----------------------|-----------------------------------|    | CLASSE DE ATIVOS     | PRODUTO                       | SUBPRODUTO           | DENOMINAÇÃO                       |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       |     -                | FIAGRO                            |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | Subscrição           | Bonus / Direito / Recibo          |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       | Fundo imobiliario    | FII                               |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | À vista              | ON / PN / UNIT                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF de Renda Variável             |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF Internacional                 |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF Renda Fixa       | ETF Renda Fixa                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    ```   # noqa: E501

    OpenAPI spec version: 1.0.0-rc3.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from variable-incomes_1_0_0-rc3_0_yml.api.balances_api import BalancesApi
from variable-incomes_1_0_0-rc3_0_yml.api.broker_note_details_api import BrokerNoteDetailsApi
from variable-incomes_1_0_0-rc3_0_yml.api.product_identification_api import ProductIdentificationApi
from variable-incomes_1_0_0-rc3_0_yml.api.product_list_api import ProductListApi
from variable-incomes_1_0_0-rc3_0_yml.api.transactions_api import TransactionsApi
from variable-incomes_1_0_0-rc3_0_yml.api.transactions_current_api import TransactionsCurrentApi
# import ApiClient
from variable-incomes_1_0_0-rc3_0_yml.api_client import ApiClient
from variable-incomes_1_0_0-rc3_0_yml.configuration import Configuration
# import models into sdk package
from variable-incomes_1_0_0-rc3_0_yml.models.enum_variable_incomes_transactions_current_transaction_type import EnumVariableIncomesTransactionsCurrentTransactionType
from variable-incomes_1_0_0-rc3_0_yml.models.enum_variable_incomes_transactions_current_type import EnumVariableIncomesTransactionsCurrentType
from variable-incomes_1_0_0-rc3_0_yml.models.enum_variable_incomes_transactions_transaction_type import EnumVariableIncomesTransactionsTransactionType
from variable-incomes_1_0_0-rc3_0_yml.models.enum_variable_incomes_transactions_type import EnumVariableIncomesTransactionsType
from variable-incomes_1_0_0-rc3_0_yml.models.inline_response423 import InlineResponse423
from variable-incomes_1_0_0-rc3_0_yml.models.inline_response4231 import InlineResponse4231
from variable-incomes_1_0_0-rc3_0_yml.models.inline_response4231_meta import InlineResponse4231Meta
from variable-incomes_1_0_0-rc3_0_yml.models.inline_response423_meta import InlineResponse423Meta
from variable-incomes_1_0_0-rc3_0_yml.models.meta_only_request_date_time import MetaOnlyRequestDateTime
from variable-incomes_1_0_0-rc3_0_yml.models.meta_single import MetaSingle
from variable-incomes_1_0_0-rc3_0_yml.models.meta_with_able_additional_properties import MetaWithAbleAdditionalProperties
from variable-incomes_1_0_0-rc3_0_yml.models.response_error_meta_single import ResponseErrorMetaSingle
from variable-incomes_1_0_0-rc3_0_yml.models.response_error_meta_single_errors import ResponseErrorMetaSingleErrors
from variable-incomes_1_0_0-rc3_0_yml.models.response_error_with_able_additional_properties import ResponseErrorWithAbleAdditionalProperties
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_balance_data import ResponseVariableIncomesBalanceData
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_balances import ResponseVariableIncomesBalances
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_broker import ResponseVariableIncomesBroker
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_broker_data import ResponseVariableIncomesBrokerData
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_broker_data_brokerage_fee import ResponseVariableIncomesBrokerDataBrokerageFee
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_broker_data_clearing_custody_fee import ResponseVariableIncomesBrokerDataClearingCustodyFee
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_broker_data_clearing_registration_fee import ResponseVariableIncomesBrokerDataClearingRegistrationFee
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_broker_data_clearing_settlement_fee import ResponseVariableIncomesBrokerDataClearingSettlementFee
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_broker_data_gross_value import ResponseVariableIncomesBrokerDataGrossValue
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_broker_data_income_tax import ResponseVariableIncomesBrokerDataIncomeTax
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_broker_data_net_value import ResponseVariableIncomesBrokerDataNetValue
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_broker_data_stock_exchange_asset_trade_notice_fee import ResponseVariableIncomesBrokerDataStockExchangeAssetTradeNoticeFee
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_broker_data_stock_exchange_fee import ResponseVariableIncomesBrokerDataStockExchangeFee
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_broker_data_taxes import ResponseVariableIncomesBrokerDataTaxes
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_product_identification import ResponseVariableIncomesProductIdentification
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_product_identification_data import ResponseVariableIncomesProductIdentificationData
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_product_list import ResponseVariableIncomesProductList
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_product_list_data import ResponseVariableIncomesProductListData
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_transactions import ResponseVariableIncomesTransactions
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_transactions_current import ResponseVariableIncomesTransactionsCurrent
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_transactions_current_data import ResponseVariableIncomesTransactionsCurrentData
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_transactions_data import ResponseVariableIncomesTransactionsData
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_transactions_data_transaction_unit_price import ResponseVariableIncomesTransactionsDataTransactionUnitPrice
from variable-incomes_1_0_0-rc3_0_yml.models.response_variable_incomes_transactions_data_transaction_value import ResponseVariableIncomesTransactionsDataTransactionValue
from variable-incomes_1_0_0-rc3_0_yml.models.variable_incomes_balances_blocked_balance import VariableIncomesBalancesBlockedBalance
from variable-incomes_1_0_0-rc3_0_yml.models.variable_incomes_balances_closing_price import VariableIncomesBalancesClosingPrice
from variable-incomes_1_0_0-rc3_0_yml.models.variable_incomes_balances_gross_amount import VariableIncomesBalancesGrossAmount
from variable-incomes_1_0_0-rc3_0_yml.models.variable_incomes_balances_links import VariableIncomesBalancesLinks
from variable-incomes_1_0_0-rc3_0_yml.models.variable_incomes_balances_meta import VariableIncomesBalancesMeta
from variable-incomes_1_0_0-rc3_0_yml.models.variable_incomes_links import VariableIncomesLinks
from variable-incomes_1_0_0-rc3_0_yml.models.variable_incomes_meta import VariableIncomesMeta
