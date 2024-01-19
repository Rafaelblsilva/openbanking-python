# coding: utf-8

"""
    API Capitalization-bonds - Open Finance Brasil

    As APIs descritas neste documento é referente a API de Capitalização da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions(object):
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
        'quota': 'float',
        'rate': 'float'
    }

    attribute_map = {
        'quota': 'quota',
        'rate': 'rate'
    }

    def __init__(self, quota=None, rate=None):  # noqa: E501
        """CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions - a model defined in Swagger"""  # noqa: E501
        self._quota = None
        self._rate = None
        self.discriminator = None
        self.quota = quota
        self.rate = rate

    @property
    def quota(self):
        """Gets the quota of this CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions.  # noqa: E501

        Parcela relativa ao Resgate Antecipado  # noqa: E501

        :return: The quota of this CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions.  # noqa: E501
        :rtype: float
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions.

        Parcela relativa ao Resgate Antecipado  # noqa: E501

        :param quota: The quota of this CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions.  # noqa: E501
        :type: float
        """
        if quota is None:
            raise ValueError("Invalid value for `quota`, must not be `None`")  # noqa: E501

        self._quota = quota

    @property
    def rate(self):
        """Gets the rate of this CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions.  # noqa: E501

        Taxa relativa ao Resgate Antecipado  # noqa: E501

        :return: The rate of this CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions.

        Taxa relativa ao Resgate Antecipado  # noqa: E501

        :param rate: The rate of this CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions.  # noqa: E501
        :type: float
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

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
        if issubclass(CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions, dict):
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
        if not isinstance(other, CapitalizationBondsProductCapitalizationPeriodEarlyRedemptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other