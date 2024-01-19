# coding: utf-8

"""
    API Pension - Open Finance Brasil

    API de Previdência do Open Finance Brasil – Fase 4. API que retorna informações de Previdência.   # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SurvivalPensionGracePeriod(object):
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
        'redemption': 'float',
        'between_redemption_requests': 'float',
        'portability': 'float',
        'between_portability_requests': 'float'
    }

    attribute_map = {
        'redemption': 'redemption',
        'between_redemption_requests': 'betweenRedemptionRequests',
        'portability': 'portability',
        'between_portability_requests': 'betweenPortabilityRequests'
    }

    def __init__(self, redemption=None, between_redemption_requests=None, portability=None, between_portability_requests=None):  # noqa: E501
        """SurvivalPensionGracePeriod - a model defined in Swagger"""  # noqa: E501
        self._redemption = None
        self._between_redemption_requests = None
        self._portability = None
        self._between_portability_requests = None
        self.discriminator = None
        self.redemption = redemption
        self.between_redemption_requests = between_redemption_requests
        self.portability = portability
        self.between_portability_requests = between_portability_requests

    @property
    def redemption(self):
        """Gets the redemption of this SurvivalPensionGracePeriod.  # noqa: E501

        Prazo em dias de carência para resgate Para Coletivos: Valor máximo da carência.   # noqa: E501

        :return: The redemption of this SurvivalPensionGracePeriod.  # noqa: E501
        :rtype: float
        """
        return self._redemption

    @redemption.setter
    def redemption(self, redemption):
        """Sets the redemption of this SurvivalPensionGracePeriod.

        Prazo em dias de carência para resgate Para Coletivos: Valor máximo da carência.   # noqa: E501

        :param redemption: The redemption of this SurvivalPensionGracePeriod.  # noqa: E501
        :type: float
        """
        if redemption is None:
            raise ValueError("Invalid value for `redemption`, must not be `None`")  # noqa: E501

        self._redemption = redemption

    @property
    def between_redemption_requests(self):
        """Gets the between_redemption_requests of this SurvivalPensionGracePeriod.  # noqa: E501

        Prazo em dias de carência entre pedidos de resgate Para Coletivos: Valor máximo da carência   # noqa: E501

        :return: The between_redemption_requests of this SurvivalPensionGracePeriod.  # noqa: E501
        :rtype: float
        """
        return self._between_redemption_requests

    @between_redemption_requests.setter
    def between_redemption_requests(self, between_redemption_requests):
        """Sets the between_redemption_requests of this SurvivalPensionGracePeriod.

        Prazo em dias de carência entre pedidos de resgate Para Coletivos: Valor máximo da carência   # noqa: E501

        :param between_redemption_requests: The between_redemption_requests of this SurvivalPensionGracePeriod.  # noqa: E501
        :type: float
        """
        if between_redemption_requests is None:
            raise ValueError("Invalid value for `between_redemption_requests`, must not be `None`")  # noqa: E501

        self._between_redemption_requests = between_redemption_requests

    @property
    def portability(self):
        """Gets the portability of this SurvivalPensionGracePeriod.  # noqa: E501

        Prazo em dias de carência para portabilidade (entre empresas diferentes).  # noqa: E501

        :return: The portability of this SurvivalPensionGracePeriod.  # noqa: E501
        :rtype: float
        """
        return self._portability

    @portability.setter
    def portability(self, portability):
        """Sets the portability of this SurvivalPensionGracePeriod.

        Prazo em dias de carência para portabilidade (entre empresas diferentes).  # noqa: E501

        :param portability: The portability of this SurvivalPensionGracePeriod.  # noqa: E501
        :type: float
        """
        if portability is None:
            raise ValueError("Invalid value for `portability`, must not be `None`")  # noqa: E501

        self._portability = portability

    @property
    def between_portability_requests(self):
        """Gets the between_portability_requests of this SurvivalPensionGracePeriod.  # noqa: E501

        Prazo em dias de carência entre pedidos de portabilidade (entre empresas diferentes).  # noqa: E501

        :return: The between_portability_requests of this SurvivalPensionGracePeriod.  # noqa: E501
        :rtype: float
        """
        return self._between_portability_requests

    @between_portability_requests.setter
    def between_portability_requests(self, between_portability_requests):
        """Sets the between_portability_requests of this SurvivalPensionGracePeriod.

        Prazo em dias de carência entre pedidos de portabilidade (entre empresas diferentes).  # noqa: E501

        :param between_portability_requests: The between_portability_requests of this SurvivalPensionGracePeriod.  # noqa: E501
        :type: float
        """
        if between_portability_requests is None:
            raise ValueError("Invalid value for `between_portability_requests`, must not be `None`")  # noqa: E501

        self._between_portability_requests = between_portability_requests

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
        if issubclass(SurvivalPensionGracePeriod, dict):
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
        if not isinstance(other, SurvivalPensionGracePeriod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other