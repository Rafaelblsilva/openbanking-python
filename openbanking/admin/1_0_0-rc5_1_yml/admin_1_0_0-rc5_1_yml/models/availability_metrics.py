# coding: utf-8

"""
    APIs Admin do Open Banking Brasil

    As API's administrativas são recursos que podem ser consumidos apenas pelo diretório para avaliação e controle da qualidade dos serviços fornecidos pelas instituições financeiras  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AvailabilityMetrics(object):
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
        'uptime': 'AvailabilityMetricsUptime',
        'downtime': 'AvailabilityMetricsDowntime'
    }

    attribute_map = {
        'uptime': 'uptime',
        'downtime': 'downtime'
    }

    def __init__(self, uptime=None, downtime=None):  # noqa: E501
        """AvailabilityMetrics - a model defined in Swagger"""  # noqa: E501
        self._uptime = None
        self._downtime = None
        self.discriminator = None
        self.uptime = uptime
        self.downtime = downtime

    @property
    def uptime(self):
        """Gets the uptime of this AvailabilityMetrics.  # noqa: E501


        :return: The uptime of this AvailabilityMetrics.  # noqa: E501
        :rtype: AvailabilityMetricsUptime
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """Sets the uptime of this AvailabilityMetrics.


        :param uptime: The uptime of this AvailabilityMetrics.  # noqa: E501
        :type: AvailabilityMetricsUptime
        """
        if uptime is None:
            raise ValueError("Invalid value for `uptime`, must not be `None`")  # noqa: E501

        self._uptime = uptime

    @property
    def downtime(self):
        """Gets the downtime of this AvailabilityMetrics.  # noqa: E501


        :return: The downtime of this AvailabilityMetrics.  # noqa: E501
        :rtype: AvailabilityMetricsDowntime
        """
        return self._downtime

    @downtime.setter
    def downtime(self, downtime):
        """Sets the downtime of this AvailabilityMetrics.


        :param downtime: The downtime of this AvailabilityMetrics.  # noqa: E501
        :type: AvailabilityMetricsDowntime
        """
        if downtime is None:
            raise ValueError("Invalid value for `downtime`, must not be `None`")  # noqa: E501

        self._downtime = downtime

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
        if issubclass(AvailabilityMetrics, dict):
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
        if not isinstance(other, AvailabilityMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
