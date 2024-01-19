# coding: utf-8

"""
    APIs Admin do Open Banking Brasil

    As API's administrativas são recursos que podem ser consumidos apenas pelo diretório para avaliação e controle da qualidade dos serviços fornecidos pelas instituições financeiras  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EndpointDowntime(object):
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
        'url': 'str',
        'partial_downtime': 'int'
    }

    attribute_map = {
        'url': 'url',
        'partial_downtime': 'partialDowntime'
    }

    def __init__(self, url=None, partial_downtime=None):  # noqa: E501
        """EndpointDowntime - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._partial_downtime = None
        self.discriminator = None
        self.url = url
        self.partial_downtime = partial_downtime

    @property
    def url(self):
        """Gets the url of this EndpointDowntime.  # noqa: E501


        :return: The url of this EndpointDowntime.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this EndpointDowntime.


        :param url: The url of this EndpointDowntime.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def partial_downtime(self):
        """Gets the partial_downtime of this EndpointDowntime.  # noqa: E501


        :return: The partial_downtime of this EndpointDowntime.  # noqa: E501
        :rtype: int
        """
        return self._partial_downtime

    @partial_downtime.setter
    def partial_downtime(self, partial_downtime):
        """Sets the partial_downtime of this EndpointDowntime.


        :param partial_downtime: The partial_downtime of this EndpointDowntime.  # noqa: E501
        :type: int
        """
        if partial_downtime is None:
            raise ValueError("Invalid value for `partial_downtime`, must not be `None`")  # noqa: E501

        self._partial_downtime = partial_downtime

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
        if issubclass(EndpointDowntime, dict):
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
        if not isinstance(other, EndpointDowntime):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
