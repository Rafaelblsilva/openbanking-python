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

class SoftwareAuthorityClaimRequest(object):
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
        'status': 'str',
        'authorisation_domain': 'str',
        'role': 'str'
    }

    attribute_map = {
        'status': 'Status',
        'authorisation_domain': 'AuthorisationDomain',
        'role': 'Role'
    }

    def __init__(self, status='Active', authorisation_domain=None, role=None):  # noqa: E501
        """SoftwareAuthorityClaimRequest - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._authorisation_domain = None
        self._role = None
        self.discriminator = None
        self.status = status
        self.authorisation_domain = authorisation_domain
        self.role = role

    @property
    def status(self):
        """Gets the status of this SoftwareAuthorityClaimRequest.  # noqa: E501

        Is this authority claim Active/Inactive, default is active  # noqa: E501

        :return: The status of this SoftwareAuthorityClaimRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SoftwareAuthorityClaimRequest.

        Is this authority claim Active/Inactive, default is active  # noqa: E501

        :param status: The status of this SoftwareAuthorityClaimRequest.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Active", "Inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def authorisation_domain(self):
        """Gets the authorisation_domain of this SoftwareAuthorityClaimRequest.  # noqa: E501

        Authorisation domain for the authority  # noqa: E501

        :return: The authorisation_domain of this SoftwareAuthorityClaimRequest.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_domain

    @authorisation_domain.setter
    def authorisation_domain(self, authorisation_domain):
        """Sets the authorisation_domain of this SoftwareAuthorityClaimRequest.

        Authorisation domain for the authority  # noqa: E501

        :param authorisation_domain: The authorisation_domain of this SoftwareAuthorityClaimRequest.  # noqa: E501
        :type: str
        """
        if authorisation_domain is None:
            raise ValueError("Invalid value for `authorisation_domain`, must not be `None`")  # noqa: E501

        self._authorisation_domain = authorisation_domain

    @property
    def role(self):
        """Gets the role of this SoftwareAuthorityClaimRequest.  # noqa: E501

        Roles for the Authority i.e. ASPSP, AISP, PISP, CBPII  # noqa: E501

        :return: The role of this SoftwareAuthorityClaimRequest.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this SoftwareAuthorityClaimRequest.

        Roles for the Authority i.e. ASPSP, AISP, PISP, CBPII  # noqa: E501

        :param role: The role of this SoftwareAuthorityClaimRequest.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

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
        if issubclass(SoftwareAuthorityClaimRequest, dict):
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
        if not isinstance(other, SoftwareAuthorityClaimRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
