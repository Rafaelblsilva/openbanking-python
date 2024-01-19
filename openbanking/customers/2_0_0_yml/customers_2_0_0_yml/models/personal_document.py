# coding: utf-8

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalDocument(object):
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
        'cpf_number': 'str',
        'passport': 'PersonalPassport'
    }

    attribute_map = {
        'cpf_number': 'cpfNumber',
        'passport': 'passport'
    }

    def __init__(self, cpf_number=None, passport=None):  # noqa: E501
        """PersonalDocument - a model defined in Swagger"""  # noqa: E501
        self._cpf_number = None
        self._passport = None
        self.discriminator = None
        if cpf_number is not None:
            self.cpf_number = cpf_number
        if passport is not None:
            self.passport = passport

    @property
    def cpf_number(self):
        """Gets the cpf_number of this PersonalDocument.  # noqa: E501

        Número completo do CPF.  Atributo que corresponde às informações mínimas exigidas pela Regulamentação em vigor.  O CPF é o Cadastro de Pessoa natural. Ele é um documento feito pela Receita Federal e serve para identificar os contribuintes. O CPF é uma numeração com 11 dígitos, que só mudam por decisão judicial. O documento é emitido pela receita federal.  [Restrição] Preenchimento obrigatório quando não for informado o passport.   # noqa: E501

        :return: The cpf_number of this PersonalDocument.  # noqa: E501
        :rtype: str
        """
        return self._cpf_number

    @cpf_number.setter
    def cpf_number(self, cpf_number):
        """Sets the cpf_number of this PersonalDocument.

        Número completo do CPF.  Atributo que corresponde às informações mínimas exigidas pela Regulamentação em vigor.  O CPF é o Cadastro de Pessoa natural. Ele é um documento feito pela Receita Federal e serve para identificar os contribuintes. O CPF é uma numeração com 11 dígitos, que só mudam por decisão judicial. O documento é emitido pela receita federal.  [Restrição] Preenchimento obrigatório quando não for informado o passport.   # noqa: E501

        :param cpf_number: The cpf_number of this PersonalDocument.  # noqa: E501
        :type: str
        """

        self._cpf_number = cpf_number

    @property
    def passport(self):
        """Gets the passport of this PersonalDocument.  # noqa: E501


        :return: The passport of this PersonalDocument.  # noqa: E501
        :rtype: PersonalPassport
        """
        return self._passport

    @passport.setter
    def passport(self, passport):
        """Sets the passport of this PersonalDocument.


        :param passport: The passport of this PersonalDocument.  # noqa: E501
        :type: PersonalPassport
        """

        self._passport = passport

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
        if issubclass(PersonalDocument, dict):
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
        if not isinstance(other, PersonalDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
