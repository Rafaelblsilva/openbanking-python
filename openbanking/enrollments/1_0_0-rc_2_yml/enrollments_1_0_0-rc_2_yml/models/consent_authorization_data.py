# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    API de Dispositivo Vínculado para suportar Iniciação de Pagamentos na Jornada Sem Redirecionamento do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc.2
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ConsentAuthorizationData(object):
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
        'enrollment_id': 'EnrollmentId',
        'risk_signals': 'ConsentAuthorizationDataRiskSignals',
        'fido_assertion': 'ConsentAuthorizationDataFidoAssertion'
    }

    attribute_map = {
        'enrollment_id': 'enrollmentId',
        'risk_signals': 'riskSignals',
        'fido_assertion': 'fidoAssertion'
    }

    def __init__(self, enrollment_id=None, risk_signals=None, fido_assertion=None):  # noqa: E501
        """ConsentAuthorizationData - a model defined in Swagger"""  # noqa: E501
        self._enrollment_id = None
        self._risk_signals = None
        self._fido_assertion = None
        self.discriminator = None
        self.enrollment_id = enrollment_id
        self.risk_signals = risk_signals
        self.fido_assertion = fido_assertion

    @property
    def enrollment_id(self):
        """Gets the enrollment_id of this ConsentAuthorizationData.  # noqa: E501


        :return: The enrollment_id of this ConsentAuthorizationData.  # noqa: E501
        :rtype: EnrollmentId
        """
        return self._enrollment_id

    @enrollment_id.setter
    def enrollment_id(self, enrollment_id):
        """Sets the enrollment_id of this ConsentAuthorizationData.


        :param enrollment_id: The enrollment_id of this ConsentAuthorizationData.  # noqa: E501
        :type: EnrollmentId
        """
        if enrollment_id is None:
            raise ValueError("Invalid value for `enrollment_id`, must not be `None`")  # noqa: E501

        self._enrollment_id = enrollment_id

    @property
    def risk_signals(self):
        """Gets the risk_signals of this ConsentAuthorizationData.  # noqa: E501


        :return: The risk_signals of this ConsentAuthorizationData.  # noqa: E501
        :rtype: ConsentAuthorizationDataRiskSignals
        """
        return self._risk_signals

    @risk_signals.setter
    def risk_signals(self, risk_signals):
        """Sets the risk_signals of this ConsentAuthorizationData.


        :param risk_signals: The risk_signals of this ConsentAuthorizationData.  # noqa: E501
        :type: ConsentAuthorizationDataRiskSignals
        """
        if risk_signals is None:
            raise ValueError("Invalid value for `risk_signals`, must not be `None`")  # noqa: E501

        self._risk_signals = risk_signals

    @property
    def fido_assertion(self):
        """Gets the fido_assertion of this ConsentAuthorizationData.  # noqa: E501


        :return: The fido_assertion of this ConsentAuthorizationData.  # noqa: E501
        :rtype: ConsentAuthorizationDataFidoAssertion
        """
        return self._fido_assertion

    @fido_assertion.setter
    def fido_assertion(self, fido_assertion):
        """Sets the fido_assertion of this ConsentAuthorizationData.


        :param fido_assertion: The fido_assertion of this ConsentAuthorizationData.  # noqa: E501
        :type: ConsentAuthorizationDataFidoAssertion
        """
        if fido_assertion is None:
            raise ValueError("Invalid value for `fido_assertion`, must not be `None`")  # noqa: E501

        self._fido_assertion = fido_assertion

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
        if issubclass(ConsentAuthorizationData, dict):
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
        if not isinstance(other, ConsentAuthorizationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
