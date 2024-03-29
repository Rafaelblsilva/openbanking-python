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

class DomainRoleDetail(object):
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
        'authorisation_domain_name': 'str',
        'authorisation_domain_role_name': 'str',
        'status': 'StatusEnum',
        'contact_role': 'ContactRoleEnum'
    }

    attribute_map = {
        'authorisation_domain_name': 'AuthorisationDomainName',
        'authorisation_domain_role_name': 'AuthorisationDomainRoleName',
        'status': 'Status',
        'contact_role': 'ContactRole'
    }

    def __init__(self, authorisation_domain_name=None, authorisation_domain_role_name=None, status=None, contact_role=None):  # noqa: E501
        """DomainRoleDetail - a model defined in Swagger"""  # noqa: E501
        self._authorisation_domain_name = None
        self._authorisation_domain_role_name = None
        self._status = None
        self._contact_role = None
        self.discriminator = None
        if authorisation_domain_name is not None:
            self.authorisation_domain_name = authorisation_domain_name
        if authorisation_domain_role_name is not None:
            self.authorisation_domain_role_name = authorisation_domain_role_name
        if status is not None:
            self.status = status
        if contact_role is not None:
            self.contact_role = contact_role

    @property
    def authorisation_domain_name(self):
        """Gets the authorisation_domain_name of this DomainRoleDetail.  # noqa: E501


        :return: The authorisation_domain_name of this DomainRoleDetail.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_domain_name

    @authorisation_domain_name.setter
    def authorisation_domain_name(self, authorisation_domain_name):
        """Sets the authorisation_domain_name of this DomainRoleDetail.


        :param authorisation_domain_name: The authorisation_domain_name of this DomainRoleDetail.  # noqa: E501
        :type: str
        """

        self._authorisation_domain_name = authorisation_domain_name

    @property
    def authorisation_domain_role_name(self):
        """Gets the authorisation_domain_role_name of this DomainRoleDetail.  # noqa: E501


        :return: The authorisation_domain_role_name of this DomainRoleDetail.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_domain_role_name

    @authorisation_domain_role_name.setter
    def authorisation_domain_role_name(self, authorisation_domain_role_name):
        """Sets the authorisation_domain_role_name of this DomainRoleDetail.


        :param authorisation_domain_role_name: The authorisation_domain_role_name of this DomainRoleDetail.  # noqa: E501
        :type: str
        """

        self._authorisation_domain_role_name = authorisation_domain_role_name

    @property
    def status(self):
        """Gets the status of this DomainRoleDetail.  # noqa: E501


        :return: The status of this DomainRoleDetail.  # noqa: E501
        :rtype: StatusEnum
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DomainRoleDetail.


        :param status: The status of this DomainRoleDetail.  # noqa: E501
        :type: StatusEnum
        """

        self._status = status

    @property
    def contact_role(self):
        """Gets the contact_role of this DomainRoleDetail.  # noqa: E501


        :return: The contact_role of this DomainRoleDetail.  # noqa: E501
        :rtype: ContactRoleEnum
        """
        return self._contact_role

    @contact_role.setter
    def contact_role(self, contact_role):
        """Sets the contact_role of this DomainRoleDetail.


        :param contact_role: The contact_role of this DomainRoleDetail.  # noqa: E501
        :type: ContactRoleEnum
        """

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
        if issubclass(DomainRoleDetail, dict):
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
        if not isinstance(other, DomainRoleDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
