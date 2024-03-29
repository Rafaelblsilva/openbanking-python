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

class AuthorisationDomainUserCreateRequest(object):
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
        'email': 'str',
        'authorisation_domain_role': 'str',
        'contact_role': 'ContactRoleEnum'
    }

    attribute_map = {
        'email': 'Email',
        'authorisation_domain_role': 'AuthorisationDomainRole',
        'contact_role': 'ContactRole'
    }

    def __init__(self, email=None, authorisation_domain_role=None, contact_role=None):  # noqa: E501
        """AuthorisationDomainUserCreateRequest - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._authorisation_domain_role = None
        self._contact_role = None
        self.discriminator = None
        self.email = email
        self.authorisation_domain_role = authorisation_domain_role
        self.contact_role = contact_role

    @property
    def email(self):
        """Gets the email of this AuthorisationDomainUserCreateRequest.  # noqa: E501

        The user email address  # noqa: E501

        :return: The email of this AuthorisationDomainUserCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this AuthorisationDomainUserCreateRequest.

        The user email address  # noqa: E501

        :param email: The email of this AuthorisationDomainUserCreateRequest.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def authorisation_domain_role(self):
        """Gets the authorisation_domain_role of this AuthorisationDomainUserCreateRequest.  # noqa: E501

        The authorisation domain role for this user  # noqa: E501

        :return: The authorisation_domain_role of this AuthorisationDomainUserCreateRequest.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_domain_role

    @authorisation_domain_role.setter
    def authorisation_domain_role(self, authorisation_domain_role):
        """Sets the authorisation_domain_role of this AuthorisationDomainUserCreateRequest.

        The authorisation domain role for this user  # noqa: E501

        :param authorisation_domain_role: The authorisation_domain_role of this AuthorisationDomainUserCreateRequest.  # noqa: E501
        :type: str
        """
        if authorisation_domain_role is None:
            raise ValueError("Invalid value for `authorisation_domain_role`, must not be `None`")  # noqa: E501

        self._authorisation_domain_role = authorisation_domain_role

    @property
    def contact_role(self):
        """Gets the contact_role of this AuthorisationDomainUserCreateRequest.  # noqa: E501


        :return: The contact_role of this AuthorisationDomainUserCreateRequest.  # noqa: E501
        :rtype: ContactRoleEnum
        """
        return self._contact_role

    @contact_role.setter
    def contact_role(self, contact_role):
        """Sets the contact_role of this AuthorisationDomainUserCreateRequest.


        :param contact_role: The contact_role of this AuthorisationDomainUserCreateRequest.  # noqa: E501
        :type: ContactRoleEnum
        """
        if contact_role is None:
            raise ValueError("Invalid value for `contact_role`, must not be `None`")  # noqa: E501

        self._contact_role = contact_role

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
        if issubclass(AuthorisationDomainUserCreateRequest, dict):
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
        if not isinstance(other, AuthorisationDomainUserCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
