# coding: utf-8

"""
    API Exchange - Open Finance Brasil

    API de Câmbio do Open Finance Brasil – Fase 4. API que retorna informações de Câmbio.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ExchangeVetValue(object):
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
        'transaction_type': 'EnumExchangeTransactionType',
        'foreign_currency': 'CurrencyCode',
        'delivery_foreign_currency': 'EnumExchangeDeliveryForeignCurrency',
        'range_transaction_category': 'EnumExchangeRangeTransactionCategory',
        'target_audience': 'EnumDistinctTargetAudienceExchange',
        'vet_amount': 'ExchangeNoIdentificationFrequencyDistribution'
    }

    attribute_map = {
        'participant': 'participant',
        'transaction_type': 'transactionType',
        'foreign_currency': 'foreignCurrency',
        'delivery_foreign_currency': 'deliveryForeignCurrency',
        'range_transaction_category': 'rangeTransactionCategory',
        'target_audience': 'targetAudience',
        'vet_amount': 'vetAmount'
    }

    def __init__(self, participant=None, transaction_type=None, foreign_currency=None, delivery_foreign_currency=None, range_transaction_category=None, target_audience=None, vet_amount=None):  # noqa: E501
        """ExchangeVetValue - a model defined in Swagger"""  # noqa: E501
        self._participant = None
        self._transaction_type = None
        self._foreign_currency = None
        self._delivery_foreign_currency = None
        self._range_transaction_category = None
        self._target_audience = None
        self._vet_amount = None
        self.discriminator = None
        self.participant = participant
        self.transaction_type = transaction_type
        self.foreign_currency = foreign_currency
        self.delivery_foreign_currency = delivery_foreign_currency
        self.range_transaction_category = range_transaction_category
        self.target_audience = target_audience
        self.vet_amount = vet_amount

    @property
    def participant(self):
        """Gets the participant of this ExchangeVetValue.  # noqa: E501


        :return: The participant of this ExchangeVetValue.  # noqa: E501
        :rtype: Participant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this ExchangeVetValue.


        :param participant: The participant of this ExchangeVetValue.  # noqa: E501
        :type: Participant
        """
        if participant is None:
            raise ValueError("Invalid value for `participant`, must not be `None`")  # noqa: E501

        self._participant = participant

    @property
    def transaction_type(self):
        """Gets the transaction_type of this ExchangeVetValue.  # noqa: E501


        :return: The transaction_type of this ExchangeVetValue.  # noqa: E501
        :rtype: EnumExchangeTransactionType
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this ExchangeVetValue.


        :param transaction_type: The transaction_type of this ExchangeVetValue.  # noqa: E501
        :type: EnumExchangeTransactionType
        """
        if transaction_type is None:
            raise ValueError("Invalid value for `transaction_type`, must not be `None`")  # noqa: E501

        self._transaction_type = transaction_type

    @property
    def foreign_currency(self):
        """Gets the foreign_currency of this ExchangeVetValue.  # noqa: E501


        :return: The foreign_currency of this ExchangeVetValue.  # noqa: E501
        :rtype: CurrencyCode
        """
        return self._foreign_currency

    @foreign_currency.setter
    def foreign_currency(self, foreign_currency):
        """Sets the foreign_currency of this ExchangeVetValue.


        :param foreign_currency: The foreign_currency of this ExchangeVetValue.  # noqa: E501
        :type: CurrencyCode
        """
        if foreign_currency is None:
            raise ValueError("Invalid value for `foreign_currency`, must not be `None`")  # noqa: E501

        self._foreign_currency = foreign_currency

    @property
    def delivery_foreign_currency(self):
        """Gets the delivery_foreign_currency of this ExchangeVetValue.  # noqa: E501


        :return: The delivery_foreign_currency of this ExchangeVetValue.  # noqa: E501
        :rtype: EnumExchangeDeliveryForeignCurrency
        """
        return self._delivery_foreign_currency

    @delivery_foreign_currency.setter
    def delivery_foreign_currency(self, delivery_foreign_currency):
        """Sets the delivery_foreign_currency of this ExchangeVetValue.


        :param delivery_foreign_currency: The delivery_foreign_currency of this ExchangeVetValue.  # noqa: E501
        :type: EnumExchangeDeliveryForeignCurrency
        """
        if delivery_foreign_currency is None:
            raise ValueError("Invalid value for `delivery_foreign_currency`, must not be `None`")  # noqa: E501

        self._delivery_foreign_currency = delivery_foreign_currency

    @property
    def range_transaction_category(self):
        """Gets the range_transaction_category of this ExchangeVetValue.  # noqa: E501


        :return: The range_transaction_category of this ExchangeVetValue.  # noqa: E501
        :rtype: EnumExchangeRangeTransactionCategory
        """
        return self._range_transaction_category

    @range_transaction_category.setter
    def range_transaction_category(self, range_transaction_category):
        """Sets the range_transaction_category of this ExchangeVetValue.


        :param range_transaction_category: The range_transaction_category of this ExchangeVetValue.  # noqa: E501
        :type: EnumExchangeRangeTransactionCategory
        """
        if range_transaction_category is None:
            raise ValueError("Invalid value for `range_transaction_category`, must not be `None`")  # noqa: E501

        self._range_transaction_category = range_transaction_category

    @property
    def target_audience(self):
        """Gets the target_audience of this ExchangeVetValue.  # noqa: E501


        :return: The target_audience of this ExchangeVetValue.  # noqa: E501
        :rtype: EnumDistinctTargetAudienceExchange
        """
        return self._target_audience

    @target_audience.setter
    def target_audience(self, target_audience):
        """Sets the target_audience of this ExchangeVetValue.


        :param target_audience: The target_audience of this ExchangeVetValue.  # noqa: E501
        :type: EnumDistinctTargetAudienceExchange
        """
        if target_audience is None:
            raise ValueError("Invalid value for `target_audience`, must not be `None`")  # noqa: E501

        self._target_audience = target_audience

    @property
    def vet_amount(self):
        """Gets the vet_amount of this ExchangeVetValue.  # noqa: E501


        :return: The vet_amount of this ExchangeVetValue.  # noqa: E501
        :rtype: ExchangeNoIdentificationFrequencyDistribution
        """
        return self._vet_amount

    @vet_amount.setter
    def vet_amount(self, vet_amount):
        """Sets the vet_amount of this ExchangeVetValue.


        :param vet_amount: The vet_amount of this ExchangeVetValue.  # noqa: E501
        :type: ExchangeNoIdentificationFrequencyDistribution
        """
        if vet_amount is None:
            raise ValueError("Invalid value for `vet_amount`, must not be `None`")  # noqa: E501

        self._vet_amount = vet_amount

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
        if issubclass(ExchangeVetValue, dict):
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
        if not isinstance(other, ExchangeVetValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
