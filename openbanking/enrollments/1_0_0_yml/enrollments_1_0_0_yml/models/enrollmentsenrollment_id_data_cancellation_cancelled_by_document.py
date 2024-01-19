# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    Família de API para permitir o pagamento sem redirecionamento via Open Finance Brasil.   Permite tanto o gerenciamento dos dispositivos vinculados as contas quanto a autorização de consentimentos criados via fluxo sem redirecionamento.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EnrollmentsenrollmentIdDataCancellationCancelledByDocument(object):
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
        'identification': 'str',
        'rel': 'str'
    }

    attribute_map = {
        'identification': 'identification',
        'rel': 'rel'
    }

    def __init__(self, identification=None, rel=None):  # noqa: E501
        """EnrollmentsenrollmentIdDataCancellationCancelledByDocument - a model defined in Swagger"""  # noqa: E501
        self._identification = None
        self._rel = None
        self.discriminator = None
        self.identification = identification
        self.rel = rel

    @property
    def identification(self):
        """Gets the identification of this EnrollmentsenrollmentIdDataCancellationCancelledByDocument.  # noqa: E501

        Número do documento do usuário responsável pelo cancelamento do vínculo de conta.  # noqa: E501

        :return: The identification of this EnrollmentsenrollmentIdDataCancellationCancelledByDocument.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this EnrollmentsenrollmentIdDataCancellationCancelledByDocument.

        Número do documento do usuário responsável pelo cancelamento do vínculo de conta.  # noqa: E501

        :param identification: The identification of this EnrollmentsenrollmentIdDataCancellationCancelledByDocument.  # noqa: E501
        :type: str
        """
        if identification is None:
            raise ValueError("Invalid value for `identification`, must not be `None`")  # noqa: E501

        self._identification = identification

    @property
    def rel(self):
        """Gets the rel of this EnrollmentsenrollmentIdDataCancellationCancelledByDocument.  # noqa: E501

        Tipo do documento do usuário responsável pelo cancelamento do vínculo de conta.  # noqa: E501

        :return: The rel of this EnrollmentsenrollmentIdDataCancellationCancelledByDocument.  # noqa: E501
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this EnrollmentsenrollmentIdDataCancellationCancelledByDocument.

        Tipo do documento do usuário responsável pelo cancelamento do vínculo de conta.  # noqa: E501

        :param rel: The rel of this EnrollmentsenrollmentIdDataCancellationCancelledByDocument.  # noqa: E501
        :type: str
        """
        if rel is None:
            raise ValueError("Invalid value for `rel`, must not be `None`")  # noqa: E501

        self._rel = rel

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
        if issubclass(EnrollmentsenrollmentIdDataCancellationCancelledByDocument, dict):
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
        if not isinstance(other, EnrollmentsenrollmentIdDataCancellationCancelledByDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other