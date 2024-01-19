# coding: utf-8

"""
    API Capitalization-bonds - Open Finance Brasil

    As APIs descritas neste documento é referente a API de Capitalização da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc3.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CapitalizationBondsProductIdentificationData(object):
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
        'participant': 'Participant',
        'society': 'CapitalizationBondsProductIdentificationDataSociety',
        'name': 'str',
        'code': 'str',
        'modality': 'EnumCapitalizationBondsProductModality',
        'cost_type': 'EnumCapitalizationBondsProductCostType',
        'terms_and_conditions': 'TermsAndConditions',
        'quotas': 'list[CapitalizationBondsProductQuota]',
        'validity': 'int',
        'serie_size': 'int',
        'capitalization_period': 'CapitalizationBondsProductCapitalizationPeriod',
        'late_payment': 'LatePayment',
        'contribution_payment': 'ContributionPayment',
        'redemption_percentage_end_term': 'str',
        'final_redemption_rate': 'str',
        'draws': 'list[CapitalizationBondsProductPrizeDraw]',
        'additional_info': 'str',
        'minimum_requirement_details': 'str',
        'target_audience': 'str'
    }

    attribute_map = {
        'participant': 'participant',
        'society': 'society',
        'name': 'name',
        'code': 'code',
        'modality': 'modality',
        'cost_type': 'costType',
        'terms_and_conditions': 'termsAndConditions',
        'quotas': 'quotas',
        'validity': 'validity',
        'serie_size': 'serieSize',
        'capitalization_period': 'capitalizationPeriod',
        'late_payment': 'latePayment',
        'contribution_payment': 'contributionPayment',
        'redemption_percentage_end_term': 'redemptionPercentageEndTerm',
        'final_redemption_rate': 'finalRedemptionRate',
        'draws': 'draws',
        'additional_info': 'additionalInfo',
        'minimum_requirement_details': 'minimumRequirementDetails',
        'target_audience': 'targetAudience'
    }

    def __init__(self, participant=None, society=None, name=None, code=None, modality=None, cost_type=None, terms_and_conditions=None, quotas=None, validity=None, serie_size=None, capitalization_period=None, late_payment=None, contribution_payment=None, redemption_percentage_end_term=None, final_redemption_rate=None, draws=None, additional_info=None, minimum_requirement_details=None, target_audience=None):  # noqa: E501
        """CapitalizationBondsProductIdentificationData - a model defined in Swagger"""  # noqa: E501
        self._participant = None
        self._society = None
        self._name = None
        self._code = None
        self._modality = None
        self._cost_type = None
        self._terms_and_conditions = None
        self._quotas = None
        self._validity = None
        self._serie_size = None
        self._capitalization_period = None
        self._late_payment = None
        self._contribution_payment = None
        self._redemption_percentage_end_term = None
        self._final_redemption_rate = None
        self._draws = None
        self._additional_info = None
        self._minimum_requirement_details = None
        self._target_audience = None
        self.discriminator = None
        self.participant = participant
        self.society = society
        self.name = name
        self.code = code
        self.modality = modality
        self.cost_type = cost_type
        self.terms_and_conditions = terms_and_conditions
        self.quotas = quotas
        if validity is not None:
            self.validity = validity
        if serie_size is not None:
            self.serie_size = serie_size
        self.capitalization_period = capitalization_period
        self.late_payment = late_payment
        self.contribution_payment = contribution_payment
        self.redemption_percentage_end_term = redemption_percentage_end_term
        self.final_redemption_rate = final_redemption_rate
        self.draws = draws
        self.additional_info = additional_info
        if minimum_requirement_details is not None:
            self.minimum_requirement_details = minimum_requirement_details
        self.target_audience = target_audience

    @property
    def participant(self):
        """Gets the participant of this CapitalizationBondsProductIdentificationData.  # noqa: E501


        :return: The participant of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: Participant
        """
        return self._participant

    @participant.setter
    def participant(self, participant):
        """Sets the participant of this CapitalizationBondsProductIdentificationData.


        :param participant: The participant of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: Participant
        """
        if participant is None:
            raise ValueError("Invalid value for `participant`, must not be `None`")  # noqa: E501

        self._participant = participant

    @property
    def society(self):
        """Gets the society of this CapitalizationBondsProductIdentificationData.  # noqa: E501


        :return: The society of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: CapitalizationBondsProductIdentificationDataSociety
        """
        return self._society

    @society.setter
    def society(self, society):
        """Sets the society of this CapitalizationBondsProductIdentificationData.


        :param society: The society of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: CapitalizationBondsProductIdentificationDataSociety
        """
        if society is None:
            raise ValueError("Invalid value for `society`, must not be `None`")  # noqa: E501

        self._society = society

    @property
    def name(self):
        """Gets the name of this CapitalizationBondsProductIdentificationData.  # noqa: E501

        Nome comercial do produto, pelo qual é identificado nos canais de distribuição e atendimento da sociedade.  # noqa: E501

        :return: The name of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CapitalizationBondsProductIdentificationData.

        Nome comercial do produto, pelo qual é identificado nos canais de distribuição e atendimento da sociedade.  # noqa: E501

        :param name: The name of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def code(self):
        """Gets the code of this CapitalizationBondsProductIdentificationData.  # noqa: E501

        Código único a ser definido pela sociedade.  # noqa: E501

        :return: The code of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CapitalizationBondsProductIdentificationData.

        Código único a ser definido pela sociedade.  # noqa: E501

        :param code: The code of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def modality(self):
        """Gets the modality of this CapitalizationBondsProductIdentificationData.  # noqa: E501


        :return: The modality of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: EnumCapitalizationBondsProductModality
        """
        return self._modality

    @modality.setter
    def modality(self, modality):
        """Sets the modality of this CapitalizationBondsProductIdentificationData.


        :param modality: The modality of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: EnumCapitalizationBondsProductModality
        """
        if modality is None:
            raise ValueError("Invalid value for `modality`, must not be `None`")  # noqa: E501

        self._modality = modality

    @property
    def cost_type(self):
        """Gets the cost_type of this CapitalizationBondsProductIdentificationData.  # noqa: E501


        :return: The cost_type of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: EnumCapitalizationBondsProductCostType
        """
        return self._cost_type

    @cost_type.setter
    def cost_type(self, cost_type):
        """Sets the cost_type of this CapitalizationBondsProductIdentificationData.


        :param cost_type: The cost_type of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: EnumCapitalizationBondsProductCostType
        """
        if cost_type is None:
            raise ValueError("Invalid value for `cost_type`, must not be `None`")  # noqa: E501

        self._cost_type = cost_type

    @property
    def terms_and_conditions(self):
        """Gets the terms_and_conditions of this CapitalizationBondsProductIdentificationData.  # noqa: E501


        :return: The terms_and_conditions of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: TermsAndConditions
        """
        return self._terms_and_conditions

    @terms_and_conditions.setter
    def terms_and_conditions(self, terms_and_conditions):
        """Sets the terms_and_conditions of this CapitalizationBondsProductIdentificationData.


        :param terms_and_conditions: The terms_and_conditions of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: TermsAndConditions
        """
        if terms_and_conditions is None:
            raise ValueError("Invalid value for `terms_and_conditions`, must not be `None`")  # noqa: E501

        self._terms_and_conditions = terms_and_conditions

    @property
    def quotas(self):
        """Gets the quotas of this CapitalizationBondsProductIdentificationData.  # noqa: E501

        Informações relativas às taxas da Quotas praticadas para cada Parcela  # noqa: E501

        :return: The quotas of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: list[CapitalizationBondsProductQuota]
        """
        return self._quotas

    @quotas.setter
    def quotas(self, quotas):
        """Sets the quotas of this CapitalizationBondsProductIdentificationData.

        Informações relativas às taxas da Quotas praticadas para cada Parcela  # noqa: E501

        :param quotas: The quotas of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: list[CapitalizationBondsProductQuota]
        """
        if quotas is None:
            raise ValueError("Invalid value for `quotas`, must not be `None`")  # noqa: E501

        self._quotas = quotas

    @property
    def validity(self):
        """Gets the validity of this CapitalizationBondsProductIdentificationData.  # noqa: E501

        Período entre a data de início e a data final para constituição do capital a ser pago ao(s) titular(es) do direito de resgate. Prazo de vigência do título de capitalização em meses (Resolução CNSP 384/20). Em meses.  # noqa: E501

        :return: The validity of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: int
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this CapitalizationBondsProductIdentificationData.

        Período entre a data de início e a data final para constituição do capital a ser pago ao(s) titular(es) do direito de resgate. Prazo de vigência do título de capitalização em meses (Resolução CNSP 384/20). Em meses.  # noqa: E501

        :param validity: The validity of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: int
        """

        self._validity = validity

    @property
    def serie_size(self):
        """Gets the serie_size of this CapitalizationBondsProductIdentificationData.  # noqa: E501

        Os títulos de capitalização que prevejam sorteio devem ser estruturados em séries, ou seja, em sequências ou em grupos de títulos submetidos às mesmas condições e características, à exceção do valor do pagamento.  # noqa: E501

        :return: The serie_size of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: int
        """
        return self._serie_size

    @serie_size.setter
    def serie_size(self, serie_size):
        """Sets the serie_size of this CapitalizationBondsProductIdentificationData.

        Os títulos de capitalização que prevejam sorteio devem ser estruturados em séries, ou seja, em sequências ou em grupos de títulos submetidos às mesmas condições e características, à exceção do valor do pagamento.  # noqa: E501

        :param serie_size: The serie_size of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: int
        """

        self._serie_size = serie_size

    @property
    def capitalization_period(self):
        """Gets the capitalization_period of this CapitalizationBondsProductIdentificationData.  # noqa: E501


        :return: The capitalization_period of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: CapitalizationBondsProductCapitalizationPeriod
        """
        return self._capitalization_period

    @capitalization_period.setter
    def capitalization_period(self, capitalization_period):
        """Sets the capitalization_period of this CapitalizationBondsProductIdentificationData.


        :param capitalization_period: The capitalization_period of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: CapitalizationBondsProductCapitalizationPeriod
        """
        if capitalization_period is None:
            raise ValueError("Invalid value for `capitalization_period`, must not be `None`")  # noqa: E501

        self._capitalization_period = capitalization_period

    @property
    def late_payment(self):
        """Gets the late_payment of this CapitalizationBondsProductIdentificationData.  # noqa: E501


        :return: The late_payment of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: LatePayment
        """
        return self._late_payment

    @late_payment.setter
    def late_payment(self, late_payment):
        """Sets the late_payment of this CapitalizationBondsProductIdentificationData.


        :param late_payment: The late_payment of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: LatePayment
        """
        if late_payment is None:
            raise ValueError("Invalid value for `late_payment`, must not be `None`")  # noqa: E501

        self._late_payment = late_payment

    @property
    def contribution_payment(self):
        """Gets the contribution_payment of this CapitalizationBondsProductIdentificationData.  # noqa: E501


        :return: The contribution_payment of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: ContributionPayment
        """
        return self._contribution_payment

    @contribution_payment.setter
    def contribution_payment(self, contribution_payment):
        """Sets the contribution_payment of this CapitalizationBondsProductIdentificationData.


        :param contribution_payment: The contribution_payment of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: ContributionPayment
        """
        if contribution_payment is None:
            raise ValueError("Invalid value for `contribution_payment`, must not be `None`")  # noqa: E501

        self._contribution_payment = contribution_payment

    @property
    def redemption_percentage_end_term(self):
        """Gets the redemption_percentage_end_term of this CapitalizationBondsProductIdentificationData.  # noqa: E501

        Percentual mínimo da soma das contribuições efetuadas que poderá ser resgatado ao final da vigência, tendo como condição os pagamentos das parcelas nos respectivos vencimentos.  # noqa: E501

        :return: The redemption_percentage_end_term of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._redemption_percentage_end_term

    @redemption_percentage_end_term.setter
    def redemption_percentage_end_term(self, redemption_percentage_end_term):
        """Sets the redemption_percentage_end_term of this CapitalizationBondsProductIdentificationData.

        Percentual mínimo da soma das contribuições efetuadas que poderá ser resgatado ao final da vigência, tendo como condição os pagamentos das parcelas nos respectivos vencimentos.  # noqa: E501

        :param redemption_percentage_end_term: The redemption_percentage_end_term of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: str
        """
        if redemption_percentage_end_term is None:
            raise ValueError("Invalid value for `redemption_percentage_end_term`, must not be `None`")  # noqa: E501

        self._redemption_percentage_end_term = redemption_percentage_end_term

    @property
    def final_redemption_rate(self):
        """Gets the final_redemption_rate of this CapitalizationBondsProductIdentificationData.  # noqa: E501

        Valor percentual (%) de resgate final permitido.  # noqa: E501

        :return: The final_redemption_rate of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._final_redemption_rate

    @final_redemption_rate.setter
    def final_redemption_rate(self, final_redemption_rate):
        """Sets the final_redemption_rate of this CapitalizationBondsProductIdentificationData.

        Valor percentual (%) de resgate final permitido.  # noqa: E501

        :param final_redemption_rate: The final_redemption_rate of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: str
        """
        if final_redemption_rate is None:
            raise ValueError("Invalid value for `final_redemption_rate`, must not be `None`")  # noqa: E501

        self._final_redemption_rate = final_redemption_rate

    @property
    def draws(self):
        """Gets the draws of this CapitalizationBondsProductIdentificationData.  # noqa: E501

        Informações relativas aos Sorteios  # noqa: E501

        :return: The draws of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: list[CapitalizationBondsProductPrizeDraw]
        """
        return self._draws

    @draws.setter
    def draws(self, draws):
        """Sets the draws of this CapitalizationBondsProductIdentificationData.

        Informações relativas aos Sorteios  # noqa: E501

        :param draws: The draws of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: list[CapitalizationBondsProductPrizeDraw]
        """
        if draws is None:
            raise ValueError("Invalid value for `draws`, must not be `None`")  # noqa: E501

        self._draws = draws

    @property
    def additional_info(self):
        """Gets the additional_info of this CapitalizationBondsProductIdentificationData.  # noqa: E501

        Campo aberto (possibilidade de incluir URL) Observação: As URLs são limitadas a 2048 caracteres mas, para o contexto do Open Insurance , foi adotado a metade deste tamanho (1024). tamanho p.ex.  ‘https://ACME.exemplo/capitalizacao/tradicional/pdf/condicoes_gerais.  # noqa: E501

        :return: The additional_info of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this CapitalizationBondsProductIdentificationData.

        Campo aberto (possibilidade de incluir URL) Observação: As URLs são limitadas a 2048 caracteres mas, para o contexto do Open Insurance , foi adotado a metade deste tamanho (1024). tamanho p.ex.  ‘https://ACME.exemplo/capitalizacao/tradicional/pdf/condicoes_gerais.  # noqa: E501

        :param additional_info: The additional_info of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: str
        """
        if additional_info is None:
            raise ValueError("Invalid value for `additional_info`, must not be `None`")  # noqa: E501

        self._additional_info = additional_info

    @property
    def minimum_requirement_details(self):
        """Gets the minimum_requirement_details of this CapitalizationBondsProductIdentificationData.  # noqa: E501

        Campo aberto (possibilidade de incluir URL). Observação: As URLs são limitadas a 2048 caracteres mas, para o contexto do Open Insurance , foi adotado a metade deste tamanho (1024). tamanho. p.ex. ‘https://ACME.exemplo/capitalizacao/tradicional/pdf/condicoes_gerais.’   # noqa: E501

        :return: The minimum_requirement_details of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._minimum_requirement_details

    @minimum_requirement_details.setter
    def minimum_requirement_details(self, minimum_requirement_details):
        """Sets the minimum_requirement_details of this CapitalizationBondsProductIdentificationData.

        Campo aberto (possibilidade de incluir URL). Observação: As URLs são limitadas a 2048 caracteres mas, para o contexto do Open Insurance , foi adotado a metade deste tamanho (1024). tamanho. p.ex. ‘https://ACME.exemplo/capitalizacao/tradicional/pdf/condicoes_gerais.’   # noqa: E501

        :param minimum_requirement_details: The minimum_requirement_details of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :type: str
        """

        self._minimum_requirement_details = minimum_requirement_details

    @property
    def target_audience(self):
        """Gets the target_audience of this CapitalizationBondsProductIdentificationData.  # noqa: E501

        A considerar os domínios abaixo:    1. Pessoa Natural   2. Pessoa Jurídica   3. Ambas (Pessoa Natural e Jurídica)   4. NA   # noqa: E501

        :return: The target_audience of this CapitalizationBondsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._target_audience

    @target_audience.setter
    def target_audience(self, target_audience):
        """Sets the target_audience of this CapitalizationBondsProductIdentificationData.

        A considerar os domínios abaixo:    1. Pessoa Natural   2. Pessoa Jurídica   3. Ambas (Pessoa Natural e Jurídica)   4. NA   # noqa: E501

        :param target_audience: The target_audience of this CapitalizationBondsProductIdentificationData.  # noqa: E501
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
        if issubclass(CapitalizationBondsProductIdentificationData, dict):
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
        if not isinstance(other, CapitalizationBondsProductIdentificationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
