# coding: utf-8

"""
    API OpenData Accounts do Open Finance Brasil

    A API descrita neste documento é referente as API Accounts da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-beta.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountsTermsConditions(object):
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
        'minimum_balance': 'MinimumBalance',
        'elegibility_criteria_info': 'str',
        'closing_process_info': 'str'
    }

    attribute_map = {
        'minimum_balance': 'minimumBalance',
        'elegibility_criteria_info': 'elegibilityCriteriaInfo',
        'closing_process_info': 'closingProcessInfo'
    }

    def __init__(self, minimum_balance=None, elegibility_criteria_info=None, closing_process_info=None):  # noqa: E501
        """AccountsTermsConditions - a model defined in Swagger"""  # noqa: E501
        self._minimum_balance = None
        self._elegibility_criteria_info = None
        self._closing_process_info = None
        self.discriminator = None
        self.minimum_balance = minimum_balance
        self.elegibility_criteria_info = elegibility_criteria_info
        self.closing_process_info = closing_process_info

    @property
    def minimum_balance(self):
        """Gets the minimum_balance of this AccountsTermsConditions.  # noqa: E501


        :return: The minimum_balance of this AccountsTermsConditions.  # noqa: E501
        :rtype: MinimumBalance
        """
        return self._minimum_balance

    @minimum_balance.setter
    def minimum_balance(self, minimum_balance):
        """Sets the minimum_balance of this AccountsTermsConditions.


        :param minimum_balance: The minimum_balance of this AccountsTermsConditions.  # noqa: E501
        :type: MinimumBalance
        """
        if minimum_balance is None:
            raise ValueError("Invalid value for `minimum_balance`, must not be `None`")  # noqa: E501

        self._minimum_balance = minimum_balance

    @property
    def elegibility_criteria_info(self):
        """Gets the elegibility_criteria_info of this AccountsTermsConditions.  # noqa: E501

        Critérios de qualificação do cliente com a finalidade de definir sua elegibilidade para a aquisição do tipo de conta. Campo Aberto  # noqa: E501

        :return: The elegibility_criteria_info of this AccountsTermsConditions.  # noqa: E501
        :rtype: str
        """
        return self._elegibility_criteria_info

    @elegibility_criteria_info.setter
    def elegibility_criteria_info(self, elegibility_criteria_info):
        """Sets the elegibility_criteria_info of this AccountsTermsConditions.

        Critérios de qualificação do cliente com a finalidade de definir sua elegibilidade para a aquisição do tipo de conta. Campo Aberto  # noqa: E501

        :param elegibility_criteria_info: The elegibility_criteria_info of this AccountsTermsConditions.  # noqa: E501
        :type: str
        """
        if elegibility_criteria_info is None:
            raise ValueError("Invalid value for `elegibility_criteria_info`, must not be `None`")  # noqa: E501

        self._elegibility_criteria_info = elegibility_criteria_info

    @property
    def closing_process_info(self):
        """Gets the closing_process_info of this AccountsTermsConditions.  # noqa: E501

        Procedimentos de encerramento para o tipo de conta tratado. Possibilidade de inscrição da URL. Endereço eletrônico de acesso ao canal. p.ex. 'https://example.com/mobile-banking'   # noqa: E501

        :return: The closing_process_info of this AccountsTermsConditions.  # noqa: E501
        :rtype: str
        """
        return self._closing_process_info

    @closing_process_info.setter
    def closing_process_info(self, closing_process_info):
        """Sets the closing_process_info of this AccountsTermsConditions.

        Procedimentos de encerramento para o tipo de conta tratado. Possibilidade de inscrição da URL. Endereço eletrônico de acesso ao canal. p.ex. 'https://example.com/mobile-banking'   # noqa: E501

        :param closing_process_info: The closing_process_info of this AccountsTermsConditions.  # noqa: E501
        :type: str
        """
        if closing_process_info is None:
            raise ValueError("Invalid value for `closing_process_info`, must not be `None`")  # noqa: E501

        self._closing_process_info = closing_process_info

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
        if issubclass(AccountsTermsConditions, dict):
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
        if not isinstance(other, AccountsTermsConditions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
