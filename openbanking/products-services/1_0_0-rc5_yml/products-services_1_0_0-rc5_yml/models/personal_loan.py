# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalLoan(object):
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
        """PersonalLoan - a model defined in Swagger"""  # noqa: E501
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
        """Gets the type of this PersonalLoan.  # noqa: E501

        Modalidades de empréstimos ofertados para pessoa Natural, conforme Circular 4015-Bacen. Segundo cartilha do Bacen: Empréstimo é um contrato entre o cliente e uma instituição financeira (banco, cooperativa de crédito, caixa econômica) pelo qual o cliente recebe uma quantia em dinheiro que deverá ser devolvida em prazo determinado, acrescida dos juros acertados. Os recursos obtidos no empréstimo não tem destinação específica.   * `EMPRESTIMO_CREDITO_PESSOAL_CONSIGNADO` -  operações de crédito com retenção de parcela do salário ou benefício do tomador, para o pagamento das prestações do empréstimo – desconto em folha de pagamento – nos termos da legislação em vigor   * `EMPRESTIMO_CREDITO_PESSOAL_SEM_CONSIGNACAO` - operações de empréstimos às pessoa natural, sem vinculação com aquisição de bem ou serviço e sem retenção de parcela do salário ou benefício do tomador para o pagamento das prestações do empréstimo   * `EMPRESTIMO_HOME_EQUITY` - empréstimos pessoa natural, garantidos por hipoteca ou por alienação fiduciária de bens imóveis residenciais, sem vinculação a aquisição de bens   * `EMPRESTIMO_MICROCREDITO_PRODUTIVO_ORIENTADO` - segundo PNMPO é o crédito concedido para financiamento das atividades produtivas, cuja metodologia será estabelecida em regulamento, observada a preferência do relacionamento direto com os empreendedores, admitido o uso de tecnologias digitais e eletrônicas que possam substituir o contato presencial   * `EMPRESTIMO_CHEQUE_ESPECIAL` - operações de crédito vinculadas à conta corrente, nas quais determinado limite de crédito é disponibilizado aos clientes para utilização de acordo com suas conveniências, sem necessidade de comunicação prévia à instituição financeira   * `EMPRESTIMO_CONTA_GARANTIDA` - operações de crédito rotativo, nas quais determinado limite de crédito é disponibilizado para utilização pelo cliente, através da simples movimentação da conta corrente e/ou solicitação formal à instituição financeira. As operações classificadas nessa modalidade não devem ter data definida para a amortização do saldo devedor, exceto a estabelecida para vigência do contrato   # noqa: E501

        :return: The type of this PersonalLoan.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PersonalLoan.

        Modalidades de empréstimos ofertados para pessoa Natural, conforme Circular 4015-Bacen. Segundo cartilha do Bacen: Empréstimo é um contrato entre o cliente e uma instituição financeira (banco, cooperativa de crédito, caixa econômica) pelo qual o cliente recebe uma quantia em dinheiro que deverá ser devolvida em prazo determinado, acrescida dos juros acertados. Os recursos obtidos no empréstimo não tem destinação específica.   * `EMPRESTIMO_CREDITO_PESSOAL_CONSIGNADO` -  operações de crédito com retenção de parcela do salário ou benefício do tomador, para o pagamento das prestações do empréstimo – desconto em folha de pagamento – nos termos da legislação em vigor   * `EMPRESTIMO_CREDITO_PESSOAL_SEM_CONSIGNACAO` - operações de empréstimos às pessoa natural, sem vinculação com aquisição de bem ou serviço e sem retenção de parcela do salário ou benefício do tomador para o pagamento das prestações do empréstimo   * `EMPRESTIMO_HOME_EQUITY` - empréstimos pessoa natural, garantidos por hipoteca ou por alienação fiduciária de bens imóveis residenciais, sem vinculação a aquisição de bens   * `EMPRESTIMO_MICROCREDITO_PRODUTIVO_ORIENTADO` - segundo PNMPO é o crédito concedido para financiamento das atividades produtivas, cuja metodologia será estabelecida em regulamento, observada a preferência do relacionamento direto com os empreendedores, admitido o uso de tecnologias digitais e eletrônicas que possam substituir o contato presencial   * `EMPRESTIMO_CHEQUE_ESPECIAL` - operações de crédito vinculadas à conta corrente, nas quais determinado limite de crédito é disponibilizado aos clientes para utilização de acordo com suas conveniências, sem necessidade de comunicação prévia à instituição financeira   * `EMPRESTIMO_CONTA_GARANTIDA` - operações de crédito rotativo, nas quais determinado limite de crédito é disponibilizado para utilização pelo cliente, através da simples movimentação da conta corrente e/ou solicitação formal à instituição financeira. As operações classificadas nessa modalidade não devem ter data definida para a amortização do saldo devedor, exceto a estabelecida para vigência do contrato   # noqa: E501

        :param type: The type of this PersonalLoan.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["EMPRESTIMO_CREDITO_PESSOAL_CONSIGNADO", "EMPRESTIMO_CREDITO_PESSOAL_SEM_CONSIGNACAO", "EMPRESTIMO_HOME_EQUITY", "EMPRESTIMO_MICROCREDITO_PRODUTIVO_ORIENTADO", "EMPRESTIMO_CHEQUE_ESPECIAL", "EMPRESTIMO_CONTA_GARANTIDA"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def fees(self):
        """Gets the fees of this PersonalLoan.  # noqa: E501


        :return: The fees of this PersonalLoan.  # noqa: E501
        :rtype: LoanFees
        """
        return self._fees

    @fees.setter
    def fees(self, fees):
        """Sets the fees of this PersonalLoan.


        :param fees: The fees of this PersonalLoan.  # noqa: E501
        :type: LoanFees
        """
        if fees is None:
            raise ValueError("Invalid value for `fees`, must not be `None`")  # noqa: E501

        self._fees = fees

    @property
    def interest_rates(self):
        """Gets the interest_rates of this PersonalLoan.  # noqa: E501

        Lista que traz o conjunto de informações necessárias para demonstrar a distribuição de frequências das taxas de juros remuneratórios da Modalidade de crédito  # noqa: E501

        :return: The interest_rates of this PersonalLoan.  # noqa: E501
        :rtype: list[LoanInterestRate]
        """
        return self._interest_rates

    @interest_rates.setter
    def interest_rates(self, interest_rates):
        """Sets the interest_rates of this PersonalLoan.

        Lista que traz o conjunto de informações necessárias para demonstrar a distribuição de frequências das taxas de juros remuneratórios da Modalidade de crédito  # noqa: E501

        :param interest_rates: The interest_rates of this PersonalLoan.  # noqa: E501
        :type: list[LoanInterestRate]
        """

        self._interest_rates = interest_rates

    @property
    def required_warranties(self):
        """Gets the required_warranties of this PersonalLoan.  # noqa: E501

        Lista das garantias exigidas  # noqa: E501

        :return: The required_warranties of this PersonalLoan.  # noqa: E501
        :rtype: list[RequiredWarranty]
        """
        return self._required_warranties

    @required_warranties.setter
    def required_warranties(self, required_warranties):
        """Sets the required_warranties of this PersonalLoan.

        Lista das garantias exigidas  # noqa: E501

        :param required_warranties: The required_warranties of this PersonalLoan.  # noqa: E501
        :type: list[RequiredWarranty]
        """
        if required_warranties is None:
            raise ValueError("Invalid value for `required_warranties`, must not be `None`")  # noqa: E501

        self._required_warranties = required_warranties

    @property
    def terms_conditions(self):
        """Gets the terms_conditions of this PersonalLoan.  # noqa: E501

        Campo aberto para informar as condições contratuais relativas à Modalidade de Financiamentos para pessoa jurídica informada. Pode ser informada a URL referente ao endereço onde constam as condições informadas. Endereço eletrônico de acesso ao canal.  # noqa: E501

        :return: The terms_conditions of this PersonalLoan.  # noqa: E501
        :rtype: str
        """
        return self._terms_conditions

    @terms_conditions.setter
    def terms_conditions(self, terms_conditions):
        """Sets the terms_conditions of this PersonalLoan.

        Campo aberto para informar as condições contratuais relativas à Modalidade de Financiamentos para pessoa jurídica informada. Pode ser informada a URL referente ao endereço onde constam as condições informadas. Endereço eletrônico de acesso ao canal.  # noqa: E501

        :param terms_conditions: The terms_conditions of this PersonalLoan.  # noqa: E501
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
        if issubclass(PersonalLoan, dict):
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
        if not isinstance(other, PersonalLoan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
