# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.1-rc1.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseDiscoveryOutageListData(object):
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
        'outage_time': 'str',
        'duration': 'str',
        'is_partial': 'bool',
        'explanation': 'str'
    }

    attribute_map = {
        'outage_time': 'outageTime',
        'duration': 'duration',
        'is_partial': 'isPartial',
        'explanation': 'explanation'
    }

    def __init__(self, outage_time=None, duration=None, is_partial=None, explanation=None):  # noqa: E501
        """ResponseDiscoveryOutageListData - a model defined in Swagger"""  # noqa: E501
        self._outage_time = None
        self._duration = None
        self._is_partial = None
        self._explanation = None
        self.discriminator = None
        self.outage_time = outage_time
        self.duration = duration
        self.is_partial = is_partial
        self.explanation = explanation

    @property
    def outage_time(self):
        """Gets the outage_time of this ResponseDiscoveryOutageListData.  # noqa: E501

        Data e hora planejada do início da indisponibilidade  # noqa: E501

        :return: The outage_time of this ResponseDiscoveryOutageListData.  # noqa: E501
        :rtype: str
        """
        return self._outage_time

    @outage_time.setter
    def outage_time(self, outage_time):
        """Sets the outage_time of this ResponseDiscoveryOutageListData.

        Data e hora planejada do início da indisponibilidade  # noqa: E501

        :param outage_time: The outage_time of this ResponseDiscoveryOutageListData.  # noqa: E501
        :type: str
        """
        if outage_time is None:
            raise ValueError("Invalid value for `outage_time`, must not be `None`")  # noqa: E501

        self._outage_time = outage_time

    @property
    def duration(self):
        """Gets the duration of this ResponseDiscoveryOutageListData.  # noqa: E501

        Duração prevista da indisponibilidade  # noqa: E501

        :return: The duration of this ResponseDiscoveryOutageListData.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ResponseDiscoveryOutageListData.

        Duração prevista da indisponibilidade  # noqa: E501

        :param duration: The duration of this ResponseDiscoveryOutageListData.  # noqa: E501
        :type: str
        """
        if duration is None:
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def is_partial(self):
        """Gets the is_partial of this ResponseDiscoveryOutageListData.  # noqa: E501

        Flag que indica se a indisponibilidade é parcial (atingindo apenas alguns end points) ou total (atingindo todos os end points)  # noqa: E501

        :return: The is_partial of this ResponseDiscoveryOutageListData.  # noqa: E501
        :rtype: bool
        """
        return self._is_partial

    @is_partial.setter
    def is_partial(self, is_partial):
        """Sets the is_partial of this ResponseDiscoveryOutageListData.

        Flag que indica se a indisponibilidade é parcial (atingindo apenas alguns end points) ou total (atingindo todos os end points)  # noqa: E501

        :param is_partial: The is_partial of this ResponseDiscoveryOutageListData.  # noqa: E501
        :type: bool
        """
        if is_partial is None:
            raise ValueError("Invalid value for `is_partial`, must not be `None`")  # noqa: E501

        self._is_partial = is_partial

    @property
    def explanation(self):
        """Gets the explanation of this ResponseDiscoveryOutageListData.  # noqa: E501

        Explicação sobre os motivos da indisponibilidade.  # noqa: E501

        :return: The explanation of this ResponseDiscoveryOutageListData.  # noqa: E501
        :rtype: str
        """
        return self._explanation

    @explanation.setter
    def explanation(self, explanation):
        """Sets the explanation of this ResponseDiscoveryOutageListData.

        Explicação sobre os motivos da indisponibilidade.  # noqa: E501

        :param explanation: The explanation of this ResponseDiscoveryOutageListData.  # noqa: E501
        :type: str
        """
        if explanation is None:
            raise ValueError("Invalid value for `explanation`, must not be `None`")  # noqa: E501

        self._explanation = explanation

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
        if issubclass(ResponseDiscoveryOutageListData, dict):
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
        if not isinstance(other, ResponseDiscoveryOutageListData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
