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
from channels_3_0_0_yml.models.cnpj import CNPJ  # noqa: F401,E501

class BankingAgentsContractor(CNPJ):
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
        'banking_agents': 'list[BankingAgent]'
    }
    if hasattr(CNPJ, "swagger_types"):
        swagger_types.update(CNPJ.swagger_types)

    attribute_map = {
        'name': 'name',
        'banking_agents': 'bankingAgents'
    }
    if hasattr(CNPJ, "attribute_map"):
        attribute_map.update(CNPJ.attribute_map)

    def __init__(self, name=None, banking_agents=None, *args, **kwargs):  # noqa: E501
        """BankingAgentsContractor - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._banking_agents = None
        self.discriminator = None
        self.name = name
        if banking_agents is not None:
            self.banking_agents = banking_agents
        CNPJ.__init__(self, *args, **kwargs)

    @property
    def name(self):
        """Gets the name of this BankingAgentsContractor.  # noqa: E501


        :return: The name of this BankingAgentsContractor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BankingAgentsContractor.


        :param name: The name of this BankingAgentsContractor.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def banking_agents(self):
        """Gets the banking_agents of this BankingAgentsContractor.  # noqa: E501


        :return: The banking_agents of this BankingAgentsContractor.  # noqa: E501
        :rtype: list[BankingAgent]
        """
        return self._banking_agents

    @banking_agents.setter
    def banking_agents(self, banking_agents):
        """Sets the banking_agents of this BankingAgentsContractor.


        :param banking_agents: The banking_agents of this BankingAgentsContractor.  # noqa: E501
        :type: list[BankingAgent]
        """

        self._banking_agents = banking_agents

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
        if issubclass(BankingAgentsContractor, dict):
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
        if not isinstance(other, BankingAgentsContractor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
