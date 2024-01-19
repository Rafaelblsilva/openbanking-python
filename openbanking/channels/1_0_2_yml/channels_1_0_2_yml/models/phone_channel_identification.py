# coding: utf-8

"""
    APIs OpenData do Open Finance Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PhoneChannelIdentification(object):
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
        'additional_info': 'str',
        'phones': 'list[PhoneChannelPhone]'
    }

    attribute_map = {
        'type': 'type',
        'additional_info': 'additionalInfo',
        'phones': 'phones'
    }

    def __init__(self, type=None, additional_info=None, phones=None):  # noqa: E501
        """PhoneChannelIdentification - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._additional_info = None
        self._phones = None
        self.discriminator = None
        self.type = type
        if additional_info is not None:
            self.additional_info = additional_info
        if phones is not None:
            self.phones = phones

    @property
    def type(self):
        """Gets the type of this PhoneChannelIdentification.  # noqa: E501

         Tipo de canal telefônico de atendimento:  * `CENTRAL_TELEFONICA`  * `SAC`  * `OUVIDORIA`  * `OUTROS`  # noqa: E501

        :return: The type of this PhoneChannelIdentification.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PhoneChannelIdentification.

         Tipo de canal telefônico de atendimento:  * `CENTRAL_TELEFONICA`  * `SAC`  * `OUVIDORIA`  * `OUTROS`  # noqa: E501

        :param type: The type of this PhoneChannelIdentification.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["CENTRAL_TELEFONICA", "SAC", "OUVIDORIA", "OUTROS"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def additional_info(self):
        """Gets the additional_info of this PhoneChannelIdentification.  # noqa: E501

        Campo de texto livre para descrever informações complementateres sobre canais telefônicos. De preenchimento obrigatório quando o tipo de canal de atendimento telefônico selecionado for \"OUTROS\"  # noqa: E501

        :return: The additional_info of this PhoneChannelIdentification.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this PhoneChannelIdentification.

        Campo de texto livre para descrever informações complementateres sobre canais telefônicos. De preenchimento obrigatório quando o tipo de canal de atendimento telefônico selecionado for \"OUTROS\"  # noqa: E501

        :param additional_info: The additional_info of this PhoneChannelIdentification.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def phones(self):
        """Gets the phones of this PhoneChannelIdentification.  # noqa: E501

        Lista de telefones do Canal de Atendimento  # noqa: E501

        :return: The phones of this PhoneChannelIdentification.  # noqa: E501
        :rtype: list[PhoneChannelPhone]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this PhoneChannelIdentification.

        Lista de telefones do Canal de Atendimento  # noqa: E501

        :param phones: The phones of this PhoneChannelIdentification.  # noqa: E501
        :type: list[PhoneChannelPhone]
        """

        self._phones = phones

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
        if issubclass(PhoneChannelIdentification, dict):
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
        if not isinstance(other, PhoneChannelIdentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
