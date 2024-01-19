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

class ApiDiscoveryEndpoint(object):
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
        'api_discovery_id': 'str',
        'api_endpoint': 'str'
    }

    attribute_map = {
        'api_discovery_id': 'ApiDiscoveryId',
        'api_endpoint': 'ApiEndpoint'
    }

    def __init__(self, api_discovery_id=None, api_endpoint=None):  # noqa: E501
        """ApiDiscoveryEndpoint - a model defined in Swagger"""  # noqa: E501
        self._api_discovery_id = None
        self._api_endpoint = None
        self.discriminator = None
        if api_discovery_id is not None:
            self.api_discovery_id = api_discovery_id
        if api_endpoint is not None:
            self.api_endpoint = api_endpoint

    @property
    def api_discovery_id(self):
        """Gets the api_discovery_id of this ApiDiscoveryEndpoint.  # noqa: E501

        Unique Id of this discovery endpoint record  # noqa: E501

        :return: The api_discovery_id of this ApiDiscoveryEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._api_discovery_id

    @api_discovery_id.setter
    def api_discovery_id(self, api_discovery_id):
        """Sets the api_discovery_id of this ApiDiscoveryEndpoint.

        Unique Id of this discovery endpoint record  # noqa: E501

        :param api_discovery_id: The api_discovery_id of this ApiDiscoveryEndpoint.  # noqa: E501
        :type: str
        """

        self._api_discovery_id = api_discovery_id

    @property
    def api_endpoint(self):
        """Gets the api_endpoint of this ApiDiscoveryEndpoint.  # noqa: E501

        A compliant URI  # noqa: E501

        :return: The api_endpoint of this ApiDiscoveryEndpoint.  # noqa: E501
        :rtype: str
        """
        return self._api_endpoint

    @api_endpoint.setter
    def api_endpoint(self, api_endpoint):
        """Sets the api_endpoint of this ApiDiscoveryEndpoint.

        A compliant URI  # noqa: E501

        :param api_endpoint: The api_endpoint of this ApiDiscoveryEndpoint.  # noqa: E501
        :type: str
        """

        self._api_endpoint = api_endpoint

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
        if issubclass(ApiDiscoveryEndpoint, dict):
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
        if not isinstance(other, ApiDiscoveryEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
