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

class PersonalCreditCard(object):
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
        'name': 'str',
        'identification': 'CreditCardIdentification',
        'rewards_program': 'CreditCardRewardsProgram',
        'fees': 'PersonalCreditCardFees',
        'interest': 'CreditCardInterest',
        'terms_conditions': 'CreditCardTermsConditions'
    }

    attribute_map = {
        'name': 'name',
        'identification': 'identification',
        'rewards_program': 'rewardsProgram',
        'fees': 'fees',
        'interest': 'interest',
        'terms_conditions': 'termsConditions'
    }

    def __init__(self, name=None, identification=None, rewards_program=None, fees=None, interest=None, terms_conditions=None):  # noqa: E501
        """PersonalCreditCard - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._identification = None
        self._rewards_program = None
        self._fees = None
        self._interest = None
        self._terms_conditions = None
        self.discriminator = None
        self.name = name
        self.identification = identification
        self.rewards_program = rewards_program
        self.fees = fees
        self.interest = interest
        self.terms_conditions = terms_conditions

    @property
    def name(self):
        """Gets the name of this PersonalCreditCard.  # noqa: E501

        Denominação/Identificação do nome da conta (cartão de crédito)  # noqa: E501

        :return: The name of this PersonalCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PersonalCreditCard.

        Denominação/Identificação do nome da conta (cartão de crédito)  # noqa: E501

        :param name: The name of this PersonalCreditCard.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def identification(self):
        """Gets the identification of this PersonalCreditCard.  # noqa: E501


        :return: The identification of this PersonalCreditCard.  # noqa: E501
        :rtype: CreditCardIdentification
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this PersonalCreditCard.


        :param identification: The identification of this PersonalCreditCard.  # noqa: E501
        :type: CreditCardIdentification
        """
        if identification is None:
            raise ValueError("Invalid value for `identification`, must not be `None`")  # noqa: E501

        self._identification = identification

    @property
    def rewards_program(self):
        """Gets the rewards_program of this PersonalCreditCard.  # noqa: E501


        :return: The rewards_program of this PersonalCreditCard.  # noqa: E501
        :rtype: CreditCardRewardsProgram
        """
        return self._rewards_program

    @rewards_program.setter
    def rewards_program(self, rewards_program):
        """Sets the rewards_program of this PersonalCreditCard.


        :param rewards_program: The rewards_program of this PersonalCreditCard.  # noqa: E501
        :type: CreditCardRewardsProgram
        """
        if rewards_program is None:
            raise ValueError("Invalid value for `rewards_program`, must not be `None`")  # noqa: E501

        self._rewards_program = rewards_program

    @property
    def fees(self):
        """Gets the fees of this PersonalCreditCard.  # noqa: E501


        :return: The fees of this PersonalCreditCard.  # noqa: E501
        :rtype: PersonalCreditCardFees
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this PersonalCreditCard.


        :param fees: The fees of this PersonalCreditCard.  # noqa: E501
        :type: PersonalCreditCardFees
        """
        if fees is None:
            raise ValueError("Invalid value for `fees`, must not be `None`")  # noqa: E501

        self._fees = fees

    @property
    def interest(self):
        """Gets the interest of this PersonalCreditCard.  # noqa: E501


        :return: The interest of this PersonalCreditCard.  # noqa: E501
        :rtype: CreditCardInterest
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this PersonalCreditCard.


        :param interest: The interest of this PersonalCreditCard.  # noqa: E501
        :type: CreditCardInterest
        """
        if interest is None:
            raise ValueError("Invalid value for `interest`, must not be `None`")  # noqa: E501

        self._interest = interest

    @property
    def terms_conditions(self):
        """Gets the terms_conditions of this PersonalCreditCard.  # noqa: E501


        :return: The terms_conditions of this PersonalCreditCard.  # noqa: E501
        :rtype: CreditCardTermsConditions
        """
        return self._terms_conditions

    @terms_conditions.setter
    def terms_conditions(self, terms_conditions):
        """Sets the terms_conditions of this PersonalCreditCard.


        :param terms_conditions: The terms_conditions of this PersonalCreditCard.  # noqa: E501
        :type: CreditCardTermsConditions
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
        if issubclass(PersonalCreditCard, dict):
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
        if not isinstance(other, PersonalCreditCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
