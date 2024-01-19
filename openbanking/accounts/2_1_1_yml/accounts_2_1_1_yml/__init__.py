# coding: utf-8

# flake8: noqa

"""
    API Accounts - Open Finance Brasil

    API de contas de depósito à vista, contas de poupança e contas pré-pagas do Open Finance Brasil – Fase 2. API que retorna informações de contas de depósito à vista, contas de poupança e contas de pagamento pré-pagas mantidas nas instituições transmissoras por seus clientes, incluindo dados de identificação da conta, saldos, limites e transações.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}/balances`   - permissions:     - GET: **ACCOUNTS_BALANCES_READ** ### `/accounts/{accountId}/transactions`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/transactions-current`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/overdraft-limits`   - permissions:     - GET: **ACCOUNTS_OVERDRAFT_LIMITS_READ**  ## Data de imutabilidade por tipo de transação​ O identificador de transações de contas é de envio obrigatório no Open Finance Brasil. De acordo com o tipo da transação deve haver o envio de um identificador único, estável e imutável em D0 ou D+1, conforme tabela abaixo ``` |---------------------------------------|-------------------------|-----------------------| | Tipo de Transação                     | Data da Obrigatoriedade | Data da Imutabilidade | |---------------------------------------|-------------------------|-----------------------| | TED                                   | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | PIX                                   | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | TRANSFERENCIA MESMA INSTITUIÇÃO (TEF) | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | TARIFA SERVIÇOS AVULSOS               | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | FOLHA DE PAGAMENTO                    | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | DOC                                   | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | BOLETO                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | CONVÊNIO ARRECADAÇÃO                  | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | PACOTE TARIFA SERVIÇOS                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | DEPÓSITO                              | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | SAQUE                                 | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | CARTÃO                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | ENCARGOS JUROS CHEQUE ESPECIAL        | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | RENDIMENTO APLICAÇÃO FINANCEIRA       | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | PORTABILIDADE SALÁRIO                 | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | RESGATE APLICAÇÃO FINANCEIRA          | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | OPERAÇÃO DE CRÉDITO                   | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | OUTROS                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| ```  Para consultar as regras aplicáveis ao comportamento do transacionID de acordo com o status da transação, consultar a página [Orientações - Contas](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/193658890)   # noqa: E501

    OpenAPI spec version: 2.1.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from accounts_2_1_1_yml.api.accounts_api import AccountsApi
# import ApiClient
from accounts_2_1_1_yml.api_client import ApiClient
from accounts_2_1_1_yml.configuration import Configuration
# import models into sdk package
from accounts_2_1_1_yml.models.account_balances_data import AccountBalancesData
from accounts_2_1_1_yml.models.account_balances_data_automatically_invested_amount import AccountBalancesDataAutomaticallyInvestedAmount
from accounts_2_1_1_yml.models.account_balances_data_available_amount import AccountBalancesDataAvailableAmount
from accounts_2_1_1_yml.models.account_balances_data_blocked_amount import AccountBalancesDataBlockedAmount
from accounts_2_1_1_yml.models.account_data import AccountData
from accounts_2_1_1_yml.models.account_identification_data import AccountIdentificationData
from accounts_2_1_1_yml.models.account_overdraft_limits_data import AccountOverdraftLimitsData
from accounts_2_1_1_yml.models.account_overdraft_limits_data_overdraft_contracted_limit import AccountOverdraftLimitsDataOverdraftContractedLimit
from accounts_2_1_1_yml.models.account_overdraft_limits_data_overdraft_used_limit import AccountOverdraftLimitsDataOverdraftUsedLimit
from accounts_2_1_1_yml.models.account_overdraft_limits_data_unarranged_overdraft_amount import AccountOverdraftLimitsDataUnarrangedOverdraftAmount
from accounts_2_1_1_yml.models.account_transactions_data import AccountTransactionsData
from accounts_2_1_1_yml.models.account_transactions_data_amount import AccountTransactionsDataAmount
from accounts_2_1_1_yml.models.enum_account_sub_type import EnumAccountSubType
from accounts_2_1_1_yml.models.enum_account_type import EnumAccountType
from accounts_2_1_1_yml.models.enum_completed_authorised_payment_indicator import EnumCompletedAuthorisedPaymentIndicator
from accounts_2_1_1_yml.models.enum_credit_debit_indicator import EnumCreditDebitIndicator
from accounts_2_1_1_yml.models.enum_partie_person_type import EnumPartiePersonType
from accounts_2_1_1_yml.models.enum_transaction_types import EnumTransactionTypes
from accounts_2_1_1_yml.models.links import Links
from accounts_2_1_1_yml.models.meta import Meta
from accounts_2_1_1_yml.models.meta_only_request_date_time import MetaOnlyRequestDateTime
from accounts_2_1_1_yml.models.response_account_balances import ResponseAccountBalances
from accounts_2_1_1_yml.models.response_account_identification import ResponseAccountIdentification
from accounts_2_1_1_yml.models.response_account_list import ResponseAccountList
from accounts_2_1_1_yml.models.response_account_overdraft_limits import ResponseAccountOverdraftLimits
from accounts_2_1_1_yml.models.response_account_transactions import ResponseAccountTransactions
from accounts_2_1_1_yml.models.response_error import ResponseError
from accounts_2_1_1_yml.models.response_error_meta_single import ResponseErrorMetaSingle
from accounts_2_1_1_yml.models.response_error_meta_single_errors import ResponseErrorMetaSingleErrors
from accounts_2_1_1_yml.models.transactions_links import TransactionsLinks
from accounts_2_1_1_yml.models.x_fapi_interaction_id import XFapiInteractionId
