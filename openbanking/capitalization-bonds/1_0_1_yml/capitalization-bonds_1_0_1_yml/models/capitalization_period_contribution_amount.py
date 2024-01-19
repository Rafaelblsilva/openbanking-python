# coding: utf-8

"""
    API Capitalization-bonds - Open Finance Brasil

    As APIs descritas neste documento é referente a API de Capitalização da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CapitalizationPeriodContributionAmount(object):
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
        'periodicity': 'str',
        'periodicity_additional_info': 'str',
        'minimum': 'str',
        'maximum': 'str',
        'allowed_value': 'float'
    }

    attribute_map = {
        'periodicity': 'periodicity',
        'periodicity_additional_info': 'periodicityAdditionalInfo',
        'minimum': 'minimum',
        'maximum': 'maximum',
        'allowed_value': 'allowedValue'
    }

    def __init__(self, periodicity=None, periodicity_additional_info=None, minimum=None, maximum=None, allowed_value=None):  # noqa: E501
        """CapitalizationPeriodContributionAmount - a model defined in Swagger"""  # noqa: E501
        self._periodicity = None
        self._periodicity_additional_info = None
        self._minimum = None
        self._maximum = None
        self._allowed_value = None
        self.discriminator = None
        self.periodicity = periodicity
        if periodicity_additional_info is not None:
            self.periodicity_additional_info = periodicity_additional_info
        self.minimum = minimum
        self.maximum = maximum
        self.allowed_value = allowed_value

    @property
    def periodicity(self):
        """Gets the periodicity of this CapitalizationPeriodContributionAmount.  # noqa: E501

        Intervalo de tempo regular previsto entre os sorteios. Conforme os domínios:   1. Único   2. Diário   3. Semanal   4. Quinzenal   5. Mensal   6. Bimestral   7. Trimestral   8. Quadrimestral   9. Semestral   10. Anual   11. Outros   12. NA   # noqa: E501

        :return: The periodicity of this CapitalizationPeriodContributionAmount.  # noqa: E501
        :rtype: str
        """
        return self._periodicity

    @periodicity.setter
    def periodicity(self, periodicity):
        """Sets the periodicity of this CapitalizationPeriodContributionAmount.

        Intervalo de tempo regular previsto entre os sorteios. Conforme os domínios:   1. Único   2. Diário   3. Semanal   4. Quinzenal   5. Mensal   6. Bimestral   7. Trimestral   8. Quadrimestral   9. Semestral   10. Anual   11. Outros   12. NA   # noqa: E501

        :param periodicity: The periodicity of this CapitalizationPeriodContributionAmount.  # noqa: E501
        :type: str
        """
        if periodicity is None:
            raise ValueError("Invalid value for `periodicity`, must not be `None`")  # noqa: E501
        allowed_values = ["UNICO", "DIARIO", "SEMANAL", "QUINZENAL", "MENSAL", "BIMESTRAL", "TRIMESTRAL", "QUADRIMESTRAL", "SEMESTRAL", "ANUAL", "OUTROS", "NA"]  # noqa: E501
        if periodicity not in allowed_values:
            raise ValueError(
                "Invalid value for `periodicity` ({0}), must be one of {1}"  # noqa: E501
                .format(periodicity, allowed_values)
            )

        self._periodicity = periodicity

    @property
    def periodicity_additional_info(self):
        """Gets the periodicity_additional_info of this CapitalizationPeriodContributionAmount.  # noqa: E501

        Restrição: Campo obrigatório para complementar a informação quando selecionada a opção 'OUTROS'  # noqa: E501

        :return: The periodicity_additional_info of this CapitalizationPeriodContributionAmount.  # noqa: E501
        :rtype: str
        """
        return self._periodicity_additional_info

    @periodicity_additional_info.setter
    def periodicity_additional_info(self, periodicity_additional_info):
        """Sets the periodicity_additional_info of this CapitalizationPeriodContributionAmount.

        Restrição: Campo obrigatório para complementar a informação quando selecionada a opção 'OUTROS'  # noqa: E501

        :param periodicity_additional_info: The periodicity_additional_info of this CapitalizationPeriodContributionAmount.  # noqa: E501
        :type: str
        """

        self._periodicity_additional_info = periodicity_additional_info

    @property
    def minimum(self):
        """Gets the minimum of this CapitalizationPeriodContributionAmount.  # noqa: E501

        Condicional: Quando modalidade for igual 'TRADICIONAL' Valor mínimo correspondente ao pagamento efetuado pelo subscritor à sociedade de capitalização.   # noqa: E501

        :return: The minimum of this CapitalizationPeriodContributionAmount.  # noqa: E501
        :rtype: str
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """Sets the minimum of this CapitalizationPeriodContributionAmount.

        Condicional: Quando modalidade for igual 'TRADICIONAL' Valor mínimo correspondente ao pagamento efetuado pelo subscritor à sociedade de capitalização.   # noqa: E501

        :param minimum: The minimum of this CapitalizationPeriodContributionAmount.  # noqa: E501
        :type: str
        """
        if minimum is None:
            raise ValueError("Invalid value for `minimum`, must not be `None`")  # noqa: E501

        self._minimum = minimum

    @property
    def maximum(self):
        """Gets the maximum of this CapitalizationPeriodContributionAmount.  # noqa: E501

        Condicional: Quando modalidade for igual 'TRADICIONAL' Valor máximo correspondente ao pagamento efetuado pelo subscritor à sociedade de capitalização.   # noqa: E501

        :return: The maximum of this CapitalizationPeriodContributionAmount.  # noqa: E501
        :rtype: str
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """Sets the maximum of this CapitalizationPeriodContributionAmount.

        Condicional: Quando modalidade for igual 'TRADICIONAL' Valor máximo correspondente ao pagamento efetuado pelo subscritor à sociedade de capitalização.   # noqa: E501

        :param maximum: The maximum of this CapitalizationPeriodContributionAmount.  # noqa: E501
        :type: str
        """
        if maximum is None:
            raise ValueError("Invalid value for `maximum`, must not be `None`")  # noqa: E501

        self._maximum = maximum

    @property
    def allowed_value(self):
        """Gets the allowed_value of this CapitalizationPeriodContributionAmount.  # noqa: E501

        Condicional: Quando modalidade for diferente de 'TRADICIONAL' Lista com os valores permitidos de contribuição ao plano.   # noqa: E501

        :return: The allowed_value of this CapitalizationPeriodContributionAmount.  # noqa: E501
        :rtype: float
        """
        return self._allowed_value

    @allowed_value.setter
    def allowed_value(self, allowed_value):
        """Sets the allowed_value of this CapitalizationPeriodContributionAmount.

        Condicional: Quando modalidade for diferente de 'TRADICIONAL' Lista com os valores permitidos de contribuição ao plano.   # noqa: E501

        :param allowed_value: The allowed_value of this CapitalizationPeriodContributionAmount.  # noqa: E501
        :type: float
        """
        if allowed_value is None:
            raise ValueError("Invalid value for `allowed_value`, must not be `None`")  # noqa: E501

        self._allowed_value = allowed_value

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
        if issubclass(CapitalizationPeriodContributionAmount, dict):
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
        if not isinstance(other, CapitalizationPeriodContributionAmount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
