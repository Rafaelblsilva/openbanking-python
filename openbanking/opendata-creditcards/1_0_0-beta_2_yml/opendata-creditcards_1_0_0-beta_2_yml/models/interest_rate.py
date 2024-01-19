# coding: utf-8

"""
    API OpenData Credit Cards do Open Finance Brasil

    A API descrita neste documento é referente as API Credit Cards da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-beta.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InterestRate(object):
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
        'referential_rate_indexer': 'ReferentialRateIndexer',
        'rate': 'str',
        'applications': 'list[ApplicationRate]',
        'minimum_rate': 'str',
        'maximum_rate': 'str'
    }

    attribute_map = {
        'referential_rate_indexer': 'referentialRateIndexer',
        'rate': 'rate',
        'applications': 'applications',
        'minimum_rate': 'minimumRate',
        'maximum_rate': 'maximumRate'
    }

    def __init__(self, referential_rate_indexer=None, rate=None, applications=None, minimum_rate=None, maximum_rate=None):  # noqa: E501
        """InterestRate - a model defined in Swagger"""  # noqa: E501
        self._referential_rate_indexer = None
        self._rate = None
        self._applications = None
        self._minimum_rate = None
        self._maximum_rate = None
        self.discriminator = None
        self.referential_rate_indexer = referential_rate_indexer
        self.rate = rate
        self.applications = applications
        self.minimum_rate = minimum_rate
        self.maximum_rate = maximum_rate

    @property
    def referential_rate_indexer(self):
        """Gets the referential_rate_indexer of this InterestRate.  # noqa: E501


        :return: The referential_rate_indexer of this InterestRate.  # noqa: E501
        :rtype: ReferentialRateIndexer
        """
        return self._referential_rate_indexer

    @referential_rate_indexer.setter
    def referential_rate_indexer(self, referential_rate_indexer):
        """Sets the referential_rate_indexer of this InterestRate.


        :param referential_rate_indexer: The referential_rate_indexer of this InterestRate.  # noqa: E501
        :type: ReferentialRateIndexer
        """
        if referential_rate_indexer is None:
            raise ValueError("Invalid value for `referential_rate_indexer`, must not be `None`")  # noqa: E501

        self._referential_rate_indexer = referential_rate_indexer

    @property
    def rate(self):
        """Gets the rate of this InterestRate.  # noqa: E501

        Percentual que incide sobre a composição das taxas de juros remuneratórios. (representa uma porcentagem Ex: 0.15 (O valor ao lado representa 15%. O valor '1 'representa 100%). A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)   # noqa: E501

        :return: The rate of this InterestRate.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this InterestRate.

        Percentual que incide sobre a composição das taxas de juros remuneratórios. (representa uma porcentagem Ex: 0.15 (O valor ao lado representa 15%. O valor '1 'representa 100%). A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)   # noqa: E501

        :param rate: The rate of this InterestRate.  # noqa: E501
        :type: str
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

    @property
    def applications(self):
        """Gets the applications of this InterestRate.  # noqa: E501

        Lista distribuição percentuais relativos à taxa de juros remuneratórios  # noqa: E501

        :return: The applications of this InterestRate.  # noqa: E501
        :rtype: list[ApplicationRate]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this InterestRate.

        Lista distribuição percentuais relativos à taxa de juros remuneratórios  # noqa: E501

        :param applications: The applications of this InterestRate.  # noqa: E501
        :type: list[ApplicationRate]
        """
        if applications is None:
            raise ValueError("Invalid value for `applications`, must not be `None`")  # noqa: E501

        self._applications = applications

    @property
    def minimum_rate(self):
        """Gets the minimum_rate of this InterestRate.  # noqa: E501

        Percentual mínimo cobrado (taxa efetiva) no mês de referência, para o Financiamento contratado  A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  # noqa: E501

        :return: The minimum_rate of this InterestRate.  # noqa: E501
        :rtype: str
        """
        return self._minimum_rate

    @minimum_rate.setter
    def minimum_rate(self, minimum_rate):
        """Sets the minimum_rate of this InterestRate.

        Percentual mínimo cobrado (taxa efetiva) no mês de referência, para o Financiamento contratado  A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  # noqa: E501

        :param minimum_rate: The minimum_rate of this InterestRate.  # noqa: E501
        :type: str
        """
        if minimum_rate is None:
            raise ValueError("Invalid value for `minimum_rate`, must not be `None`")  # noqa: E501

        self._minimum_rate = minimum_rate

    @property
    def maximum_rate(self):
        """Gets the maximum_rate of this InterestRate.  # noqa: E501

        Percentual máximo cobrado (taxa efetiva) no mês de referência, para o Financiamento contratado  A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  # noqa: E501

        :return: The maximum_rate of this InterestRate.  # noqa: E501
        :rtype: str
        """
        return self._maximum_rate

    @maximum_rate.setter
    def maximum_rate(self, maximum_rate):
        """Sets the maximum_rate of this InterestRate.

        Percentual máximo cobrado (taxa efetiva) no mês de referência, para o Financiamento contratado  A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)  # noqa: E501

        :param maximum_rate: The maximum_rate of this InterestRate.  # noqa: E501
        :type: str
        """
        if maximum_rate is None:
            raise ValueError("Invalid value for `maximum_rate`, must not be `None`")  # noqa: E501

        self._maximum_rate = maximum_rate

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
        if issubclass(InterestRate, dict):
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
        if not isinstance(other, InterestRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
