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

class FeeReferentialRateIndexer(object):
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
        'rate': 'str'
    }

    attribute_map = {
        'referential_rate_indexer': 'referentialRateIndexer',
        'rate': 'rate'
    }

    def __init__(self, referential_rate_indexer=None, rate=None):  # noqa: E501
        """FeeReferentialRateIndexer - a model defined in Swagger"""  # noqa: E501
        self._referential_rate_indexer = None
        self._rate = None
        self.discriminator = None
        self.referential_rate_indexer = referential_rate_indexer
        self.rate = rate

    @property
    def referential_rate_indexer(self):
        """Gets the referential_rate_indexer of this FeeReferentialRateIndexer.  # noqa: E501


        :return: The referential_rate_indexer of this FeeReferentialRateIndexer.  # noqa: E501
        :rtype: ReferentialRateIndexer
        """
        return self._referential_rate_indexer

    @referential_rate_indexer.setter
    def referential_rate_indexer(self, referential_rate_indexer):
        """Sets the referential_rate_indexer of this FeeReferentialRateIndexer.


        :param referential_rate_indexer: The referential_rate_indexer of this FeeReferentialRateIndexer.  # noqa: E501
        :type: ReferentialRateIndexer
        """
        if referential_rate_indexer is None:
            raise ValueError("Invalid value for `referential_rate_indexer`, must not be `None`")  # noqa: E501

        self._referential_rate_indexer = referential_rate_indexer

    @property
    def rate(self):
        """Gets the rate of this FeeReferentialRateIndexer.  # noqa: E501

        Percentual que incide sobre a composição das taxas de juros remuneratórios. (representa uma porcentagem Ex: 0.15 (O valor ao lado representa 15%. O valor '1 'representa 100%). A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)   # noqa: E501

        :return: The rate of this FeeReferentialRateIndexer.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this FeeReferentialRateIndexer.

        Percentual que incide sobre a composição das taxas de juros remuneratórios. (representa uma porcentagem Ex: 0.15 (O valor ao lado representa 15%. O valor '1 'representa 100%). A apuração pode acontecer com até 4 casas decimais. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)   # noqa: E501

        :param rate: The rate of this FeeReferentialRateIndexer.  # noqa: E501
        :type: str
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

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
        if issubclass(FeeReferentialRateIndexer, dict):
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
        if not isinstance(other, FeeReferentialRateIndexer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
