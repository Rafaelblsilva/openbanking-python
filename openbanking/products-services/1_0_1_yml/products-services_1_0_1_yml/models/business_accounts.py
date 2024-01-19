# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BusinessAccounts(object):
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
        'type': 'AccountType',
        'fees': 'BusinessAccountsFees',
        'service_bundles': 'list[ServiceBundle]',
        'opening_closing_channels': 'list[OpeningClosingChannels]',
        'additional_info': 'str',
        'transaction_methods': 'list[TransactionMethods]',
        'terms_conditions': 'AccountsTermsConditions',
        'income_rate': 'AccountsIncomeRate'
    }

    attribute_map = {
        'type': 'type',
        'fees': 'fees',
        'service_bundles': 'serviceBundles',
        'opening_closing_channels': 'openingClosingChannels',
        'additional_info': 'additionalInfo',
        'transaction_methods': 'transactionMethods',
        'terms_conditions': 'termsConditions',
        'income_rate': 'incomeRate'
    }

    def __init__(self, type=None, fees=None, service_bundles=None, opening_closing_channels=None, additional_info=None, transaction_methods=None, terms_conditions=None, income_rate=None):  # noqa: E501
        """BusinessAccounts - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._fees = None
        self._service_bundles = None
        self._opening_closing_channels = None
        self._additional_info = None
        self._transaction_methods = None
        self._terms_conditions = None
        self._income_rate = None
        self.discriminator = None
        self.type = type
        self.fees = fees
        self.service_bundles = service_bundles
        self.opening_closing_channels = opening_closing_channels
        if additional_info is not None:
            self.additional_info = additional_info
        self.transaction_methods = transaction_methods
        self.terms_conditions = terms_conditions
        self.income_rate = income_rate

    @property
    def type(self):
        """Gets the type of this BusinessAccounts.  # noqa: E501


        :return: The type of this BusinessAccounts.  # noqa: E501
        :rtype: AccountType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BusinessAccounts.


        :param type: The type of this BusinessAccounts.  # noqa: E501
        :type: AccountType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def fees(self):
        """Gets the fees of this BusinessAccounts.  # noqa: E501


        :return: The fees of this BusinessAccounts.  # noqa: E501
        :rtype: BusinessAccountsFees
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this BusinessAccounts.


        :param fees: The fees of this BusinessAccounts.  # noqa: E501
        :type: BusinessAccountsFees
        """
        if fees is None:
            raise ValueError("Invalid value for `fees`, must not be `None`")  # noqa: E501

        self._fees = fees

    @property
    def service_bundles(self):
        """Gets the service_bundles of this BusinessAccounts.  # noqa: E501

        Lista dos serviços que compõe o pacote de serviços  # noqa: E501

        :return: The service_bundles of this BusinessAccounts.  # noqa: E501
        :rtype: list[ServiceBundle]
        """
        return self._service_bundles

    @service_bundles.setter
    def service_bundles(self, service_bundles):
        """Sets the service_bundles of this BusinessAccounts.

        Lista dos serviços que compõe o pacote de serviços  # noqa: E501

        :param service_bundles: The service_bundles of this BusinessAccounts.  # noqa: E501
        :type: list[ServiceBundle]
        """
        if service_bundles is None:
            raise ValueError("Invalid value for `service_bundles`, must not be `None`")  # noqa: E501

        self._service_bundles = service_bundles

    @property
    def opening_closing_channels(self):
        """Gets the opening_closing_channels of this BusinessAccounts.  # noqa: E501

        Lista dos canais para aberturas e encerramento  # noqa: E501

        :return: The opening_closing_channels of this BusinessAccounts.  # noqa: E501
        :rtype: list[OpeningClosingChannels]
        """
        return self._opening_closing_channels

    @opening_closing_channels.setter
    def opening_closing_channels(self, opening_closing_channels):
        """Sets the opening_closing_channels of this BusinessAccounts.

        Lista dos canais para aberturas e encerramento  # noqa: E501

        :param opening_closing_channels: The opening_closing_channels of this BusinessAccounts.  # noqa: E501
        :type: list[OpeningClosingChannels]
        """
        if opening_closing_channels is None:
            raise ValueError("Invalid value for `opening_closing_channels`, must not be `None`")  # noqa: E501

        self._opening_closing_channels = opening_closing_channels

    @property
    def additional_info(self):
        """Gets the additional_info of this BusinessAccounts.  # noqa: E501

        Texto livre para complementar informação relativa ao Canal disponível, quando no campo ''openingClosingChannels'' estiver preenchida a opção ''Outros'' Restrição: Campo de preenchimento obrigatório se ''openingCloseChannels'' estiver preenchida a opção ''OUTROS''   # noqa: E501

        :return: The additional_info of this BusinessAccounts.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this BusinessAccounts.

        Texto livre para complementar informação relativa ao Canal disponível, quando no campo ''openingClosingChannels'' estiver preenchida a opção ''Outros'' Restrição: Campo de preenchimento obrigatório se ''openingCloseChannels'' estiver preenchida a opção ''OUTROS''   # noqa: E501

        :param additional_info: The additional_info of this BusinessAccounts.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def transaction_methods(self):
        """Gets the transaction_methods of this BusinessAccounts.  # noqa: E501

        Lista de formas de movimentação  # noqa: E501

        :return: The transaction_methods of this BusinessAccounts.  # noqa: E501
        :rtype: list[TransactionMethods]
        """
        return self._transaction_methods

    @transaction_methods.setter
    def transaction_methods(self, transaction_methods):
        """Sets the transaction_methods of this BusinessAccounts.

        Lista de formas de movimentação  # noqa: E501

        :param transaction_methods: The transaction_methods of this BusinessAccounts.  # noqa: E501
        :type: list[TransactionMethods]
        """
        if transaction_methods is None:
            raise ValueError("Invalid value for `transaction_methods`, must not be `None`")  # noqa: E501

        self._transaction_methods = transaction_methods

    @property
    def terms_conditions(self):
        """Gets the terms_conditions of this BusinessAccounts.  # noqa: E501


        :return: The terms_conditions of this BusinessAccounts.  # noqa: E501
        :rtype: AccountsTermsConditions
        """
        return self._terms_conditions

    @terms_conditions.setter
    def terms_conditions(self, terms_conditions):
        """Sets the terms_conditions of this BusinessAccounts.


        :param terms_conditions: The terms_conditions of this BusinessAccounts.  # noqa: E501
        :type: AccountsTermsConditions
        """
        if terms_conditions is None:
            raise ValueError("Invalid value for `terms_conditions`, must not be `None`")  # noqa: E501

        self._terms_conditions = terms_conditions

    @property
    def income_rate(self):
        """Gets the income_rate of this BusinessAccounts.  # noqa: E501


        :return: The income_rate of this BusinessAccounts.  # noqa: E501
        :rtype: AccountsIncomeRate
        """
        return self._income_rate

    @income_rate.setter
    def income_rate(self, income_rate):
        """Sets the income_rate of this BusinessAccounts.


        :param income_rate: The income_rate of this BusinessAccounts.  # noqa: E501
        :type: AccountsIncomeRate
        """
        if income_rate is None:
            raise ValueError("Invalid value for `income_rate`, must not be `None`")  # noqa: E501

        self._income_rate = income_rate

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
        if issubclass(BusinessAccounts, dict):
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
        if not isinstance(other, BusinessAccounts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
