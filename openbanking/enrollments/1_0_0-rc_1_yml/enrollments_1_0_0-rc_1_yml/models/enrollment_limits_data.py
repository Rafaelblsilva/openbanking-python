# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    API de Dispositivo Vínculado para suportar Iniciação de Pagamentos na Jornada Sem Redirecionamento do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc.1
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EnrollmentLimitsData(object):
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
        'transaction_limit': 'str',
        'daily_limit': 'str'
    }

    attribute_map = {
        'transaction_limit': 'transactionLimit',
        'daily_limit': 'dailyLimit'
    }

    def __init__(self, transaction_limit=None, daily_limit=None):  # noqa: E501
        """EnrollmentLimitsData - a model defined in Swagger"""  # noqa: E501
        self._transaction_limit = None
        self._daily_limit = None
        self.discriminator = None
        self.transaction_limit = transaction_limit
        self.daily_limit = daily_limit

    @property
    def transaction_limit(self):
        """Gets the transaction_limit of this EnrollmentLimitsData.  # noqa: E501

        Valor máximo, por transação, admitido para este vínculo de conta. Este limite não garante a autorização de iniciações de pagamento; servindo como referência para a iniciadora evitar a criação de consentimentos de valores tais que, garantidamente, não serão autorizados.   # noqa: E501

        :return: The transaction_limit of this EnrollmentLimitsData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_limit

    @transaction_limit.setter
    def transaction_limit(self, transaction_limit):
        """Sets the transaction_limit of this EnrollmentLimitsData.

        Valor máximo, por transação, admitido para este vínculo de conta. Este limite não garante a autorização de iniciações de pagamento; servindo como referência para a iniciadora evitar a criação de consentimentos de valores tais que, garantidamente, não serão autorizados.   # noqa: E501

        :param transaction_limit: The transaction_limit of this EnrollmentLimitsData.  # noqa: E501
        :type: str
        """
        if transaction_limit is None:
            raise ValueError("Invalid value for `transaction_limit`, must not be `None`")  # noqa: E501

        self._transaction_limit = transaction_limit

    @property
    def daily_limit(self):
        """Gets the daily_limit of this EnrollmentLimitsData.  # noqa: E501

        Limite diário cumulativo para este vínculo de conta. Este limite não garante a autorização de iniciações de pagamento; servindo como referência para a iniciadora evitar a criação de consentimentos para valores tais que, garantidamente, não serão autorizados.   # noqa: E501

        :return: The daily_limit of this EnrollmentLimitsData.  # noqa: E501
        :rtype: str
        """
        return self._daily_limit

    @daily_limit.setter
    def daily_limit(self, daily_limit):
        """Sets the daily_limit of this EnrollmentLimitsData.

        Limite diário cumulativo para este vínculo de conta. Este limite não garante a autorização de iniciações de pagamento; servindo como referência para a iniciadora evitar a criação de consentimentos para valores tais que, garantidamente, não serão autorizados.   # noqa: E501

        :param daily_limit: The daily_limit of this EnrollmentLimitsData.  # noqa: E501
        :type: str
        """
        if daily_limit is None:
            raise ValueError("Invalid value for `daily_limit`, must not be `None`")  # noqa: E501

        self._daily_limit = daily_limit

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
        if issubclass(EnrollmentLimitsData, dict):
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
        if not isinstance(other, EnrollmentLimitsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
