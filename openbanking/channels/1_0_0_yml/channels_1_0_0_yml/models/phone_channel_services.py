# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PhoneChannelServices(object):
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
        'codes': 'list[str]',
        'additional_info': 'str'
    }

    attribute_map = {
        'codes': 'codes',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, codes=None, additional_info=None):  # noqa: E501
        """PhoneChannelServices - a model defined in Swagger"""  # noqa: E501
        self._codes = None
        self._additional_info = None
        self.discriminator = None
        self.codes = codes
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def codes(self):
        """Gets the codes of this PhoneChannelServices.  # noqa: E501


        :return: The codes of this PhoneChannelServices.  # noqa: E501
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """Sets the codes of this PhoneChannelServices.


        :param codes: The codes of this PhoneChannelServices.  # noqa: E501
        :type: list[str]
        """
        if codes is None:
            raise ValueError("Invalid value for `codes`, must not be `None`")  # noqa: E501
        allowed_values = ["ABERTURA_CONTAS", "RECEBIMENTOS_PAGAMENTOS_TRANSFERENCIAS_ELETRONICAS", "RECEBIMENTOS_PAGAMENTOS_QUALQUER_NATUREZA", "OPERACOES_CREDITO", "CARTAO_CREDITO", "OPERACOES_CAMBIO", "INVESTIMENTOS", "SEGUROS", "RECLAMACAO", "CANCELAMENTO", "INFORMACOES", "FALAR_ATENDENTE", "OUTROS"]  # noqa: E501
        if not set(codes).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `codes` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(codes) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._codes = codes

    @property
    def additional_info(self):
        """Gets the additional_info of this PhoneChannelServices.  # noqa: E501

        Campo de texto livre para descrever mais sobre os serviços  # noqa: E501

        :return: The additional_info of this PhoneChannelServices.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this PhoneChannelServices.

        Campo de texto livre para descrever mais sobre os serviços  # noqa: E501

        :param additional_info: The additional_info of this PhoneChannelServices.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

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
        if issubclass(PhoneChannelServices, dict):
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
        if not isinstance(other, PhoneChannelServices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
