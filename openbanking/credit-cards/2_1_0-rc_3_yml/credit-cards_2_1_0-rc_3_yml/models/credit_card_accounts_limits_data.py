# coding: utf-8

"""
    API Credit-cards-accounts - Open Finance Brasil

    API de contas de pagamento pós-pagas do Open Finance Brasil – Fase 2. API que retorna informações de contas de pagamento pós-paga mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, produto, bandeira, limites de crédito, informações sobre transações de pagamento efetuadas e faturas.  Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.\\ ### `/accounts/{creditCardAccountId}/bills`   - description:     - Só deve ser informada uma fatura já fechada.     - Qualquer pagamento deve ser contado para a última fatura fechada. ### `/accounts/{creditCardAccountId}/bills/{billId}/transactions`   - description:     - A lista a retornar se refere a transações após base 2/clearing/conciliado ### `/accounts/{creditCardAccountId}/transactions`   - description:     - A lista a retornar se refere a transações após base 2/clearing/conciliado  ## Permissions necessárias para a API Credit-cards-accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}/bills`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_READ** ### `/accounts/{creditCardAccountId}/bills/{billId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/limits`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_LIMITS_READ** ### `/accounts/{creditCardAccountId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/transactions-current`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ**  ## Data de imutabilidade por tipo de transação O identificador de transações de cartão de crédito é de envio obrigatório no Open Finance Brasil. De acordo com o tipo da transação deve haver o envio de um identificador único, estável e imutável, conforme tabela abaixo. ```   |-------------------|-------------------------|-----------------------|   | Tipo de Transação | Data da Obrigatoriedade | Data da Imutabilidade |   |-------------------|-------------------------|-----------------------|   | PAGAMENTO         | DO                      | Fatura fechada        |   |-------------------|-------------------------|-----------------------|   | TARIFA            | DO                      | Fatura fechada        |   |-------------------|-------------------------|-----------------------|   | OPERACOES_CRED    | DO                      | Fatura fechada        |   |-------------------|-------------------------|-----------------------|   | ESTORNO           | DO                      | Fatura fechada        |   |-------------------|-------------------------|-----------------------|   | CASHBACK          | DO                      | Fatura fechada        |   |-------------------|-------------------------|-----------------------|   | OUTROS            | DO                      | Fatura fechada        |   |-------------------|-------------------------|-----------------------|   ```   # noqa: E501

    OpenAPI spec version: 2.1.0-rc.3
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardAccountsLimitsData(object):
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
        'credit_line_limit_type': 'EnumCreditCardAccountsLineLimitType',
        'consolidation_type': 'EnumCreditCardAccountsConsolidationType',
        'identification_number': 'str',
        'line_name': 'str',
        'line_name_additional_info': 'str',
        'is_limit_flexible': 'bool',
        'limit_amount': 'CreditCardsLimitAmount',
        'used_amount': 'CreditCardsUsedAmount',
        'available_amount': 'CreditCardsAvailableAmount',
        'customized_limit_amount': 'CreditCardAccountsLimitsDataCustomizedLimitAmount'
    }

    attribute_map = {
        'credit_line_limit_type': 'creditLineLimitType',
        'consolidation_type': 'consolidationType',
        'identification_number': 'identificationNumber',
        'line_name': 'lineName',
        'line_name_additional_info': 'lineNameAdditionalInfo',
        'is_limit_flexible': 'isLimitFlexible',
        'limit_amount': 'limitAmount',
        'used_amount': 'usedAmount',
        'available_amount': 'availableAmount',
        'customized_limit_amount': 'customizedLimitAmount'
    }

    def __init__(self, credit_line_limit_type=None, consolidation_type=None, identification_number=None, line_name=None, line_name_additional_info=None, is_limit_flexible=None, limit_amount=None, used_amount=None, available_amount=None, customized_limit_amount=None):  # noqa: E501
        """CreditCardAccountsLimitsData - a model defined in Swagger"""  # noqa: E501
        self._credit_line_limit_type = None
        self._consolidation_type = None
        self._identification_number = None
        self._line_name = None
        self._line_name_additional_info = None
        self._is_limit_flexible = None
        self._limit_amount = None
        self._used_amount = None
        self._available_amount = None
        self._customized_limit_amount = None
        self.discriminator = None
        self.credit_line_limit_type = credit_line_limit_type
        self.consolidation_type = consolidation_type
        self.identification_number = identification_number
        if line_name is not None:
            self.line_name = line_name
        if line_name_additional_info is not None:
            self.line_name_additional_info = line_name_additional_info
        self.is_limit_flexible = is_limit_flexible
        if limit_amount is not None:
            self.limit_amount = limit_amount
        self.used_amount = used_amount
        if available_amount is not None:
            self.available_amount = available_amount
        if customized_limit_amount is not None:
            self.customized_limit_amount = customized_limit_amount

    @property
    def credit_line_limit_type(self):
        """Gets the credit_line_limit_type of this CreditCardAccountsLimitsData.  # noqa: E501


        :return: The credit_line_limit_type of this CreditCardAccountsLimitsData.  # noqa: E501
        :rtype: EnumCreditCardAccountsLineLimitType
        """
        return self._credit_line_limit_type

    @credit_line_limit_type.setter
    def credit_line_limit_type(self, credit_line_limit_type):
        """Sets the credit_line_limit_type of this CreditCardAccountsLimitsData.


        :param credit_line_limit_type: The credit_line_limit_type of this CreditCardAccountsLimitsData.  # noqa: E501
        :type: EnumCreditCardAccountsLineLimitType
        """
        if credit_line_limit_type is None:
            raise ValueError("Invalid value for `credit_line_limit_type`, must not be `None`")  # noqa: E501

        self._credit_line_limit_type = credit_line_limit_type

    @property
    def consolidation_type(self):
        """Gets the consolidation_type of this CreditCardAccountsLimitsData.  # noqa: E501


        :return: The consolidation_type of this CreditCardAccountsLimitsData.  # noqa: E501
        :rtype: EnumCreditCardAccountsConsolidationType
        """
        return self._consolidation_type

    @consolidation_type.setter
    def consolidation_type(self, consolidation_type):
        """Sets the consolidation_type of this CreditCardAccountsLimitsData.


        :param consolidation_type: The consolidation_type of this CreditCardAccountsLimitsData.  # noqa: E501
        :type: EnumCreditCardAccountsConsolidationType
        """
        if consolidation_type is None:
            raise ValueError("Invalid value for `consolidation_type`, must not be `None`")  # noqa: E501

        self._consolidation_type = consolidation_type

    @property
    def identification_number(self):
        """Gets the identification_number of this CreditCardAccountsLimitsData.  # noqa: E501

        Número de identificação do cartão: corresponde aos 4 últimos dígitos do cartão para PF, ou então, preencher com um identificador para PJ, com as caracteristicas definidas para os IDs no Open Finance.   # noqa: E501

        :return: The identification_number of this CreditCardAccountsLimitsData.  # noqa: E501
        :rtype: str
        """
        return self._identification_number

    @identification_number.setter
    def identification_number(self, identification_number):
        """Sets the identification_number of this CreditCardAccountsLimitsData.

        Número de identificação do cartão: corresponde aos 4 últimos dígitos do cartão para PF, ou então, preencher com um identificador para PJ, com as caracteristicas definidas para os IDs no Open Finance.   # noqa: E501

        :param identification_number: The identification_number of this CreditCardAccountsLimitsData.  # noqa: E501
        :type: str
        """
        if identification_number is None:
            raise ValueError("Invalid value for `identification_number`, must not be `None`")  # noqa: E501

        self._identification_number = identification_number

    @property
    def line_name(self):
        """Gets the line_name of this CreditCardAccountsLimitsData.  # noqa: E501


        :return: The line_name of this CreditCardAccountsLimitsData.  # noqa: E501
        :rtype: str
        """
        return self._line_name

    @line_name.setter
    def line_name(self, line_name):
        """Sets the line_name of this CreditCardAccountsLimitsData.


        :param line_name: The line_name of this CreditCardAccountsLimitsData.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREDITO_A_VISTA", "CREDITO_PARCELADO", "SAQUE_CREDITO_BRASIL", "SAQUE_CREDITO_EXTERIOR", "EMPRESTIMO_CARTAO_CONSIGNADO", "OUTROS"]  # noqa: E501
        if line_name not in allowed_values:
            raise ValueError(
                "Invalid value for `line_name` ({0}), must be one of {1}"  # noqa: E501
                .format(line_name, allowed_values)
            )

        self._line_name = line_name

    @property
    def line_name_additional_info(self):
        """Gets the line_name_additional_info of this CreditCardAccountsLimitsData.  # noqa: E501

        Campo de preenchimento obrigatório se selecionada a opção 'OUTRAS' em lineName.  # noqa: E501

        :return: The line_name_additional_info of this CreditCardAccountsLimitsData.  # noqa: E501
        :rtype: str
        """
        return self._line_name_additional_info

    @line_name_additional_info.setter
    def line_name_additional_info(self, line_name_additional_info):
        """Sets the line_name_additional_info of this CreditCardAccountsLimitsData.

        Campo de preenchimento obrigatório se selecionada a opção 'OUTRAS' em lineName.  # noqa: E501

        :param line_name_additional_info: The line_name_additional_info of this CreditCardAccountsLimitsData.  # noqa: E501
        :type: str
        """

        self._line_name_additional_info = line_name_additional_info

    @property
    def is_limit_flexible(self):
        """Gets the is_limit_flexible of this CreditCardAccountsLimitsData.  # noqa: E501

        True= Indica que a conta cartão possui limite total flexível ou “sem limite”. False = Indica que a conta cartão possui limite predeterminado exibido no canal para o cliente.  # noqa: E501

        :return: The is_limit_flexible of this CreditCardAccountsLimitsData.  # noqa: E501
        :rtype: bool
        """
        return self._is_limit_flexible

    @is_limit_flexible.setter
    def is_limit_flexible(self, is_limit_flexible):
        """Sets the is_limit_flexible of this CreditCardAccountsLimitsData.

        True= Indica que a conta cartão possui limite total flexível ou “sem limite”. False = Indica que a conta cartão possui limite predeterminado exibido no canal para o cliente.  # noqa: E501

        :param is_limit_flexible: The is_limit_flexible of this CreditCardAccountsLimitsData.  # noqa: E501
        :type: bool
        """
        if is_limit_flexible is None:
            raise ValueError("Invalid value for `is_limit_flexible`, must not be `None`")  # noqa: E501

        self._is_limit_flexible = is_limit_flexible

    @property
    def limit_amount(self):
        """Gets the limit_amount of this CreditCardAccountsLimitsData.  # noqa: E501


        :return: The limit_amount of this CreditCardAccountsLimitsData.  # noqa: E501
        :rtype: CreditCardsLimitAmount
        """
        return self._limit_amount

    @limit_amount.setter
    def limit_amount(self, limit_amount):
        """Sets the limit_amount of this CreditCardAccountsLimitsData.


        :param limit_amount: The limit_amount of this CreditCardAccountsLimitsData.  # noqa: E501
        :type: CreditCardsLimitAmount
        """

        self._limit_amount = limit_amount

    @property
    def used_amount(self):
        """Gets the used_amount of this CreditCardAccountsLimitsData.  # noqa: E501


        :return: The used_amount of this CreditCardAccountsLimitsData.  # noqa: E501
        :rtype: CreditCardsUsedAmount
        """
        return self._used_amount

    @used_amount.setter
    def used_amount(self, used_amount):
        """Sets the used_amount of this CreditCardAccountsLimitsData.


        :param used_amount: The used_amount of this CreditCardAccountsLimitsData.  # noqa: E501
        :type: CreditCardsUsedAmount
        """
        if used_amount is None:
            raise ValueError("Invalid value for `used_amount`, must not be `None`")  # noqa: E501

        self._used_amount = used_amount

    @property
    def available_amount(self):
        """Gets the available_amount of this CreditCardAccountsLimitsData.  # noqa: E501


        :return: The available_amount of this CreditCardAccountsLimitsData.  # noqa: E501
        :rtype: CreditCardsAvailableAmount
        """
        return self._available_amount

    @available_amount.setter
    def available_amount(self, available_amount):
        """Sets the available_amount of this CreditCardAccountsLimitsData.


        :param available_amount: The available_amount of this CreditCardAccountsLimitsData.  # noqa: E501
        :type: CreditCardsAvailableAmount
        """

        self._available_amount = available_amount

    @property
    def customized_limit_amount(self):
        """Gets the customized_limit_amount of this CreditCardAccountsLimitsData.  # noqa: E501


        :return: The customized_limit_amount of this CreditCardAccountsLimitsData.  # noqa: E501
        :rtype: CreditCardAccountsLimitsDataCustomizedLimitAmount
        """
        return self._customized_limit_amount

    @customized_limit_amount.setter
    def customized_limit_amount(self, customized_limit_amount):
        """Sets the customized_limit_amount of this CreditCardAccountsLimitsData.


        :param customized_limit_amount: The customized_limit_amount of this CreditCardAccountsLimitsData.  # noqa: E501
        :type: CreditCardAccountsLimitsDataCustomizedLimitAmount
        """

        self._customized_limit_amount = customized_limit_amount

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
        if issubclass(CreditCardAccountsLimitsData, dict):
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
        if not isinstance(other, CreditCardAccountsLimitsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
