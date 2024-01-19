# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardIdentificationProduct(object):
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
        'type': 'str',
        'additional_info': 'str'
    }

    attribute_map = {
        'type': 'type',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, type=None, additional_info=None):  # noqa: E501
        """CreditCardIdentificationProduct - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._additional_info = None
        self.discriminator = None
        self.type = type
        self.additional_info = additional_info

    @property
    def type(self):
        """Gets the type of this CreditCardIdentificationProduct.  # noqa: E501

        Categoria atribuída a um cartão de pagamento, sob uma certa denominação, que lhe agrega um conjunto de vantagens, diferenciando-o de acordo com o perfil do portador. Essa categoria é definida pelo BACEN e está contida no documento de nome 'Elaboração e Remessa de Informações Relativas aos Cartões de Pagamento  Emissores'  # noqa: E501

        :return: The type of this CreditCardIdentificationProduct.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreditCardIdentificationProduct.

        Categoria atribuída a um cartão de pagamento, sob uma certa denominação, que lhe agrega um conjunto de vantagens, diferenciando-o de acordo com o perfil do portador. Essa categoria é definida pelo BACEN e está contida no documento de nome 'Elaboração e Remessa de Informações Relativas aos Cartões de Pagamento  Emissores'  # noqa: E501

        :param type: The type of this CreditCardIdentificationProduct.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["CLASSIC_NACIONAL", "CLASSIC_INTERNACIONAL", "GOLD", "PLATINUM", "INFINITE", "ELECTRON", "STANDARD_NACIONAL", "STANDARD_INTERNACIONAL", "ELETRONIC", "BLACK", "REDESHOP", "MAESTRO_MASTERCARD_MAESTRO", "GREEN", "BLUE", "BLUEBOX", "PROFISSIONAL_LIBERAL", "CHEQUE_ELETRONICO", "CORPORATIVO", "EMPRESARIAL", "COMPRAS", "OUTROS"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def additional_info(self):
        """Gets the additional_info of this CreditCardIdentificationProduct.  # noqa: E501

        Informações complementares se tipo de Cartão 'OUTROS'. Campo deve ser obrigatoriamente preenchido se selecionado 'OUTROS'  # noqa: E501

        :return: The additional_info of this CreditCardIdentificationProduct.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this CreditCardIdentificationProduct.

        Informações complementares se tipo de Cartão 'OUTROS'. Campo deve ser obrigatoriamente preenchido se selecionado 'OUTROS'  # noqa: E501

        :param additional_info: The additional_info of this CreditCardIdentificationProduct.  # noqa: E501
        :type: str
        """
        if additional_info is None:
            raise ValueError("Invalid value for `additional_info`, must not be `None`")  # noqa: E501

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
        if issubclass(CreditCardIdentificationProduct, dict):
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
        if not isinstance(other, CreditCardIdentificationProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
