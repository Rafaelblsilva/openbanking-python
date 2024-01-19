# coding: utf-8

"""
    API's OpenData do Open Finance Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalUnarrangedAccountOverdraft(object):
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
        'fees': 'PersonalUnarrangedAccountOverdraftFee',
        'interest_rates': 'list[UnarrangedAccountOverdraftRate]',
        'terms_conditions': 'str'
    }

    attribute_map = {
        'fees': 'fees',
        'interest_rates': 'interestRates',
        'terms_conditions': 'termsConditions'
    }

    def __init__(self, fees=None, interest_rates=None, terms_conditions=None):  # noqa: E501
        """PersonalUnarrangedAccountOverdraft - a model defined in Swagger"""  # noqa: E501
        self._fees = None
        self._interest_rates = None
        self._terms_conditions = None
        self.discriminator = None
        self.fees = fees
        if interest_rates is not None:
            self.interest_rates = interest_rates
        self.terms_conditions = terms_conditions

    @property
    def fees(self):
        """Gets the fees of this PersonalUnarrangedAccountOverdraft.  # noqa: E501


        :return: The fees of this PersonalUnarrangedAccountOverdraft.  # noqa: E501
        :rtype: PersonalUnarrangedAccountOverdraftFee
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this PersonalUnarrangedAccountOverdraft.


        :param fees: The fees of this PersonalUnarrangedAccountOverdraft.  # noqa: E501
        :type: PersonalUnarrangedAccountOverdraftFee
        """
        if fees is None:
            raise ValueError("Invalid value for `fees`, must not be `None`")  # noqa: E501

        self._fees = fees

    @property
    def interest_rates(self):
        """Gets the interest_rates of this PersonalUnarrangedAccountOverdraft.  # noqa: E501

        Lista que traz o conjunto de informações necessárias para demonstrar a distribuição de frequências das taxas de juros remuneratórios da Modalidade de crédito  # noqa: E501

        :return: The interest_rates of this PersonalUnarrangedAccountOverdraft.  # noqa: E501
        :rtype: list[UnarrangedAccountOverdraftRate]
        """
        return self._interest_rates

    @interest_rates.setter
    def interest_rates(self, interest_rates):
        """Sets the interest_rates of this PersonalUnarrangedAccountOverdraft.

        Lista que traz o conjunto de informações necessárias para demonstrar a distribuição de frequências das taxas de juros remuneratórios da Modalidade de crédito  # noqa: E501

        :param interest_rates: The interest_rates of this PersonalUnarrangedAccountOverdraft.  # noqa: E501
        :type: list[UnarrangedAccountOverdraftRate]
        """

        self._interest_rates = interest_rates

    @property
    def terms_conditions(self):
        """Gets the terms_conditions of this PersonalUnarrangedAccountOverdraft.  # noqa: E501

        Campo aberto para informar as condições contratuais relativas à Modalidade de Adiantamento a depositante para pessoa natural. Pode ser informada a URL referente ao endereço onde constam as condições informadas. Endereço eletrônico de acesso ao canal.  # noqa: E501

        :return: The terms_conditions of this PersonalUnarrangedAccountOverdraft.  # noqa: E501
        :rtype: str
        """
        return self._terms_conditions

    @terms_conditions.setter
    def terms_conditions(self, terms_conditions):
        """Sets the terms_conditions of this PersonalUnarrangedAccountOverdraft.

        Campo aberto para informar as condições contratuais relativas à Modalidade de Adiantamento a depositante para pessoa natural. Pode ser informada a URL referente ao endereço onde constam as condições informadas. Endereço eletrônico de acesso ao canal.  # noqa: E501

        :param terms_conditions: The terms_conditions of this PersonalUnarrangedAccountOverdraft.  # noqa: E501
        :type: str
        """
        if terms_conditions is None:
            raise ValueError("Invalid value for `terms_conditions`, must not be `None`")  # noqa: E501

        self._terms_conditions = terms_conditions

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
        if issubclass(PersonalUnarrangedAccountOverdraft, dict):
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
        if not isinstance(other, PersonalUnarrangedAccountOverdraft):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
