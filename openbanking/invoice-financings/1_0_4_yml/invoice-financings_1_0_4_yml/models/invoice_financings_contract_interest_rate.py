# coding: utf-8

"""
    API Invoice-financings - Open Banking Brasil

    API de informações de operações de antecipação de recebíveis do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo antecipação de recebíveis – direitos creditórios descontados - mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Invoice-financings  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}`   - permissions:     - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **INVOICE_FINANCINGS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **INVOICE_FINANCINGS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.4
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InvoiceFinancingsContractInterestRate(object):
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
        'tax_type': 'str',
        'interest_rate_type': 'EnumContractInterestRateType',
        'tax_periodicity': 'EnumContractTaxPeriodicity',
        'calculation': 'EnumContractCalculation',
        'referential_rate_indexer_type': 'EnumContractReferentialRateIndexerType',
        'referential_rate_indexer_sub_type': 'EnumContractReferentialRateIndexerSubType',
        'referential_rate_indexer_additional_info': 'str',
        'pre_fixed_rate': 'float',
        'post_fixed_rate': 'float',
        'additional_info': 'str'
    }

    attribute_map = {
        'tax_type': 'taxType',
        'interest_rate_type': 'interestRateType',
        'tax_periodicity': 'taxPeriodicity',
        'calculation': 'calculation',
        'referential_rate_indexer_type': 'referentialRateIndexerType',
        'referential_rate_indexer_sub_type': 'referentialRateIndexerSubType',
        'referential_rate_indexer_additional_info': 'referentialRateIndexerAdditionalInfo',
        'pre_fixed_rate': 'preFixedRate',
        'post_fixed_rate': 'postFixedRate',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, tax_type=None, interest_rate_type=None, tax_periodicity=None, calculation=None, referential_rate_indexer_type=None, referential_rate_indexer_sub_type=None, referential_rate_indexer_additional_info=None, pre_fixed_rate=None, post_fixed_rate=None, additional_info=None):  # noqa: E501
        """InvoiceFinancingsContractInterestRate - a model defined in Swagger"""  # noqa: E501
        self._tax_type = None
        self._interest_rate_type = None
        self._tax_periodicity = None
        self._calculation = None
        self._referential_rate_indexer_type = None
        self._referential_rate_indexer_sub_type = None
        self._referential_rate_indexer_additional_info = None
        self._pre_fixed_rate = None
        self._post_fixed_rate = None
        self._additional_info = None
        self.discriminator = None
        self.tax_type = tax_type
        self.interest_rate_type = interest_rate_type
        self.tax_periodicity = tax_periodicity
        self.calculation = calculation
        self.referential_rate_indexer_type = referential_rate_indexer_type
        if referential_rate_indexer_sub_type is not None:
            self.referential_rate_indexer_sub_type = referential_rate_indexer_sub_type
        if referential_rate_indexer_additional_info is not None:
            self.referential_rate_indexer_additional_info = referential_rate_indexer_additional_info
        self.pre_fixed_rate = pre_fixed_rate
        self.post_fixed_rate = post_fixed_rate
        self.additional_info = additional_info

    @property
    def tax_type(self):
        """Gets the tax_type of this InvoiceFinancingsContractInterestRate.  # noqa: E501

        \"Tipo de Taxa (vide  Enum) - NOMINAL (taxa nominal é uma taxa de juros em que a unidade referencial não coincide com a unidade de tempo da capitalização. Ela é sempre fornecida em termos anuais, e seus períodos de capitalização podem ser diários, mensais, trimestrais ou semestrais. p.ex. Uma taxa de 12% ao ano com capitalização mensal) - EFETIVA (É a taxa de juros em que a unidade referencial coincide com a unidade de tempo da capitalização. Como as unidades de medida de tempo da taxa de juros e dos períodos de capitalização são iguais, usa-se exemplos simples como 1% ao mês, 60% ao ano)\"   # noqa: E501

        :return: The tax_type of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :rtype: str
        """
        return self._tax_type

    @tax_type.setter
    def tax_type(self, tax_type):
        """Sets the tax_type of this InvoiceFinancingsContractInterestRate.

        \"Tipo de Taxa (vide  Enum) - NOMINAL (taxa nominal é uma taxa de juros em que a unidade referencial não coincide com a unidade de tempo da capitalização. Ela é sempre fornecida em termos anuais, e seus períodos de capitalização podem ser diários, mensais, trimestrais ou semestrais. p.ex. Uma taxa de 12% ao ano com capitalização mensal) - EFETIVA (É a taxa de juros em que a unidade referencial coincide com a unidade de tempo da capitalização. Como as unidades de medida de tempo da taxa de juros e dos períodos de capitalização são iguais, usa-se exemplos simples como 1% ao mês, 60% ao ano)\"   # noqa: E501

        :param tax_type: The tax_type of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :type: str
        """
        if tax_type is None:
            raise ValueError("Invalid value for `tax_type`, must not be `None`")  # noqa: E501
        allowed_values = ["NOMINAL", "EFETIVA"]  # noqa: E501
        if tax_type not in allowed_values:
            raise ValueError(
                "Invalid value for `tax_type` ({0}), must be one of {1}"  # noqa: E501
                .format(tax_type, allowed_values)
            )

        self._tax_type = tax_type

    @property
    def interest_rate_type(self):
        """Gets the interest_rate_type of this InvoiceFinancingsContractInterestRate.  # noqa: E501


        :return: The interest_rate_type of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :rtype: EnumContractInterestRateType
        """
        return self._interest_rate_type

    @interest_rate_type.setter
    def interest_rate_type(self, interest_rate_type):
        """Sets the interest_rate_type of this InvoiceFinancingsContractInterestRate.


        :param interest_rate_type: The interest_rate_type of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :type: EnumContractInterestRateType
        """
        if interest_rate_type is None:
            raise ValueError("Invalid value for `interest_rate_type`, must not be `None`")  # noqa: E501

        self._interest_rate_type = interest_rate_type

    @property
    def tax_periodicity(self):
        """Gets the tax_periodicity of this InvoiceFinancingsContractInterestRate.  # noqa: E501


        :return: The tax_periodicity of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :rtype: EnumContractTaxPeriodicity
        """
        return self._tax_periodicity

    @tax_periodicity.setter
    def tax_periodicity(self, tax_periodicity):
        """Sets the tax_periodicity of this InvoiceFinancingsContractInterestRate.


        :param tax_periodicity: The tax_periodicity of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :type: EnumContractTaxPeriodicity
        """
        if tax_periodicity is None:
            raise ValueError("Invalid value for `tax_periodicity`, must not be `None`")  # noqa: E501

        self._tax_periodicity = tax_periodicity

    @property
    def calculation(self):
        """Gets the calculation of this InvoiceFinancingsContractInterestRate.  # noqa: E501


        :return: The calculation of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :rtype: EnumContractCalculation
        """
        return self._calculation

    @calculation.setter
    def calculation(self, calculation):
        """Sets the calculation of this InvoiceFinancingsContractInterestRate.


        :param calculation: The calculation of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :type: EnumContractCalculation
        """
        if calculation is None:
            raise ValueError("Invalid value for `calculation`, must not be `None`")  # noqa: E501

        self._calculation = calculation

    @property
    def referential_rate_indexer_type(self):
        """Gets the referential_rate_indexer_type of this InvoiceFinancingsContractInterestRate.  # noqa: E501


        :return: The referential_rate_indexer_type of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :rtype: EnumContractReferentialRateIndexerType
        """
        return self._referential_rate_indexer_type

    @referential_rate_indexer_type.setter
    def referential_rate_indexer_type(self, referential_rate_indexer_type):
        """Sets the referential_rate_indexer_type of this InvoiceFinancingsContractInterestRate.


        :param referential_rate_indexer_type: The referential_rate_indexer_type of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :type: EnumContractReferentialRateIndexerType
        """
        if referential_rate_indexer_type is None:
            raise ValueError("Invalid value for `referential_rate_indexer_type`, must not be `None`")  # noqa: E501

        self._referential_rate_indexer_type = referential_rate_indexer_type

    @property
    def referential_rate_indexer_sub_type(self):
        """Gets the referential_rate_indexer_sub_type of this InvoiceFinancingsContractInterestRate.  # noqa: E501


        :return: The referential_rate_indexer_sub_type of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :rtype: EnumContractReferentialRateIndexerSubType
        """
        return self._referential_rate_indexer_sub_type

    @referential_rate_indexer_sub_type.setter
    def referential_rate_indexer_sub_type(self, referential_rate_indexer_sub_type):
        """Sets the referential_rate_indexer_sub_type of this InvoiceFinancingsContractInterestRate.


        :param referential_rate_indexer_sub_type: The referential_rate_indexer_sub_type of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :type: EnumContractReferentialRateIndexerSubType
        """

        self._referential_rate_indexer_sub_type = referential_rate_indexer_sub_type

    @property
    def referential_rate_indexer_additional_info(self):
        """Gets the referential_rate_indexer_additional_info of this InvoiceFinancingsContractInterestRate.  # noqa: E501

        Campo livre para complementar a informação relativa ao Tipo de taxa referencial ou indexador. [Restrição] Obrigatório para complementar a informação relativa ao Tipo de taxa referencial ou indexador, quando selecionada o tipo ou subtipo OUTRO.   # noqa: E501

        :return: The referential_rate_indexer_additional_info of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :rtype: str
        """
        return self._referential_rate_indexer_additional_info

    @referential_rate_indexer_additional_info.setter
    def referential_rate_indexer_additional_info(self, referential_rate_indexer_additional_info):
        """Sets the referential_rate_indexer_additional_info of this InvoiceFinancingsContractInterestRate.

        Campo livre para complementar a informação relativa ao Tipo de taxa referencial ou indexador. [Restrição] Obrigatório para complementar a informação relativa ao Tipo de taxa referencial ou indexador, quando selecionada o tipo ou subtipo OUTRO.   # noqa: E501

        :param referential_rate_indexer_additional_info: The referential_rate_indexer_additional_info of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :type: str
        """

        self._referential_rate_indexer_additional_info = referential_rate_indexer_additional_info

    @property
    def pre_fixed_rate(self):
        """Gets the pre_fixed_rate of this InvoiceFinancingsContractInterestRate.  # noqa: E501

        Taxa pré fixada aplicada sob o contrato da modalidade crédito. p.ex. 0.0045. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)   # noqa: E501

        :return: The pre_fixed_rate of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :rtype: float
        """
        return self._pre_fixed_rate

    @pre_fixed_rate.setter
    def pre_fixed_rate(self, pre_fixed_rate):
        """Sets the pre_fixed_rate of this InvoiceFinancingsContractInterestRate.

        Taxa pré fixada aplicada sob o contrato da modalidade crédito. p.ex. 0.0045. O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)   # noqa: E501

        :param pre_fixed_rate: The pre_fixed_rate of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :type: float
        """
        if pre_fixed_rate is None:
            raise ValueError("Invalid value for `pre_fixed_rate`, must not be `None`")  # noqa: E501

        self._pre_fixed_rate = pre_fixed_rate

    @property
    def post_fixed_rate(self):
        """Gets the post_fixed_rate of this InvoiceFinancingsContractInterestRate.  # noqa: E501

        Taxa pós fixada aplicada sob o contrato da modalidade crédito. p.ex. 0.0045 .O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)   # noqa: E501

        :return: The post_fixed_rate of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :rtype: float
        """
        return self._post_fixed_rate

    @post_fixed_rate.setter
    def post_fixed_rate(self, post_fixed_rate):
        """Sets the post_fixed_rate of this InvoiceFinancingsContractInterestRate.

        Taxa pós fixada aplicada sob o contrato da modalidade crédito. p.ex. 0.0045 .O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)   # noqa: E501

        :param post_fixed_rate: The post_fixed_rate of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :type: float
        """
        if post_fixed_rate is None:
            raise ValueError("Invalid value for `post_fixed_rate`, must not be `None`")  # noqa: E501

        self._post_fixed_rate = post_fixed_rate

    @property
    def additional_info(self):
        """Gets the additional_info of this InvoiceFinancingsContractInterestRate.  # noqa: E501

        Texto com informações adicionais sobre a composição das taxas de juros pactuadas  # noqa: E501

        :return: The additional_info of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this InvoiceFinancingsContractInterestRate.

        Texto com informações adicionais sobre a composição das taxas de juros pactuadas  # noqa: E501

        :param additional_info: The additional_info of this InvoiceFinancingsContractInterestRate.  # noqa: E501
        :type: str
        """
        if additional_info is None:
            raise ValueError("Invalid value for `additional_info`, must not be `None`")  # noqa: E501

        self._additional_info = additional_info

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
        if issubclass(InvoiceFinancingsContractInterestRate, dict):
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
        if not isinstance(other, InvoiceFinancingsContractInterestRate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
