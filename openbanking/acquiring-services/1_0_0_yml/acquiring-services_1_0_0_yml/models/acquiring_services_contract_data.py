# coding: utf-8

"""
    API Acquiring Services - Open Finance Brasil

    API de Credenciamento do Open Finance Brasil – Fase 4. API que retorna informações de Credenciamento.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AcquiringServicesContractData(object):
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
        'participant': 'AcquiringParticipant',
        'fee_name': 'EnumAcquiringServicesFeeName',
        'code': 'EnumAcquiringServicesCode',
        'prices': 'list[Price]',
        'charging_trigger_info': 'str',
        'minimum': 'str',
        'maximum': 'str'
    }

    attribute_map = {
        'participant': 'participant',
        'fee_name': 'feeName',
        'code': 'code',
        'prices': 'prices',
        'charging_trigger_info': 'chargingTriggerInfo',
        'minimum': 'minimum',
        'maximum': 'maximum'
    }

    def __init__(self, participant=None, fee_name=None, code=None, prices=None, charging_trigger_info=None, minimum=None, maximum=None):  # noqa: E501
        """AcquiringServicesContractData - a model defined in Swagger"""  # noqa: E501
        self._participant = None
        self._fee_name = None
        self._code = None
        self._prices = None
        self._charging_trigger_info = None
        self._minimum = None
        self._maximum = None
        self.discriminator = None
        self.participant = participant
        self.fee_name = fee_name
        self.code = code
        self.prices = prices
        self.charging_trigger_info = charging_trigger_info
        self.minimum = minimum
        self.maximum = maximum

    @property
    def participant(self):
        """Gets the participant of this AcquiringServicesContractData.  # noqa: E501


        :return: The participant of this AcquiringServicesContractData.  # noqa: E501
        :rtype: AcquiringParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this AcquiringServicesContractData.


        :param participant: The participant of this AcquiringServicesContractData.  # noqa: E501
        :type: AcquiringParticipant
        """
        if participant is None:
            raise ValueError("Invalid value for `participant`, must not be `None`")  # noqa: E501

        self._participant = participant

    @property
    def fee_name(self):
        """Gets the fee_name of this AcquiringServicesContractData.  # noqa: E501


        :return: The fee_name of this AcquiringServicesContractData.  # noqa: E501
        :rtype: EnumAcquiringServicesFeeName
        """
        return self._fee_name

    @fee_name.setter
    def fee_name(self, fee_name):
        """Sets the fee_name of this AcquiringServicesContractData.


        :param fee_name: The fee_name of this AcquiringServicesContractData.  # noqa: E501
        :type: EnumAcquiringServicesFeeName
        """
        if fee_name is None:
            raise ValueError("Invalid value for `fee_name`, must not be `None`")  # noqa: E501

        self._fee_name = fee_name

    @property
    def code(self):
        """Gets the code of this AcquiringServicesContractData.  # noqa: E501


        :return: The code of this AcquiringServicesContractData.  # noqa: E501
        :rtype: EnumAcquiringServicesCode
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this AcquiringServicesContractData.


        :param code: The code of this AcquiringServicesContractData.  # noqa: E501
        :type: EnumAcquiringServicesCode
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def prices(self):
        """Gets the prices of this AcquiringServicesContractData.  # noqa: E501


        :return: The prices of this AcquiringServicesContractData.  # noqa: E501
        :rtype: list[Price]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """Sets the prices of this AcquiringServicesContractData.


        :param prices: The prices of this AcquiringServicesContractData.  # noqa: E501
        :type: list[Price]
        """
        if prices is None:
            raise ValueError("Invalid value for `prices`, must not be `None`")  # noqa: E501

        self._prices = prices

    @property
    def charging_trigger_info(self):
        """Gets the charging_trigger_info of this AcquiringServicesContractData.  # noqa: E501

        Descrição do Fator gerador de cobrança que incide sobre o serviço de credenciamento.   # noqa: E501

        :return: The charging_trigger_info of this AcquiringServicesContractData.  # noqa: E501
        :rtype: str
        """
        return self._charging_trigger_info

    @charging_trigger_info.setter
    def charging_trigger_info(self, charging_trigger_info):
        """Sets the charging_trigger_info of this AcquiringServicesContractData.

        Descrição do Fator gerador de cobrança que incide sobre o serviço de credenciamento.   # noqa: E501

        :param charging_trigger_info: The charging_trigger_info of this AcquiringServicesContractData.  # noqa: E501
        :type: str
        """
        if charging_trigger_info is None:
            raise ValueError("Invalid value for `charging_trigger_info`, must not be `None`")  # noqa: E501

        self._charging_trigger_info = charging_trigger_info

    @property
    def minimum(self):
        """Gets the minimum of this AcquiringServicesContractData.  # noqa: E501

        Valor mínimo  # noqa: E501

        :return: The minimum of this AcquiringServicesContractData.  # noqa: E501
        :rtype: str
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this AcquiringServicesContractData.

        Valor mínimo  # noqa: E501

        :param minimum: The minimum of this AcquiringServicesContractData.  # noqa: E501
        :type: str
        """
        if minimum is None:
            raise ValueError("Invalid value for `minimum`, must not be `None`")  # noqa: E501

        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this AcquiringServicesContractData.  # noqa: E501

        Valor máximo  # noqa: E501

        :return: The maximum of this AcquiringServicesContractData.  # noqa: E501
        :rtype: str
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this AcquiringServicesContractData.

        Valor máximo  # noqa: E501

        :param maximum: The maximum of this AcquiringServicesContractData.  # noqa: E501
        :type: str
        """
        if maximum is None:
            raise ValueError("Invalid value for `maximum`, must not be `None`")  # noqa: E501

        self._maximum = maximum

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
        if issubclass(AcquiringServicesContractData, dict):
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
        if not isinstance(other, AcquiringServicesContractData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
