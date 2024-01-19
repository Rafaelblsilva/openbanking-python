# coding: utf-8

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 1.0.3
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalContacts(object):
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
        'postal_addresses': 'list[PersonalPostalAddress]',
        'phones': 'list[CustomerPhone]',
        'emails': 'list[CustomerEmail]'
    }

    attribute_map = {
        'postal_addresses': 'postalAddresses',
        'phones': 'phones',
        'emails': 'emails'
    }

    def __init__(self, postal_addresses=None, phones=None, emails=None):  # noqa: E501
        """PersonalContacts - a model defined in Swagger"""  # noqa: E501
        self._postal_addresses = None
        self._phones = None
        self._emails = None
        self.discriminator = None
        self.postal_addresses = postal_addresses
        self.phones = phones
        self.emails = emails

    @property
    def postal_addresses(self):
        """Gets the postal_addresses of this PersonalContacts.  # noqa: E501

        Lista de endereços da pessoa natural  # noqa: E501

        :return: The postal_addresses of this PersonalContacts.  # noqa: E501
        :rtype: list[PersonalPostalAddress]
        """
        return self._postal_addresses

    @postal_addresses.setter
    def postal_addresses(self, postal_addresses):
        """Sets the postal_addresses of this PersonalContacts.

        Lista de endereços da pessoa natural  # noqa: E501

        :param postal_addresses: The postal_addresses of this PersonalContacts.  # noqa: E501
        :type: list[PersonalPostalAddress]
        """
        if postal_addresses is None:
            raise ValueError("Invalid value for `postal_addresses`, must not be `None`")  # noqa: E501

        self._postal_addresses = postal_addresses

    @property
    def phones(self):
        """Gets the phones of this PersonalContacts.  # noqa: E501

        Lista com telefones de contato da pessoa natural  # noqa: E501

        :return: The phones of this PersonalContacts.  # noqa: E501
        :rtype: list[CustomerPhone]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this PersonalContacts.

        Lista com telefones de contato da pessoa natural  # noqa: E501

        :param phones: The phones of this PersonalContacts.  # noqa: E501
        :type: list[CustomerPhone]
        """
        if phones is None:
            raise ValueError("Invalid value for `phones`, must not be `None`")  # noqa: E501

        self._phones = phones

    @property
    def emails(self):
        """Gets the emails of this PersonalContacts.  # noqa: E501

        Lista e-mails de contato  # noqa: E501

        :return: The emails of this PersonalContacts.  # noqa: E501
        :rtype: list[CustomerEmail]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this PersonalContacts.

        Lista e-mails de contato  # noqa: E501

        :param emails: The emails of this PersonalContacts.  # noqa: E501
        :type: list[CustomerEmail]
        """
        if emails is None:
            raise ValueError("Invalid value for `emails`, must not be `None`")  # noqa: E501

        self._emails = emails

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
        if issubclass(PersonalContacts, dict):
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
        if not isinstance(other, PersonalContacts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
