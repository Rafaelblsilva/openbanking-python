# coding: utf-8

"""
    API Capitalization-bonds - Open Finance Brasil

    As APIs descritas neste documento é referente a API de Capitalização da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CapitalizationBondsProductQuota(object):
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
        'quota': 'float',
        'capitalization_quota': 'str',
        'raffle_quota': 'str',
        'charging_quota': 'str'
    }

    attribute_map = {
        'quota': 'quota',
        'capitalization_quota': 'capitalizationQuota',
        'raffle_quota': 'raffleQuota',
        'charging_quota': 'chargingQuota'
    }

    def __init__(self, quota=None, capitalization_quota=None, raffle_quota=None, charging_quota=None):  # noqa: E501
        """CapitalizationBondsProductQuota - a model defined in Swagger"""  # noqa: E501
        self._quota = None
        self._capitalization_quota = None
        self._raffle_quota = None
        self._charging_quota = None
        self.discriminator = None
        self.quota = quota
        self.capitalization_quota = capitalization_quota
        self.raffle_quota = raffle_quota
        self.charging_quota = charging_quota

    @property
    def quota(self):
        """Gets the quota of this CapitalizationBondsProductQuota.  # noqa: E501

        Número da parcela.  # noqa: E501

        :return: The quota of this CapitalizationBondsProductQuota.  # noqa: E501
        :rtype: float
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this CapitalizationBondsProductQuota.

        Número da parcela.  # noqa: E501

        :param quota: The quota of this CapitalizationBondsProductQuota.  # noqa: E501
        :type: float
        """
        if quota is None:
            raise ValueError("Invalid value for `quota`, must not be `None`")  # noqa: E501

        self._quota = quota

    @property
    def capitalization_quota(self):
        """Gets the capitalization_quota of this CapitalizationBondsProductQuota.  # noqa: E501

        Percentual da contribuição destinado à constituição de capital referente ao direito de resgate. (Resolução CNSP 384/20) Em porcentagem(%).  # noqa: E501

        :return: The capitalization_quota of this CapitalizationBondsProductQuota.  # noqa: E501
        :rtype: str
        """
        return self._capitalization_quota

    @capitalization_quota.setter
    def capitalization_quota(self, capitalization_quota):
        """Sets the capitalization_quota of this CapitalizationBondsProductQuota.

        Percentual da contribuição destinado à constituição de capital referente ao direito de resgate. (Resolução CNSP 384/20) Em porcentagem(%).  # noqa: E501

        :param capitalization_quota: The capitalization_quota of this CapitalizationBondsProductQuota.  # noqa: E501
        :type: str
        """
        if capitalization_quota is None:
            raise ValueError("Invalid value for `capitalization_quota`, must not be `None`")  # noqa: E501

        self._capitalization_quota = capitalization_quota

    @property
    def raffle_quota(self):
        """Gets the raffle_quota of this CapitalizationBondsProductQuota.  # noqa: E501

        Percentual da contribuição destinado a custear os sorteios, se previstos no plano. (Resolução CNSP 384/20) Em porcentagem(%).  # noqa: E501

        :return: The raffle_quota of this CapitalizationBondsProductQuota.  # noqa: E501
        :rtype: str
        """
        return self._raffle_quota

    @raffle_quota.setter
    def raffle_quota(self, raffle_quota):
        """Sets the raffle_quota of this CapitalizationBondsProductQuota.

        Percentual da contribuição destinado a custear os sorteios, se previstos no plano. (Resolução CNSP 384/20) Em porcentagem(%).  # noqa: E501

        :param raffle_quota: The raffle_quota of this CapitalizationBondsProductQuota.  # noqa: E501
        :type: str
        """
        if raffle_quota is None:
            raise ValueError("Invalid value for `raffle_quota`, must not be `None`")  # noqa: E501

        self._raffle_quota = raffle_quota

    @property
    def charging_quota(self):
        """Gets the charging_quota of this CapitalizationBondsProductQuota.  # noqa: E501

        Percentual da contribuição destinado aos custos de despesas com corretagem, colocação e administração do título de capitalização, emissão, divulgação, lucro da sociedade de capitalização e eventuais despesas relativas ao custeio da contemplação obrigatória e da distribuição de bônus. (Resolução CNSP 384/20) Em porcentagem(%).  # noqa: E501

        :return: The charging_quota of this CapitalizationBondsProductQuota.  # noqa: E501
        :rtype: str
        """
        return self._charging_quota

    @charging_quota.setter
    def charging_quota(self, charging_quota):
        """Sets the charging_quota of this CapitalizationBondsProductQuota.

        Percentual da contribuição destinado aos custos de despesas com corretagem, colocação e administração do título de capitalização, emissão, divulgação, lucro da sociedade de capitalização e eventuais despesas relativas ao custeio da contemplação obrigatória e da distribuição de bônus. (Resolução CNSP 384/20) Em porcentagem(%).  # noqa: E501

        :param charging_quota: The charging_quota of this CapitalizationBondsProductQuota.  # noqa: E501
        :type: str
        """
        if charging_quota is None:
            raise ValueError("Invalid value for `charging_quota`, must not be `None`")  # noqa: E501

        self._charging_quota = charging_quota

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
        if issubclass(CapitalizationBondsProductQuota, dict):
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
        if not isinstance(other, CapitalizationBondsProductQuota):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
