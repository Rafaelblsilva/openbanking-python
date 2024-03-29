# coding: utf-8

"""
    API Exchange - Open Finance Brasil

    API de Câmbio do Open Finance Brasil – Fase 4. API que retorna informações de Câmbio.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExchangeOnlineRate(object):
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
        'participant': 'Participant',
        'foreign_currency': 'CurrencyCode',
        'delivery_foreign_currency': 'EnumExchangeDeliveryForeignCurrency',
        'transaction_type': 'EnumExchangeTransactionType',
        'transaction_category': 'EnumExchangeTransactionCategory',
        'target_audience': 'EnumDistinctTargetAudienceExchange',
        'value': 'str',
        'value_update_date_time': 'datetime',
        'disclaimer': 'str'
    }

    attribute_map = {
        'participant': 'participant',
        'foreign_currency': 'foreignCurrency',
        'delivery_foreign_currency': 'deliveryForeignCurrency',
        'transaction_type': 'transactionType',
        'transaction_category': 'transactionCategory',
        'target_audience': 'targetAudience',
        'value': 'value',
        'value_update_date_time': 'valueUpdateDateTime',
        'disclaimer': 'disclaimer'
    }

    def __init__(self, participant=None, foreign_currency=None, delivery_foreign_currency=None, transaction_type=None, transaction_category=None, target_audience=None, value=None, value_update_date_time=None, disclaimer=None):  # noqa: E501
        """ExchangeOnlineRate - a model defined in Swagger"""  # noqa: E501
        self._participant = None
        self._foreign_currency = None
        self._delivery_foreign_currency = None
        self._transaction_type = None
        self._transaction_category = None
        self._target_audience = None
        self._value = None
        self._value_update_date_time = None
        self._disclaimer = None
        self.discriminator = None
        self.participant = participant
        self.foreign_currency = foreign_currency
        self.delivery_foreign_currency = delivery_foreign_currency
        self.transaction_type = transaction_type
        self.transaction_category = transaction_category
        self.target_audience = target_audience
        self.value = value
        self.value_update_date_time = value_update_date_time
        self.disclaimer = disclaimer

    @property
    def participant(self):
        """Gets the participant of this ExchangeOnlineRate.  # noqa: E501


        :return: The participant of this ExchangeOnlineRate.  # noqa: E501
        :rtype: Participant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this ExchangeOnlineRate.


        :param participant: The participant of this ExchangeOnlineRate.  # noqa: E501
        :type: Participant
        """
        if participant is None:
            raise ValueError("Invalid value for `participant`, must not be `None`")  # noqa: E501

        self._participant = participant

    @property
    def foreign_currency(self):
        """Gets the foreign_currency of this ExchangeOnlineRate.  # noqa: E501


        :return: The foreign_currency of this ExchangeOnlineRate.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._foreign_currency

    @foreign_currency.setter
    def foreign_currency(self, foreign_currency):
        """Sets the foreign_currency of this ExchangeOnlineRate.


        :param foreign_currency: The foreign_currency of this ExchangeOnlineRate.  # noqa: E501
        :type: CurrencyCode
        """
        if foreign_currency is None:
            raise ValueError("Invalid value for `foreign_currency`, must not be `None`")  # noqa: E501

        self._foreign_currency = foreign_currency

    @property
    def delivery_foreign_currency(self):
        """Gets the delivery_foreign_currency of this ExchangeOnlineRate.  # noqa: E501


        :return: The delivery_foreign_currency of this ExchangeOnlineRate.  # noqa: E501
        :rtype: EnumExchangeDeliveryForeignCurrency
        """
        return self._delivery_foreign_currency

    @delivery_foreign_currency.setter
    def delivery_foreign_currency(self, delivery_foreign_currency):
        """Sets the delivery_foreign_currency of this ExchangeOnlineRate.


        :param delivery_foreign_currency: The delivery_foreign_currency of this ExchangeOnlineRate.  # noqa: E501
        :type: EnumExchangeDeliveryForeignCurrency
        """
        if delivery_foreign_currency is None:
            raise ValueError("Invalid value for `delivery_foreign_currency`, must not be `None`")  # noqa: E501

        self._delivery_foreign_currency = delivery_foreign_currency

    @property
    def transaction_type(self):
        """Gets the transaction_type of this ExchangeOnlineRate.  # noqa: E501


        :return: The transaction_type of this ExchangeOnlineRate.  # noqa: E501
        :rtype: EnumExchangeTransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this ExchangeOnlineRate.


        :param transaction_type: The transaction_type of this ExchangeOnlineRate.  # noqa: E501
        :type: EnumExchangeTransactionType
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def transaction_category(self):
        """Gets the transaction_category of this ExchangeOnlineRate.  # noqa: E501


        :return: The transaction_category of this ExchangeOnlineRate.  # noqa: E501
        :rtype: EnumExchangeTransactionCategory
        """
        return self._transaction_category

    @transaction_category.setter
    def transaction_category(self, transaction_category):
        """Sets the transaction_category of this ExchangeOnlineRate.


        :param transaction_category: The transaction_category of this ExchangeOnlineRate.  # noqa: E501
        :type: EnumExchangeTransactionCategory
        """
        if transaction_category is None:
            raise ValueError("Invalid value for `transaction_category`, must not be `None`")  # noqa: E501

        self._transaction_category = transaction_category

    @property
    def target_audience(self):
        """Gets the target_audience of this ExchangeOnlineRate.  # noqa: E501


        :return: The target_audience of this ExchangeOnlineRate.  # noqa: E501
        :rtype: EnumDistinctTargetAudienceExchange
        """
        return self._target_audience

    @target_audience.setter
    def target_audience(self, target_audience):
        """Sets the target_audience of this ExchangeOnlineRate.


        :param target_audience: The target_audience of this ExchangeOnlineRate.  # noqa: E501
        :type: EnumDistinctTargetAudienceExchange
        """
        if target_audience is None:
            raise ValueError("Invalid value for `target_audience`, must not be `None`")  # noqa: E501

        self._target_audience = target_audience

    @property
    def value(self):
        """Gets the value of this ExchangeOnlineRate.  # noqa: E501

        Valor da operação.  # noqa: E501

        :return: The value of this ExchangeOnlineRate.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ExchangeOnlineRate.

        Valor da operação.  # noqa: E501

        :param value: The value of this ExchangeOnlineRate.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def value_update_date_time(self):
        """Gets the value_update_date_time of this ExchangeOnlineRate.  # noqa: E501

        Data e hora da última atualização da cotação.  # noqa: E501

        :return: The value_update_date_time of this ExchangeOnlineRate.  # noqa: E501
        :rtype: datetime
        """
        return self._value_update_date_time

    @value_update_date_time.setter
    def value_update_date_time(self, value_update_date_time):
        """Sets the value_update_date_time of this ExchangeOnlineRate.

        Data e hora da última atualização da cotação.  # noqa: E501

        :param value_update_date_time: The value_update_date_time of this ExchangeOnlineRate.  # noqa: E501
        :type: datetime
        """
        if value_update_date_time is None:
            raise ValueError("Invalid value for `value_update_date_time`, must not be `None`")  # noqa: E501

        self._value_update_date_time = value_update_date_time

    @property
    def disclaimer(self):
        """Gets the disclaimer of this ExchangeOnlineRate.  # noqa: E501

        Disclaimer informando que a taxa apresentada é somente informativa, para a contratação de uma operação, deverá ser consultado o canal correspondente de cada instituição.  # noqa: E501

        :return: The disclaimer of this ExchangeOnlineRate.  # noqa: E501
        :rtype: str
        """
        return self._disclaimer

    @disclaimer.setter
    def disclaimer(self, disclaimer):
        """Sets the disclaimer of this ExchangeOnlineRate.

        Disclaimer informando que a taxa apresentada é somente informativa, para a contratação de uma operação, deverá ser consultado o canal correspondente de cada instituição.  # noqa: E501

        :param disclaimer: The disclaimer of this ExchangeOnlineRate.  # noqa: E501
        :type: str
        """
        if disclaimer is None:
            raise ValueError("Invalid value for `disclaimer`, must not be `None`")  # noqa: E501

        self._disclaimer = disclaimer

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
        if issubclass(ExchangeOnlineRate, dict):
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
        if not isinstance(other, ExchangeOnlineRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
