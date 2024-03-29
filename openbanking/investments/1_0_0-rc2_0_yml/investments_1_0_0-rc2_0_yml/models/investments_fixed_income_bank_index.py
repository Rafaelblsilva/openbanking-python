# coding: utf-8

"""
    API Investments - Open Finance Brasil

    Estas APIs visam o compartilhamento de dados sobre Investimentos e suas características entre as Instituições Financeiras participantes do Open Finance Brasil   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InvestmentsFixedIncomeBankIndex(object):
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
        'indexer': 'EnumInvestmentsFixedIncomeBankIndexer',
        'indexer_additional_info': 'str',
        'issue_remuneration_rate': 'InvestmentsNoIdentificationFrequencyDistribution'
    }

    attribute_map = {
        'indexer': 'indexer',
        'indexer_additional_info': 'indexerAdditionalInfo',
        'issue_remuneration_rate': 'issueRemunerationRate'
    }

    def __init__(self, indexer=None, indexer_additional_info=None, issue_remuneration_rate=None):  # noqa: E501
        """InvestmentsFixedIncomeBankIndex - a model defined in Swagger"""  # noqa: E501
        self._indexer = None
        self._indexer_additional_info = None
        self._issue_remuneration_rate = None
        self.discriminator = None
        self.indexer = indexer
        if indexer_additional_info is not None:
            self.indexer_additional_info = indexer_additional_info
        self.issue_remuneration_rate = issue_remuneration_rate

    @property
    def indexer(self):
        """Gets the indexer of this InvestmentsFixedIncomeBankIndex.  # noqa: E501


        :return: The indexer of this InvestmentsFixedIncomeBankIndex.  # noqa: E501
        :rtype: EnumInvestmentsFixedIncomeBankIndexer
        """
        return self._indexer

    @indexer.setter
    def indexer(self, indexer):
        """Sets the indexer of this InvestmentsFixedIncomeBankIndex.


        :param indexer: The indexer of this InvestmentsFixedIncomeBankIndex.  # noqa: E501
        :type: EnumInvestmentsFixedIncomeBankIndexer
        """
        if indexer is None:
            raise ValueError("Invalid value for `indexer`, must not be `None`")  # noqa: E501

        self._indexer = indexer

    @property
    def indexer_additional_info(self):
        """Gets the indexer_additional_info of this InvestmentsFixedIncomeBankIndex.  # noqa: E501

        Campo livre para preenchimento das informações adicionais referente ao encargo.  [Restrição] Obrigatório quando \"indexer\" for igual 'OUTROS'.   # noqa: E501

        :return: The indexer_additional_info of this InvestmentsFixedIncomeBankIndex.  # noqa: E501
        :rtype: str
        """
        return self._indexer_additional_info

    @indexer_additional_info.setter
    def indexer_additional_info(self, indexer_additional_info):
        """Sets the indexer_additional_info of this InvestmentsFixedIncomeBankIndex.

        Campo livre para preenchimento das informações adicionais referente ao encargo.  [Restrição] Obrigatório quando \"indexer\" for igual 'OUTROS'.   # noqa: E501

        :param indexer_additional_info: The indexer_additional_info of this InvestmentsFixedIncomeBankIndex.  # noqa: E501
        :type: str
        """

        self._indexer_additional_info = indexer_additional_info

    @property
    def issue_remuneration_rate(self):
        """Gets the issue_remuneration_rate of this InvestmentsFixedIncomeBankIndex.  # noqa: E501


        :return: The issue_remuneration_rate of this InvestmentsFixedIncomeBankIndex.  # noqa: E501
        :rtype: InvestmentsNoIdentificationFrequencyDistribution
        """
        return self._issue_remuneration_rate

    @issue_remuneration_rate.setter
    def issue_remuneration_rate(self, issue_remuneration_rate):
        """Sets the issue_remuneration_rate of this InvestmentsFixedIncomeBankIndex.


        :param issue_remuneration_rate: The issue_remuneration_rate of this InvestmentsFixedIncomeBankIndex.  # noqa: E501
        :type: InvestmentsNoIdentificationFrequencyDistribution
        """
        if issue_remuneration_rate is None:
            raise ValueError("Invalid value for `issue_remuneration_rate`, must not be `None`")  # noqa: E501

        self._issue_remuneration_rate = issue_remuneration_rate

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
        if issubclass(InvestmentsFixedIncomeBankIndex, dict):
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
        if not isinstance(other, InvestmentsFixedIncomeBankIndex):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
