# coding: utf-8

"""
    Participantes Open Finance Brasil

    Informações sobre os participantes do Open Finance Brasil que estão registrados no Diretório.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UserCreateRequest(object):
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
        'user_email': 'str',
        'terms_and_conditions_id': 'int'
    }

    attribute_map = {
        'user_email': 'UserEmail',
        'terms_and_conditions_id': 'TermsAndConditionsId'
    }

    def __init__(self, user_email=None, terms_and_conditions_id=None):  # noqa: E501
        """UserCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._user_email = None
        self._terms_and_conditions_id = None
        self.discriminator = None
        self.user_email = user_email
        self.terms_and_conditions_id = terms_and_conditions_id

    @property
    def user_email(self):
        """Gets the user_email of this UserCreateRequest.  # noqa: E501

        User's email  # noqa: E501

        :return: The user_email of this UserCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this UserCreateRequest.

        User's email  # noqa: E501

        :param user_email: The user_email of this UserCreateRequest.  # noqa: E501
        :type: str
        """
        if user_email is None:
            raise ValueError("Invalid value for `user_email`, must not be `None`")  # noqa: E501

        self._user_email = user_email

    @property
    def terms_and_conditions_id(self):
        """Gets the terms_and_conditions_id of this UserCreateRequest.  # noqa: E501

        Id of the TnC(type = Directory), user has agreed to  # noqa: E501

        :return: The terms_and_conditions_id of this UserCreateRequest.  # noqa: E501
        :rtype: int
        """
        return self._terms_and_conditions_id

    @terms_and_conditions_id.setter
    def terms_and_conditions_id(self, terms_and_conditions_id):
        """Sets the terms_and_conditions_id of this UserCreateRequest.

        Id of the TnC(type = Directory), user has agreed to  # noqa: E501

        :param terms_and_conditions_id: The terms_and_conditions_id of this UserCreateRequest.  # noqa: E501
        :type: int
        """
        if terms_and_conditions_id is None:
            raise ValueError("Invalid value for `terms_and_conditions_id`, must not be `None`")  # noqa: E501

        self._terms_and_conditions_id = terms_and_conditions_id

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
        if issubclass(UserCreateRequest, dict):
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
        if not isinstance(other, UserCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
