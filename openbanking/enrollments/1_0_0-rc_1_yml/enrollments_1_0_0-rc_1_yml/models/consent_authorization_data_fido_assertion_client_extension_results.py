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

class ConsentAuthorizationDataFidoAssertionClientExtensionResults(object):
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
        'additional_prop1': 'str',
        'additional_prop2': 'str'
    }

    attribute_map = {
        'additional_prop1': 'additionalProp1',
        'additional_prop2': 'additionalProp2'
    }

    def __init__(self, additional_prop1=None, additional_prop2=None):  # noqa: E501
        """ConsentAuthorizationDataFidoAssertionClientExtensionResults - a model defined in Swagger"""  # noqa: E501
        self._additional_prop1 = None
        self._additional_prop2 = None
        self.discriminator = None
        if additional_prop1 is not None:
            self.additional_prop1 = additional_prop1
        if additional_prop2 is not None:
            self.additional_prop2 = additional_prop2

    @property
    def additional_prop1(self):
        """Gets the additional_prop1 of this ConsentAuthorizationDataFidoAssertionClientExtensionResults.  # noqa: E501

        Propriedade adicional.  # noqa: E501

        :return: The additional_prop1 of this ConsentAuthorizationDataFidoAssertionClientExtensionResults.  # noqa: E501
        :rtype: str
        """
        return self._additional_prop1

    @additional_prop1.setter
    def additional_prop1(self, additional_prop1):
        """Sets the additional_prop1 of this ConsentAuthorizationDataFidoAssertionClientExtensionResults.

        Propriedade adicional.  # noqa: E501

        :param additional_prop1: The additional_prop1 of this ConsentAuthorizationDataFidoAssertionClientExtensionResults.  # noqa: E501
        :type: str
        """

        self._additional_prop1 = additional_prop1

    @property
    def additional_prop2(self):
        """Gets the additional_prop2 of this ConsentAuthorizationDataFidoAssertionClientExtensionResults.  # noqa: E501

        Propriedade adicional.  # noqa: E501

        :return: The additional_prop2 of this ConsentAuthorizationDataFidoAssertionClientExtensionResults.  # noqa: E501
        :rtype: str
        """
        return self._additional_prop2

    @additional_prop2.setter
    def additional_prop2(self, additional_prop2):
        """Sets the additional_prop2 of this ConsentAuthorizationDataFidoAssertionClientExtensionResults.

        Propriedade adicional.  # noqa: E501

        :param additional_prop2: The additional_prop2 of this ConsentAuthorizationDataFidoAssertionClientExtensionResults.  # noqa: E501
        :type: str
        """

        self._additional_prop2 = additional_prop2

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
        if issubclass(ConsentAuthorizationDataFidoAssertionClientExtensionResults, dict):
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
        if not isinstance(other, ConsentAuthorizationDataFidoAssertionClientExtensionResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
