# coding: utf-8

"""
    API Credit Fixed Incomes - Open Finance Brasil

    API de informações de operações de Renda Fixa Crédito do Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Renda Fixa Crédito (Debêntures, CRI/CRA) mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação do produto, rentabilidade, quantidade, prazos, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. A exposição se dará por cada operação de renda fixa contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseError(object):
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
        'errors': 'list[ResponseErrorMetaSingleErrors]',
        'meta': 'ResponseErrorMeta'
    }

    attribute_map = {
        'errors': 'errors',
        'meta': 'meta'
    }

    def __init__(self, errors=None, meta=None):  # noqa: E501
        """ResponseError - a model defined in Swagger"""  # noqa: E501
        self._errors = None
        self._meta = None
        self.discriminator = None
        self.errors = errors
        if meta is not None:
            self.meta = meta

    @property
    def errors(self):
        """Gets the errors of this ResponseError.  # noqa: E501


        :return: The errors of this ResponseError.  # noqa: E501
        :rtype: list[ResponseErrorMetaSingleErrors]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ResponseError.


        :param errors: The errors of this ResponseError.  # noqa: E501
        :type: list[ResponseErrorMetaSingleErrors]
        """
        if errors is None:
            raise ValueError("Invalid value for `errors`, must not be `None`")  # noqa: E501

        self._errors = errors

    @property
    def meta(self):
        """Gets the meta of this ResponseError.  # noqa: E501


        :return: The meta of this ResponseError.  # noqa: E501
        :rtype: ResponseErrorMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ResponseError.


        :param meta: The meta of this ResponseError.  # noqa: E501
        :type: ResponseErrorMeta
        """

        self._meta = meta

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
        if issubclass(ResponseError, dict):
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
        if not isinstance(other, ResponseError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
