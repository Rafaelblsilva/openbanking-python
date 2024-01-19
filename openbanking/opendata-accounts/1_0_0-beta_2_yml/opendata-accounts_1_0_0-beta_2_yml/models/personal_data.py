# coding: utf-8

"""
    API OpenData Accounts do Open Finance Brasil

    A API descrita neste documento é referente as API Accounts da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-beta.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalData(object):
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
        'participant': 'PersonalDataParticipant',
        'type': 'AccountType',
        'fees': 'AccountFee',
        'service_bundles': 'list[ServiceBundle]',
        'opening_closing_channels': 'list[OpeningClosingChannels]',
        'opening_closing_channels_additional_info': 'str',
        'transaction_methods': 'list[TransactionMethods]',
        'terms_conditions': 'AccountsTermsConditions',
        'income_rate': 'AccountsIncomeRate'
    }

    attribute_map = {
        'participant': 'participant',
        'type': 'type',
        'fees': 'fees',
        'service_bundles': 'serviceBundles',
        'opening_closing_channels': 'openingClosingChannels',
        'opening_closing_channels_additional_info': 'openingClosingChannelsAdditionalInfo',
        'transaction_methods': 'transactionMethods',
        'terms_conditions': 'termsConditions',
        'income_rate': 'incomeRate'
    }

    def __init__(self, participant=None, type=None, fees=None, service_bundles=None, opening_closing_channels=None, opening_closing_channels_additional_info=None, transaction_methods=None, terms_conditions=None, income_rate=None):  # noqa: E501
        """PersonalData - a model defined in Swagger"""  # noqa: E501
        self._participant = None
        self._type = None
        self._fees = None
        self._service_bundles = None
        self._opening_closing_channels = None
        self._opening_closing_channels_additional_info = None
        self._transaction_methods = None
        self._terms_conditions = None
        self._income_rate = None
        self.discriminator = None
        self.participant = participant
        self.type = type
        self.fees = fees
        if service_bundles is not None:
            self.service_bundles = service_bundles
        self.opening_closing_channels = opening_closing_channels
        if opening_closing_channels_additional_info is not None:
            self.opening_closing_channels_additional_info = opening_closing_channels_additional_info
        self.transaction_methods = transaction_methods
        self.terms_conditions = terms_conditions
        if income_rate is not None:
            self.income_rate = income_rate

    @property
    def participant(self):
        """Gets the participant of this PersonalData.  # noqa: E501


        :return: The participant of this PersonalData.  # noqa: E501
        :rtype: PersonalDataParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this PersonalData.


        :param participant: The participant of this PersonalData.  # noqa: E501
        :type: PersonalDataParticipant
        """
        if participant is None:
            raise ValueError("Invalid value for `participant`, must not be `None`")  # noqa: E501

        self._participant = participant

    @property
    def type(self):
        """Gets the type of this PersonalData.  # noqa: E501


        :return: The type of this PersonalData.  # noqa: E501
        :rtype: AccountType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PersonalData.


        :param type: The type of this PersonalData.  # noqa: E501
        :type: AccountType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def fees(self):
        """Gets the fees of this PersonalData.  # noqa: E501


        :return: The fees of this PersonalData.  # noqa: E501
        :rtype: AccountFee
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this PersonalData.


        :param fees: The fees of this PersonalData.  # noqa: E501
        :type: AccountFee
        """
        if fees is None:
            raise ValueError("Invalid value for `fees`, must not be `None`")  # noqa: E501

        self._fees = fees

    @property
    def service_bundles(self):
        """Gets the service_bundles of this PersonalData.  # noqa: E501

        Lista dos pacotes de serviços de contas com serviços essenciais padronizados e regulados pela Resolução BC 3919, de 25/11/2010  [Restrição] - Obrigatório quando \"type\" for igual \"CONTA_DEPOSITO_A_VISTA\" (conta corrente) ou \"CONTA_POUPANCA\", porque existem hoje pacotes passíveis de cobrança diferentes dos serviços essenciais (que não são cobrados);  - Opcional quando \"type\" for igual \"CONTA_PAGAMENTO_PRE_PAGA\" ficando condicionado caso a instituição tenha pacote de serviço atrelado a este tipo de conta.   # noqa: E501

        :return: The service_bundles of this PersonalData.  # noqa: E501
        :rtype: list[ServiceBundle]
        """
        return self._service_bundles

    @service_bundles.setter
    def service_bundles(self, service_bundles):
        """Sets the service_bundles of this PersonalData.

        Lista dos pacotes de serviços de contas com serviços essenciais padronizados e regulados pela Resolução BC 3919, de 25/11/2010  [Restrição] - Obrigatório quando \"type\" for igual \"CONTA_DEPOSITO_A_VISTA\" (conta corrente) ou \"CONTA_POUPANCA\", porque existem hoje pacotes passíveis de cobrança diferentes dos serviços essenciais (que não são cobrados);  - Opcional quando \"type\" for igual \"CONTA_PAGAMENTO_PRE_PAGA\" ficando condicionado caso a instituição tenha pacote de serviço atrelado a este tipo de conta.   # noqa: E501

        :param service_bundles: The service_bundles of this PersonalData.  # noqa: E501
        :type: list[ServiceBundle]
        """

        self._service_bundles = service_bundles

    @property
    def opening_closing_channels(self):
        """Gets the opening_closing_channels of this PersonalData.  # noqa: E501

        Lista dos canais para aberturas e encerramento  # noqa: E501

        :return: The opening_closing_channels of this PersonalData.  # noqa: E501
        :rtype: list[OpeningClosingChannels]
        """
        return self._opening_closing_channels

    @opening_closing_channels.setter
    def opening_closing_channels(self, opening_closing_channels):
        """Sets the opening_closing_channels of this PersonalData.

        Lista dos canais para aberturas e encerramento  # noqa: E501

        :param opening_closing_channels: The opening_closing_channels of this PersonalData.  # noqa: E501
        :type: list[OpeningClosingChannels]
        """
        if opening_closing_channels is None:
            raise ValueError("Invalid value for `opening_closing_channels`, must not be `None`")  # noqa: E501

        self._opening_closing_channels = opening_closing_channels

    @property
    def opening_closing_channels_additional_info(self):
        """Gets the opening_closing_channels_additional_info of this PersonalData.  # noqa: E501

        Campo livre para preenchimento das informações adicionais referente ao \"openingClosingChannels\".   [Restrição] Obrigatório quando \"openingClosingChannels\" for igual 'OUTROS'.   # noqa: E501

        :return: The opening_closing_channels_additional_info of this PersonalData.  # noqa: E501
        :rtype: str
        """
        return self._opening_closing_channels_additional_info

    @opening_closing_channels_additional_info.setter
    def opening_closing_channels_additional_info(self, opening_closing_channels_additional_info):
        """Sets the opening_closing_channels_additional_info of this PersonalData.

        Campo livre para preenchimento das informações adicionais referente ao \"openingClosingChannels\".   [Restrição] Obrigatório quando \"openingClosingChannels\" for igual 'OUTROS'.   # noqa: E501

        :param opening_closing_channels_additional_info: The opening_closing_channels_additional_info of this PersonalData.  # noqa: E501
        :type: str
        """

        self._opening_closing_channels_additional_info = opening_closing_channels_additional_info

    @property
    def transaction_methods(self):
        """Gets the transaction_methods of this PersonalData.  # noqa: E501

        Lista de formas de movimentação  # noqa: E501

        :return: The transaction_methods of this PersonalData.  # noqa: E501
        :rtype: list[TransactionMethods]
        """
        return self._transaction_methods

    @transaction_methods.setter
    def transaction_methods(self, transaction_methods):
        """Sets the transaction_methods of this PersonalData.

        Lista de formas de movimentação  # noqa: E501

        :param transaction_methods: The transaction_methods of this PersonalData.  # noqa: E501
        :type: list[TransactionMethods]
        """
        if transaction_methods is None:
            raise ValueError("Invalid value for `transaction_methods`, must not be `None`")  # noqa: E501

        self._transaction_methods = transaction_methods

    @property
    def terms_conditions(self):
        """Gets the terms_conditions of this PersonalData.  # noqa: E501


        :return: The terms_conditions of this PersonalData.  # noqa: E501
        :rtype: AccountsTermsConditions
        """
        return self._terms_conditions

    @terms_conditions.setter
    def terms_conditions(self, terms_conditions):
        """Sets the terms_conditions of this PersonalData.


        :param terms_conditions: The terms_conditions of this PersonalData.  # noqa: E501
        :type: AccountsTermsConditions
        """
        if terms_conditions is None:
            raise ValueError("Invalid value for `terms_conditions`, must not be `None`")  # noqa: E501

        self._terms_conditions = terms_conditions

    @property
    def income_rate(self):
        """Gets the income_rate of this PersonalData.  # noqa: E501


        :return: The income_rate of this PersonalData.  # noqa: E501
        :rtype: AccountsIncomeRate
        """
        return self._income_rate

    @income_rate.setter
    def income_rate(self, income_rate):
        """Sets the income_rate of this PersonalData.


        :param income_rate: The income_rate of this PersonalData.  # noqa: E501
        :type: AccountsIncomeRate
        """

        self._income_rate = income_rate

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
        if issubclass(PersonalData, dict):
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
        if not isinstance(other, PersonalData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
