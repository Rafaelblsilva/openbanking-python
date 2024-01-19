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

class ResponseMetricsListData(object):
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
        'request_time': 'datetime',
        'availability': 'AvailabilityMetrics',
        'invocations': 'InvocationMetrics',
        'average_response': 'AverageMetrics',
        'average_tps': 'AverageTPSMetrics',
        'peak_tps': 'PeakTPSMetrics',
        'errors': 'ErrorMetrics',
        'rejections': 'RejectionMetrics'
    }

    attribute_map = {
        'request_time': 'requestTime',
        'availability': 'availability',
        'invocations': 'invocations',
        'average_response': 'averageResponse',
        'average_tps': 'averageTps',
        'peak_tps': 'peakTps',
        'errors': 'errors',
        'rejections': 'rejections'
    }

    def __init__(self, request_time=None, availability=None, invocations=None, average_response=None, average_tps=None, peak_tps=None, errors=None, rejections=None):  # noqa: E501
        """ResponseMetricsListData - a model defined in Swagger"""  # noqa: E501
        self._request_time = None
        self._availability = None
        self._invocations = None
        self._average_response = None
        self._average_tps = None
        self._peak_tps = None
        self._errors = None
        self._rejections = None
        self.discriminator = None
        self.request_time = request_time
        self.availability = availability
        self.invocations = invocations
        self.average_response = average_response
        self.average_tps = average_tps
        self.peak_tps = peak_tps
        self.errors = errors
        self.rejections = rejections

    @property
    def request_time(self):
        """Gets the request_time of this ResponseMetricsListData.  # noqa: E501

        Data e hora que as métricas foram requisitadas.  # noqa: E501

        :return: The request_time of this ResponseMetricsListData.  # noqa: E501
        :rtype: datetime
        """
        return self._request_time

    @request_time.setter
    def request_time(self, request_time):
        """Sets the request_time of this ResponseMetricsListData.

        Data e hora que as métricas foram requisitadas.  # noqa: E501

        :param request_time: The request_time of this ResponseMetricsListData.  # noqa: E501
        :type: datetime
        """
        if request_time is None:
            raise ValueError("Invalid value for `request_time`, must not be `None`")  # noqa: E501

        self._request_time = request_time

    @property
    def availability(self):
        """Gets the availability of this ResponseMetricsListData.  # noqa: E501


        :return: The availability of this ResponseMetricsListData.  # noqa: E501
        :rtype: AvailabilityMetrics
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this ResponseMetricsListData.


        :param availability: The availability of this ResponseMetricsListData.  # noqa: E501
        :type: AvailabilityMetrics
        """
        if availability is None:
            raise ValueError("Invalid value for `availability`, must not be `None`")  # noqa: E501

        self._availability = availability

    @property
    def invocations(self):
        """Gets the invocations of this ResponseMetricsListData.  # noqa: E501


        :return: The invocations of this ResponseMetricsListData.  # noqa: E501
        :rtype: InvocationMetrics
        """
        return self._invocations

    @invocations.setter
    def invocations(self, invocations):
        """Sets the invocations of this ResponseMetricsListData.


        :param invocations: The invocations of this ResponseMetricsListData.  # noqa: E501
        :type: InvocationMetrics
        """
        if invocations is None:
            raise ValueError("Invalid value for `invocations`, must not be `None`")  # noqa: E501

        self._invocations = invocations

    @property
    def average_response(self):
        """Gets the average_response of this ResponseMetricsListData.  # noqa: E501


        :return: The average_response of this ResponseMetricsListData.  # noqa: E501
        :rtype: AverageMetrics
        """
        return self._average_response

    @average_response.setter
    def average_response(self, average_response):
        """Sets the average_response of this ResponseMetricsListData.


        :param average_response: The average_response of this ResponseMetricsListData.  # noqa: E501
        :type: AverageMetrics
        """
        if average_response is None:
            raise ValueError("Invalid value for `average_response`, must not be `None`")  # noqa: E501

        self._average_response = average_response

    @property
    def average_tps(self):
        """Gets the average_tps of this ResponseMetricsListData.  # noqa: E501


        :return: The average_tps of this ResponseMetricsListData.  # noqa: E501
        :rtype: AverageTPSMetrics
        """
        return self._average_tps

    @average_tps.setter
    def average_tps(self, average_tps):
        """Sets the average_tps of this ResponseMetricsListData.


        :param average_tps: The average_tps of this ResponseMetricsListData.  # noqa: E501
        :type: AverageTPSMetrics
        """
        if average_tps is None:
            raise ValueError("Invalid value for `average_tps`, must not be `None`")  # noqa: E501

        self._average_tps = average_tps

    @property
    def peak_tps(self):
        """Gets the peak_tps of this ResponseMetricsListData.  # noqa: E501


        :return: The peak_tps of this ResponseMetricsListData.  # noqa: E501
        :rtype: PeakTPSMetrics
        """
        return self._peak_tps

    @peak_tps.setter
    def peak_tps(self, peak_tps):
        """Sets the peak_tps of this ResponseMetricsListData.


        :param peak_tps: The peak_tps of this ResponseMetricsListData.  # noqa: E501
        :type: PeakTPSMetrics
        """
        if peak_tps is None:
            raise ValueError("Invalid value for `peak_tps`, must not be `None`")  # noqa: E501

        self._peak_tps = peak_tps

    @property
    def errors(self):
        """Gets the errors of this ResponseMetricsListData.  # noqa: E501


        :return: The errors of this ResponseMetricsListData.  # noqa: E501
        :rtype: ErrorMetrics
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ResponseMetricsListData.


        :param errors: The errors of this ResponseMetricsListData.  # noqa: E501
        :type: ErrorMetrics
        """
        if errors is None:
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def rejections(self):
        """Gets the rejections of this ResponseMetricsListData.  # noqa: E501


        :return: The rejections of this ResponseMetricsListData.  # noqa: E501
        :rtype: RejectionMetrics
        """
        return self._rejections

    @rejections.setter
    def rejections(self, rejections):
        """Sets the rejections of this ResponseMetricsListData.


        :param rejections: The rejections of this ResponseMetricsListData.  # noqa: E501
        :type: RejectionMetrics
        """
        if rejections is None:
            raise ValueError("Invalid value for `rejections`, must not be `None`")  # noqa: E501

        self._rejections = rejections

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
        if issubclass(ResponseMetricsListData, dict):
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
        if not isinstance(other, ResponseMetricsListData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
