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

class ServiceBundleServiceDetail(object):
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
        'code': 'str',
        'charging_trigger_info': 'str',
        'event_limit_quantity': 'str',
        'free_event_quantity': 'str'
    }

    attribute_map = {
        'code': 'code',
        'charging_trigger_info': 'chargingTriggerInfo',
        'event_limit_quantity': 'eventLimitQuantity',
        'free_event_quantity': 'freeEventQuantity'
    }

    def __init__(self, code=None, charging_trigger_info=None, event_limit_quantity=None, free_event_quantity=None):  # noqa: E501
        """ServiceBundleServiceDetail - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._charging_trigger_info = None
        self._event_limit_quantity = None
        self._free_event_quantity = None
        self.discriminator = None
        self.code = code
        self.charging_trigger_info = charging_trigger_info
        self.event_limit_quantity = event_limit_quantity
        self.free_event_quantity = free_event_quantity

    @property
    def code(self):
        """Gets the code of this ServiceBundleServiceDetail.  # noqa: E501

        Código que identifica o Serviço que compõe o Pacote de Serviços, podendo ser da lista de Serviços Prioritários ou Outros Serviços. p.ex. segundo Resolução 3.919 do Bacen: 'SAQUE_TERMINAL'.   # noqa: E501

        :return: The code of this ServiceBundleServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ServiceBundleServiceDetail.

        Código que identifica o Serviço que compõe o Pacote de Serviços, podendo ser da lista de Serviços Prioritários ou Outros Serviços. p.ex. segundo Resolução 3.919 do Bacen: 'SAQUE_TERMINAL'.   # noqa: E501

        :param code: The code of this ServiceBundleServiceDetail.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def charging_trigger_info(self):
        """Gets the charging_trigger_info of this ServiceBundleServiceDetail.  # noqa: E501

        Fatos geradores de cobrança que incidem sobre serviço que compõe o Pacote de Serviços.   # noqa: E501

        :return: The charging_trigger_info of this ServiceBundleServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._charging_trigger_info

    @charging_trigger_info.setter
    def charging_trigger_info(self, charging_trigger_info):
        """Sets the charging_trigger_info of this ServiceBundleServiceDetail.

        Fatos geradores de cobrança que incidem sobre serviço que compõe o Pacote de Serviços.   # noqa: E501

        :param charging_trigger_info: The charging_trigger_info of this ServiceBundleServiceDetail.  # noqa: E501
        :type: str
        """
        if charging_trigger_info is None:
            raise ValueError("Invalid value for `charging_trigger_info`, must not be `None`")  # noqa: E501

        self._charging_trigger_info = charging_trigger_info

    @property
    def event_limit_quantity(self):
        """Gets the event_limit_quantity of this ServiceBundleServiceDetail.  # noqa: E501

        Segundo Resolução  4196, BCB, de 2013: Quantidade de eventos previstos no Pacote de Serviços (Número de eventos incluídos no mês) p.ex.'2'. No caso de quantidade ilimitada, reportar 999999   # noqa: E501

        :return: The event_limit_quantity of this ServiceBundleServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._event_limit_quantity

    @event_limit_quantity.setter
    def event_limit_quantity(self, event_limit_quantity):
        """Sets the event_limit_quantity of this ServiceBundleServiceDetail.

        Segundo Resolução  4196, BCB, de 2013: Quantidade de eventos previstos no Pacote de Serviços (Número de eventos incluídos no mês) p.ex.'2'. No caso de quantidade ilimitada, reportar 999999   # noqa: E501

        :param event_limit_quantity: The event_limit_quantity of this ServiceBundleServiceDetail.  # noqa: E501
        :type: str
        """
        if event_limit_quantity is None:
            raise ValueError("Invalid value for `event_limit_quantity`, must not be `None`")  # noqa: E501

        self._event_limit_quantity = event_limit_quantity

    @property
    def free_event_quantity(self):
        """Gets the free_event_quantity of this ServiceBundleServiceDetail.  # noqa: E501

        Segundo Resolução  4196, BCB, de 2013: Quantidade de eventos previstos no Pacote de Serviços com isenção de Tarifa.p.ex.'1'  No caso de quantidade ilimitada, reportar 999999   # noqa: E501

        :return: The free_event_quantity of this ServiceBundleServiceDetail.  # noqa: E501
        :rtype: str
        """
        return self._free_event_quantity

    @free_event_quantity.setter
    def free_event_quantity(self, free_event_quantity):
        """Sets the free_event_quantity of this ServiceBundleServiceDetail.

        Segundo Resolução  4196, BCB, de 2013: Quantidade de eventos previstos no Pacote de Serviços com isenção de Tarifa.p.ex.'1'  No caso de quantidade ilimitada, reportar 999999   # noqa: E501

        :param free_event_quantity: The free_event_quantity of this ServiceBundleServiceDetail.  # noqa: E501
        :type: str
        """
        if free_event_quantity is None:
            raise ValueError("Invalid value for `free_event_quantity`, must not be `None`")  # noqa: E501

        self._free_event_quantity = free_event_quantity

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
        if issubclass(ServiceBundleServiceDetail, dict):
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
        if not isinstance(other, ServiceBundleServiceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
