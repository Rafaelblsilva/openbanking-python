# coding: utf-8

"""
    API Webhook - Open Finance Brasil

    API de Webhook é responsável por notificar eventos definidos em cada uma das APIs que possuem a funcionalidade no Open Finance Brasil.    Informações sobre endpoints suportados e funcionamento podem ser encontrados na página <a href=\"https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/105021661/Conven+o+de+Webhook\">Convenção de Webhook</a>, disponível no portal do desenvolvedor do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-beta.3
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RequestBodyWebhookData(object):
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
        'timestamp': 'datetime'
    }

    attribute_map = {
        'timestamp': 'timestamp'
    }

    def __init__(self, timestamp=None):  # noqa: E501
        """RequestBodyWebhookData - a model defined in Swagger"""  # noqa: E501
        self._timestamp = None
        self.discriminator = None
        self.timestamp = timestamp

    @property
    def timestamp(self):
        """Gets the timestamp of this RequestBodyWebhookData.  # noqa: E501

        Data e hora em que ocorreu o evento responsável pelo disparo da notificação via webhook, conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :return: The timestamp of this RequestBodyWebhookData.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this RequestBodyWebhookData.

        Data e hora em que ocorreu o evento responsável pelo disparo da notificação via webhook, conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :param timestamp: The timestamp of this RequestBodyWebhookData.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

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
        if issubclass(RequestBodyWebhookData, dict):
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
        if not isinstance(other, RequestBodyWebhookData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
