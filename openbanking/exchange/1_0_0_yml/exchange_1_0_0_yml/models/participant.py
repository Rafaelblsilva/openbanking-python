# coding: utf-8

"""
    API Exchange - Open Finance Brasil

    API de Câmbio do Open Finance Brasil – Fase 4. API que retorna informações de Câmbio.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Participant(object):
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
        'brand': 'str',
        'name': 'str',
        'cnpj_number': 'CnpjNumber',
        'url_complementary_list': 'str'
    }

    attribute_map = {
        'brand': 'brand',
        'name': 'name',
        'cnpj_number': 'cnpjNumber',
        'url_complementary_list': 'urlComplementaryList'
    }

    def __init__(self, brand=None, name=None, cnpj_number=None, url_complementary_list=None):  # noqa: E501
        """Participant - a model defined in Swagger"""  # noqa: E501
        self._brand = None
        self._name = None
        self._cnpj_number = None
        self._url_complementary_list = None
        self.discriminator = None
        self.brand = brand
        self.name = name
        self.cnpj_number = cnpj_number
        if url_complementary_list is not None:
            self.url_complementary_list = url_complementary_list

    @property
    def brand(self):
        """Gets the brand of this Participant.  # noqa: E501

        Nome da marca reportada pelo participante do Open Finance. O conceito a que se refere a 'marca' é em essência uma promessa da empresa em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes.  # noqa: E501

        :return: The brand of this Participant.  # noqa: E501
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this Participant.

        Nome da marca reportada pelo participante do Open Finance. O conceito a que se refere a 'marca' é em essência uma promessa da empresa em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes.  # noqa: E501

        :param brand: The brand of this Participant.  # noqa: E501
        :type: str
        """
        if brand is None:
            raise ValueError("Invalid value for `brand`, must not be `None`")  # noqa: E501

        self._brand = brand

    @property
    def name(self):
        """Gets the name of this Participant.  # noqa: E501

        Nome do participante do Open Finance.  # noqa: E501

        :return: The name of this Participant.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Participant.

        Nome do participante do Open Finance.  # noqa: E501

        :param name: The name of this Participant.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cnpj_number(self):
        """Gets the cnpj_number of this Participant.  # noqa: E501


        :return: The cnpj_number of this Participant.  # noqa: E501
        :rtype: CnpjNumber
        """
        return self._cnpj_number

    @cnpj_number.setter
    def cnpj_number(self, cnpj_number):
        """Sets the cnpj_number of this Participant.


        :param cnpj_number: The cnpj_number of this Participant.  # noqa: E501
        :type: CnpjNumber
        """
        if cnpj_number is None:
            raise ValueError("Invalid value for `cnpj_number`, must not be `None`")  # noqa: E501

        self._cnpj_number = cnpj_number

    @property
    def url_complementary_list(self):
        """Gets the url_complementary_list of this Participant.  # noqa: E501

        Espera-se que valor de retorno, após acesso ao link ‘urlComplementaryList’, deve ser array de objeto com a estrutura abaixo:  - ‘name’ com o valor contido no campo ‘LegalEntityName’ conforme cadastro no diretório;  - 'cnpjNumber' com o valor contido no campo CNPJ (‘RegistrationNumber’) correspondente a esta instituição;  - Ambos do tipo string;  - Ambos obrigatórios.   # noqa: E501

        :return: The url_complementary_list of this Participant.  # noqa: E501
        :rtype: str
        """
        return self._url_complementary_list

    @url_complementary_list.setter
    def url_complementary_list(self, url_complementary_list):
        """Sets the url_complementary_list of this Participant.

        Espera-se que valor de retorno, após acesso ao link ‘urlComplementaryList’, deve ser array de objeto com a estrutura abaixo:  - ‘name’ com o valor contido no campo ‘LegalEntityName’ conforme cadastro no diretório;  - 'cnpjNumber' com o valor contido no campo CNPJ (‘RegistrationNumber’) correspondente a esta instituição;  - Ambos do tipo string;  - Ambos obrigatórios.   # noqa: E501

        :param url_complementary_list: The url_complementary_list of this Participant.  # noqa: E501
        :type: str
        """

        self._url_complementary_list = url_complementary_list

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
        if issubclass(Participant, dict):
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
        if not isinstance(other, Participant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other