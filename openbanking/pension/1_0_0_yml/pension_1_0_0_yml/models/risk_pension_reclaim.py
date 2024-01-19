# coding: utf-8

"""
    API Pension - Open Finance Brasil

    API de Previdência do Open Finance Brasil – Fase 4. API que retorna informações de Previdência.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RiskPensionReclaim(object):
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
        'table': 'list[RiskPensionReclaimTableItem]',
        'grace_period': 'RiskPensionGracePeriod',
        'differenciated_percentage': 'object'
    }

    attribute_map = {
        'table': 'table',
        'grace_period': 'gracePeriod',
        'differenciated_percentage': 'differenciatedPercentage'
    }

    def __init__(self, table=None, grace_period=None, differenciated_percentage=None):  # noqa: E501
        """RiskPensionReclaim - a model defined in Swagger"""  # noqa: E501
        self._table = None
        self._grace_period = None
        self._differenciated_percentage = None
        self.discriminator = None
        if table is not None:
            self.table = table
        self.grace_period = grace_period
        if differenciated_percentage is not None:
            self.differenciated_percentage = differenciated_percentage

    @property
    def table(self):
        """Gets the table of this RiskPensionReclaim.  # noqa: E501


        :return: The table of this RiskPensionReclaim.  # noqa: E501
        :rtype: list[RiskPensionReclaimTableItem]
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this RiskPensionReclaim.


        :param table: The table of this RiskPensionReclaim.  # noqa: E501
        :type: list[RiskPensionReclaimTableItem]
        """

        self._table = table

    @property
    def grace_period(self):
        """Gets the grace_period of this RiskPensionReclaim.  # noqa: E501


        :return: The grace_period of this RiskPensionReclaim.  # noqa: E501
        :rtype: RiskPensionGracePeriod
        """
        return self._grace_period

    @grace_period.setter
    def grace_period(self, grace_period):
        """Sets the grace_period of this RiskPensionReclaim.


        :param grace_period: The grace_period of this RiskPensionReclaim.  # noqa: E501
        :type: RiskPensionGracePeriod
        """
        if grace_period is None:
            raise ValueError("Invalid value for `grace_period`, must not be `None`")  # noqa: E501

        self._grace_period = grace_period

    @property
    def differenciated_percentage(self):
        """Gets the differenciated_percentage of this RiskPensionReclaim.  # noqa: E501

        Campo aberto (possibilidade de incluir URL)  # noqa: E501

        :return: The differenciated_percentage of this RiskPensionReclaim.  # noqa: E501
        :rtype: object
        """
        return self._differenciated_percentage

    @differenciated_percentage.setter
    def differenciated_percentage(self, differenciated_percentage):
        """Sets the differenciated_percentage of this RiskPensionReclaim.

        Campo aberto (possibilidade de incluir URL)  # noqa: E501

        :param differenciated_percentage: The differenciated_percentage of this RiskPensionReclaim.  # noqa: E501
        :type: object
        """

        self._differenciated_percentage = differenciated_percentage

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
        if issubclass(RiskPensionReclaim, dict):
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
        if not isinstance(other, RiskPensionReclaim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
