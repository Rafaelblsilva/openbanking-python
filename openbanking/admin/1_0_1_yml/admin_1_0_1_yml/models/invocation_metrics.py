# coding: utf-8

"""
    APIs Admin do Open Banking Brasil

    As API's administrativas são recursos que podem ser consumidos apenas pelo diretório para avaliação e controle da qualidade dos serviços fornecidos pelas instituições financeiras  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InvocationMetrics(object):
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
        'unauthenticated': 'InvocationMetricsUnauthenticated',
        'high_priority': 'InvocationMetricsHighPriority',
        'medium_priority': 'InvocationMetricsMediumPriority',
        'unattended': 'InvocationMetricsUnattended'
    }

    attribute_map = {
        'unauthenticated': 'unauthenticated',
        'high_priority': 'highPriority',
        'medium_priority': 'mediumPriority',
        'unattended': 'unattended'
    }

    def __init__(self, unauthenticated=None, high_priority=None, medium_priority=None, unattended=None):  # noqa: E501
        """InvocationMetrics - a model defined in Swagger"""  # noqa: E501
        self._unauthenticated = None
        self._high_priority = None
        self._medium_priority = None
        self._unattended = None
        self.discriminator = None
        self.unauthenticated = unauthenticated
        self.high_priority = high_priority
        self.medium_priority = medium_priority
        self.unattended = unattended

    @property
    def unauthenticated(self):
        """Gets the unauthenticated of this InvocationMetrics.  # noqa: E501


        :return: The unauthenticated of this InvocationMetrics.  # noqa: E501
        :rtype: InvocationMetricsUnauthenticated
        """
        return self._unauthenticated

    @unauthenticated.setter
    def unauthenticated(self, unauthenticated):
        """Sets the unauthenticated of this InvocationMetrics.


        :param unauthenticated: The unauthenticated of this InvocationMetrics.  # noqa: E501
        :type: InvocationMetricsUnauthenticated
        """
        if unauthenticated is None:
            raise ValueError("Invalid value for `unauthenticated`, must not be `None`")  # noqa: E501

        self._unauthenticated = unauthenticated

    @property
    def high_priority(self):
        """Gets the high_priority of this InvocationMetrics.  # noqa: E501


        :return: The high_priority of this InvocationMetrics.  # noqa: E501
        :rtype: InvocationMetricsHighPriority
        """
        return self._high_priority

    @high_priority.setter
    def high_priority(self, high_priority):
        """Sets the high_priority of this InvocationMetrics.


        :param high_priority: The high_priority of this InvocationMetrics.  # noqa: E501
        :type: InvocationMetricsHighPriority
        """
        if high_priority is None:
            raise ValueError("Invalid value for `high_priority`, must not be `None`")  # noqa: E501

        self._high_priority = high_priority

    @property
    def medium_priority(self):
        """Gets the medium_priority of this InvocationMetrics.  # noqa: E501


        :return: The medium_priority of this InvocationMetrics.  # noqa: E501
        :rtype: InvocationMetricsMediumPriority
        """
        return self._medium_priority

    @medium_priority.setter
    def medium_priority(self, medium_priority):
        """Sets the medium_priority of this InvocationMetrics.


        :param medium_priority: The medium_priority of this InvocationMetrics.  # noqa: E501
        :type: InvocationMetricsMediumPriority
        """
        if medium_priority is None:
            raise ValueError("Invalid value for `medium_priority`, must not be `None`")  # noqa: E501

        self._medium_priority = medium_priority

    @property
    def unattended(self):
        """Gets the unattended of this InvocationMetrics.  # noqa: E501


        :return: The unattended of this InvocationMetrics.  # noqa: E501
        :rtype: InvocationMetricsUnattended
        """
        return self._unattended

    @unattended.setter
    def unattended(self, unattended):
        """Sets the unattended of this InvocationMetrics.


        :param unattended: The unattended of this InvocationMetrics.  # noqa: E501
        :type: InvocationMetricsUnattended
        """
        if unattended is None:
            raise ValueError("Invalid value for `unattended`, must not be `None`")  # noqa: E501

        self._unattended = unattended

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
        if issubclass(InvocationMetrics, dict):
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
        if not isinstance(other, InvocationMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other