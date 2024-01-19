# coding: utf-8

"""
    API OpenData Channels do Open Finance Brasil

    A API descrita neste documento é referente as API Channels da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 2.0.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BranchAvailability(object):
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
        'standards': 'list[BranchAvailabilityStandards]',
        'exception': 'str',
        'is_public_access_allowed': 'bool'
    }

    attribute_map = {
        'standards': 'standards',
        'exception': 'exception',
        'is_public_access_allowed': 'isPublicAccessAllowed'
    }

    def __init__(self, standards=None, exception=None, is_public_access_allowed=None):  # noqa: E501
        """BranchAvailability - a model defined in Swagger"""  # noqa: E501
        self._standards = None
        self._exception = None
        self._is_public_access_allowed = None
        self.discriminator = None
        self.standards = standards
        if exception is not None:
            self.exception = exception
        if is_public_access_allowed is not None:
            self.is_public_access_allowed = is_public_access_allowed

    @property
    def standards(self):
        """Gets the standards of this BranchAvailability.  # noqa: E501

        Lista disponibilidade padrão da depêndencia por dias da semana  # noqa: E501

        :return: The standards of this BranchAvailability.  # noqa: E501
        :rtype: list[BranchAvailabilityStandards]
        """
        return self._standards

    @standards.setter
    def standards(self, standards):
        """Sets the standards of this BranchAvailability.

        Lista disponibilidade padrão da depêndencia por dias da semana  # noqa: E501

        :param standards: The standards of this BranchAvailability.  # noqa: E501
        :type: list[BranchAvailabilityStandards]
        """
        if standards is None:
            raise ValueError("Invalid value for `standards`, must not be `None`")  # noqa: E501

        self._standards = standards

    @property
    def exception(self):
        """Gets the exception of this BranchAvailability.  # noqa: E501

        Em campo texto devem ser registradas todas as Exceções para o não atendimento  # noqa: E501

        :return: The exception of this BranchAvailability.  # noqa: E501
        :rtype: str
        """
        return self._exception

    @exception.setter
    def exception(self, exception):
        """Sets the exception of this BranchAvailability.

        Em campo texto devem ser registradas todas as Exceções para o não atendimento  # noqa: E501

        :param exception: The exception of this BranchAvailability.  # noqa: E501
        :type: str
        """

        self._exception = exception

    @property
    def is_public_access_allowed(self):
        """Gets the is_public_access_allowed of this BranchAvailability.  # noqa: E501

        Indica se a instalação da Dependência tem acesso restrito a clientes  # noqa: E501

        :return: The is_public_access_allowed of this BranchAvailability.  # noqa: E501
        :rtype: bool
        """
        return self._is_public_access_allowed

    @is_public_access_allowed.setter
    def is_public_access_allowed(self, is_public_access_allowed):
        """Sets the is_public_access_allowed of this BranchAvailability.

        Indica se a instalação da Dependência tem acesso restrito a clientes  # noqa: E501

        :param is_public_access_allowed: The is_public_access_allowed of this BranchAvailability.  # noqa: E501
        :type: bool
        """

        self._is_public_access_allowed = is_public_access_allowed

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
        if issubclass(BranchAvailability, dict):
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
        if not isinstance(other, BranchAvailability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
