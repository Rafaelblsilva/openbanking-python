# coding: utf-8

"""
    API Pension - Open Finance Brasil

    API de Previdência do Open Finance Brasil – Fase 4. API que retorna informações de Previdência.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SurvivalPensionCosts(object):
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
        'loading_antecipated': 'SurvivalPensionLoadingAntecipated',
        'loading_late': 'SurvivalPensionLoadingLate'
    }

    attribute_map = {
        'loading_antecipated': 'loadingAntecipated',
        'loading_late': 'loadingLate'
    }

    def __init__(self, loading_antecipated=None, loading_late=None):  # noqa: E501
        """SurvivalPensionCosts - a model defined in Swagger"""  # noqa: E501
        self._loading_antecipated = None
        self._loading_late = None
        self.discriminator = None
        self.loading_antecipated = loading_antecipated
        self.loading_late = loading_late

    @property
    def loading_antecipated(self):
        """Gets the loading_antecipated of this SurvivalPensionCosts.  # noqa: E501


        :return: The loading_antecipated of this SurvivalPensionCosts.  # noqa: E501
        :rtype: SurvivalPensionLoadingAntecipated
        """
        return self._loading_antecipated

    @loading_antecipated.setter
    def loading_antecipated(self, loading_antecipated):
        """Sets the loading_antecipated of this SurvivalPensionCosts.


        :param loading_antecipated: The loading_antecipated of this SurvivalPensionCosts.  # noqa: E501
        :type: SurvivalPensionLoadingAntecipated
        """
        if loading_antecipated is None:
            raise ValueError("Invalid value for `loading_antecipated`, must not be `None`")  # noqa: E501

        self._loading_antecipated = loading_antecipated

    @property
    def loading_late(self):
        """Gets the loading_late of this SurvivalPensionCosts.  # noqa: E501


        :return: The loading_late of this SurvivalPensionCosts.  # noqa: E501
        :rtype: SurvivalPensionLoadingLate
        """
        return self._loading_late

    @loading_late.setter
    def loading_late(self, loading_late):
        """Sets the loading_late of this SurvivalPensionCosts.


        :param loading_late: The loading_late of this SurvivalPensionCosts.  # noqa: E501
        :type: SurvivalPensionLoadingLate
        """
        if loading_late is None:
            raise ValueError("Invalid value for `loading_late`, must not be `None`")  # noqa: E501

        self._loading_late = loading_late

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
        if issubclass(SurvivalPensionCosts, dict):
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
        if not isinstance(other, SurvivalPensionCosts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
