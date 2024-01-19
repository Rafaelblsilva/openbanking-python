# coding: utf-8

"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NewCar(object):
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
        'contract_base': 'ContractBase',
        'maximum_calculating_period': 'int'
    }

    attribute_map = {
        'contract_base': 'contractBase',
        'maximum_calculating_period': 'maximumCalculatingPeriod'
    }

    def __init__(self, contract_base=None, maximum_calculating_period=None):  # noqa: E501
        """NewCar - a model defined in Swagger"""  # noqa: E501
        self._contract_base = None
        self._maximum_calculating_period = None
        self.discriminator = None
        if contract_base is not None:
            self.contract_base = contract_base
        if maximum_calculating_period is not None:
            self.maximum_calculating_period = maximum_calculating_period

    @property
    def contract_base(self):
        """Gets the contract_base of this NewCar.  # noqa: E501


        :return: The contract_base of this NewCar.  # noqa: E501
        :rtype: ContractBase
        """
        return self._contract_base

    @contract_base.setter
    def contract_base(self, contract_base):
        """Sets the contract_base of this NewCar.


        :param contract_base: The contract_base of this NewCar.  # noqa: E501
        :type: ContractBase
        """

        self._contract_base = contract_base

    @property
    def maximum_calculating_period(self):
        """Gets the maximum_calculating_period of this NewCar.  # noqa: E501

        Prazo máximo para veículo zero quilômetro em meses  # noqa: E501

        :return: The maximum_calculating_period of this NewCar.  # noqa: E501
        :rtype: int
        """
        return self._maximum_calculating_period

    @maximum_calculating_period.setter
    def maximum_calculating_period(self, maximum_calculating_period):
        """Sets the maximum_calculating_period of this NewCar.

        Prazo máximo para veículo zero quilômetro em meses  # noqa: E501

        :param maximum_calculating_period: The maximum_calculating_period of this NewCar.  # noqa: E501
        :type: int
        """

        self._maximum_calculating_period = maximum_calculating_period

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
        if issubclass(NewCar, dict):
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
        if not isinstance(other, NewCar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
