# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    Família de API para permitir o pagamento sem redirecionamento via Open Finance Brasil.   Permite tanto o gerenciamento dos dispositivos vinculados as contas quanto a autorização de consentimentos criados via fluxo sem redirecionamento.   # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RiskSignalsDataIntegrity(object):
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
        'app_recognition_verdict': 'str',
        'device_recognition_verdict': 'str'
    }

    attribute_map = {
        'app_recognition_verdict': 'appRecognitionVerdict',
        'device_recognition_verdict': 'deviceRecognitionVerdict'
    }

    def __init__(self, app_recognition_verdict=None, device_recognition_verdict=None):  # noqa: E501
        """RiskSignalsDataIntegrity - a model defined in Swagger"""  # noqa: E501
        self._app_recognition_verdict = None
        self._device_recognition_verdict = None
        self.discriminator = None
        if app_recognition_verdict is not None:
            self.app_recognition_verdict = app_recognition_verdict
        if device_recognition_verdict is not None:
            self.device_recognition_verdict = device_recognition_verdict

    @property
    def app_recognition_verdict(self):
        """Gets the app_recognition_verdict of this RiskSignalsDataIntegrity.  # noqa: E501

        Informa a integridade do app  # noqa: E501

        :return: The app_recognition_verdict of this RiskSignalsDataIntegrity.  # noqa: E501
        :rtype: str
        """
        return self._app_recognition_verdict

    @app_recognition_verdict.setter
    def app_recognition_verdict(self, app_recognition_verdict):
        """Sets the app_recognition_verdict of this RiskSignalsDataIntegrity.

        Informa a integridade do app  # noqa: E501

        :param app_recognition_verdict: The app_recognition_verdict of this RiskSignalsDataIntegrity.  # noqa: E501
        :type: str
        """

        self._app_recognition_verdict = app_recognition_verdict

    @property
    def device_recognition_verdict(self):
        """Gets the device_recognition_verdict of this RiskSignalsDataIntegrity.  # noqa: E501

        Informa a integridade do dispositivo  # noqa: E501

        :return: The device_recognition_verdict of this RiskSignalsDataIntegrity.  # noqa: E501
        :rtype: str
        """
        return self._device_recognition_verdict

    @device_recognition_verdict.setter
    def device_recognition_verdict(self, device_recognition_verdict):
        """Sets the device_recognition_verdict of this RiskSignalsDataIntegrity.

        Informa a integridade do dispositivo  # noqa: E501

        :param device_recognition_verdict: The device_recognition_verdict of this RiskSignalsDataIntegrity.  # noqa: E501
        :type: str
        """

        self._device_recognition_verdict = device_recognition_verdict

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
        if issubclass(RiskSignalsDataIntegrity, dict):
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
        if not isinstance(other, RiskSignalsDataIntegrity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
