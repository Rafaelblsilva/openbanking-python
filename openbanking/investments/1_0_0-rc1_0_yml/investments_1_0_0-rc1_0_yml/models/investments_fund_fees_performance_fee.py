# coding: utf-8

"""
    API Investments - Open Finance Brasil

    Estas APIs visam o compartilhamento de dados sobre Investimentos e suas características entre as Instituições Financeiras participantes do Open Finance Brasil   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InvestmentsFundFeesPerformanceFee(object):
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
        'method': 'EnumInvestmentsFundFeesPerformanceFeeMethod',
        'benchmark': 'EnumInvestmentsFundFeesPerformanceFeeBenchmark',
        'benchmark_additional_info': 'str',
        'amount': 'str'
    }

    attribute_map = {
        'method': 'method',
        'benchmark': 'benchmark',
        'benchmark_additional_info': 'benchmarkAdditionalInfo',
        'amount': 'amount'
    }

    def __init__(self, method=None, benchmark=None, benchmark_additional_info=None, amount=None):  # noqa: E501
        """InvestmentsFundFeesPerformanceFee - a model defined in Swagger"""  # noqa: E501
        self._method = None
        self._benchmark = None
        self._benchmark_additional_info = None
        self._amount = None
        self.discriminator = None
        if method is not None:
            self.method = method
        if benchmark is not None:
            self.benchmark = benchmark
        if benchmark_additional_info is not None:
            self.benchmark_additional_info = benchmark_additional_info
        if amount is not None:
            self.amount = amount

    @property
    def method(self):
        """Gets the method of this InvestmentsFundFeesPerformanceFee.  # noqa: E501


        :return: The method of this InvestmentsFundFeesPerformanceFee.  # noqa: E501
        :rtype: EnumInvestmentsFundFeesPerformanceFeeMethod
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this InvestmentsFundFeesPerformanceFee.


        :param method: The method of this InvestmentsFundFeesPerformanceFee.  # noqa: E501
        :type: EnumInvestmentsFundFeesPerformanceFeeMethod
        """

        self._method = method

    @property
    def benchmark(self):
        """Gets the benchmark of this InvestmentsFundFeesPerformanceFee.  # noqa: E501


        :return: The benchmark of this InvestmentsFundFeesPerformanceFee.  # noqa: E501
        :rtype: EnumInvestmentsFundFeesPerformanceFeeBenchmark
        """
        return self._benchmark

    @benchmark.setter
    def benchmark(self, benchmark):
        """Sets the benchmark of this InvestmentsFundFeesPerformanceFee.


        :param benchmark: The benchmark of this InvestmentsFundFeesPerformanceFee.  # noqa: E501
        :type: EnumInvestmentsFundFeesPerformanceFeeBenchmark
        """

        self._benchmark = benchmark

    @property
    def benchmark_additional_info(self):
        """Gets the benchmark_additional_info of this InvestmentsFundFeesPerformanceFee.  # noqa: E501

        Campo a ser preenchido pelas participantes quando houver ‘Outros’ no campo ‘Taxa de Performance - Benchmark’.  # noqa: E501

        :return: The benchmark_additional_info of this InvestmentsFundFeesPerformanceFee.  # noqa: E501
        :rtype: str
        """
        return self._benchmark_additional_info

    @benchmark_additional_info.setter
    def benchmark_additional_info(self, benchmark_additional_info):
        """Sets the benchmark_additional_info of this InvestmentsFundFeesPerformanceFee.

        Campo a ser preenchido pelas participantes quando houver ‘Outros’ no campo ‘Taxa de Performance - Benchmark’.  # noqa: E501

        :param benchmark_additional_info: The benchmark_additional_info of this InvestmentsFundFeesPerformanceFee.  # noqa: E501
        :type: str
        """

        self._benchmark_additional_info = benchmark_additional_info

    @property
    def amount(self):
        """Gets the amount of this InvestmentsFundFeesPerformanceFee.  # noqa: E501

        Taxa cobrada do fundo em função de resultado conforme regras dispostas no regulamento do fundo.  # noqa: E501

        :return: The amount of this InvestmentsFundFeesPerformanceFee.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InvestmentsFundFeesPerformanceFee.

        Taxa cobrada do fundo em função de resultado conforme regras dispostas no regulamento do fundo.  # noqa: E501

        :param amount: The amount of this InvestmentsFundFeesPerformanceFee.  # noqa: E501
        :type: str
        """

        self._amount = amount

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
        if issubclass(InvestmentsFundFeesPerformanceFee, dict):
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
        if not isinstance(other, InvestmentsFundFeesPerformanceFee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
