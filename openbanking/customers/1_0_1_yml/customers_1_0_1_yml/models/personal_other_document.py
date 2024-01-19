# coding: utf-8

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalOtherDocument(object):
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
        'type': 'EnumPersonalOtherDocumentType',
        'type_additional_info': 'str',
        'number': 'str',
        'check_digit': 'str',
        'additional_info': 'str',
        'expiration_date': 'date'
    }

    attribute_map = {
        'type': 'type',
        'type_additional_info': 'typeAdditionalInfo',
        'number': 'number',
        'check_digit': 'checkDigit',
        'additional_info': 'additionalInfo',
        'expiration_date': 'expirationDate'
    }

    def __init__(self, type=None, type_additional_info=None, number=None, check_digit=None, additional_info=None, expiration_date=None):  # noqa: E501
        """PersonalOtherDocument - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._type_additional_info = None
        self._number = None
        self._check_digit = None
        self._additional_info = None
        self._expiration_date = None
        self.discriminator = None
        self.type = type
        self.type_additional_info = type_additional_info
        self.number = number
        self.check_digit = check_digit
        if additional_info is not None:
            self.additional_info = additional_info
        self.expiration_date = expiration_date

    @property
    def type(self):
        """Gets the type of this PersonalOtherDocument.  # noqa: E501


        :return: The type of this PersonalOtherDocument.  # noqa: E501
        :rtype: EnumPersonalOtherDocumentType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PersonalOtherDocument.


        :param type: The type of this PersonalOtherDocument.  # noqa: E501
        :type: EnumPersonalOtherDocumentType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def type_additional_info(self):
        """Gets the type_additional_info of this PersonalOtherDocument.  # noqa: E501

        Campo livre de preenchimento obrigatório se selecionada a opção OUTROS tipos de documentos  # noqa: E501

        :return: The type_additional_info of this PersonalOtherDocument.  # noqa: E501
        :rtype: str
        """
        return self._type_additional_info

    @type_additional_info.setter
    def type_additional_info(self, type_additional_info):
        """Sets the type_additional_info of this PersonalOtherDocument.

        Campo livre de preenchimento obrigatório se selecionada a opção OUTROS tipos de documentos  # noqa: E501

        :param type_additional_info: The type_additional_info of this PersonalOtherDocument.  # noqa: E501
        :type: str
        """
        if type_additional_info is None:
            raise ValueError("Invalid value for `type_additional_info`, must not be `None`")  # noqa: E501

        self._type_additional_info = type_additional_info

    @property
    def number(self):
        """Gets the number of this PersonalOtherDocument.  # noqa: E501

        Identificação/Número do documento informado  # noqa: E501

        :return: The number of this PersonalOtherDocument.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this PersonalOtherDocument.

        Identificação/Número do documento informado  # noqa: E501

        :param number: The number of this PersonalOtherDocument.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def check_digit(self):
        """Gets the check_digit of this PersonalOtherDocument.  # noqa: E501

        Dígito verificador do documento informado. De preenchimento obrigatório se o documento informado tiver dígito verificador  # noqa: E501

        :return: The check_digit of this PersonalOtherDocument.  # noqa: E501
        :rtype: str
        """
        return self._check_digit

    @check_digit.setter
    def check_digit(self, check_digit):
        """Sets the check_digit of this PersonalOtherDocument.

        Dígito verificador do documento informado. De preenchimento obrigatório se o documento informado tiver dígito verificador  # noqa: E501

        :param check_digit: The check_digit of this PersonalOtherDocument.  # noqa: E501
        :type: str
        """
        if check_digit is None:
            raise ValueError("Invalid value for `check_digit`, must not be `None`")  # noqa: E501

        self._check_digit = check_digit

    @property
    def additional_info(self):
        """Gets the additional_info of this PersonalOtherDocument.  # noqa: E501

        Para documentos em que se aplique o uso do local de emissão o mesmo deve ser enviado mandatoriamente, com a informação de órgão e UF. Exemplo: RG, local de emissão: SSP/RS. [Restrição] Obrigatório quando o Local de Emissão do Documento for relevante.   # noqa: E501

        :return: The additional_info of this PersonalOtherDocument.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this PersonalOtherDocument.

        Para documentos em que se aplique o uso do local de emissão o mesmo deve ser enviado mandatoriamente, com a informação de órgão e UF. Exemplo: RG, local de emissão: SSP/RS. [Restrição] Obrigatório quando o Local de Emissão do Documento for relevante.   # noqa: E501

        :param additional_info: The additional_info of this PersonalOtherDocument.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def expiration_date(self):
        """Gets the expiration_date of this PersonalOtherDocument.  # noqa: E501

        Data de validade do documento informado, conforme especificação RFC-3339.  # noqa: E501

        :return: The expiration_date of this PersonalOtherDocument.  # noqa: E501
        :rtype: date
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        """Sets the expiration_date of this PersonalOtherDocument.

        Data de validade do documento informado, conforme especificação RFC-3339.  # noqa: E501

        :param expiration_date: The expiration_date of this PersonalOtherDocument.  # noqa: E501
        :type: date
        """
        if expiration_date is None:
            raise ValueError("Invalid value for `expiration_date`, must not be `None`")  # noqa: E501

        self._expiration_date = expiration_date

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
        if issubclass(PersonalOtherDocument, dict):
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
        if not isinstance(other, PersonalOtherDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
