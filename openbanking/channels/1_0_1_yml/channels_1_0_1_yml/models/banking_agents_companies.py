# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from channels_1_0_1_yml.models.cnpj import CNPJ  # noqa: F401,E501

class BankingAgentsCompanies(CNPJ):
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
        'contractors': 'list[BankingAgentsContractor]'
    }
    if hasattr(CNPJ, "swagger_types"):
        swagger_types.update(CNPJ.swagger_types)

    attribute_map = {
        'name': 'name',
        'contractors': 'contractors'
    }
    if hasattr(CNPJ, "attribute_map"):
        attribute_map.update(CNPJ.attribute_map)

    def __init__(self, name=None, contractors=None, *args, **kwargs):  # noqa: E501
        """BankingAgentsCompanies - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._contractors = None
        self.discriminator = None
        self.name = name
        self.contractors = contractors
        CNPJ.__init__(self, *args, **kwargs)

    @property
    def name(self):
        """Gets the name of this BankingAgentsCompanies.  # noqa: E501

        Nome da Instituição, pertencente à marca, responsável pelo Correspondente Bancário no país.  # noqa: E501

        :return: The name of this BankingAgentsCompanies.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BankingAgentsCompanies.

        Nome da Instituição, pertencente à marca, responsável pelo Correspondente Bancário no país.  # noqa: E501

        :param name: The name of this BankingAgentsCompanies.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def contractors(self):
        """Gets the contractors of this BankingAgentsCompanies.  # noqa: E501

        Relação de informações de um contratante do serviço de correspondente.  # noqa: E501

        :return: The contractors of this BankingAgentsCompanies.  # noqa: E501
        :rtype: list[BankingAgentsContractor]
        """
        return self._contractors

    @contractors.setter
    def contractors(self, contractors):
        """Sets the contractors of this BankingAgentsCompanies.

        Relação de informações de um contratante do serviço de correspondente.  # noqa: E501

        :param contractors: The contractors of this BankingAgentsCompanies.  # noqa: E501
        :type: list[BankingAgentsContractor]
        """
        if contractors is None:
            raise ValueError("Invalid value for `contractors`, must not be `None`")  # noqa: E501

        self._contractors = contractors

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
        if issubclass(BankingAgentsCompanies, dict):
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
        if not isinstance(other, BankingAgentsCompanies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
