# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ElectronicChannelIdentification(object):
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
        'urls': 'list[ElectronicChannelUrl]'
    }

    attribute_map = {
        'type': 'type',
        'additional_info': 'additionalInfo',
        'urls': 'urls'
    }

    def __init__(self, type=None, additional_info=None, urls=None):  # noqa: E501
        """ElectronicChannelIdentification - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._additional_info = None
        self._urls = None
        self.discriminator = None
        self.type = type
        if additional_info is not None:
            self.additional_info = additional_info
        self.urls = urls

    @property
    def type(self):
        """Gets the type of this ElectronicChannelIdentification.  # noqa: E501

        Tipo de canal de atendimento eletrônico  # noqa: E501

        :return: The type of this ElectronicChannelIdentification.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ElectronicChannelIdentification.

        Tipo de canal de atendimento eletrônico  # noqa: E501

        :param type: The type of this ElectronicChannelIdentification.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["INTERNET_BANKING", "MOBILE_BANKING", "SAC", "OUVIDORIA", "CHAT", "OUTROS"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def additional_info(self):
        """Gets the additional_info of this ElectronicChannelIdentification.  # noqa: E501

        Campo de texto livre para descrever complementação de informações necessárias. De preenchimento obrigatório para  o tipo de canal de atendimento 'OUTROS' Restrição: Preenchimento obrigatório para o tipo de canal de atendimento 'OUTROS'   # noqa: E501

        :return: The additional_info of this ElectronicChannelIdentification.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this ElectronicChannelIdentification.

        Campo de texto livre para descrever complementação de informações necessárias. De preenchimento obrigatório para  o tipo de canal de atendimento 'OUTROS' Restrição: Preenchimento obrigatório para o tipo de canal de atendimento 'OUTROS'   # noqa: E501

        :param additional_info: The additional_info of this ElectronicChannelIdentification.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def urls(self):
        """Gets the urls of this ElectronicChannelIdentification.  # noqa: E501

        Lista das URLs que atendem um tipo de canal eletrônico selecionado  # noqa: E501

        :return: The urls of this ElectronicChannelIdentification.  # noqa: E501
        :rtype: list[ElectronicChannelUrl]
        """
        return self._urls

    @urls.setter
    def urls(self, urls):
        """Sets the urls of this ElectronicChannelIdentification.

        Lista das URLs que atendem um tipo de canal eletrônico selecionado  # noqa: E501

        :param urls: The urls of this ElectronicChannelIdentification.  # noqa: E501
        :type: list[ElectronicChannelUrl]
        """
        if urls is None:
            raise ValueError("Invalid value for `urls`, must not be `None`")  # noqa: E501

        self._urls = urls

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
        if issubclass(ElectronicChannelIdentification, dict):
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
        if not isinstance(other, ElectronicChannelIdentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
