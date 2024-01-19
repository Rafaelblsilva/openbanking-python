# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CNPJ(object):
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
        'cnpj_number': 'str'
    }

    attribute_map = {
        'cnpj_number': 'cnpjNumber'
    }

    def __init__(self, cnpj_number=None):  # noqa: E501
        """CNPJ - a model defined in Swagger"""  # noqa: E501
        self._cnpj_number = None
        self.discriminator = None
        if cnpj_number is not None:
            self.cnpj_number = cnpj_number

    @property
    def cnpj_number(self):
        """Gets the cnpj_number of this CNPJ.  # noqa: E501

        Número completo do CNPJ da instituição  # noqa: E501

        :return: The cnpj_number of this CNPJ.  # noqa: E501
        :rtype: str
        """
        return self._cnpj_number

    @cnpj_number.setter
    def cnpj_number(self, cnpj_number):
        """Sets the cnpj_number of this CNPJ.

        Número completo do CNPJ da instituição  # noqa: E501

        :param cnpj_number: The cnpj_number of this CNPJ.  # noqa: E501
        :type: str
        """

        self._cnpj_number = cnpj_number

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
        if issubclass(CNPJ, dict):
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
        if not isinstance(other, CNPJ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
