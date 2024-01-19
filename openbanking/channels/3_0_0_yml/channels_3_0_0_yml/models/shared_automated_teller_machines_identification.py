# coding: utf-8

"""
    APIs OpenData do Open Finance Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SharedAutomatedTellerMachinesIdentification(object):
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
        'owner_name': 'str'
    }

    attribute_map = {
        'owner_name': 'ownerName'
    }

    def __init__(self, owner_name=None):  # noqa: E501
        """SharedAutomatedTellerMachinesIdentification - a model defined in Swagger"""  # noqa: E501
        self._owner_name = None
        self.discriminator = None
        if owner_name is not None:
            self.owner_name = owner_name

    @property
    def owner_name(self):
        """Gets the owner_name of this SharedAutomatedTellerMachinesIdentification.  # noqa: E501

        Nome do proprietário do terminal de Autoatendimento Compartilhado  # noqa: E501

        :return: The owner_name of this SharedAutomatedTellerMachinesIdentification.  # noqa: E501
        :rtype: str
        """
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        """Sets the owner_name of this SharedAutomatedTellerMachinesIdentification.

        Nome do proprietário do terminal de Autoatendimento Compartilhado  # noqa: E501

        :param owner_name: The owner_name of this SharedAutomatedTellerMachinesIdentification.  # noqa: E501
        :type: str
        """

        self._owner_name = owner_name

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
        if issubclass(SharedAutomatedTellerMachinesIdentification, dict):
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
        if not isinstance(other, SharedAutomatedTellerMachinesIdentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
