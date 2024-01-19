# coding: utf-8

"""
    API Investments - Open Finance Brasil

    Estas APIs visam o compartilhamento de dados sobre Investimentos e suas características entre as Instituições Financeiras participantes do Open Finance Brasil   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InvestmentsFixedIncomeBank(object):
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
        'participant': 'InvestmentsParticipant',
        'issuer_institution_cnpj_number': 'str',
        'issuer_institution_name': 'str',
        'investment_type': 'EnumInvestmentsFixedIncomeBankProductType',
        'index': 'InvestmentsFixedIncomeBankIndex',
        'investment_conditions': 'InvestmentsFixedIncomeBankInvestmentConditions',
        'target_audience': 'EnumDistinctTargetAudience'
    }

    attribute_map = {
        'participant': 'participant',
        'issuer_institution_cnpj_number': 'issuerInstitutionCnpjNumber',
        'issuer_institution_name': 'issuerInstitutionName',
        'investment_type': 'investmentType',
        'index': 'index',
        'investment_conditions': 'investmentConditions',
        'target_audience': 'targetAudience'
    }

    def __init__(self, participant=None, issuer_institution_cnpj_number=None, issuer_institution_name=None, investment_type=None, index=None, investment_conditions=None, target_audience=None):  # noqa: E501
        """InvestmentsFixedIncomeBank - a model defined in Swagger"""  # noqa: E501
        self._participant = None
        self._issuer_institution_cnpj_number = None
        self._issuer_institution_name = None
        self._investment_type = None
        self._index = None
        self._investment_conditions = None
        self._target_audience = None
        self.discriminator = None
        self.participant = participant
        self.issuer_institution_cnpj_number = issuer_institution_cnpj_number
        self.issuer_institution_name = issuer_institution_name
        self.investment_type = investment_type
        self.index = index
        self.investment_conditions = investment_conditions
        self.target_audience = target_audience

    @property
    def participant(self):
        """Gets the participant of this InvestmentsFixedIncomeBank.  # noqa: E501


        :return: The participant of this InvestmentsFixedIncomeBank.  # noqa: E501
        :rtype: InvestmentsParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this InvestmentsFixedIncomeBank.


        :param participant: The participant of this InvestmentsFixedIncomeBank.  # noqa: E501
        :type: InvestmentsParticipant
        """
        if participant is None:
            raise ValueError("Invalid value for `participant`, must not be `None`")  # noqa: E501

        self._participant = participant

    @property
    def issuer_institution_cnpj_number(self):
        """Gets the issuer_institution_cnpj_number of this InvestmentsFixedIncomeBank.  # noqa: E501

        CNPJ da instituição emissora.  # noqa: E501

        :return: The issuer_institution_cnpj_number of this InvestmentsFixedIncomeBank.  # noqa: E501
        :rtype: str
        """
        return self._issuer_institution_cnpj_number

    @issuer_institution_cnpj_number.setter
    def issuer_institution_cnpj_number(self, issuer_institution_cnpj_number):
        """Sets the issuer_institution_cnpj_number of this InvestmentsFixedIncomeBank.

        CNPJ da instituição emissora.  # noqa: E501

        :param issuer_institution_cnpj_number: The issuer_institution_cnpj_number of this InvestmentsFixedIncomeBank.  # noqa: E501
        :type: str
        """
        if issuer_institution_cnpj_number is None:
            raise ValueError("Invalid value for `issuer_institution_cnpj_number`, must not be `None`")  # noqa: E501

        self._issuer_institution_cnpj_number = issuer_institution_cnpj_number

    @property
    def issuer_institution_name(self):
        """Gets the issuer_institution_name of this InvestmentsFixedIncomeBank.  # noqa: E501

        Nome da instituição emissora.  # noqa: E501

        :return: The issuer_institution_name of this InvestmentsFixedIncomeBank.  # noqa: E501
        :rtype: str
        """
        return self._issuer_institution_name

    @issuer_institution_name.setter
    def issuer_institution_name(self, issuer_institution_name):
        """Sets the issuer_institution_name of this InvestmentsFixedIncomeBank.

        Nome da instituição emissora.  # noqa: E501

        :param issuer_institution_name: The issuer_institution_name of this InvestmentsFixedIncomeBank.  # noqa: E501
        :type: str
        """
        if issuer_institution_name is None:
            raise ValueError("Invalid value for `issuer_institution_name`, must not be `None`")  # noqa: E501

        self._issuer_institution_name = issuer_institution_name

    @property
    def investment_type(self):
        """Gets the investment_type of this InvestmentsFixedIncomeBank.  # noqa: E501


        :return: The investment_type of this InvestmentsFixedIncomeBank.  # noqa: E501
        :rtype: EnumInvestmentsFixedIncomeBankProductType
        """
        return self._investment_type

    @investment_type.setter
    def investment_type(self, investment_type):
        """Sets the investment_type of this InvestmentsFixedIncomeBank.


        :param investment_type: The investment_type of this InvestmentsFixedIncomeBank.  # noqa: E501
        :type: EnumInvestmentsFixedIncomeBankProductType
        """
        if investment_type is None:
            raise ValueError("Invalid value for `investment_type`, must not be `None`")  # noqa: E501

        self._investment_type = investment_type

    @property
    def index(self):
        """Gets the index of this InvestmentsFixedIncomeBank.  # noqa: E501


        :return: The index of this InvestmentsFixedIncomeBank.  # noqa: E501
        :rtype: InvestmentsFixedIncomeBankIndex
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this InvestmentsFixedIncomeBank.


        :param index: The index of this InvestmentsFixedIncomeBank.  # noqa: E501
        :type: InvestmentsFixedIncomeBankIndex
        """
        if index is None:
            raise ValueError("Invalid value for `index`, must not be `None`")  # noqa: E501

        self._index = index

    @property
    def investment_conditions(self):
        """Gets the investment_conditions of this InvestmentsFixedIncomeBank.  # noqa: E501


        :return: The investment_conditions of this InvestmentsFixedIncomeBank.  # noqa: E501
        :rtype: InvestmentsFixedIncomeBankInvestmentConditions
        """
        return self._investment_conditions

    @investment_conditions.setter
    def investment_conditions(self, investment_conditions):
        """Sets the investment_conditions of this InvestmentsFixedIncomeBank.


        :param investment_conditions: The investment_conditions of this InvestmentsFixedIncomeBank.  # noqa: E501
        :type: InvestmentsFixedIncomeBankInvestmentConditions
        """
        if investment_conditions is None:
            raise ValueError("Invalid value for `investment_conditions`, must not be `None`")  # noqa: E501

        self._investment_conditions = investment_conditions

    @property
    def target_audience(self):
        """Gets the target_audience of this InvestmentsFixedIncomeBank.  # noqa: E501


        :return: The target_audience of this InvestmentsFixedIncomeBank.  # noqa: E501
        :rtype: EnumDistinctTargetAudience
        """
        return self._target_audience

    @target_audience.setter
    def target_audience(self, target_audience):
        """Sets the target_audience of this InvestmentsFixedIncomeBank.


        :param target_audience: The target_audience of this InvestmentsFixedIncomeBank.  # noqa: E501
        :type: EnumDistinctTargetAudience
        """
        if target_audience is None:
            raise ValueError("Invalid value for `target_audience`, must not be `None`")  # noqa: E501

        self._target_audience = target_audience

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
        if issubclass(InvestmentsFixedIncomeBank, dict):
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
        if not isinstance(other, InvestmentsFixedIncomeBank):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
