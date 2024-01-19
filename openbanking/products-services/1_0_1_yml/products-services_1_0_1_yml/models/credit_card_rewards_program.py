# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardRewardsProgram(object):
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
        'has_reward_program': 'bool',
        'reward_program_info': 'str'
    }

    attribute_map = {
        'has_reward_program': 'hasRewardProgram',
        'reward_program_info': 'rewardProgramInfo'
    }

    def __init__(self, has_reward_program=None, reward_program_info=None):  # noqa: E501
        """CreditCardRewardsProgram - a model defined in Swagger"""  # noqa: E501
        self._has_reward_program = None
        self._reward_program_info = None
        self.discriminator = None
        self.has_reward_program = has_reward_program
        if reward_program_info is not None:
            self.reward_program_info = reward_program_info

    @property
    def has_reward_program(self):
        """Gets the has_reward_program of this CreditCardRewardsProgram.  # noqa: E501

        Indicador da existência de programa de fidelidade/recompensa associado à conta de pagamento pós-paga (cartão) true false  # noqa: E501

        :return: The has_reward_program of this CreditCardRewardsProgram.  # noqa: E501
        :rtype: bool
        """
        return self._has_reward_program

    @has_reward_program.setter
    def has_reward_program(self, has_reward_program):
        """Sets the has_reward_program of this CreditCardRewardsProgram.

        Indicador da existência de programa de fidelidade/recompensa associado à conta de pagamento pós-paga (cartão) true false  # noqa: E501

        :param has_reward_program: The has_reward_program of this CreditCardRewardsProgram.  # noqa: E501
        :type: bool
        """
        if has_reward_program is None:
            raise ValueError("Invalid value for `has_reward_program`, must not be `None`")  # noqa: E501

        self._has_reward_program = has_reward_program

    @property
    def reward_program_info(self):
        """Gets the reward_program_info of this CreditCardRewardsProgram.  # noqa: E501

        Informações de termos e condições do programa de fidelidade/recompensa. Pode ser informada a URL referente ao endereço onde constam as condições informadas. Será de preenchimento obrigatório caso o campo hasRewardProgram esteja preenchido como true  # noqa: E501

        :return: The reward_program_info of this CreditCardRewardsProgram.  # noqa: E501
        :rtype: str
        """
        return self._reward_program_info

    @reward_program_info.setter
    def reward_program_info(self, reward_program_info):
        """Sets the reward_program_info of this CreditCardRewardsProgram.

        Informações de termos e condições do programa de fidelidade/recompensa. Pode ser informada a URL referente ao endereço onde constam as condições informadas. Será de preenchimento obrigatório caso o campo hasRewardProgram esteja preenchido como true  # noqa: E501

        :param reward_program_info: The reward_program_info of this CreditCardRewardsProgram.  # noqa: E501
        :type: str
        """

        self._reward_program_info = reward_program_info

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
        if issubclass(CreditCardRewardsProgram, dict):
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
        if not isinstance(other, CreditCardRewardsProgram):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
