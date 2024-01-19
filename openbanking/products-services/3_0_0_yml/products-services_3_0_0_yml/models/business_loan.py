# coding: utf-8

"""
    API's OpenData do Open Finance Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Finance Brasil.  # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BusinessLoan(object):
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
        'type': 'str',
        'fees': 'LoanFees',
        'interest_rates': 'list[LoanInterestRate]',
        'required_warranties': 'list[RequiredWarranty]',
        'terms_conditions': 'str'
    }

    attribute_map = {
        'type': 'type',
        'fees': 'fees',
        'interest_rates': 'interestRates',
        'required_warranties': 'requiredWarranties',
        'terms_conditions': 'termsConditions'
    }

    def __init__(self, type=None, fees=None, interest_rates=None, required_warranties=None, terms_conditions=None):  # noqa: E501
        """BusinessLoan - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._fees = None
        self._interest_rates = None
        self._required_warranties = None
        self._terms_conditions = None
        self.discriminator = None
        self.type = type
        self.fees = fees
        if interest_rates is not None:
            self.interest_rates = interest_rates
        self.required_warranties = required_warranties
        self.terms_conditions = terms_conditions

    @property
    def type(self):
        """Gets the type of this BusinessLoan.  # noqa: E501

        Modalidades de empréstimos ofertados para pessoas Jurídicas, conforme Circular 4015-Bacen. Segundo cartilha do Bacen: Empréstimo é um contrato entre o cliente e uma instituição financeira (banco, cooperativa de crédito, caixa econômica) pelo qual o cliente recebe uma quantia em dinheiro que deverá ser devolvida em prazo determinado, acrescida dos juros acertados. Os recursos obtidos no empréstimo não tem destinação específica. * Empréstimo-Microcrédito Produtivo Orientado - segundo PNMPO é o crédito concedido para financiamento das atividades produtivas, cuja metodologia será estabelecida em regulamento, observada a preferência do relacionamento direto com os empreendedores, admitido o uso de tecnologias digitais e eletrônicas que possam substituir o contato presencial * Empréstimo-Cheque especial - operações de crédito vinculadas à conta corrente, nas quais determinado limite de crédito é disponibilizado aos clientes para utilização de acordo com suas conveniências, sem necessidade de comunicação prévia à instituição financeira * Empréstimo-Conta garantida - operações de crédito rotativo, nas quais determinado limite de crédito é disponibilizado para utilização pelo cliente, através da simples movimentação da conta corrente e/ou solicitação formal à instituição financeira. As operações classificadas nessa modalidade não devem ter data definida para a amortização do saldo devedor, exceto a estabelecida para vigência do contrato * Empréstimo-Capital de giro com prazo de vencimento até 365 dias: operações de crédito voltadas para o financiamento de curto prazo (igual ou inferior a 365 dias) das pessoas jurídicas, vinculadas às necessidades de capital de giro e a um contrato específico que estabeleça prazos, taxas e garantias * Empréstimo-Capital de giro com prazo vencimento superior a 365 dias: operações de crédito voltadas para o financiamento de médio e longo prazo (superior a 365 dias) das pessoas jurídicas, vinculadas às necessidades de capital de giro e a um contrato específico que estabeleça prazos, taxas e garantias * Empréstimo-Capital de giro rotativo: operações de crédito voltadas para o financiamento de capital de giro, vinculadas a um contrato que estabeleça linha de crédito rotativo, de forma que, à medida que a empresa devedora amortize os empréstimos já tomados, o limite disponível para utilização seja restituído, e amortizações com datas predeterminadas, podendo ser facultado ao devedor repactuar o fluxo de pagamentos ao longo da vigência do contrato   # noqa: E501

        :return: The type of this BusinessLoan.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BusinessLoan.

        Modalidades de empréstimos ofertados para pessoas Jurídicas, conforme Circular 4015-Bacen. Segundo cartilha do Bacen: Empréstimo é um contrato entre o cliente e uma instituição financeira (banco, cooperativa de crédito, caixa econômica) pelo qual o cliente recebe uma quantia em dinheiro que deverá ser devolvida em prazo determinado, acrescida dos juros acertados. Os recursos obtidos no empréstimo não tem destinação específica. * Empréstimo-Microcrédito Produtivo Orientado - segundo PNMPO é o crédito concedido para financiamento das atividades produtivas, cuja metodologia será estabelecida em regulamento, observada a preferência do relacionamento direto com os empreendedores, admitido o uso de tecnologias digitais e eletrônicas que possam substituir o contato presencial * Empréstimo-Cheque especial - operações de crédito vinculadas à conta corrente, nas quais determinado limite de crédito é disponibilizado aos clientes para utilização de acordo com suas conveniências, sem necessidade de comunicação prévia à instituição financeira * Empréstimo-Conta garantida - operações de crédito rotativo, nas quais determinado limite de crédito é disponibilizado para utilização pelo cliente, através da simples movimentação da conta corrente e/ou solicitação formal à instituição financeira. As operações classificadas nessa modalidade não devem ter data definida para a amortização do saldo devedor, exceto a estabelecida para vigência do contrato * Empréstimo-Capital de giro com prazo de vencimento até 365 dias: operações de crédito voltadas para o financiamento de curto prazo (igual ou inferior a 365 dias) das pessoas jurídicas, vinculadas às necessidades de capital de giro e a um contrato específico que estabeleça prazos, taxas e garantias * Empréstimo-Capital de giro com prazo vencimento superior a 365 dias: operações de crédito voltadas para o financiamento de médio e longo prazo (superior a 365 dias) das pessoas jurídicas, vinculadas às necessidades de capital de giro e a um contrato específico que estabeleça prazos, taxas e garantias * Empréstimo-Capital de giro rotativo: operações de crédito voltadas para o financiamento de capital de giro, vinculadas a um contrato que estabeleça linha de crédito rotativo, de forma que, à medida que a empresa devedora amortize os empréstimos já tomados, o limite disponível para utilização seja restituído, e amortizações com datas predeterminadas, podendo ser facultado ao devedor repactuar o fluxo de pagamentos ao longo da vigência do contrato   # noqa: E501

        :param type: The type of this BusinessLoan.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["EMPRESTIMO_MICROCREDITO_PRODUTIVO_ORIENTADO", "EMPRESTIMO_CHEQUE_ESPECIAL", "EMPRESTIMO_CONTA_GARANTIDA", "EMPRESTIMO_CAPITAL_GIRO_PRAZO_VENCIMENTO_ATE_365_DIAS", "EMPRESTIMO_CAPITAL_GIRO_PRAZO_VENCIMENTO_SUPERIOR_365_DIAS", "EMPRESTIMO_CAPITAL_GIRO_ROTATIVO"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def fees(self):
        """Gets the fees of this BusinessLoan.  # noqa: E501


        :return: The fees of this BusinessLoan.  # noqa: E501
        :rtype: LoanFees
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this BusinessLoan.


        :param fees: The fees of this BusinessLoan.  # noqa: E501
        :type: LoanFees
        """
        if fees is None:
            raise ValueError("Invalid value for `fees`, must not be `None`")  # noqa: E501

        self._fees = fees

    @property
    def interest_rates(self):
        """Gets the interest_rates of this BusinessLoan.  # noqa: E501

        Lista que traz o conjunto de informações necessárias para demonstrar a distribuição de frequências das taxas de juros remuneratórios da Modalidade de crédito  # noqa: E501

        :return: The interest_rates of this BusinessLoan.  # noqa: E501
        :rtype: list[LoanInterestRate]
        """
        return self._interest_rates

    @interest_rates.setter
    def interest_rates(self, interest_rates):
        """Sets the interest_rates of this BusinessLoan.

        Lista que traz o conjunto de informações necessárias para demonstrar a distribuição de frequências das taxas de juros remuneratórios da Modalidade de crédito  # noqa: E501

        :param interest_rates: The interest_rates of this BusinessLoan.  # noqa: E501
        :type: list[LoanInterestRate]
        """

        self._interest_rates = interest_rates

    @property
    def required_warranties(self):
        """Gets the required_warranties of this BusinessLoan.  # noqa: E501

        Lista das garantias exigidas  # noqa: E501

        :return: The required_warranties of this BusinessLoan.  # noqa: E501
        :rtype: list[RequiredWarranty]
        """
        return self._required_warranties

    @required_warranties.setter
    def required_warranties(self, required_warranties):
        """Sets the required_warranties of this BusinessLoan.

        Lista das garantias exigidas  # noqa: E501

        :param required_warranties: The required_warranties of this BusinessLoan.  # noqa: E501
        :type: list[RequiredWarranty]
        """
        if required_warranties is None:
            raise ValueError("Invalid value for `required_warranties`, must not be `None`")  # noqa: E501

        self._required_warranties = required_warranties

    @property
    def terms_conditions(self):
        """Gets the terms_conditions of this BusinessLoan.  # noqa: E501

        Campo aberto para informar as condições contratuais relativas à Modalidade de Empréstimo para pessoa jurídica informada. Pode ser informada a URL referente ao endereço onde constam as condições informadas. Endereço eletrônico de acesso ao canal.  # noqa: E501

        :return: The terms_conditions of this BusinessLoan.  # noqa: E501
        :rtype: str
        """
        return self._terms_conditions

    @terms_conditions.setter
    def terms_conditions(self, terms_conditions):
        """Sets the terms_conditions of this BusinessLoan.

        Campo aberto para informar as condições contratuais relativas à Modalidade de Empréstimo para pessoa jurídica informada. Pode ser informada a URL referente ao endereço onde constam as condições informadas. Endereço eletrônico de acesso ao canal.  # noqa: E501

        :param terms_conditions: The terms_conditions of this BusinessLoan.  # noqa: E501
        :type: str
        """
        if terms_conditions is None:
            raise ValueError("Invalid value for `terms_conditions`, must not be `None`")  # noqa: E501

        self._terms_conditions = terms_conditions

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
        if issubclass(BusinessLoan, dict):
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
        if not isinstance(other, BusinessLoan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
