# coding: utf-8

"""
    APIs OpenData do Open Finance Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 2.0.0-beta.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseErrorMetaSingleMeta(object):
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
        'request_date_time': 'datetime'
    }

    attribute_map = {
        'request_date_time': 'requestDateTime'
    }

    def __init__(self, request_date_time=None):  # noqa: E501
        """ResponseErrorMetaSingleMeta - a model defined in Swagger"""  # noqa: E501
        self._request_date_time = None
        self.discriminator = None
        self.request_date_time = request_date_time

    @property
    def request_date_time(self):
        """Gets the request_date_time of this ResponseErrorMetaSingleMeta.  # noqa: E501

        Data e hora da consulta, conforme especificação RFC-3339, formato UTC.  # noqa: E501

        :return: The request_date_time of this ResponseErrorMetaSingleMeta.  # noqa: E501
        :rtype: datetime
        """
        return self._request_date_time

    @request_date_time.setter
    def request_date_time(self, request_date_time):
        """Sets the request_date_time of this ResponseErrorMetaSingleMeta.

        Data e hora da consulta, conforme especificação RFC-3339, formato UTC.  # noqa: E501

        :param request_date_time: The request_date_time of this ResponseErrorMetaSingleMeta.  # noqa: E501
        :type: datetime
        """
        if request_date_time is None:
            raise ValueError("Invalid value for `request_date_time`, must not be `None`")  # noqa: E501

        self._request_date_time = request_date_time

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
        if issubclass(ResponseErrorMetaSingleMeta, dict):
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
        if not isinstance(other, ResponseErrorMetaSingleMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
