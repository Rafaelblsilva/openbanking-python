# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    API de Dispositivo Vínculado para suportar Iniciação de Pagamentos na Jornada Sem Redirecionamento do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc.2
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ConsentAuthorizationDataFidoAssertionResponse(object):
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
        'client_data_json': 'str',
        'authenticator_data': 'str',
        'signature': 'str',
        'user_handle': 'str'
    }

    attribute_map = {
        'client_data_json': 'clientDataJSON',
        'authenticator_data': 'authenticatorData',
        'signature': 'signature',
        'user_handle': 'userHandle'
    }

    def __init__(self, client_data_json=None, authenticator_data=None, signature=None, user_handle=None):  # noqa: E501
        """ConsentAuthorizationDataFidoAssertionResponse - a model defined in Swagger"""  # noqa: E501
        self._client_data_json = None
        self._authenticator_data = None
        self._signature = None
        self._user_handle = None
        self.discriminator = None
        self.client_data_json = client_data_json
        self.authenticator_data = authenticator_data
        self.signature = signature
        self.user_handle = user_handle

    @property
    def client_data_json(self):
        """Gets the client_data_json of this ConsentAuthorizationDataFidoAssertionResponse.  # noqa: E501

        Agrega as informações do aplicativo que gerou a credencial.  # noqa: E501

        :return: The client_data_json of this ConsentAuthorizationDataFidoAssertionResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_data_json

    @client_data_json.setter
    def client_data_json(self, client_data_json):
        """Sets the client_data_json of this ConsentAuthorizationDataFidoAssertionResponse.

        Agrega as informações do aplicativo que gerou a credencial.  # noqa: E501

        :param client_data_json: The client_data_json of this ConsentAuthorizationDataFidoAssertionResponse.  # noqa: E501
        :type: str
        """
        if client_data_json is None:
            raise ValueError("Invalid value for `client_data_json`, must not be `None`")  # noqa: E501

        self._client_data_json = client_data_json

    @property
    def authenticator_data(self):
        """Gets the authenticator_data of this ConsentAuthorizationDataFidoAssertionResponse.  # noqa: E501

        Representa a estrutura de dados do autenticador.  # noqa: E501

        :return: The authenticator_data of this ConsentAuthorizationDataFidoAssertionResponse.  # noqa: E501
        :rtype: str
        """
        return self._authenticator_data

    @authenticator_data.setter
    def authenticator_data(self, authenticator_data):
        """Sets the authenticator_data of this ConsentAuthorizationDataFidoAssertionResponse.

        Representa a estrutura de dados do autenticador.  # noqa: E501

        :param authenticator_data: The authenticator_data of this ConsentAuthorizationDataFidoAssertionResponse.  # noqa: E501
        :type: str
        """
        if authenticator_data is None:
            raise ValueError("Invalid value for `authenticator_data`, must not be `None`")  # noqa: E501

        self._authenticator_data = authenticator_data

    @property
    def signature(self):
        """Gets the signature of this ConsentAuthorizationDataFidoAssertionResponse.  # noqa: E501

        Sequencia de bytes contendo a assinatura.  # noqa: E501

        :return: The signature of this ConsentAuthorizationDataFidoAssertionResponse.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this ConsentAuthorizationDataFidoAssertionResponse.

        Sequencia de bytes contendo a assinatura.  # noqa: E501

        :param signature: The signature of this ConsentAuthorizationDataFidoAssertionResponse.  # noqa: E501
        :type: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def user_handle(self):
        """Gets the user_handle of this ConsentAuthorizationDataFidoAssertionResponse.  # noqa: E501

        Nome de usuário que foi enviado durante a criação da credencial.  # noqa: E501

        :return: The user_handle of this ConsentAuthorizationDataFidoAssertionResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_handle

    @user_handle.setter
    def user_handle(self, user_handle):
        """Sets the user_handle of this ConsentAuthorizationDataFidoAssertionResponse.

        Nome de usuário que foi enviado durante a criação da credencial.  # noqa: E501

        :param user_handle: The user_handle of this ConsentAuthorizationDataFidoAssertionResponse.  # noqa: E501
        :type: str
        """
        if user_handle is None:
            raise ValueError("Invalid value for `user_handle`, must not be `None`")  # noqa: E501

        self._user_handle = user_handle

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
        if issubclass(ConsentAuthorizationDataFidoAssertionResponse, dict):
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
        if not isinstance(other, ConsentAuthorizationDataFidoAssertionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
