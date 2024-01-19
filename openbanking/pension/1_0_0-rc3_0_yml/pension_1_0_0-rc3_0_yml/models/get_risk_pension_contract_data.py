# coding: utf-8

"""
    API Pension - Open Finance Brasil

    API de Previdência do Open Finance Brasil – Fase 4. API que retorna informações de Previdência.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc3.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GetRiskPensionContractData(object):
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
        'participant': 'PensionParticipant',
        'society': 'PensionSociety',
        'name': 'str',
        'code': 'str',
        'modality': 'EnumProductModality',
        'coverages': 'list[Coverage]',
        'assistance_types': 'list[EnumAssistanceType]',
        'assistance_types_additional_infos': 'list[str]',
        'additional': 'EnumAdditional',
        'terms_and_conditions': 'list[TermsAndConditions]',
        'pmbac_remuneration': 'RiskPensionEnumPmbacRemuneration',
        'premium_update_index': 'RiskPensionEnumPremiumUpdateIndex',
        'age_adjustment': 'AgeAdjustment',
        'financial_regime_contract_type': 'RiskPensionEnumFinancialRegime',
        'reclaim': 'RiskPensionReclaim',
        'other_guaranteed_values': 'RiskPensionEnumOtherGuaranteedValues',
        'contribution_payment': 'RiskPensionEnumContributionPayment',
        'minimum_requirement': 'RiskPensionMinimumRequirement',
        'target_audience': 'str'
    }

    attribute_map = {
        'participant': 'participant',
        'society': 'society',
        'name': 'name',
        'code': 'code',
        'modality': 'modality',
        'coverages': 'coverages',
        'assistance_types': 'assistanceTypes',
        'assistance_types_additional_infos': 'assistanceTypesAdditionalInfos',
        'additional': 'additional',
        'terms_and_conditions': 'termsAndConditions',
        'pmbac_remuneration': 'pmbacRemuneration',
        'premium_update_index': 'premiumUpdateIndex',
        'age_adjustment': 'ageAdjustment',
        'financial_regime_contract_type': 'financialRegimeContractType',
        'reclaim': 'reclaim',
        'other_guaranteed_values': 'otherGuaranteedValues',
        'contribution_payment': 'contributionPayment',
        'minimum_requirement': 'minimumRequirement',
        'target_audience': 'targetAudience'
    }

    def __init__(self, participant=None, society=None, name=None, code=None, modality=None, coverages=None, assistance_types=None, assistance_types_additional_infos=None, additional=None, terms_and_conditions=None, pmbac_remuneration=None, premium_update_index=None, age_adjustment=None, financial_regime_contract_type=None, reclaim=None, other_guaranteed_values=None, contribution_payment=None, minimum_requirement=None, target_audience=None):  # noqa: E501
        """GetRiskPensionContractData - a model defined in Swagger"""  # noqa: E501
        self._participant = None
        self._society = None
        self._name = None
        self._code = None
        self._modality = None
        self._coverages = None
        self._assistance_types = None
        self._assistance_types_additional_infos = None
        self._additional = None
        self._terms_and_conditions = None
        self._pmbac_remuneration = None
        self._premium_update_index = None
        self._age_adjustment = None
        self._financial_regime_contract_type = None
        self._reclaim = None
        self._other_guaranteed_values = None
        self._contribution_payment = None
        self._minimum_requirement = None
        self._target_audience = None
        self.discriminator = None
        self.participant = participant
        self.society = society
        self.name = name
        self.code = code
        self.modality = modality
        self.coverages = coverages
        if assistance_types is not None:
            self.assistance_types = assistance_types
        if assistance_types_additional_infos is not None:
            self.assistance_types_additional_infos = assistance_types_additional_infos
        if additional is not None:
            self.additional = additional
        self.terms_and_conditions = terms_and_conditions
        if pmbac_remuneration is not None:
            self.pmbac_remuneration = pmbac_remuneration
        self.premium_update_index = premium_update_index
        if age_adjustment is not None:
            self.age_adjustment = age_adjustment
        if financial_regime_contract_type is not None:
            self.financial_regime_contract_type = financial_regime_contract_type
        if reclaim is not None:
            self.reclaim = reclaim
        self.other_guaranteed_values = other_guaranteed_values
        self.contribution_payment = contribution_payment
        self.minimum_requirement = minimum_requirement
        self.target_audience = target_audience

    @property
    def participant(self):
        """Gets the participant of this GetRiskPensionContractData.  # noqa: E501


        :return: The participant of this GetRiskPensionContractData.  # noqa: E501
        :rtype: PensionParticipant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this GetRiskPensionContractData.


        :param participant: The participant of this GetRiskPensionContractData.  # noqa: E501
        :type: PensionParticipant
        """
        if participant is None:
            raise ValueError("Invalid value for `participant`, must not be `None`")  # noqa: E501

        self._participant = participant

    @property
    def society(self):
        """Gets the society of this GetRiskPensionContractData.  # noqa: E501


        :return: The society of this GetRiskPensionContractData.  # noqa: E501
        :rtype: PensionSociety
        """
        return self._society

    @society.setter
    def society(self, society):
        """Sets the society of this GetRiskPensionContractData.


        :param society: The society of this GetRiskPensionContractData.  # noqa: E501
        :type: PensionSociety
        """
        if society is None:
            raise ValueError("Invalid value for `society`, must not be `None`")  # noqa: E501

        self._society = society

    @property
    def name(self):
        """Gets the name of this GetRiskPensionContractData.  # noqa: E501

        Nome comercial do produto, pelo qual é identificado nos canais de distribuição e atendimento da sociedade.  # noqa: E501

        :return: The name of this GetRiskPensionContractData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetRiskPensionContractData.

        Nome comercial do produto, pelo qual é identificado nos canais de distribuição e atendimento da sociedade.  # noqa: E501

        :param name: The name of this GetRiskPensionContractData.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def code(self):
        """Gets the code of this GetRiskPensionContractData.  # noqa: E501

        Código único a ser definido pela sociedade.  # noqa: E501

        :return: The code of this GetRiskPensionContractData.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this GetRiskPensionContractData.

        Código único a ser definido pela sociedade.  # noqa: E501

        :param code: The code of this GetRiskPensionContractData.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def modality(self):
        """Gets the modality of this GetRiskPensionContractData.  # noqa: E501


        :return: The modality of this GetRiskPensionContractData.  # noqa: E501
        :rtype: EnumProductModality
        """
        return self._modality

    @modality.setter
    def modality(self, modality):
        """Sets the modality of this GetRiskPensionContractData.


        :param modality: The modality of this GetRiskPensionContractData.  # noqa: E501
        :type: EnumProductModality
        """
        if modality is None:
            raise ValueError("Invalid value for `modality`, must not be `None`")  # noqa: E501

        self._modality = modality

    @property
    def coverages(self):
        """Gets the coverages of this GetRiskPensionContractData.  # noqa: E501


        :return: The coverages of this GetRiskPensionContractData.  # noqa: E501
        :rtype: list[Coverage]
        """
        return self._coverages

    @coverages.setter
    def coverages(self, coverages):
        """Sets the coverages of this GetRiskPensionContractData.


        :param coverages: The coverages of this GetRiskPensionContractData.  # noqa: E501
        :type: list[Coverage]
        """
        if coverages is None:
            raise ValueError("Invalid value for `coverages`, must not be `None`")  # noqa: E501

        self._coverages = coverages

    @property
    def assistance_types(self):
        """Gets the assistance_types of this GetRiskPensionContractData.  # noqa: E501


        :return: The assistance_types of this GetRiskPensionContractData.  # noqa: E501
        :rtype: list[EnumAssistanceType]
        """
        return self._assistance_types

    @assistance_types.setter
    def assistance_types(self, assistance_types):
        """Sets the assistance_types of this GetRiskPensionContractData.


        :param assistance_types: The assistance_types of this GetRiskPensionContractData.  # noqa: E501
        :type: list[EnumAssistanceType]
        """

        self._assistance_types = assistance_types

    @property
    def assistance_types_additional_infos(self):
        """Gets the assistance_types_additional_infos of this GetRiskPensionContractData.  # noqa: E501

        Lista a ser preenchida pelas participantes quando houver 'Outros' no campo 'Tipo de Assistência'.  # noqa: E501

        :return: The assistance_types_additional_infos of this GetRiskPensionContractData.  # noqa: E501
        :rtype: list[str]
        """
        return self._assistance_types_additional_infos

    @assistance_types_additional_infos.setter
    def assistance_types_additional_infos(self, assistance_types_additional_infos):
        """Sets the assistance_types_additional_infos of this GetRiskPensionContractData.

        Lista a ser preenchida pelas participantes quando houver 'Outros' no campo 'Tipo de Assistência'.  # noqa: E501

        :param assistance_types_additional_infos: The assistance_types_additional_infos of this GetRiskPensionContractData.  # noqa: E501
        :type: list[str]
        """

        self._assistance_types_additional_infos = assistance_types_additional_infos

    @property
    def additional(self):
        """Gets the additional of this GetRiskPensionContractData.  # noqa: E501


        :return: The additional of this GetRiskPensionContractData.  # noqa: E501
        :rtype: EnumAdditional
        """
        return self._additional

    @additional.setter
    def additional(self, additional):
        """Sets the additional of this GetRiskPensionContractData.


        :param additional: The additional of this GetRiskPensionContractData.  # noqa: E501
        :type: EnumAdditional
        """

        self._additional = additional

    @property
    def terms_and_conditions(self):
        """Gets the terms_and_conditions of this GetRiskPensionContractData.  # noqa: E501


        :return: The terms_and_conditions of this GetRiskPensionContractData.  # noqa: E501
        :rtype: list[TermsAndConditions]
        """
        return self._terms_and_conditions

    @terms_and_conditions.setter
    def terms_and_conditions(self, terms_and_conditions):
        """Sets the terms_and_conditions of this GetRiskPensionContractData.


        :param terms_and_conditions: The terms_and_conditions of this GetRiskPensionContractData.  # noqa: E501
        :type: list[TermsAndConditions]
        """
        if terms_and_conditions is None:
            raise ValueError("Invalid value for `terms_and_conditions`, must not be `None`")  # noqa: E501

        self._terms_and_conditions = terms_and_conditions

    @property
    def pmbac_remuneration(self):
        """Gets the pmbac_remuneration of this GetRiskPensionContractData.  # noqa: E501


        :return: The pmbac_remuneration of this GetRiskPensionContractData.  # noqa: E501
        :rtype: RiskPensionEnumPmbacRemuneration
        """
        return self._pmbac_remuneration

    @pmbac_remuneration.setter
    def pmbac_remuneration(self, pmbac_remuneration):
        """Sets the pmbac_remuneration of this GetRiskPensionContractData.


        :param pmbac_remuneration: The pmbac_remuneration of this GetRiskPensionContractData.  # noqa: E501
        :type: RiskPensionEnumPmbacRemuneration
        """

        self._pmbac_remuneration = pmbac_remuneration

    @property
    def premium_update_index(self):
        """Gets the premium_update_index of this GetRiskPensionContractData.  # noqa: E501


        :return: The premium_update_index of this GetRiskPensionContractData.  # noqa: E501
        :rtype: RiskPensionEnumPremiumUpdateIndex
        """
        return self._premium_update_index

    @premium_update_index.setter
    def premium_update_index(self, premium_update_index):
        """Sets the premium_update_index of this GetRiskPensionContractData.


        :param premium_update_index: The premium_update_index of this GetRiskPensionContractData.  # noqa: E501
        :type: RiskPensionEnumPremiumUpdateIndex
        """
        if premium_update_index is None:
            raise ValueError("Invalid value for `premium_update_index`, must not be `None`")  # noqa: E501

        self._premium_update_index = premium_update_index

    @property
    def age_adjustment(self):
        """Gets the age_adjustment of this GetRiskPensionContractData.  # noqa: E501


        :return: The age_adjustment of this GetRiskPensionContractData.  # noqa: E501
        :rtype: AgeAdjustment
        """
        return self._age_adjustment

    @age_adjustment.setter
    def age_adjustment(self, age_adjustment):
        """Sets the age_adjustment of this GetRiskPensionContractData.


        :param age_adjustment: The age_adjustment of this GetRiskPensionContractData.  # noqa: E501
        :type: AgeAdjustment
        """

        self._age_adjustment = age_adjustment

    @property
    def financial_regime_contract_type(self):
        """Gets the financial_regime_contract_type of this GetRiskPensionContractData.  # noqa: E501


        :return: The financial_regime_contract_type of this GetRiskPensionContractData.  # noqa: E501
        :rtype: RiskPensionEnumFinancialRegime
        """
        return self._financial_regime_contract_type

    @financial_regime_contract_type.setter
    def financial_regime_contract_type(self, financial_regime_contract_type):
        """Sets the financial_regime_contract_type of this GetRiskPensionContractData.


        :param financial_regime_contract_type: The financial_regime_contract_type of this GetRiskPensionContractData.  # noqa: E501
        :type: RiskPensionEnumFinancialRegime
        """

        self._financial_regime_contract_type = financial_regime_contract_type

    @property
    def reclaim(self):
        """Gets the reclaim of this GetRiskPensionContractData.  # noqa: E501


        :return: The reclaim of this GetRiskPensionContractData.  # noqa: E501
        :rtype: RiskPensionReclaim
        """
        return self._reclaim

    @reclaim.setter
    def reclaim(self, reclaim):
        """Sets the reclaim of this GetRiskPensionContractData.


        :param reclaim: The reclaim of this GetRiskPensionContractData.  # noqa: E501
        :type: RiskPensionReclaim
        """

        self._reclaim = reclaim

    @property
    def other_guaranteed_values(self):
        """Gets the other_guaranteed_values of this GetRiskPensionContractData.  # noqa: E501


        :return: The other_guaranteed_values of this GetRiskPensionContractData.  # noqa: E501
        :rtype: RiskPensionEnumOtherGuaranteedValues
        """
        return self._other_guaranteed_values

    @other_guaranteed_values.setter
    def other_guaranteed_values(self, other_guaranteed_values):
        """Sets the other_guaranteed_values of this GetRiskPensionContractData.


        :param other_guaranteed_values: The other_guaranteed_values of this GetRiskPensionContractData.  # noqa: E501
        :type: RiskPensionEnumOtherGuaranteedValues
        """
        if other_guaranteed_values is None:
            raise ValueError("Invalid value for `other_guaranteed_values`, must not be `None`")  # noqa: E501

        self._other_guaranteed_values = other_guaranteed_values

    @property
    def contribution_payment(self):
        """Gets the contribution_payment of this GetRiskPensionContractData.  # noqa: E501


        :return: The contribution_payment of this GetRiskPensionContractData.  # noqa: E501
        :rtype: RiskPensionEnumContributionPayment
        """
        return self._contribution_payment

    @contribution_payment.setter
    def contribution_payment(self, contribution_payment):
        """Sets the contribution_payment of this GetRiskPensionContractData.


        :param contribution_payment: The contribution_payment of this GetRiskPensionContractData.  # noqa: E501
        :type: RiskPensionEnumContributionPayment
        """
        if contribution_payment is None:
            raise ValueError("Invalid value for `contribution_payment`, must not be `None`")  # noqa: E501

        self._contribution_payment = contribution_payment

    @property
    def minimum_requirement(self):
        """Gets the minimum_requirement of this GetRiskPensionContractData.  # noqa: E501


        :return: The minimum_requirement of this GetRiskPensionContractData.  # noqa: E501
        :rtype: RiskPensionMinimumRequirement
        """
        return self._minimum_requirement

    @minimum_requirement.setter
    def minimum_requirement(self, minimum_requirement):
        """Sets the minimum_requirement of this GetRiskPensionContractData.


        :param minimum_requirement: The minimum_requirement of this GetRiskPensionContractData.  # noqa: E501
        :type: RiskPensionMinimumRequirement
        """
        if minimum_requirement is None:
            raise ValueError("Invalid value for `minimum_requirement`, must not be `None`")  # noqa: E501

        self._minimum_requirement = minimum_requirement

    @property
    def target_audience(self):
        """Gets the target_audience of this GetRiskPensionContractData.  # noqa: E501

        A considerar os domínios abaixo:    1. Pessoa Natural   2. Pessoa Jurídica   3. Ambas (Pessoa Natural e Jurídica)   4. NA   # noqa: E501

        :return: The target_audience of this GetRiskPensionContractData.  # noqa: E501
        :rtype: str
        """
        return self._target_audience

    @target_audience.setter
    def target_audience(self, target_audience):
        """Sets the target_audience of this GetRiskPensionContractData.

        A considerar os domínios abaixo:    1. Pessoa Natural   2. Pessoa Jurídica   3. Ambas (Pessoa Natural e Jurídica)   4. NA   # noqa: E501

        :param target_audience: The target_audience of this GetRiskPensionContractData.  # noqa: E501
        :type: str
        """
        if target_audience is None:
            raise ValueError("Invalid value for `target_audience`, must not be `None`")  # noqa: E501
        allowed_values = ["PESSOA_NATURAL", "PESSOA_JURIDICA", "PESSOA_NATURAL_JURIDICA", "NA"]  # noqa: E501
        if target_audience not in allowed_values:
            raise ValueError(
                "Invalid value for `target_audience` ({0}), must be one of {1}"  # noqa: E501
                .format(target_audience, allowed_values)
            )

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
        if issubclass(GetRiskPensionContractData, dict):
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
        if not isinstance(other, GetRiskPensionContractData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other