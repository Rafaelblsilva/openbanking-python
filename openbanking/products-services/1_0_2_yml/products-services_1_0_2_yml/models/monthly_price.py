# coding: utf-8

"""
    API's OpenData do Open Finance Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MonthlyPrice(object):
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
        'interval': 'PriceIntervals',
        'monthly_fee': 'str',
        'currency': 'Currency',
        'customers': 'Customer'
    }

    attribute_map = {
        'interval': 'interval',
        'monthly_fee': 'monthlyFee',
        'currency': 'currency',
        'customers': 'customers'
    }

    def __init__(self, interval=None, monthly_fee=None, currency=None, customers=None):  # noqa: E501
        """MonthlyPrice - a model defined in Swagger"""  # noqa: E501
        self._interval = None
        self._monthly_fee = None
        self._currency = None
        self._customers = None
        self.discriminator = None
        self.interval = interval
        self.monthly_fee = monthly_fee
        self.currency = currency
        self.customers = customers

    @property
    def interval(self):
        """Gets the interval of this MonthlyPrice.  # noqa: E501


        :return: The interval of this MonthlyPrice.  # noqa: E501
        :rtype: PriceIntervals
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this MonthlyPrice.


        :param interval: The interval of this MonthlyPrice.  # noqa: E501
        :type: PriceIntervals
        """
        if interval is None:
            raise ValueError("Invalid value for `interval`, must not be `None`")  # noqa: E501

        self._interval = interval

    @property
    def monthly_fee(self):
        """Gets the monthly_fee of this MonthlyPrice.  # noqa: E501

        Valor da mediana de cada faixa relativa ao serviço ofertado, informado no período, conforme Res nº 32 BCB, 2020. p.ex. ''45.00'' (representa um valor monetário. p.ex: 1547368.92. Este valor, considerando que a moeda seja BRL, significa R$ 1.547.368,92. O único separador presente deve ser o ''.'' (ponto) para indicar a casa decimal. Não deve haver separador de milhar)   # noqa: E501

        :return: The monthly_fee of this MonthlyPrice.  # noqa: E501
        :rtype: str
        """
        return self._monthly_fee

    @monthly_fee.setter
    def monthly_fee(self, monthly_fee):
        """Sets the monthly_fee of this MonthlyPrice.

        Valor da mediana de cada faixa relativa ao serviço ofertado, informado no período, conforme Res nº 32 BCB, 2020. p.ex. ''45.00'' (representa um valor monetário. p.ex: 1547368.92. Este valor, considerando que a moeda seja BRL, significa R$ 1.547.368,92. O único separador presente deve ser o ''.'' (ponto) para indicar a casa decimal. Não deve haver separador de milhar)   # noqa: E501

        :param monthly_fee: The monthly_fee of this MonthlyPrice.  # noqa: E501
        :type: str
        """
        if monthly_fee is None:
            raise ValueError("Invalid value for `monthly_fee`, must not be `None`")  # noqa: E501

        self._monthly_fee = monthly_fee

    @property
    def currency(self):
        """Gets the currency of this MonthlyPrice.  # noqa: E501


        :return: The currency of this MonthlyPrice.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this MonthlyPrice.


        :param currency: The currency of this MonthlyPrice.  # noqa: E501
        :type: Currency
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def customers(self):
        """Gets the customers of this MonthlyPrice.  # noqa: E501


        :return: The customers of this MonthlyPrice.  # noqa: E501
        :rtype: Customer
        """
        return self._customers

    @customers.setter
    def customers(self, customers):
        """Sets the customers of this MonthlyPrice.


        :param customers: The customers of this MonthlyPrice.  # noqa: E501
        :type: Customer
        """
        if customers is None:
            raise ValueError("Invalid value for `customers`, must not be `None`")  # noqa: E501

        self._customers = customers

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
        if issubclass(MonthlyPrice, dict):
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
        if not isinstance(other, MonthlyPrice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
