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

class Remuneration(object):
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
        'pre_fixed_rate': 'str',
        'post_fixed_indexer_percentage': 'str',
        'rate_type': 'EnumRateType',
        'rate_periodicity': 'EnumRatePeriodicity',
        'calculation': 'EnumCalculation',
        'indexer': 'EnumBankFixedIncomeIndexer',
        'indexer_additional_info': 'str'
    }

    attribute_map = {
        'pre_fixed_rate': 'preFixedRate',
        'post_fixed_indexer_percentage': 'postFixedIndexerPercentage',
        'rate_type': 'rateType',
        'rate_periodicity': 'ratePeriodicity',
        'calculation': 'calculation',
        'indexer': 'indexer',
        'indexer_additional_info': 'indexerAdditionalInfo'
    }

    def __init__(self, pre_fixed_rate=None, post_fixed_indexer_percentage=None, rate_type=None, rate_periodicity=None, calculation=None, indexer=None, indexer_additional_info=None):  # noqa: E501
        """Remuneration - a model defined in Swagger"""  # noqa: E501
        self._pre_fixed_rate = None
        self._post_fixed_indexer_percentage = None
        self._rate_type = None
        self._rate_periodicity = None
        self._calculation = None
        self._indexer = None
        self._indexer_additional_info = None
        self.discriminator = None
        if pre_fixed_rate is not None:
            self.pre_fixed_rate = pre_fixed_rate
        if post_fixed_indexer_percentage is not None:
            self.post_fixed_indexer_percentage = post_fixed_indexer_percentage
        self.rate_type = rate_type
        self.rate_periodicity = rate_periodicity
        self.calculation = calculation
        self.indexer = indexer
        if indexer_additional_info is not None:
            self.indexer_additional_info = indexer_additional_info

    @property
    def pre_fixed_rate(self):
        """Gets the pre_fixed_rate of this Remuneration.  # noqa: E501

        Taxa de remuneração pré fixada de emissão do título.  p.ex. 0.014500.  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%).    [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver 'PRE_FIXADO' no campo 'indexer' ou quando se tratar de produto com remuneração híbrida.   # noqa: E501

        :return: The pre_fixed_rate of this Remuneration.  # noqa: E501
        :rtype: str
        """
        return self._pre_fixed_rate

    @pre_fixed_rate.setter
    def pre_fixed_rate(self, pre_fixed_rate):
        """Sets the pre_fixed_rate of this Remuneration.

        Taxa de remuneração pré fixada de emissão do título.  p.ex. 0.014500.  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%).    [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver 'PRE_FIXADO' no campo 'indexer' ou quando se tratar de produto com remuneração híbrida.   # noqa: E501

        :param pre_fixed_rate: The pre_fixed_rate of this Remuneration.  # noqa: E501
        :type: str
        """

        self._pre_fixed_rate = pre_fixed_rate

    @property
    def post_fixed_indexer_percentage(self):
        """Gets the post_fixed_indexer_percentage of this Remuneration.  # noqa: E501

        Percentual do indexador pós fixado de emissão do  título.  p.ex. 0.014500.  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%).  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo 'indexer' for preenchido de forma diferente de 'PRE_FIXADO' ou quando se tratar de produto com remuneração híbrida.   # noqa: E501

        :return: The post_fixed_indexer_percentage of this Remuneration.  # noqa: E501
        :rtype: str
        """
        return self._post_fixed_indexer_percentage

    @post_fixed_indexer_percentage.setter
    def post_fixed_indexer_percentage(self, post_fixed_indexer_percentage):
        """Sets the post_fixed_indexer_percentage of this Remuneration.

        Percentual do indexador pós fixado de emissão do  título.  p.ex. 0.014500.  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%).  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo 'indexer' for preenchido de forma diferente de 'PRE_FIXADO' ou quando se tratar de produto com remuneração híbrida.   # noqa: E501

        :param post_fixed_indexer_percentage: The post_fixed_indexer_percentage of this Remuneration.  # noqa: E501
        :type: str
        """

        self._post_fixed_indexer_percentage = post_fixed_indexer_percentage

    @property
    def rate_type(self):
        """Gets the rate_type of this Remuneration.  # noqa: E501


        :return: The rate_type of this Remuneration.  # noqa: E501
        :rtype: EnumRateType
        """
        return self._rate_type

    @rate_type.setter
    def rate_type(self, rate_type):
        """Sets the rate_type of this Remuneration.


        :param rate_type: The rate_type of this Remuneration.  # noqa: E501
        :type: EnumRateType
        """
        if rate_type is None:
            raise ValueError("Invalid value for `rate_type`, must not be `None`")  # noqa: E501

        self._rate_type = rate_type

    @property
    def rate_periodicity(self):
        """Gets the rate_periodicity of this Remuneration.  # noqa: E501


        :return: The rate_periodicity of this Remuneration.  # noqa: E501
        :rtype: EnumRatePeriodicity
        """
        return self._rate_periodicity

    @rate_periodicity.setter
    def rate_periodicity(self, rate_periodicity):
        """Sets the rate_periodicity of this Remuneration.


        :param rate_periodicity: The rate_periodicity of this Remuneration.  # noqa: E501
        :type: EnumRatePeriodicity
        """
        if rate_periodicity is None:
            raise ValueError("Invalid value for `rate_periodicity`, must not be `None`")  # noqa: E501

        self._rate_periodicity = rate_periodicity

    @property
    def calculation(self):
        """Gets the calculation of this Remuneration.  # noqa: E501


        :return: The calculation of this Remuneration.  # noqa: E501
        :rtype: EnumCalculation
        """
        return self._calculation

    @calculation.setter
    def calculation(self, calculation):
        """Sets the calculation of this Remuneration.


        :param calculation: The calculation of this Remuneration.  # noqa: E501
        :type: EnumCalculation
        """
        if calculation is None:
            raise ValueError("Invalid value for `calculation`, must not be `None`")  # noqa: E501

        self._calculation = calculation

    @property
    def indexer(self):
        """Gets the indexer of this Remuneration.  # noqa: E501


        :return: The indexer of this Remuneration.  # noqa: E501
        :rtype: EnumBankFixedIncomeIndexer
        """
        return self._indexer

    @indexer.setter
    def indexer(self, indexer):
        """Sets the indexer of this Remuneration.


        :param indexer: The indexer of this Remuneration.  # noqa: E501
        :type: EnumBankFixedIncomeIndexer
        """
        if indexer is None:
            raise ValueError("Invalid value for `indexer`, must not be `None`")  # noqa: E501

        self._indexer = indexer

    @property
    def indexer_additional_info(self):
        """Gets the indexer_additional_info of this Remuneration.  # noqa: E501

        Informações adicionais do indexador  [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver 'Outros' no campo 'indexer'.   # noqa: E501

        :return: The indexer_additional_info of this Remuneration.  # noqa: E501
        :rtype: str
        """
        return self._indexer_additional_info

    @indexer_additional_info.setter
    def indexer_additional_info(self, indexer_additional_info):
        """Sets the indexer_additional_info of this Remuneration.

        Informações adicionais do indexador  [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver 'Outros' no campo 'indexer'.   # noqa: E501

        :param indexer_additional_info: The indexer_additional_info of this Remuneration.  # noqa: E501
        :type: str
        """

        self._indexer_additional_info = indexer_additional_info

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
        if issubclass(Remuneration, dict):
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
        if not isinstance(other, Remuneration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
