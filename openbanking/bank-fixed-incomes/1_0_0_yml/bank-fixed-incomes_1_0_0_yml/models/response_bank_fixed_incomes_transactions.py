# coding: utf-8

"""
    API Bank Fixed Incomes - Open Finance Brasil

    API de informações de operações de Renda Fixa Bancária Open Finance Brasil (Fase 4). API que retorna informações de operações de investimento do tipo Renda Fixa Bancária (CDB/RDB, LCI e LCA) mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação do produto, rentabilidade, quantidade, prazos, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. A exposição se dará por cada operação de renda fixa contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseBankFixedIncomesTransactions(object):
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
        'data': 'list[BankFixedIncomesProductMovement]',
        'links': 'BankFixedIncomeLinks',
        'meta': 'BankFixedIncomesTransactionsMeta'
    }

    attribute_map = {
        'data': 'data',
        'links': 'links',
        'meta': 'meta'
    }

    def __init__(self, data=None, links=None, meta=None):  # noqa: E501
        """ResponseBankFixedIncomesTransactions - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._links = None
        self._meta = None
        self.discriminator = None
        self.data = data
        self.links = links
        self.meta = meta

    @property
    def data(self):
        """Gets the data of this ResponseBankFixedIncomesTransactions.  # noqa: E501


        :return: The data of this ResponseBankFixedIncomesTransactions.  # noqa: E501
        :rtype: list[BankFixedIncomesProductMovement]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ResponseBankFixedIncomesTransactions.


        :param data: The data of this ResponseBankFixedIncomesTransactions.  # noqa: E501
        :type: list[BankFixedIncomesProductMovement]
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def links(self):
        """Gets the links of this ResponseBankFixedIncomesTransactions.  # noqa: E501


        :return: The links of this ResponseBankFixedIncomesTransactions.  # noqa: E501
        :rtype: BankFixedIncomeLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ResponseBankFixedIncomesTransactions.


        :param links: The links of this ResponseBankFixedIncomesTransactions.  # noqa: E501
        :type: BankFixedIncomeLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def meta(self):
        """Gets the meta of this ResponseBankFixedIncomesTransactions.  # noqa: E501


        :return: The meta of this ResponseBankFixedIncomesTransactions.  # noqa: E501
        :rtype: BankFixedIncomesTransactionsMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ResponseBankFixedIncomesTransactions.


        :param meta: The meta of this ResponseBankFixedIncomesTransactions.  # noqa: E501
        :type: BankFixedIncomesTransactionsMeta
        """
        if meta is None:
            raise ValueError("Invalid value for `meta`, must not be `None`")  # noqa: E501

        self._meta = meta

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
        if issubclass(ResponseBankFixedIncomesTransactions, dict):
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
        if not isinstance(other, ResponseBankFixedIncomesTransactions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
