# coding: utf-8

"""
    API OpenData Financings do Open Finance Brasil

    A API descrita neste documento é referente as API Financings da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-beta.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BusinessFinancingData(object):
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
        'participant': 'Participant',
        'type': 'str',
        'fees': 'BusinessFinancingFee',
        'interest_rates': 'list[FinancingInterestRate]',
        'required_warranties': 'list[RequiredWarranty]',
        'terms_conditions': 'str'
    }

    attribute_map = {
        'participant': 'participant',
        'type': 'type',
        'fees': 'fees',
        'interest_rates': 'interestRates',
        'required_warranties': 'requiredWarranties',
        'terms_conditions': 'termsConditions'
    }

    def __init__(self, participant=None, type=None, fees=None, interest_rates=None, required_warranties=None, terms_conditions=None):  # noqa: E501
        """BusinessFinancingData - a model defined in Swagger"""  # noqa: E501
        self._participant = None
        self._type = None
        self._fees = None
        self._interest_rates = None
        self._required_warranties = None
        self._terms_conditions = None
        self.discriminator = None
        if participant is not None:
            self.participant = participant
        self.type = type
        self.fees = fees
        self.interest_rates = interest_rates
        self.required_warranties = required_warranties
        self.terms_conditions = terms_conditions

    @property
    def participant(self):
        """Gets the participant of this BusinessFinancingData.  # noqa: E501


        :return: The participant of this BusinessFinancingData.  # noqa: E501
        :rtype: Participant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this BusinessFinancingData.


        :param participant: The participant of this BusinessFinancingData.  # noqa: E501
        :type: Participant
        """

        self._participant = participant

    @property
    def type(self):
        """Gets the type of this BusinessFinancingData.  # noqa: E501

        Modalidades de financiamentos ofertados para pessoas jurídicas, conforme Circular 4015-Bacen. Segundo cartilha do Bacen: Financiamento é um contrato entre o cliente e uma instituição financeira, mas com, destinação específica como para a aquisição de veículo ou de bem imóvel, que funcionam como garantia para o crédito concedido  # noqa: E501

        :return: The type of this BusinessFinancingData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BusinessFinancingData.

        Modalidades de financiamentos ofertados para pessoas jurídicas, conforme Circular 4015-Bacen. Segundo cartilha do Bacen: Financiamento é um contrato entre o cliente e uma instituição financeira, mas com, destinação específica como para a aquisição de veículo ou de bem imóvel, que funcionam como garantia para o crédito concedido  # noqa: E501

        :param type: The type of this BusinessFinancingData.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["FINANCIAMENTO_AQUISICAO_BENS_VEICULOS_AUTOMOTORES", "FINANCIAMENTO_AQUISICAO_BENS_OUTROS_BENS", "FINANCIAMENTO_MICROCREDITO", "FINANCIAMENTO_RURAL_CUSTEIO", "FINANCIAMENTO_RURAL_INVESTIMENTO", "FINANCIAMENTO_RURAL_COMERCIALIZACAO", "FINANCIAMENTO_RURAL_INDUSTRIALIZACAO", "FINANCIAMENTO_IMOBILIARIO_SISTEMA_FINANCEIRO_HABITACAO_SFH", "FINANCIAMENTO_IMOBILIARIO_SISTEMA_FINANCEIRO_HABITACAO_SFI"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def fees(self):
        """Gets the fees of this BusinessFinancingData.  # noqa: E501


        :return: The fees of this BusinessFinancingData.  # noqa: E501
        :rtype: BusinessFinancingFee
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this BusinessFinancingData.


        :param fees: The fees of this BusinessFinancingData.  # noqa: E501
        :type: BusinessFinancingFee
        """
        if fees is None:
            raise ValueError("Invalid value for `fees`, must not be `None`")  # noqa: E501

        self._fees = fees

    @property
    def interest_rates(self):
        """Gets the interest_rates of this BusinessFinancingData.  # noqa: E501

        Lista que traz o conjunto de informações necessárias para demonstrar a distribuição de frequências das taxas de juros remuneratórios da Modalidade de crédito  # noqa: E501

        :return: The interest_rates of this BusinessFinancingData.  # noqa: E501
        :rtype: list[FinancingInterestRate]
        """
        return self._interest_rates

    @interest_rates.setter
    def interest_rates(self, interest_rates):
        """Sets the interest_rates of this BusinessFinancingData.

        Lista que traz o conjunto de informações necessárias para demonstrar a distribuição de frequências das taxas de juros remuneratórios da Modalidade de crédito  # noqa: E501

        :param interest_rates: The interest_rates of this BusinessFinancingData.  # noqa: E501
        :type: list[FinancingInterestRate]
        """
        if interest_rates is None:
            raise ValueError("Invalid value for `interest_rates`, must not be `None`")  # noqa: E501

        self._interest_rates = interest_rates

    @property
    def required_warranties(self):
        """Gets the required_warranties of this BusinessFinancingData.  # noqa: E501


        :return: The required_warranties of this BusinessFinancingData.  # noqa: E501
        :rtype: list[RequiredWarranty]
        """
        return self._required_warranties

    @required_warranties.setter
    def required_warranties(self, required_warranties):
        """Sets the required_warranties of this BusinessFinancingData.


        :param required_warranties: The required_warranties of this BusinessFinancingData.  # noqa: E501
        :type: list[RequiredWarranty]
        """
        if required_warranties is None:
            raise ValueError("Invalid value for `required_warranties`, must not be `None`")  # noqa: E501

        self._required_warranties = required_warranties

    @property
    def terms_conditions(self):
        """Gets the terms_conditions of this BusinessFinancingData.  # noqa: E501

        Campo aberto para informar as condições contratuais relativas à Modalidade de Financiamentos para pessoa jurídica informada. Pode ser informada a URL referente ao endereço onde constam as condições informadas. Endereço eletrônico de acesso ao canal.  # noqa: E501

        :return: The terms_conditions of this BusinessFinancingData.  # noqa: E501
        :rtype: str
        """
        return self._terms_conditions

    @terms_conditions.setter
    def terms_conditions(self, terms_conditions):
        """Sets the terms_conditions of this BusinessFinancingData.

        Campo aberto para informar as condições contratuais relativas à Modalidade de Financiamentos para pessoa jurídica informada. Pode ser informada a URL referente ao endereço onde constam as condições informadas. Endereço eletrônico de acesso ao canal.  # noqa: E501

        :param terms_conditions: The terms_conditions of this BusinessFinancingData.  # noqa: E501
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
        if issubclass(BusinessFinancingData, dict):
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
        if not isinstance(other, BusinessFinancingData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
