# coding: utf-8

"""
    API Capitalization-bonds - Open Finance Brasil

    As APIs descritas neste documento é referente a API de Capitalização da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc3.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LatePayment(object):
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
        'suspension_months': 'float',
        'period_extension_option': 'bool'
    }

    attribute_map = {
        'suspension_months': 'suspensionMonths',
        'period_extension_option': 'periodExtensionOption'
    }

    def __init__(self, suspension_months=None, period_extension_option=None):  # noqa: E501
        """LatePayment - a model defined in Swagger"""  # noqa: E501
        self._suspension_months = None
        self._period_extension_option = None
        self.discriminator = None
        self.suspension_months = suspension_months
        if period_extension_option is not None:
            self.period_extension_option = period_extension_option

    @property
    def suspension_months(self):
        """Gets the suspension_months of this LatePayment.  # noqa: E501

        Conforme manual SUSEP: Prazo máximo (contínuo ou intermitente) em meses que o título fica suspenso por atraso de pagamento, antes de ser cancelado (não aplicável a pagamento único).  # noqa: E501

        :return: The suspension_months of this LatePayment.  # noqa: E501
        :rtype: float
        """
        return self._suspension_months

    @suspension_months.setter
    def suspension_months(self, suspension_months):
        """Sets the suspension_months of this LatePayment.

        Conforme manual SUSEP: Prazo máximo (contínuo ou intermitente) em meses que o título fica suspenso por atraso de pagamento, antes de ser cancelado (não aplicável a pagamento único).  # noqa: E501

        :param suspension_months: The suspension_months of this LatePayment.  # noqa: E501
        :type: float
        """
        if suspension_months is None:
            raise ValueError("Invalid value for `suspension_months`, must not be `None`")  # noqa: E501

        self._suspension_months = suspension_months

    @property
    def period_extension_option(self):
        """Gets the period_extension_option of this LatePayment.  # noqa: E501

        Alteração do prazo de vigência original, pela suspensão (não aplicável a pagamento único). A considerar os seguintes domínios: 1. true 2. false   # noqa: E501

        :return: The period_extension_option of this LatePayment.  # noqa: E501
        :rtype: bool
        """
        return self._period_extension_option

    @period_extension_option.setter
    def period_extension_option(self, period_extension_option):
        """Sets the period_extension_option of this LatePayment.

        Alteração do prazo de vigência original, pela suspensão (não aplicável a pagamento único). A considerar os seguintes domínios: 1. true 2. false   # noqa: E501

        :param period_extension_option: The period_extension_option of this LatePayment.  # noqa: E501
        :type: bool
        """

        self._period_extension_option = period_extension_option

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
        if issubclass(LatePayment, dict):
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
        if not isinstance(other, LatePayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
