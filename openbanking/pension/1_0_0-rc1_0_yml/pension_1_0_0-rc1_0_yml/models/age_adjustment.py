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

class AgeAdjustment(object):
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
        'criterias': 'list[str]',
        'frequency': 'int'
    }

    attribute_map = {
        'criterias': 'criterias',
        'frequency': 'frequency'
    }

    def __init__(self, criterias=None, frequency=None):  # noqa: E501
        """AgeAdjustment - a model defined in Swagger"""  # noqa: E501
        self._criterias = None
        self._frequency = None
        self.discriminator = None
        self.criterias = criterias
        self.frequency = frequency

    @property
    def criterias(self):
        """Gets the criterias of this AgeAdjustment.  # noqa: E501


        :return: The criterias of this AgeAdjustment.  # noqa: E501
        :rtype: list[str]
        """
        return self._criterias

    @criterias.setter
    def criterias(self, criterias):
        """Sets the criterias of this AgeAdjustment.


        :param criterias: The criterias of this AgeAdjustment.  # noqa: E501
        :type: list[str]
        """
        if criterias is None:
            raise ValueError("Invalid value for `criterias`, must not be `None`")  # noqa: E501
        allowed_values = ["APOS_PERIODO_ANOS", "CADA_PERIODO_ANOS", "MUDANCA_FAIXA_ETARIA", "NAO_APLICAVEL"]  # noqa: E501
        if not set(criterias).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `criterias` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(criterias) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._criterias = criterias

    @property
    def frequency(self):
        """Gets the frequency of this AgeAdjustment.  # noqa: E501

        Período em anos, caso critério de reenquadramento após ou a cada período em anos.  # noqa: E501

        :return: The frequency of this AgeAdjustment.  # noqa: E501
        :rtype: int
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this AgeAdjustment.

        Período em anos, caso critério de reenquadramento após ou a cada período em anos.  # noqa: E501

        :param frequency: The frequency of this AgeAdjustment.  # noqa: E501
        :type: int
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501

        self._frequency = frequency

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
        if issubclass(AgeAdjustment, dict):
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
        if not isinstance(other, AgeAdjustment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
