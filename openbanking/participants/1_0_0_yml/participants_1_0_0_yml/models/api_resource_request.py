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

class ApiResourceRequest(object):
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
        'api_family_type': 'ApiFamilyType',
        'api_version': 'float'
    }

    attribute_map = {
        'api_family_type': 'ApiFamilyType',
        'api_version': 'ApiVersion'
    }

    def __init__(self, api_family_type=None, api_version=None):  # noqa: E501
        """ApiResourceRequest - a model defined in Swagger"""  # noqa: E501
        self._api_family_type = None
        self._api_version = None
        self.discriminator = None
        if api_family_type is not None:
            self.api_family_type = api_family_type
        if api_version is not None:
            self.api_version = api_version

    @property
    def api_family_type(self):
        """Gets the api_family_type of this ApiResourceRequest.  # noqa: E501


        :return: The api_family_type of this ApiResourceRequest.  # noqa: E501
        :rtype: ApiFamilyType
        """
        return self._api_family_type

    @api_family_type.setter
    def api_family_type(self, api_family_type):
        """Sets the api_family_type of this ApiResourceRequest.


        :param api_family_type: The api_family_type of this ApiResourceRequest.  # noqa: E501
        :type: ApiFamilyType
        """

        self._api_family_type = api_family_type

    @property
    def api_version(self):
        """Gets the api_version of this ApiResourceRequest.  # noqa: E501

        The version number of the API  # noqa: E501

        :return: The api_version of this ApiResourceRequest.  # noqa: E501
        :rtype: float
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ApiResourceRequest.

        The version number of the API  # noqa: E501

        :param api_version: The api_version of this ApiResourceRequest.  # noqa: E501
        :type: float
        """

        self._api_version = api_version

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
        if issubclass(ApiResourceRequest, dict):
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
        if not isinstance(other, ApiResourceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
