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
from products-services_1_0_0-rc5_yml.models.company import Company  # noqa: F401,E501

class PersonalCreditCardCompany(Company):
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
        'personal_credit_cards': 'list[PersonalCreditCard]'
    }
    if hasattr(Company, "swagger_types"):
        swagger_types.update(Company.swagger_types)

    attribute_map = {
        'personal_credit_cards': 'personalCreditCards'
    }
    if hasattr(Company, "attribute_map"):
        attribute_map.update(Company.attribute_map)

    def __init__(self, personal_credit_cards=None, *args, **kwargs):  # noqa: E501
        """PersonalCreditCardCompany - a model defined in Swagger"""  # noqa: E501
        self._personal_credit_cards = None
        self.discriminator = None
        self.personal_credit_cards = personal_credit_cards
        Company.__init__(self, *args, **kwargs)

    @property
    def personal_credit_cards(self):
        """Gets the personal_credit_cards of this PersonalCreditCardCompany.  # noqa: E501

        Lista das contas de pagamento pós-paga  # noqa: E501

        :return: The personal_credit_cards of this PersonalCreditCardCompany.  # noqa: E501
        :rtype: list[PersonalCreditCard]
        """
        return self._personal_credit_cards

    @personal_credit_cards.setter
    def personal_credit_cards(self, personal_credit_cards):
        """Sets the personal_credit_cards of this PersonalCreditCardCompany.

        Lista das contas de pagamento pós-paga  # noqa: E501

        :param personal_credit_cards: The personal_credit_cards of this PersonalCreditCardCompany.  # noqa: E501
        :type: list[PersonalCreditCard]
        """
        if personal_credit_cards is None:
            raise ValueError("Invalid value for `personal_credit_cards`, must not be `None`")  # noqa: E501

        self._personal_credit_cards = personal_credit_cards

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
        if issubclass(PersonalCreditCardCompany, dict):
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
        if not isinstance(other, PersonalCreditCardCompany):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
