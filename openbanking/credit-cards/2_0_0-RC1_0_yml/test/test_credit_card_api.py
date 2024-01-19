# coding: utf-8

"""
    API Credit-cards-accounts - Open Banking Brasil

    API de contas de pagamento pós-pagas do Open Banking Brasil – Fase 2. API que retorna informações de contas de pagamento pós-paga mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, produto, bandeira, limites de crédito, informações sobre transações de pagamento efetuadas e faturas.  Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.\\ ### `/accounts/{creditCardAccountId}/bills`   - description:     - Só deve ser informada uma fatura já fechada.     - Qualquer pagamento deve ser contado para a última fatura fechada. ### `/accounts/{creditCardAccountId}/bills/{billId}/transactions`   - description:     - A lista a retornar se refere a transações após base 2/clearing/conciliado ### `/accounts/{creditCardAccountId}/transactions`   - description:     - A lista a retornar se refere a transações após base 2/clearing/conciliado  ## Permissions necessárias para a API Credit-cards-accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}/bills`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_READ** ### `/accounts/{creditCardAccountId}/bills/{billId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/limits`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_LIMITS_READ** ### `/accounts/{creditCardAccountId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/transactions-current`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ**   # noqa: E501

    OpenAPI spec version: 2.0.0-RC1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import credit-cards_2_0_0-RC1_0_yml
from credit-cards_2_0_0-RC1_0_yml.api.credit_card_api import CreditCardApi  # noqa: E501
from credit-cards_2_0_0-RC1_0_yml.rest import ApiException


class TestCreditCardApi(unittest.TestCase):
    """CreditCardApi unit test stubs"""

    def setUp(self):
        self.api = CreditCardApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_credit_cards_get_accounts(self):
        """Test case for credit_cards_get_accounts

        Conjunto de informações das Contas de pagamento pós paga  # noqa: E501
        """
        pass

    def test_credit_cards_get_accounts_credit_card_account_id(self):
        """Test case for credit_cards_get_accounts_credit_card_account_id

        Obtém os dados de identificação da conta identificada por creditCardAccountId.  # noqa: E501
        """
        pass

    def test_credit_cards_get_accounts_credit_card_account_id_bills(self):
        """Test case for credit_cards_get_accounts_credit_card_account_id_bills

        Obtém a lista de faturas da conta identificada por creditCardAccountId.  # noqa: E501
        """
        pass

    def test_credit_cards_get_accounts_credit_card_account_id_bills_bill_id_transactions(self):
        """Test case for credit_cards_get_accounts_credit_card_account_id_bills_bill_id_transactions

        Obtém a lista de transações da conta identificada por creditCardAccountId e billId.  # noqa: E501
        """
        pass

    def test_credit_cards_get_accounts_credit_card_account_id_limits(self):
        """Test case for credit_cards_get_accounts_credit_card_account_id_limits

        Obtém os limites da conta identificada por creditCardAccountId.  # noqa: E501
        """
        pass

    def test_credit_cards_get_accounts_credit_card_account_id_transactions(self):
        """Test case for credit_cards_get_accounts_credit_card_account_id_transactions

        Obtém a lista de transações da conta identificada por creditCardAccountId.  # noqa: E501
        """
        pass

    def test_credit_cards_get_accounts_credit_card_account_id_transactions_current(self):
        """Test case for credit_cards_get_accounts_credit_card_account_id_transactions_current

        Obtém a lista de transações da conta identificada por creditCardAccountId.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
