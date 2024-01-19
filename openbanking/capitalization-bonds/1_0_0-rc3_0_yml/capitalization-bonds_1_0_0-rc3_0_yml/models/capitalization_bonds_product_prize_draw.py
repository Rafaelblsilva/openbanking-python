# coding: utf-8

"""
    API Capitalization-bonds - Open Finance Brasil

    As APIs descritas neste documento é referente a API de Capitalização da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc3.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CapitalizationBondsProductPrizeDraw(object):
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
        'time_interval': 'str',
        'time_interval_additional_info': 'str',
        'quantity': 'float',
        'prize_multiplier': 'float',
        'early_settlement_raffle': 'bool',
        'mandatory_contemplation': 'bool',
        'rule_description': 'str',
        'minimum_contemplation_probability': 'str'
    }

    attribute_map = {
        'time_interval': 'timeInterval',
        'time_interval_additional_info': 'timeIntervalAdditionalInfo',
        'quantity': 'quantity',
        'prize_multiplier': 'prizeMultiplier',
        'early_settlement_raffle': 'earlySettlementRaffle',
        'mandatory_contemplation': 'mandatoryContemplation',
        'rule_description': 'ruleDescription',
        'minimum_contemplation_probability': 'minimumContemplationProbability'
    }

    def __init__(self, time_interval=None, time_interval_additional_info=None, quantity=None, prize_multiplier=None, early_settlement_raffle=None, mandatory_contemplation=None, rule_description=None, minimum_contemplation_probability=None):  # noqa: E501
        """CapitalizationBondsProductPrizeDraw - a model defined in Swagger"""  # noqa: E501
        self._time_interval = None
        self._time_interval_additional_info = None
        self._quantity = None
        self._prize_multiplier = None
        self._early_settlement_raffle = None
        self._mandatory_contemplation = None
        self._rule_description = None
        self._minimum_contemplation_probability = None
        self.discriminator = None
        self.time_interval = time_interval
        if time_interval_additional_info is not None:
            self.time_interval_additional_info = time_interval_additional_info
        self.quantity = quantity
        self.prize_multiplier = prize_multiplier
        if early_settlement_raffle is not None:
            self.early_settlement_raffle = early_settlement_raffle
        if mandatory_contemplation is not None:
            self.mandatory_contemplation = mandatory_contemplation
        if rule_description is not None:
            self.rule_description = rule_description
        self.minimum_contemplation_probability = minimum_contemplation_probability

    @property
    def time_interval(self):
        """Gets the time_interval of this CapitalizationBondsProductPrizeDraw.  # noqa: E501

        Intervalo de tempo regular previsto entre os sorteios. Conforme os domínios:   - UNICO   - DIÁRIO   - SEMANAL   - QUINZENAL   - MENSAL   - BIMESTRAL   - TRIMESTRAL   - QUADRIMESTRAL   - SEMESTRAL   - ANUAL   - OUTROS   - NA   # noqa: E501

        :return: The time_interval of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :rtype: str
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this CapitalizationBondsProductPrizeDraw.

        Intervalo de tempo regular previsto entre os sorteios. Conforme os domínios:   - UNICO   - DIÁRIO   - SEMANAL   - QUINZENAL   - MENSAL   - BIMESTRAL   - TRIMESTRAL   - QUADRIMESTRAL   - SEMESTRAL   - ANUAL   - OUTROS   - NA   # noqa: E501

        :param time_interval: The time_interval of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :type: str
        """
        if time_interval is None:
            raise ValueError("Invalid value for `time_interval`, must not be `None`")  # noqa: E501
        allowed_values = ["UNICO", "DIÁRIO", "SEMANAL", "QUINZENAL", "MENSAL", "BIMESTRAL", "TRIMESTRAL", "QUADRIMESTRAL", "SEMESTRAL", "ANUAL", "OUTROS", "NA"]  # noqa: E501
        if time_interval not in allowed_values:
            raise ValueError(
                "Invalid value for `time_interval` ({0}), must be one of {1}"  # noqa: E501
                .format(time_interval, allowed_values)
            )

        self._time_interval = time_interval

    @property
    def time_interval_additional_info(self):
        """Gets the time_interval_additional_info of this CapitalizationBondsProductPrizeDraw.  # noqa: E501

        Restrição: Campo obrigatório para complementar a informação quando selecionada a opção 'OUTROS'  # noqa: E501

        :return: The time_interval_additional_info of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :rtype: str
        """
        return self._time_interval_additional_info

    @time_interval_additional_info.setter
    def time_interval_additional_info(self, time_interval_additional_info):
        """Sets the time_interval_additional_info of this CapitalizationBondsProductPrizeDraw.

        Restrição: Campo obrigatório para complementar a informação quando selecionada a opção 'OUTROS'  # noqa: E501

        :param time_interval_additional_info: The time_interval_additional_info of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :type: str
        """

        self._time_interval_additional_info = time_interval_additional_info

    @property
    def quantity(self):
        """Gets the quantity of this CapitalizationBondsProductPrizeDraw.  # noqa: E501

        Número da quantidade de sorteios previstos ao longo da vigência.  # noqa: E501

        :return: The quantity of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CapitalizationBondsProductPrizeDraw.

        Número da quantidade de sorteios previstos ao longo da vigência.  # noqa: E501

        :param quantity: The quantity of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def prize_multiplier(self):
        """Gets the prize_multiplier of this CapitalizationBondsProductPrizeDraw.  # noqa: E501

        Valor dos sorteios representado por múltiplo do valor de contribuição. Por exemplo: 5 vezes valor da contribuição  # noqa: E501

        :return: The prize_multiplier of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :rtype: float
        """
        return self._prize_multiplier

    @prize_multiplier.setter
    def prize_multiplier(self, prize_multiplier):
        """Sets the prize_multiplier of this CapitalizationBondsProductPrizeDraw.

        Valor dos sorteios representado por múltiplo do valor de contribuição. Por exemplo: 5 vezes valor da contribuição  # noqa: E501

        :param prize_multiplier: The prize_multiplier of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :type: float
        """
        if prize_multiplier is None:
            raise ValueError("Invalid value for `prize_multiplier`, must not be `None`")  # noqa: E501

        self._prize_multiplier = prize_multiplier

    @property
    def early_settlement_raffle(self):
        """Gets the early_settlement_raffle of this CapitalizationBondsProductPrizeDraw.  # noqa: E501

        Modelo de sorteio que acarreta, ao título contemplado, o seu resgate total obrigatório (Resolução Normativa 384/20). Conforme os domínios:  1. true  2. false   # noqa: E501

        :return: The early_settlement_raffle of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :rtype: bool
        """
        return self._early_settlement_raffle

    @early_settlement_raffle.setter
    def early_settlement_raffle(self, early_settlement_raffle):
        """Sets the early_settlement_raffle of this CapitalizationBondsProductPrizeDraw.

        Modelo de sorteio que acarreta, ao título contemplado, o seu resgate total obrigatório (Resolução Normativa 384/20). Conforme os domínios:  1. true  2. false   # noqa: E501

        :param early_settlement_raffle: The early_settlement_raffle of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :type: bool
        """

        self._early_settlement_raffle = early_settlement_raffle

    @property
    def mandatory_contemplation(self):
        """Gets the mandatory_contemplation of this CapitalizationBondsProductPrizeDraw.  # noqa: E501

        Possibilidade de realização de sorteio com previsão de que o título sorteado seja obrigatoriamente um título comercializado, desde que atingidos os requisitos definidos nas condições gerais do plano. Conforme os domínios:   1. true   2. false   # noqa: E501

        :return: The mandatory_contemplation of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :rtype: bool
        """
        return self._mandatory_contemplation

    @mandatory_contemplation.setter
    def mandatory_contemplation(self, mandatory_contemplation):
        """Sets the mandatory_contemplation of this CapitalizationBondsProductPrizeDraw.

        Possibilidade de realização de sorteio com previsão de que o título sorteado seja obrigatoriamente um título comercializado, desde que atingidos os requisitos definidos nas condições gerais do plano. Conforme os domínios:   1. true   2. false   # noqa: E501

        :param mandatory_contemplation: The mandatory_contemplation of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :type: bool
        """

        self._mandatory_contemplation = mandatory_contemplation

    @property
    def rule_description(self):
        """Gets the rule_description of this CapitalizationBondsProductPrizeDraw.  # noqa: E501

        Campo aberto para complementar a regra dos sorteios do produto, a ser feita para cada participante.  # noqa: E501

        :return: The rule_description of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :rtype: str
        """
        return self._rule_description

    @rule_description.setter
    def rule_description(self, rule_description):
        """Sets the rule_description of this CapitalizationBondsProductPrizeDraw.

        Campo aberto para complementar a regra dos sorteios do produto, a ser feita para cada participante.  # noqa: E501

        :param rule_description: The rule_description of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :type: str
        """

        self._rule_description = rule_description

    @property
    def minimum_contemplation_probability(self):
        """Gets the minimum_contemplation_probability of this CapitalizationBondsProductPrizeDraw.  # noqa: E501

        Número representativo da probabilidade mínima de contemplação nos sorteios, em porcentagem (%).  # noqa: E501

        :return: The minimum_contemplation_probability of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :rtype: str
        """
        return self._minimum_contemplation_probability

    @minimum_contemplation_probability.setter
    def minimum_contemplation_probability(self, minimum_contemplation_probability):
        """Sets the minimum_contemplation_probability of this CapitalizationBondsProductPrizeDraw.

        Número representativo da probabilidade mínima de contemplação nos sorteios, em porcentagem (%).  # noqa: E501

        :param minimum_contemplation_probability: The minimum_contemplation_probability of this CapitalizationBondsProductPrizeDraw.  # noqa: E501
        :type: str
        """
        if minimum_contemplation_probability is None:
            raise ValueError("Invalid value for `minimum_contemplation_probability`, must not be `None`")  # noqa: E501

        self._minimum_contemplation_probability = minimum_contemplation_probability

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
        if issubclass(CapitalizationBondsProductPrizeDraw, dict):
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
        if not isinstance(other, CapitalizationBondsProductPrizeDraw):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
