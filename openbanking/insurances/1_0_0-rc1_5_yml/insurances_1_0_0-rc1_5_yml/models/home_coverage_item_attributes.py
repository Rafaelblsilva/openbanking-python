# coding: utf-8

"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.5
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class HomeCoverageItemAttributes(object):
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
        'min_lmi': 'CoverageItemAttributesMinLMI',
        'max_lmi': 'CoverageItemAttributesMaxLMI',
        'min_deductible_amount': 'HomeMinDeductibleAmount',
        'insured_mandatory_participation_percentage': 'str'
    }

    attribute_map = {
        'min_lmi': 'minLMI',
        'max_lmi': 'maxLMI',
        'min_deductible_amount': 'minDeductibleAmount',
        'insured_mandatory_participation_percentage': 'insuredMandatoryParticipationPercentage'
    }

    def __init__(self, min_lmi=None, max_lmi=None, min_deductible_amount=None, insured_mandatory_participation_percentage=None):  # noqa: E501
        """HomeCoverageItemAttributes - a model defined in Swagger"""  # noqa: E501
        self._min_lmi = None
        self._max_lmi = None
        self._min_deductible_amount = None
        self._insured_mandatory_participation_percentage = None
        self.discriminator = None
        if min_lmi is not None:
            self.min_lmi = min_lmi
        if max_lmi is not None:
            self.max_lmi = max_lmi
        if min_deductible_amount is not None:
            self.min_deductible_amount = min_deductible_amount
        if insured_mandatory_participation_percentage is not None:
            self.insured_mandatory_participation_percentage = insured_mandatory_participation_percentage

    @property
    def min_lmi(self):
        """Gets the min_lmi of this HomeCoverageItemAttributes.  # noqa: E501


        :return: The min_lmi of this HomeCoverageItemAttributes.  # noqa: E501
        :rtype: CoverageItemAttributesMinLMI
        """
        return self._min_lmi

    @min_lmi.setter
    def min_lmi(self, min_lmi):
        """Sets the min_lmi of this HomeCoverageItemAttributes.


        :param min_lmi: The min_lmi of this HomeCoverageItemAttributes.  # noqa: E501
        :type: CoverageItemAttributesMinLMI
        """

        self._min_lmi = min_lmi

    @property
    def max_lmi(self):
        """Gets the max_lmi of this HomeCoverageItemAttributes.  # noqa: E501


        :return: The max_lmi of this HomeCoverageItemAttributes.  # noqa: E501
        :rtype: CoverageItemAttributesMaxLMI
        """
        return self._max_lmi

    @max_lmi.setter
    def max_lmi(self, max_lmi):
        """Sets the max_lmi of this HomeCoverageItemAttributes.


        :param max_lmi: The max_lmi of this HomeCoverageItemAttributes.  # noqa: E501
        :type: CoverageItemAttributesMaxLMI
        """

        self._max_lmi = max_lmi

    @property
    def min_deductible_amount(self):
        """Gets the min_deductible_amount of this HomeCoverageItemAttributes.  # noqa: E501


        :return: The min_deductible_amount of this HomeCoverageItemAttributes.  # noqa: E501
        :rtype: HomeMinDeductibleAmount
        """
        return self._min_deductible_amount

    @min_deductible_amount.setter
    def min_deductible_amount(self, min_deductible_amount):
        """Sets the min_deductible_amount of this HomeCoverageItemAttributes.


        :param min_deductible_amount: The min_deductible_amount of this HomeCoverageItemAttributes.  # noqa: E501
        :type: HomeMinDeductibleAmount
        """

        self._min_deductible_amount = min_deductible_amount

    @property
    def insured_mandatory_participation_percentage(self):
        """Gets the insured_mandatory_participation_percentage of this HomeCoverageItemAttributes.  # noqa: E501

        Participação Obrigatória é o valor ou percentual definido na apólice referente à responsabilidade do Segurado nos prejuízos indenizáveis decorrentes de sinistros cobertos. (Circular SUSEP 347/07). Listagem de percentual de franquia e/ou Percentual Participação Obrigatória do Segurado estabelecida pela sociedade para cada tipo de cobertura do produto. Observação: Sugestão de Criação do campo em substituição ao campo abaixo ‘Valor Máximo de Franquia’.  # noqa: E501

        :return: The insured_mandatory_participation_percentage of this HomeCoverageItemAttributes.  # noqa: E501
        :rtype: str
        """
        return self._insured_mandatory_participation_percentage

    @insured_mandatory_participation_percentage.setter
    def insured_mandatory_participation_percentage(self, insured_mandatory_participation_percentage):
        """Sets the insured_mandatory_participation_percentage of this HomeCoverageItemAttributes.

        Participação Obrigatória é o valor ou percentual definido na apólice referente à responsabilidade do Segurado nos prejuízos indenizáveis decorrentes de sinistros cobertos. (Circular SUSEP 347/07). Listagem de percentual de franquia e/ou Percentual Participação Obrigatória do Segurado estabelecida pela sociedade para cada tipo de cobertura do produto. Observação: Sugestão de Criação do campo em substituição ao campo abaixo ‘Valor Máximo de Franquia’.  # noqa: E501

        :param insured_mandatory_participation_percentage: The insured_mandatory_participation_percentage of this HomeCoverageItemAttributes.  # noqa: E501
        :type: str
        """

        self._insured_mandatory_participation_percentage = insured_mandatory_participation_percentage

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
        if issubclass(HomeCoverageItemAttributes, dict):
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
        if not isinstance(other, HomeCoverageItemAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
