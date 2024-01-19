# coding: utf-8

"""
    API Credit-cards-accounts - Open Banking Brasil

    API de contas de pagamento pós-pagas do Open Banking Brasil – Fase 2. API que retorna informações de contas de pagamento pós-paga mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, produto, bandeira, limites de crédito, informações sobre transações de pagamento efetuadas e faturas.  Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.   # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.    ## Permissions necessárias para a API Credit-cards-accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_READ** ### `/accounts/{creditCardAccountId}/bills`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_READ** ### `/accounts/{creditCardAccountId}/{billId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ** ### `/accounts/{creditCardAccountId}/limits`           - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_LIMITS_READ** ### `/accounts/{creditCardAccountId}/transactions`   - permissions:     - GET: **CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.5
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditCardsAccountsIdentificationData(object):
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
        'name': 'str',
        'product_type': 'EnumCreditCardAccountsProductType',
        'product_additional_info': 'str',
        'credit_card_network': 'EnumCreditCardAccountNetwork',
        'network_additional_info': 'str',
        'payment_method': 'CreditCardsAccountPaymentMethod'
    }

    attribute_map = {
        'name': 'name',
        'product_type': 'productType',
        'product_additional_info': 'productAdditionalInfo',
        'credit_card_network': 'creditCardNetwork',
        'network_additional_info': 'networkAdditionalInfo',
        'payment_method': 'paymentMethod'
    }

    def __init__(self, name=None, product_type=None, product_additional_info=None, credit_card_network=None, network_additional_info=None, payment_method=None):  # noqa: E501
        """CreditCardsAccountsIdentificationData - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._product_type = None
        self._product_additional_info = None
        self._credit_card_network = None
        self._network_additional_info = None
        self._payment_method = None
        self.discriminator = None
        self.name = name
        self.product_type = product_type
        if product_additional_info is not None:
            self.product_additional_info = product_additional_info
        self.credit_card_network = credit_card_network
        if network_additional_info is not None:
            self.network_additional_info = network_additional_info
        self.payment_method = payment_method

    @property
    def name(self):
        """Gets the name of this CreditCardsAccountsIdentificationData.  # noqa: E501

        Denominação/Identificação do nome da conta de pagamento pós-paga (cartão). Conforme CIRCULAR Nº 3.680,BCB, 2013: 'conta de pagamento pós-paga: destinada à execução de transações de pagamento que independem do aporte prévio de recursos'.   # noqa: E501

        :return: The name of this CreditCardsAccountsIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreditCardsAccountsIdentificationData.

        Denominação/Identificação do nome da conta de pagamento pós-paga (cartão). Conforme CIRCULAR Nº 3.680,BCB, 2013: 'conta de pagamento pós-paga: destinada à execução de transações de pagamento que independem do aporte prévio de recursos'.   # noqa: E501

        :param name: The name of this CreditCardsAccountsIdentificationData.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def product_type(self):
        """Gets the product_type of this CreditCardsAccountsIdentificationData.  # noqa: E501


        :return: The product_type of this CreditCardsAccountsIdentificationData.  # noqa: E501
        :rtype: EnumCreditCardAccountsProductType
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this CreditCardsAccountsIdentificationData.


        :param product_type: The product_type of this CreditCardsAccountsIdentificationData.  # noqa: E501
        :type: EnumCreditCardAccountsProductType
        """
        if product_type is None:
            raise ValueError("Invalid value for `product_type`, must not be `None`")  # noqa: E501

        self._product_type = product_type

    @property
    def product_additional_info(self):
        """Gets the product_additional_info of this CreditCardsAccountsIdentificationData.  # noqa: E501

        Informações complementares se tipo de Cartão 'OUTROS'  # noqa: E501

        :return: The product_additional_info of this CreditCardsAccountsIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._product_additional_info

    @product_additional_info.setter
    def product_additional_info(self, product_additional_info):
        """Sets the product_additional_info of this CreditCardsAccountsIdentificationData.

        Informações complementares se tipo de Cartão 'OUTROS'  # noqa: E501

        :param product_additional_info: The product_additional_info of this CreditCardsAccountsIdentificationData.  # noqa: E501
        :type: str
        """

        self._product_additional_info = product_additional_info

    @property
    def credit_card_network(self):
        """Gets the credit_card_network of this CreditCardsAccountsIdentificationData.  # noqa: E501


        :return: The credit_card_network of this CreditCardsAccountsIdentificationData.  # noqa: E501
        :rtype: EnumCreditCardAccountNetwork
        """
        return self._credit_card_network

    @credit_card_network.setter
    def credit_card_network(self, credit_card_network):
        """Sets the credit_card_network of this CreditCardsAccountsIdentificationData.


        :param credit_card_network: The credit_card_network of this CreditCardsAccountsIdentificationData.  # noqa: E501
        :type: EnumCreditCardAccountNetwork
        """
        if credit_card_network is None:
            raise ValueError("Invalid value for `credit_card_network`, must not be `None`")  # noqa: E501

        self._credit_card_network = credit_card_network

    @property
    def network_additional_info(self):
        """Gets the network_additional_info of this CreditCardsAccountsIdentificationData.  # noqa: E501

        Texto livre para especificar categoria de bandeira marcada como 'OUTRAS'.  # noqa: E501

        :return: The network_additional_info of this CreditCardsAccountsIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._network_additional_info

    @network_additional_info.setter
    def network_additional_info(self, network_additional_info):
        """Sets the network_additional_info of this CreditCardsAccountsIdentificationData.

        Texto livre para especificar categoria de bandeira marcada como 'OUTRAS'.  # noqa: E501

        :param network_additional_info: The network_additional_info of this CreditCardsAccountsIdentificationData.  # noqa: E501
        :type: str
        """

        self._network_additional_info = network_additional_info

    @property
    def payment_method(self):
        """Gets the payment_method of this CreditCardsAccountsIdentificationData.  # noqa: E501


        :return: The payment_method of this CreditCardsAccountsIdentificationData.  # noqa: E501
        :rtype: CreditCardsAccountPaymentMethod
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this CreditCardsAccountsIdentificationData.


        :param payment_method: The payment_method of this CreditCardsAccountsIdentificationData.  # noqa: E501
        :type: CreditCardsAccountPaymentMethod
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501

        self._payment_method = payment_method

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
        if issubclass(CreditCardsAccountsIdentificationData, dict):
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
        if not isinstance(other, CreditCardsAccountsIdentificationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
