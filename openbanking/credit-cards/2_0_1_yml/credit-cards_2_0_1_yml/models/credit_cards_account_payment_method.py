# coding: utf-8

"""
    API Credit-cards-accounts - Open Finance Brasil

    API de contas de pagamento pós-pagas do Open Finance Brasil – Fase 2. API que retorna informações de contas de pagamento pós-paga mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, produto, bandeira, limites de crédito, informações sobre transações de pagamento efetuadas e faturas.  Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.\\ ### `/accounts/{creditCardAccountId}/bills`   - description:     - Só deve ser informada uma fatura já fechada.     - Qualquer pagamento deve ser contado para a última fatura fechada. ### `/accounts/{creditCardAccountId}/bills/{billId}/transactions`   - description:     - A lista a retornar se refere a transações após base 2/clearing/conciliado ### `/accounts/{creditCardAccountId}/transactions`   - description:     - A lista a retornar se refere a transações após base 2/clearing/conciliado  ## Permissions necessárias para a API Credit-cards-accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}/bills`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_READ** ### `/accounts/{creditCardAccountId}/bills/{billId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/limits`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_LIMITS_READ** ### `/accounts/{creditCardAccountId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/transactions-current`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ**   # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardsAccountPaymentMethod(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'identification_number': 'str',
        'is_multiple_credit_card': 'bool'
    }

    attribute_map = {
        'identification_number': 'identificationNumber',
        'is_multiple_credit_card': 'isMultipleCreditCard'
    }

    def __init__(self, identification_number=None, is_multiple_credit_card=None):  # noqa: E501
        """CreditCardsAccountPaymentMethod - a model defined in Swagger"""  # noqa: E501
        self._identification_number = None
        self._is_multiple_credit_card = None
        self.discriminator = None
        self.identification_number = identification_number
        self.is_multiple_credit_card = is_multiple_credit_card

    @property
    def identification_number(self):
        """Gets the identification_number of this CreditCardsAccountPaymentMethod.  # noqa: E501

        Número de identificação do cartão: corresponde aos 4 últimos dígitos do cartão para pessoa natural, ou então, preencher com um identificador para pessoa jurídica, com as características definidas para os IDs no Open Finance.   # noqa: E501

        :return: The identification_number of this CreditCardsAccountPaymentMethod.  # noqa: E501
        :rtype: str
        """
        return self._identification_number

    @identification_number.setter
    def identification_number(self, identification_number):
        """Sets the identification_number of this CreditCardsAccountPaymentMethod.

        Número de identificação do cartão: corresponde aos 4 últimos dígitos do cartão para pessoa natural, ou então, preencher com um identificador para pessoa jurídica, com as características definidas para os IDs no Open Finance.   # noqa: E501

        :param identification_number: The identification_number of this CreditCardsAccountPaymentMethod.  # noqa: E501
        :type: str
        """
        if identification_number is None:
            raise ValueError("Invalid value for `identification_number`, must not be `None`")  # noqa: E501

        self._identification_number = identification_number

    @property
    def is_multiple_credit_card(self):
        """Gets the is_multiple_credit_card of this CreditCardsAccountPaymentMethod.  # noqa: E501

        Indica se o Cartão de crédito associado à conta pagamento pós-paga é múltiplo ou não. Cartões denominados múltiplos possuem tanto a função crédito quanto a função débito, devendo o proprietário do cartão, no momento de sua utilização, informar se o pagamento é na função crédito (que leva a um pagamento futuro, por meio de uma fatura do cartão de crédito) ou na função débito.   # noqa: E501

        :return: The is_multiple_credit_card of this CreditCardsAccountPaymentMethod.  # noqa: E501
        :rtype: bool
        """
        return self._is_multiple_credit_card

    @is_multiple_credit_card.setter
    def is_multiple_credit_card(self, is_multiple_credit_card):
        """Sets the is_multiple_credit_card of this CreditCardsAccountPaymentMethod.

        Indica se o Cartão de crédito associado à conta pagamento pós-paga é múltiplo ou não. Cartões denominados múltiplos possuem tanto a função crédito quanto a função débito, devendo o proprietário do cartão, no momento de sua utilização, informar se o pagamento é na função crédito (que leva a um pagamento futuro, por meio de uma fatura do cartão de crédito) ou na função débito.   # noqa: E501

        :param is_multiple_credit_card: The is_multiple_credit_card of this CreditCardsAccountPaymentMethod.  # noqa: E501
        :type: bool
        """
        if is_multiple_credit_card is None:
            raise ValueError("Invalid value for `is_multiple_credit_card`, must not be `None`")  # noqa: E501

        self._is_multiple_credit_card = is_multiple_credit_card

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CreditCardsAccountPaymentMethod, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreditCardsAccountPaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
