# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalFinancing(object):
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
        'type': 'str',
        'fees': 'PersonalFinancingFee',
        'interest_rate': 'FinancingInterestRate',
        'required_warranties': 'list[RequiredWarranty]',
        'terms_conditions': 'str'
    }

    attribute_map = {
        'type': 'type',
        'fees': 'fees',
        'interest_rate': 'interestRate',
        'required_warranties': 'requiredWarranties',
        'terms_conditions': 'termsConditions'
    }

    def __init__(self, type=None, fees=None, interest_rate=None, required_warranties=None, terms_conditions=None):  # noqa: E501
        """PersonalFinancing - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._fees = None
        self._interest_rate = None
        self._required_warranties = None
        self._terms_conditions = None
        self.discriminator = None
        self.type = type
        self.fees = fees
        self.interest_rate = interest_rate
        self.required_warranties = required_warranties
        self.terms_conditions = terms_conditions

    @property
    def type(self):
        """Gets the type of this PersonalFinancing.  # noqa: E501

        Modalidades de financiamentos ofertados para pessoas naturais, conforme Circular 4015-Bacen. Segundo cartilha do Bacen: Financiamento é um contrato entre o cliente e uma instituição financeira, mas com, destinação específica como para a aquisição de veículo ou de bem imóvel, que funcionam como garantia para o crédito concedido  # noqa: E501

        :return: The type of this PersonalFinancing.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PersonalFinancing.

        Modalidades de financiamentos ofertados para pessoas naturais, conforme Circular 4015-Bacen. Segundo cartilha do Bacen: Financiamento é um contrato entre o cliente e uma instituição financeira, mas com, destinação específica como para a aquisição de veículo ou de bem imóvel, que funcionam como garantia para o crédito concedido  # noqa: E501

        :param type: The type of this PersonalFinancing.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["FINANCIAMENTO_AQUISICAO_BENS_VEICULOS_AUTOMOTORES", "FINANCIAMENTO_AQUISICAO_BENS_OUTROS_BENS", "FINANCIAMENTO_MICROCREDITO", "FINANCIAMENTO_RURAL_CUSTEIO", "FINANCIAMENTO_RURAL_INVESTIMENTO", "FINANCIAMENTO_RURAL_COMERCIALIZACAO", "FINANCIAMENTO_RURAL_INDUSTRIALIZACAO", "FINANCIAMENTO_IMOBILIARIO_SISTEMA_FINANCEIRO_HABILITACAO_SFH", "FINANCIAMENTO_IMOBILIARIO_SISTEMA_FINANCEIRO_HABILITACAO_SFI"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def fees(self):
        """Gets the fees of this PersonalFinancing.  # noqa: E501


        :return: The fees of this PersonalFinancing.  # noqa: E501
        :rtype: PersonalFinancingFee
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this PersonalFinancing.


        :param fees: The fees of this PersonalFinancing.  # noqa: E501
        :type: PersonalFinancingFee
        """
        if fees is None:
            raise ValueError("Invalid value for `fees`, must not be `None`")  # noqa: E501

        self._fees = fees

    @property
    def interest_rate(self):
        """Gets the interest_rate of this PersonalFinancing.  # noqa: E501


        :return: The interest_rate of this PersonalFinancing.  # noqa: E501
        :rtype: FinancingInterestRate
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, interest_rate):
        """Sets the interest_rate of this PersonalFinancing.


        :param interest_rate: The interest_rate of this PersonalFinancing.  # noqa: E501
        :type: FinancingInterestRate
        """
        if interest_rate is None:
            raise ValueError("Invalid value for `interest_rate`, must not be `None`")  # noqa: E501

        self._interest_rate = interest_rate

    @property
    def required_warranties(self):
        """Gets the required_warranties of this PersonalFinancing.  # noqa: E501


        :return: The required_warranties of this PersonalFinancing.  # noqa: E501
        :rtype: list[RequiredWarranty]
        """
        return self._required_warranties

    @required_warranties.setter
    def required_warranties(self, required_warranties):
        """Sets the required_warranties of this PersonalFinancing.


        :param required_warranties: The required_warranties of this PersonalFinancing.  # noqa: E501
        :type: list[RequiredWarranty]
        """
        if required_warranties is None:
            raise ValueError("Invalid value for `required_warranties`, must not be `None`")  # noqa: E501

        self._required_warranties = required_warranties

    @property
    def terms_conditions(self):
        """Gets the terms_conditions of this PersonalFinancing.  # noqa: E501

        Campo aberto para informar as condições contratuais relativas ao produto ou serviço informado. Pode ser informada a URL referente ao endereço onde constam as condições informadas.  # noqa: E501

        :return: The terms_conditions of this PersonalFinancing.  # noqa: E501
        :rtype: str
        """
        return self._terms_conditions

    @terms_conditions.setter
    def terms_conditions(self, terms_conditions):
        """Sets the terms_conditions of this PersonalFinancing.

        Campo aberto para informar as condições contratuais relativas ao produto ou serviço informado. Pode ser informada a URL referente ao endereço onde constam as condições informadas.  # noqa: E501

        :param terms_conditions: The terms_conditions of this PersonalFinancing.  # noqa: E501
        :type: str
        """
        if terms_conditions is None:
            raise ValueError("Invalid value for `terms_conditions`, must not be `None`")  # noqa: E501

        self._terms_conditions = terms_conditions

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
        if issubclass(PersonalFinancing, dict):
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
        if not isinstance(other, PersonalFinancing):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
