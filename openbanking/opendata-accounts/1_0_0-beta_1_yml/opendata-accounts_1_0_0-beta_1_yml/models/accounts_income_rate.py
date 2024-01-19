# coding: utf-8

"""
    API OpenData Accounts do Open Finance Brasil

    A API descrita neste documento é referente as API Accounts da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountsIncomeRate(object):
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
        'saving_account': 'str',
        'prepaid_payment_account': 'str'
    }

    attribute_map = {
        'saving_account': 'savingAccount',
        'prepaid_payment_account': 'prepaidPaymentAccount'
    }

    def __init__(self, saving_account=None, prepaid_payment_account=None):  # noqa: E501
        """AccountsIncomeRate - a model defined in Swagger"""  # noqa: E501
        self._saving_account = None
        self._prepaid_payment_account = None
        self.discriminator = None
        if saving_account is not None:
            self.saving_account = saving_account
        if prepaid_payment_account is not None:
            self.prepaid_payment_account = prepaid_payment_account

    @property
    def saving_account(self):
        """Gets the saving_account of this AccountsIncomeRate.  # noqa: E501

        Descrição da Remuneração especificamente para Conta de Poupança. Deve ser preenchido com a determinação legal vigente.   [Restrição] Obrigatório quando \"type\" for igual \"CONTA_POUPANCA\".   # noqa: E501

        :return: The saving_account of this AccountsIncomeRate.  # noqa: E501
        :rtype: str
        """
        return self._saving_account

    @saving_account.setter
    def saving_account(self, saving_account):
        """Sets the saving_account of this AccountsIncomeRate.

        Descrição da Remuneração especificamente para Conta de Poupança. Deve ser preenchido com a determinação legal vigente.   [Restrição] Obrigatório quando \"type\" for igual \"CONTA_POUPANCA\".   # noqa: E501

        :param saving_account: The saving_account of this AccountsIncomeRate.  # noqa: E501
        :type: str
        """

        self._saving_account = saving_account

    @property
    def prepaid_payment_account(self):
        """Gets the prepaid_payment_account of this AccountsIncomeRate.  # noqa: E501

        Campo Livre. Deve explicitar o Percentual em favor do titular da conta de pagamento pré-paga.  # noqa: E501

        :return: The prepaid_payment_account of this AccountsIncomeRate.  # noqa: E501
        :rtype: str
        """
        return self._prepaid_payment_account

    @prepaid_payment_account.setter
    def prepaid_payment_account(self, prepaid_payment_account):
        """Sets the prepaid_payment_account of this AccountsIncomeRate.

        Campo Livre. Deve explicitar o Percentual em favor do titular da conta de pagamento pré-paga.  # noqa: E501

        :param prepaid_payment_account: The prepaid_payment_account of this AccountsIncomeRate.  # noqa: E501
        :type: str
        """

        self._prepaid_payment_account = prepaid_payment_account

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
        if issubclass(AccountsIncomeRate, dict):
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
        if not isinstance(other, AccountsIncomeRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
