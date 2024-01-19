# coding: utf-8

"""
    API's OpenData do Open Finance Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardIdentificationCreditCard(object):
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
        'network': 'str',
        'additional_info': 'str'
    }

    attribute_map = {
        'network': 'network',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, network=None, additional_info=None):  # noqa: E501
        """CreditCardIdentificationCreditCard - a model defined in Swagger"""  # noqa: E501
        self._network = None
        self._additional_info = None
        self.discriminator = None
        self.network = network
        self.additional_info = additional_info

    @property
    def network(self):
        """Gets the network of this CreditCardIdentificationCreditCard.  # noqa: E501

        Categoria de Bandeiras de Cartões de Crédito (Instituidor do arranjo de pagamento). Bandeira é a detentora de todos os direitos e deveres da utilização da marca estampada no cartão, inclusive as bandeiras pertencentes aos emissores. p.ex. \"American Express\", \"Diners Club\" Essas bandeiras estão definidas em documento do BACEN de nome \"Elaboração e Remessa de Informações Relativas aos Cartões de Pagamento  Emissores\"  # noqa: E501

        :return: The network of this CreditCardIdentificationCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this CreditCardIdentificationCreditCard.

        Categoria de Bandeiras de Cartões de Crédito (Instituidor do arranjo de pagamento). Bandeira é a detentora de todos os direitos e deveres da utilização da marca estampada no cartão, inclusive as bandeiras pertencentes aos emissores. p.ex. \"American Express\", \"Diners Club\" Essas bandeiras estão definidas em documento do BACEN de nome \"Elaboração e Remessa de Informações Relativas aos Cartões de Pagamento  Emissores\"  # noqa: E501

        :param network: The network of this CreditCardIdentificationCreditCard.  # noqa: E501
        :type: str
        """
        if network is None:
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501
        allowed_values = ["VISA", "MASTERCARD", "AMERICAN_EXPRESS", "DINERS_CLUB", "HIPERCARD", "BANDEIRA_PROPRIA", "CHEQUE_ELETRONICO", "ELO", "OUTRAS"]  # noqa: E501
        if network not in allowed_values:
            raise ValueError(
                "Invalid value for `network` ({0}), must be one of {1}"  # noqa: E501
                .format(network, allowed_values)
            )

        self._network = network

    @property
    def additional_info(self):
        """Gets the additional_info of this CreditCardIdentificationCreditCard.  # noqa: E501

        Texto livre para especificar categoria de bandeira marcada como 'OUTRAS'. Campo deve ser obrigatoriamente preenchido se campo network vier selecionado como 'OUTROS'  # noqa: E501

        :return: The additional_info of this CreditCardIdentificationCreditCard.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this CreditCardIdentificationCreditCard.

        Texto livre para especificar categoria de bandeira marcada como 'OUTRAS'. Campo deve ser obrigatoriamente preenchido se campo network vier selecionado como 'OUTROS'  # noqa: E501

        :param additional_info: The additional_info of this CreditCardIdentificationCreditCard.  # noqa: E501
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
        if issubclass(CreditCardIdentificationCreditCard, dict):
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
        if not isinstance(other, CreditCardIdentificationCreditCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
