# coding: utf-8

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 2.0.0-RC1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InformedIncomeAmount(object):
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
        'amount': 'str',
        'currency': 'str'
    }

    attribute_map = {
        'amount': 'amount',
        'currency': 'currency'
    }

    def __init__(self, amount=None, currency=None):  # noqa: E501
        """InformedIncomeAmount - a model defined in Swagger"""  # noqa: E501
        self._amount = None
        self._currency = None
        self.discriminator = None
        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        """Gets the amount of this InformedIncomeAmount.  # noqa: E501

        Valor total da renda informada. Expresso em valor monetário com no mínimo 2 casas e no máximo 4 casas decimais.  Renda primária indica os montantes a pagar ou a receber em troca do uso temporário de recursos financeiros, trabalho ou ativos não financeiros não produzidos, a saber, remuneração de trabalhadores, renda de investimentos e demais rendas primárias. Fazem parte da primeira a remuneração do trabalho assalariado (salários e ordenados); da segunda, renda de investimento direto, renda de investimento em carteira, renda de outros investimentos e renda de ativos de reserva; e da terceira, tributos sobre a produção e importação, subsídios e aluguéis. Fonte: Banco Central do Brasil – Departamento Econômico   # noqa: E501

        :return: The amount of this InformedIncomeAmount.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InformedIncomeAmount.

        Valor total da renda informada. Expresso em valor monetário com no mínimo 2 casas e no máximo 4 casas decimais.  Renda primária indica os montantes a pagar ou a receber em troca do uso temporário de recursos financeiros, trabalho ou ativos não financeiros não produzidos, a saber, remuneração de trabalhadores, renda de investimentos e demais rendas primárias. Fazem parte da primeira a remuneração do trabalho assalariado (salários e ordenados); da segunda, renda de investimento direto, renda de investimento em carteira, renda de outros investimentos e renda de ativos de reserva; e da terceira, tributos sobre a produção e importação, subsídios e aluguéis. Fonte: Banco Central do Brasil – Departamento Econômico   # noqa: E501

        :param amount: The amount of this InformedIncomeAmount.  # noqa: E501
        :type: str
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this InformedIncomeAmount.  # noqa: E501

        Moeda referente ao valor monetário, seguindo o modelo ISO-4217.  # noqa: E501

        :return: The currency of this InformedIncomeAmount.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InformedIncomeAmount.

        Moeda referente ao valor monetário, seguindo o modelo ISO-4217.  # noqa: E501

        :param currency: The currency of this InformedIncomeAmount.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

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
        if issubclass(InformedIncomeAmount, dict):
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
        if not isinstance(other, InformedIncomeAmount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
