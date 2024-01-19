# coding: utf-8

"""
    API's OpenData do Open Finance Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountPriorityService(object):
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
        'name': 'PriorityServiceName',
        'code': 'AccountPriorityServiceCode',
        'charging_trigger_info': 'str',
        'prices': 'list[Price]',
        'minimum': 'MinimumPrice',
        'maximum': 'MaximumPrice'
    }

    attribute_map = {
        'name': 'name',
        'code': 'code',
        'charging_trigger_info': 'chargingTriggerInfo',
        'prices': 'prices',
        'minimum': 'minimum',
        'maximum': 'maximum'
    }

    def __init__(self, name=None, code=None, charging_trigger_info=None, prices=None, minimum=None, maximum=None):  # noqa: E501
        """AccountPriorityService - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._code = None
        self._charging_trigger_info = None
        self._prices = None
        self._minimum = None
        self._maximum = None
        self.discriminator = None
        self.name = name
        self.code = code
        self.charging_trigger_info = charging_trigger_info
        self.prices = prices
        self.minimum = minimum
        self.maximum = maximum

    @property
    def name(self):
        """Gets the name of this AccountPriorityService.  # noqa: E501


        :return: The name of this AccountPriorityService.  # noqa: E501
        :rtype: PriorityServiceName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountPriorityService.


        :param name: The name of this AccountPriorityService.  # noqa: E501
        :type: PriorityServiceName
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def code(self):
        """Gets the code of this AccountPriorityService.  # noqa: E501


        :return: The code of this AccountPriorityService.  # noqa: E501
        :rtype: AccountPriorityServiceCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AccountPriorityService.


        :param code: The code of this AccountPriorityService.  # noqa: E501
        :type: AccountPriorityServiceCode
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def charging_trigger_info(self):
        """Gets the charging_trigger_info of this AccountPriorityService.  # noqa: E501

        Fatos geradores de cobrança que incidem sobre os serviços prioritários, segundo Resolução 3.919 do Bacen, para pessoa natural.  # noqa: E501

        :return: The charging_trigger_info of this AccountPriorityService.  # noqa: E501
        :rtype: str
        """
        return self._charging_trigger_info

    @charging_trigger_info.setter
    def charging_trigger_info(self, charging_trigger_info):
        """Sets the charging_trigger_info of this AccountPriorityService.

        Fatos geradores de cobrança que incidem sobre os serviços prioritários, segundo Resolução 3.919 do Bacen, para pessoa natural.  # noqa: E501

        :param charging_trigger_info: The charging_trigger_info of this AccountPriorityService.  # noqa: E501
        :type: str
        """
        if charging_trigger_info is None:
            raise ValueError("Invalid value for `charging_trigger_info`, must not be `None`")  # noqa: E501

        self._charging_trigger_info = charging_trigger_info

    @property
    def prices(self):
        """Gets the prices of this AccountPriorityService.  # noqa: E501

        Lista distribuição preços tarifas de serviços  # noqa: E501

        :return: The prices of this AccountPriorityService.  # noqa: E501
        :rtype: list[Price]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """Sets the prices of this AccountPriorityService.

        Lista distribuição preços tarifas de serviços  # noqa: E501

        :param prices: The prices of this AccountPriorityService.  # noqa: E501
        :type: list[Price]
        """
        if prices is None:
            raise ValueError("Invalid value for `prices`, must not be `None`")  # noqa: E501

        self._prices = prices

    @property
    def minimum(self):
        """Gets the minimum of this AccountPriorityService.  # noqa: E501


        :return: The minimum of this AccountPriorityService.  # noqa: E501
        :rtype: MinimumPrice
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this AccountPriorityService.


        :param minimum: The minimum of this AccountPriorityService.  # noqa: E501
        :type: MinimumPrice
        """
        if minimum is None:
            raise ValueError("Invalid value for `minimum`, must not be `None`")  # noqa: E501

        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this AccountPriorityService.  # noqa: E501


        :return: The maximum of this AccountPriorityService.  # noqa: E501
        :rtype: MaximumPrice
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this AccountPriorityService.


        :param maximum: The maximum of this AccountPriorityService.  # noqa: E501
        :type: MaximumPrice
        """
        if maximum is None:
            raise ValueError("Invalid value for `maximum`, must not be `None`")  # noqa: E501

        self._maximum = maximum

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
        if issubclass(AccountPriorityService, dict):
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
        if not isinstance(other, AccountPriorityService):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
