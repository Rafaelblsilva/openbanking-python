# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PhoneChannel(object):
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
        'identification': 'PhoneChannelIdentification',
        'services': 'list[PhoneChannelService]'
    }

    attribute_map = {
        'identification': 'identification',
        'services': 'services'
    }

    def __init__(self, identification=None, services=None):  # noqa: E501
        """PhoneChannel - a model defined in Swagger"""  # noqa: E501
        self._identification = None
        self._services = None
        self.discriminator = None
        self.identification = identification
        self.services = services

    @property
    def identification(self):
        """Gets the identification of this PhoneChannel.  # noqa: E501


        :return: The identification of this PhoneChannel.  # noqa: E501
        :rtype: PhoneChannelIdentification
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this PhoneChannel.


        :param identification: The identification of this PhoneChannel.  # noqa: E501
        :type: PhoneChannelIdentification
        """
        if identification is None:
            raise ValueError("Invalid value for `identification`, must not be `None`")  # noqa: E501

        self._identification = identification

    @property
    def services(self):
        """Gets the services of this PhoneChannel.  # noqa: E501

        Traz a relação de serviços disponbilizados pelo Canal de Atendimento  # noqa: E501

        :return: The services of this PhoneChannel.  # noqa: E501
        :rtype: list[PhoneChannelService]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this PhoneChannel.

        Traz a relação de serviços disponbilizados pelo Canal de Atendimento  # noqa: E501

        :param services: The services of this PhoneChannel.  # noqa: E501
        :type: list[PhoneChannelService]
        """
        if services is None:
            raise ValueError("Invalid value for `services`, must not be `None`")  # noqa: E501

        self._services = services

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
        if issubclass(PhoneChannel, dict):
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
        if not isinstance(other, PhoneChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other