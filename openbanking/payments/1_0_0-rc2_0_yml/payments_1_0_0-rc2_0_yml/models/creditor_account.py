# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, reponsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openId` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditorAccount(object):
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
        'ispb': 'str',
        'issuer': 'str',
        'number': 'str',
        'check_digit': 'str',
        'account_type': 'EnumAccountPaymentsType'
    }

    attribute_map = {
        'ispb': 'ispb',
        'issuer': 'issuer',
        'number': 'number',
        'check_digit': 'checkDigit',
        'account_type': 'accountType'
    }

    def __init__(self, ispb=None, issuer=None, number=None, check_digit=None, account_type=None):  # noqa: E501
        """CreditorAccount - a model defined in Swagger"""  # noqa: E501
        self._ispb = None
        self._issuer = None
        self._number = None
        self._check_digit = None
        self._account_type = None
        self.discriminator = None
        self.ispb = ispb
        if issuer is not None:
            self.issuer = issuer
        self.number = number
        self.check_digit = check_digit
        self.account_type = account_type

    @property
    def ispb(self):
        """Gets the ispb of this CreditorAccount.  # noqa: E501

        Deve ser preenchido com o ISPB (Identificador do Sistema de Pagamentos Brasileiros) do participante do SPI (Sistema de pagamentos instantâneos) somente com números.   # noqa: E501

        :return: The ispb of this CreditorAccount.  # noqa: E501
        :rtype: str
        """
        return self._ispb

    @ispb.setter
    def ispb(self, ispb):
        """Sets the ispb of this CreditorAccount.

        Deve ser preenchido com o ISPB (Identificador do Sistema de Pagamentos Brasileiros) do participante do SPI (Sistema de pagamentos instantâneos) somente com números.   # noqa: E501

        :param ispb: The ispb of this CreditorAccount.  # noqa: E501
        :type: str
        """
        if ispb is None:
            raise ValueError("Invalid value for `ispb`, must not be `None`")  # noqa: E501

        self._ispb = ispb

    @property
    def issuer(self):
        """Gets the issuer of this CreditorAccount.  # noqa: E501

        Código da Agência emissora da conta sem dígito.   (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito,   no exercício de atividades da instituição, não podendo ser móvel ou transitória).   [Restrição] Preenchimento obrigatório para os seguintes tipos de conta: CACC (CONTA_DEPOSITO_A_VISTA), SVGS (CONTA_POUPANCA) e SLRY (CONTA_SALARIO).   # noqa: E501

        :return: The issuer of this CreditorAccount.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this CreditorAccount.

        Código da Agência emissora da conta sem dígito.   (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito,   no exercício de atividades da instituição, não podendo ser móvel ou transitória).   [Restrição] Preenchimento obrigatório para os seguintes tipos de conta: CACC (CONTA_DEPOSITO_A_VISTA), SVGS (CONTA_POUPANCA) e SLRY (CONTA_SALARIO).   # noqa: E501

        :param issuer: The issuer of this CreditorAccount.  # noqa: E501
        :type: str
        """

        self._issuer = issuer

    @property
    def number(self):
        """Gets the number of this CreditorAccount.  # noqa: E501

        Número da conta sem o dígito.  # noqa: E501

        :return: The number of this CreditorAccount.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this CreditorAccount.

        Número da conta sem o dígito.  # noqa: E501

        :param number: The number of this CreditorAccount.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def check_digit(self):
        """Gets the check_digit of this CreditorAccount.  # noqa: E501

        Dígito da conta.  # noqa: E501

        :return: The check_digit of this CreditorAccount.  # noqa: E501
        :rtype: str
        """
        return self._check_digit

    @check_digit.setter
    def check_digit(self, check_digit):
        """Sets the check_digit of this CreditorAccount.

        Dígito da conta.  # noqa: E501

        :param check_digit: The check_digit of this CreditorAccount.  # noqa: E501
        :type: str
        """
        if check_digit is None:
            raise ValueError("Invalid value for `check_digit`, must not be `None`")  # noqa: E501

        self._check_digit = check_digit

    @property
    def account_type(self):
        """Gets the account_type of this CreditorAccount.  # noqa: E501


        :return: The account_type of this CreditorAccount.  # noqa: E501
        :rtype: EnumAccountPaymentsType
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this CreditorAccount.


        :param account_type: The account_type of this CreditorAccount.  # noqa: E501
        :type: EnumAccountPaymentsType
        """
        if account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

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
        if issubclass(CreditorAccount, dict):
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
        if not isinstance(other, CreditorAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
