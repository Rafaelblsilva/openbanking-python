# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardInterestInterestRates(object):
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
        'code': 'str',
        'additional_info': 'str',
        'prices': 'list[CreditCardInterestPrices]',
        'minimum_rate': 'str',
        'maximum_rate': 'str'
    }

    attribute_map = {
        'code': 'code',
        'additional_info': 'additionalInfo',
        'prices': 'prices',
        'minimum_rate': 'minimumRate',
        'maximum_rate': 'maximumRate'
    }

    def __init__(self, code=None, additional_info=None, prices=None, minimum_rate=None, maximum_rate=None):  # noqa: E501
        """CreditCardInterestInterestRates - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._additional_info = None
        self._prices = None
        self._minimum_rate = None
        self._maximum_rate = None
        self.discriminator = None
        self.code = code
        if additional_info is not None:
            self.additional_info = additional_info
        self.prices = prices
        self.minimum_rate = minimum_rate
        self.maximum_rate = maximum_rate

    @property
    def code(self):
        """Gets the code of this CreditCardInterestInterestRates.  # noqa: E501

        Lista de outras operações de crédito  # noqa: E501

        :return: The code of this CreditCardInterestInterestRates.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CreditCardInterestInterestRates.

        Lista de outras operações de crédito  # noqa: E501

        :param code: The code of this CreditCardInterestInterestRates.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        allowed_values = ["SAQUE_A_CREDITO", "PAGAMENTOS_CONTAS", "OUTROS"]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def additional_info(self):
        """Gets the additional_info of this CreditCardInterestInterestRates.  # noqa: E501

        Campo Texto para descrever outras operações de crédito marcadas como 'Outros'  # noqa: E501

        :return: The additional_info of this CreditCardInterestInterestRates.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this CreditCardInterestInterestRates.

        Campo Texto para descrever outras operações de crédito marcadas como 'Outros'  # noqa: E501

        :param additional_info: The additional_info of this CreditCardInterestInterestRates.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def prices(self):
        """Gets the prices of this CreditCardInterestInterestRates.  # noqa: E501


        :return: The prices of this CreditCardInterestInterestRates.  # noqa: E501
        :rtype: list[CreditCardInterestPrices]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """Sets the prices of this CreditCardInterestInterestRates.


        :param prices: The prices of this CreditCardInterestInterestRates.  # noqa: E501
        :type: list[CreditCardInterestPrices]
        """
        if prices is None:
            raise ValueError("Invalid value for `prices`, must not be `None`")  # noqa: E501

        self._prices = prices

    @property
    def minimum_rate(self):
        """Gets the minimum_rate of this CreditCardInterestInterestRates.  # noqa: E501

        Percentual mínimo cobrado (taxa efetiva) para  outras operações de crédito do mês de referência.  # noqa: E501

        :return: The minimum_rate of this CreditCardInterestInterestRates.  # noqa: E501
        :rtype: str
        """
        return self._minimum_rate

    @minimum_rate.setter
    def minimum_rate(self, minimum_rate):
        """Sets the minimum_rate of this CreditCardInterestInterestRates.

        Percentual mínimo cobrado (taxa efetiva) para  outras operações de crédito do mês de referência.  # noqa: E501

        :param minimum_rate: The minimum_rate of this CreditCardInterestInterestRates.  # noqa: E501
        :type: str
        """
        if minimum_rate is None:
            raise ValueError("Invalid value for `minimum_rate`, must not be `None`")  # noqa: E501

        self._minimum_rate = minimum_rate

    @property
    def maximum_rate(self):
        """Gets the maximum_rate of this CreditCardInterestInterestRates.  # noqa: E501

        Percentual máximo cobrado (taxa efetiva) para  outras operações de crédito do mês de referência.  # noqa: E501

        :return: The maximum_rate of this CreditCardInterestInterestRates.  # noqa: E501
        :rtype: str
        """
        return self._maximum_rate

    @maximum_rate.setter
    def maximum_rate(self, maximum_rate):
        """Sets the maximum_rate of this CreditCardInterestInterestRates.

        Percentual máximo cobrado (taxa efetiva) para  outras operações de crédito do mês de referência.  # noqa: E501

        :param maximum_rate: The maximum_rate of this CreditCardInterestInterestRates.  # noqa: E501
        :type: str
        """
        if maximum_rate is None:
            raise ValueError("Invalid value for `maximum_rate`, must not be `None`")  # noqa: E501

        self._maximum_rate = maximum_rate

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
        if issubclass(CreditCardInterestInterestRates, dict):
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
        if not isinstance(other, CreditCardInterestInterestRates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
