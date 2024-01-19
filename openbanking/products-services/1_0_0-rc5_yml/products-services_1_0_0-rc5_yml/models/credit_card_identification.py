# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardIdentification(object):
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
        'product': 'CreditCardIdentificationProduct',
        'credit_card': 'CreditCardIdentificationCreditCard'
    }

    attribute_map = {
        'product': 'product',
        'credit_card': 'creditCard'
    }

    def __init__(self, product=None, credit_card=None):  # noqa: E501
        """CreditCardIdentification - a model defined in Swagger"""  # noqa: E501
        self._product = None
        self._credit_card = None
        self.discriminator = None
        self.product = product
        self.credit_card = credit_card

    @property
    def product(self):
        """Gets the product of this CreditCardIdentification.  # noqa: E501


        :return: The product of this CreditCardIdentification.  # noqa: E501
        :rtype: CreditCardIdentificationProduct
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this CreditCardIdentification.


        :param product: The product of this CreditCardIdentification.  # noqa: E501
        :type: CreditCardIdentificationProduct
        """
        if product is None:
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def credit_card(self):
        """Gets the credit_card of this CreditCardIdentification.  # noqa: E501


        :return: The credit_card of this CreditCardIdentification.  # noqa: E501
        :rtype: CreditCardIdentificationCreditCard
        """
        return self._credit_card

    @credit_card.setter
    def credit_card(self, credit_card):
        """Sets the credit_card of this CreditCardIdentification.


        :param credit_card: The credit_card of this CreditCardIdentification.  # noqa: E501
        :type: CreditCardIdentificationCreditCard
        """
        if credit_card is None:
            raise ValueError("Invalid value for `credit_card`, must not be `None`")  # noqa: E501

        self._credit_card = credit_card

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
        if issubclass(CreditCardIdentification, dict):
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
        if not isinstance(other, CreditCardIdentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
