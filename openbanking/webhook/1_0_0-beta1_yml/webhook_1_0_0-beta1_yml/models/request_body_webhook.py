# coding: utf-8

"""
    API Webhook - Open Finance Brasil

    API de Webhook é responsável por notificar eventos definidos em cada uma das APIs que possuem a funcionalidade no Open Finance Brasil.  <u>Endpoints que possuem a funcionalidade de Webhook</u> <br/>  Na versão atual, temos os seguintes endpoints:   API Payments v2:   - POST /pix/payments   - POST /consents  # Orientações <u>Todos os endpoints nessa API utilizam-se de mTLS para autenticação, não possuem scopes e permissions específicos de segurança. Toda a segurança é feita via certificado(mTLS – BRCAC).</u>  Dado que as URLs do ecossistema são formadas com a configuração abaixo:   \\<host> / \\<string> / \\<api> / \\<versão> / \\<recurso>  <u>Para a utilização desse recurso é necessário que:</u> - Iniciadoras de pagamentos e/ou Receptora de dados: Precisam cadastrar a sua URI base (\\<host>) no diretório de participantes no campo `<CAMPO_A_DEFINIR>`, - Detentoras de contas e/ou Transmissora de dados: Precisam construir a URI de notificação da seguinte forma:  <u>Exemplo de URI do consentimento:</u> <br/> <br/> <img src=\"./img/image001.png\" alt=\"Image Webhook\"/> <br/> <br/>  <u>Exemplo de URI do pagamento:</u> <br/> <br/> <img src=\"./img/image002.png\" alt=\"Image Webhook\"/>   # noqa: E501

    OpenAPI spec version: 1.0.0-beta1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RequestBodyWebhook(object):
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
        'data': 'RequestBodyWebhookData'
    }

    attribute_map = {
        'data': 'data'
    }

    def __init__(self, data=None):  # noqa: E501
        """RequestBodyWebhook - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self.discriminator = None
        self.data = data

    @property
    def data(self):
        """Gets the data of this RequestBodyWebhook.  # noqa: E501


        :return: The data of this RequestBodyWebhook.  # noqa: E501
        :rtype: RequestBodyWebhookData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this RequestBodyWebhook.


        :param data: The data of this RequestBodyWebhook.  # noqa: E501
        :type: RequestBodyWebhookData
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if issubclass(RequestBodyWebhook, dict):
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
        if not isinstance(other, RequestBodyWebhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
