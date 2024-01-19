# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    API de Dispositivo Vínculado para suportar Iniciação de Pagamentos na Jornada Sem Redirecionamento do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-beta.1
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EnrollmentFidoOptionsInputData(object):
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
        'rp': 'str',
        'platform': 'str'
    }

    attribute_map = {
        'rp': 'rp',
        'platform': 'platform'
    }

    def __init__(self, rp=None, platform=None):  # noqa: E501
        """EnrollmentFidoOptionsInputData - a model defined in Swagger"""  # noqa: E501
        self._rp = None
        self._platform = None
        self.discriminator = None
        self.rp = rp
        self.platform = platform

    @property
    def rp(self):
        """Gets the rp of this EnrollmentFidoOptionsInputData.  # noqa: E501

        Identificador único da Relying Party.  # noqa: E501

        :return: The rp of this EnrollmentFidoOptionsInputData.  # noqa: E501
        :rtype: str
        """
        return self._rp

    @rp.setter
    def rp(self, rp):
        """Sets the rp of this EnrollmentFidoOptionsInputData.

        Identificador único da Relying Party.  # noqa: E501

        :param rp: The rp of this EnrollmentFidoOptionsInputData.  # noqa: E501
        :type: str
        """
        if rp is None:
            raise ValueError("Invalid value for `rp`, must not be `None`")  # noqa: E501

        self._rp = rp

    @property
    def platform(self):
        """Gets the platform of this EnrollmentFidoOptionsInputData.  # noqa: E501

        Indica a plataforma em que o usuário criará a nova credencial FIDO2.  Este campo permite que o servidor FIDO inclua extensões de acordo com a plataforma utilizada.   # noqa: E501

        :return: The platform of this EnrollmentFidoOptionsInputData.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this EnrollmentFidoOptionsInputData.

        Indica a plataforma em que o usuário criará a nova credencial FIDO2.  Este campo permite que o servidor FIDO inclua extensões de acordo com a plataforma utilizada.   # noqa: E501

        :param platform: The platform of this EnrollmentFidoOptionsInputData.  # noqa: E501
        :type: str
        """
        if platform is None:
            raise ValueError("Invalid value for `platform`, must not be `None`")  # noqa: E501
        allowed_values = ["ANDROID", "BROWSER", "CROSS_PLATFORM", "IOS"]  # noqa: E501
        if platform not in allowed_values:
            raise ValueError(
                "Invalid value for `platform` ({0}), must be one of {1}"  # noqa: E501
                .format(platform, allowed_values)
            )

        self._platform = platform

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
        if issubclass(EnrollmentFidoOptionsInputData, dict):
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
        if not isinstance(other, EnrollmentFidoOptionsInputData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
