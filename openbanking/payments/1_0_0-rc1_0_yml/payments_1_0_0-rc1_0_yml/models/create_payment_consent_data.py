# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, reponsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openId` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreatePaymentConsentData(object):
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
        'creditor': 'Identification',
        'payment': 'PaymentConsent',
        'debtor_account': 'DebtorAccount'
    }

    attribute_map = {
        'creditor': 'creditor',
        'payment': 'payment',
        'debtor_account': 'debtorAccount'
    }

    def __init__(self, creditor=None, payment=None, debtor_account=None):  # noqa: E501
        """CreatePaymentConsentData - a model defined in Swagger"""  # noqa: E501
        self._creditor = None
        self._payment = None
        self._debtor_account = None
        self.discriminator = None
        self.creditor = creditor
        self.payment = payment
        if debtor_account is not None:
            self.debtor_account = debtor_account

    @property
    def creditor(self):
        """Gets the creditor of this CreatePaymentConsentData.  # noqa: E501


        :return: The creditor of this CreatePaymentConsentData.  # noqa: E501
        :rtype: Identification
        """
        return self._creditor

    @creditor.setter
    def creditor(self, creditor):
        """Sets the creditor of this CreatePaymentConsentData.


        :param creditor: The creditor of this CreatePaymentConsentData.  # noqa: E501
        :type: Identification
        """
        if creditor is None:
            raise ValueError("Invalid value for `creditor`, must not be `None`")  # noqa: E501

        self._creditor = creditor

    @property
    def payment(self):
        """Gets the payment of this CreatePaymentConsentData.  # noqa: E501


        :return: The payment of this CreatePaymentConsentData.  # noqa: E501
        :rtype: PaymentConsent
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this CreatePaymentConsentData.


        :param payment: The payment of this CreatePaymentConsentData.  # noqa: E501
        :type: PaymentConsent
        """
        if payment is None:
            raise ValueError("Invalid value for `payment`, must not be `None`")  # noqa: E501

        self._payment = payment

    @property
    def debtor_account(self):
        """Gets the debtor_account of this CreatePaymentConsentData.  # noqa: E501


        :return: The debtor_account of this CreatePaymentConsentData.  # noqa: E501
        :rtype: DebtorAccount
        """
        return self._debtor_account

    @debtor_account.setter
    def debtor_account(self, debtor_account):
        """Sets the debtor_account of this CreatePaymentConsentData.


        :param debtor_account: The debtor_account of this CreatePaymentConsentData.  # noqa: E501
        :type: DebtorAccount
        """

        self._debtor_account = debtor_account

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
        if issubclass(CreatePaymentConsentData, dict):
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
        if not isinstance(other, CreatePaymentConsentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
