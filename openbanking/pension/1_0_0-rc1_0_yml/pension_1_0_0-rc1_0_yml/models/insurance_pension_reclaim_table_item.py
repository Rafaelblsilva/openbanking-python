# coding: utf-8

"""
    API Pension - Open Finance Brasil

    API de Previdência do Open Finance Brasil – Fase 4. API que retorna informações de Previdência.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InsurancePensionReclaimTableItem(object):
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
        'initial_month_range': 'int',
        'final_month_range': 'int',
        'percentage': 'str'
    }

    attribute_map = {
        'initial_month_range': 'initialMonthRange',
        'final_month_range': 'finalMonthRange',
        'percentage': 'percentage'
    }

    def __init__(self, initial_month_range=None, final_month_range=None, percentage=None):  # noqa: E501
        """InsurancePensionReclaimTableItem - a model defined in Swagger"""  # noqa: E501
        self._initial_month_range = None
        self._final_month_range = None
        self._percentage = None
        self.discriminator = None
        if initial_month_range is not None:
            self.initial_month_range = initial_month_range
        if final_month_range is not None:
            self.final_month_range = final_month_range
        if percentage is not None:
            self.percentage = percentage

    @property
    def initial_month_range(self):
        """Gets the initial_month_range of this InsurancePensionReclaimTableItem.  # noqa: E501


        :return: The initial_month_range of this InsurancePensionReclaimTableItem.  # noqa: E501
        :rtype: int
        """
        return self._initial_month_range

    @initial_month_range.setter
    def initial_month_range(self, initial_month_range):
        """Sets the initial_month_range of this InsurancePensionReclaimTableItem.


        :param initial_month_range: The initial_month_range of this InsurancePensionReclaimTableItem.  # noqa: E501
        :type: int
        """

        self._initial_month_range = initial_month_range

    @property
    def final_month_range(self):
        """Gets the final_month_range of this InsurancePensionReclaimTableItem.  # noqa: E501


        :return: The final_month_range of this InsurancePensionReclaimTableItem.  # noqa: E501
        :rtype: int
        """
        return self._final_month_range

    @final_month_range.setter
    def final_month_range(self, final_month_range):
        """Sets the final_month_range of this InsurancePensionReclaimTableItem.


        :param final_month_range: The final_month_range of this InsurancePensionReclaimTableItem.  # noqa: E501
        :type: int
        """

        self._final_month_range = final_month_range

    @property
    def percentage(self):
        """Gets the percentage of this InsurancePensionReclaimTableItem.  # noqa: E501

        Percentual de faixa de resgate.  # noqa: E501

        :return: The percentage of this InsurancePensionReclaimTableItem.  # noqa: E501
        :rtype: str
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this InsurancePensionReclaimTableItem.

        Percentual de faixa de resgate.  # noqa: E501

        :param percentage: The percentage of this InsurancePensionReclaimTableItem.  # noqa: E501
        :type: str
        """

        self._percentage = percentage

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
        if issubclass(InsurancePensionReclaimTableItem, dict):
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
        if not isinstance(other, InsurancePensionReclaimTableItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
