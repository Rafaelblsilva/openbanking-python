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

class FidoPublicKeyCredentialDescriptor(object):
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
        'id': 'str',
        'type': 'str',
        'transports': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'transports': 'transports'
    }

    def __init__(self, id=None, type=None, transports=None):  # noqa: E501
        """FidoPublicKeyCredentialDescriptor - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._transports = None
        self.discriminator = None
        self.id = id
        self.type = type
        if transports is not None:
            self.transports = transports

    @property
    def id(self):
        """Gets the id of this FidoPublicKeyCredentialDescriptor.  # noqa: E501

        Identificador único da credencial.  # noqa: E501

        :return: The id of this FidoPublicKeyCredentialDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FidoPublicKeyCredentialDescriptor.

        Identificador único da credencial.  # noqa: E501

        :param id: The id of this FidoPublicKeyCredentialDescriptor.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this FidoPublicKeyCredentialDescriptor.  # noqa: E501

        Identificador do tipo de credencial.  # noqa: E501

        :return: The type of this FidoPublicKeyCredentialDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FidoPublicKeyCredentialDescriptor.

        Identificador do tipo de credencial.  # noqa: E501

        :param type: The type of this FidoPublicKeyCredentialDescriptor.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def transports(self):
        """Gets the transports of this FidoPublicKeyCredentialDescriptor.  # noqa: E501

        Indicação opcional de como o cliente pode se comunicar com o autenticador do dispositivo.  # noqa: E501

        :return: The transports of this FidoPublicKeyCredentialDescriptor.  # noqa: E501
        :rtype: list[str]
        """
        return self._transports

    @transports.setter
    def transports(self, transports):
        """Sets the transports of this FidoPublicKeyCredentialDescriptor.

        Indicação opcional de como o cliente pode se comunicar com o autenticador do dispositivo.  # noqa: E501

        :param transports: The transports of this FidoPublicKeyCredentialDescriptor.  # noqa: E501
        :type: list[str]
        """

        self._transports = transports

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
        if issubclass(FidoPublicKeyCredentialDescriptor, dict):
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
        if not isinstance(other, FidoPublicKeyCredentialDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other