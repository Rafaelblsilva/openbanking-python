# coding: utf-8

"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalInsurancePremiumPayment(object):
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
        'payment_methods': 'list[EnumPremiumPaymentMethodTypePersonal]',
        'frequencies': 'list[EnumPersonalInsurancePremiumPaymentFrequency]',
        'contribution_tax': 'str'
    }

    attribute_map = {
        'payment_methods': 'paymentMethods',
        'frequencies': 'frequencies',
        'contribution_tax': 'contributionTax'
    }

    def __init__(self, payment_methods=None, frequencies=None, contribution_tax=None):  # noqa: E501
        """PersonalInsurancePremiumPayment - a model defined in Swagger"""  # noqa: E501
        self._payment_methods = None
        self._frequencies = None
        self._contribution_tax = None
        self.discriminator = None
        self.payment_methods = payment_methods
        self.frequencies = frequencies
        if contribution_tax is not None:
            self.contribution_tax = contribution_tax

    @property
    def payment_methods(self):
        """Gets the payment_methods of this PersonalInsurancePremiumPayment.  # noqa: E501


        :return: The payment_methods of this PersonalInsurancePremiumPayment.  # noqa: E501
        :rtype: list[EnumPremiumPaymentMethodTypePersonal]
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """Sets the payment_methods of this PersonalInsurancePremiumPayment.


        :param payment_methods: The payment_methods of this PersonalInsurancePremiumPayment.  # noqa: E501
        :type: list[EnumPremiumPaymentMethodTypePersonal]
        """
        if payment_methods is None:
            raise ValueError("Invalid value for `payment_methods`, must not be `None`")  # noqa: E501

        self._payment_methods = payment_methods

    @property
    def frequencies(self):
        """Gets the frequencies of this PersonalInsurancePremiumPayment.  # noqa: E501


        :return: The frequencies of this PersonalInsurancePremiumPayment.  # noqa: E501
        :rtype: list[EnumPersonalInsurancePremiumPaymentFrequency]
        """
        return self._frequencies

    @frequencies.setter
    def frequencies(self, frequencies):
        """Sets the frequencies of this PersonalInsurancePremiumPayment.


        :param frequencies: The frequencies of this PersonalInsurancePremiumPayment.  # noqa: E501
        :type: list[EnumPersonalInsurancePremiumPaymentFrequency]
        """
        if frequencies is None:
            raise ValueError("Invalid value for `frequencies`, must not be `None`")  # noqa: E501

        self._frequencies = frequencies

    @property
    def contribution_tax(self):
        """Gets the contribution_tax of this PersonalInsurancePremiumPayment.  # noqa: E501

        Distribuição de frequência relativa aos valores referentes às taxas cobradas, nos termos do Anexo III.  # noqa: E501

        :return: The contribution_tax of this PersonalInsurancePremiumPayment.  # noqa: E501
        :rtype: str
        """
        return self._contribution_tax

    @contribution_tax.setter
    def contribution_tax(self, contribution_tax):
        """Sets the contribution_tax of this PersonalInsurancePremiumPayment.

        Distribuição de frequência relativa aos valores referentes às taxas cobradas, nos termos do Anexo III.  # noqa: E501

        :param contribution_tax: The contribution_tax of this PersonalInsurancePremiumPayment.  # noqa: E501
        :type: str
        """

        self._contribution_tax = contribution_tax

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
        if issubclass(PersonalInsurancePremiumPayment, dict):
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
        if not isinstance(other, PersonalInsurancePremiumPayment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
