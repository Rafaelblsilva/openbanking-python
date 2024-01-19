# coding: utf-8

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 1.0.3
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BusinessAccount(object):
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
        'compe_code': 'str',
        'branch_code': 'str',
        'number': 'str',
        'check_digit': 'str',
        'type': 'str'
    }

    attribute_map = {
        'compe_code': 'compeCode',
        'branch_code': 'branchCode',
        'number': 'number',
        'check_digit': 'checkDigit',
        'type': 'type'
    }

    def __init__(self, compe_code=None, branch_code=None, number=None, check_digit=None, type=None):  # noqa: E501
        """BusinessAccount - a model defined in Swagger"""  # noqa: E501
        self._compe_code = None
        self._branch_code = None
        self._number = None
        self._check_digit = None
        self._type = None
        self.discriminator = None
        self.compe_code = compe_code
        self.branch_code = branch_code
        self.number = number
        self.check_digit = check_digit
        self.type = type

    @property
    def compe_code(self):
        """Gets the compe_code of this BusinessAccount.  # noqa: E501

        Código identificador atribuído pelo Banco Central do Brasil às instituições participantes do STR (Sistema de Transferência de reservas).O Compe (Sistema de Compensação de Cheques e Outros Papéis) é um sistema que identifica e processa as compensações bancárias. Ele é representado por um código de três dígitos que serve como identificador de bancos, sendo assim, cada instituição bancária possui um número exclusivo  # noqa: E501

        :return: The compe_code of this BusinessAccount.  # noqa: E501
        :rtype: str
        """
        return self._compe_code

    @compe_code.setter
    def compe_code(self, compe_code):
        """Sets the compe_code of this BusinessAccount.

        Código identificador atribuído pelo Banco Central do Brasil às instituições participantes do STR (Sistema de Transferência de reservas).O Compe (Sistema de Compensação de Cheques e Outros Papéis) é um sistema que identifica e processa as compensações bancárias. Ele é representado por um código de três dígitos que serve como identificador de bancos, sendo assim, cada instituição bancária possui um número exclusivo  # noqa: E501

        :param compe_code: The compe_code of this BusinessAccount.  # noqa: E501
        :type: str
        """
        if compe_code is None:
            raise ValueError("Invalid value for `compe_code`, must not be `None`")  # noqa: E501

        self._compe_code = compe_code

    @property
    def branch_code(self):
        """Gets the branch_code of this BusinessAccount.  # noqa: E501

        Código da Agência detentora da conta. (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória)   # noqa: E501

        :return: The branch_code of this BusinessAccount.  # noqa: E501
        :rtype: str
        """
        return self._branch_code

    @branch_code.setter
    def branch_code(self, branch_code):
        """Sets the branch_code of this BusinessAccount.

        Código da Agência detentora da conta. (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória)   # noqa: E501

        :param branch_code: The branch_code of this BusinessAccount.  # noqa: E501
        :type: str
        """
        if branch_code is None:
            raise ValueError("Invalid value for `branch_code`, must not be `None`")  # noqa: E501

        self._branch_code = branch_code

    @property
    def number(self):
        """Gets the number of this BusinessAccount.  # noqa: E501

        Número da conta   # noqa: E501

        :return: The number of this BusinessAccount.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this BusinessAccount.

        Número da conta   # noqa: E501

        :param number: The number of this BusinessAccount.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def check_digit(self):
        """Gets the check_digit of this BusinessAccount.  # noqa: E501

        Dígito da conta   # noqa: E501

        :return: The check_digit of this BusinessAccount.  # noqa: E501
        :rtype: str
        """
        return self._check_digit

    @check_digit.setter
    def check_digit(self, check_digit):
        """Sets the check_digit of this BusinessAccount.

        Dígito da conta   # noqa: E501

        :param check_digit: The check_digit of this BusinessAccount.  # noqa: E501
        :type: str
        """
        if check_digit is None:
            raise ValueError("Invalid value for `check_digit`, must not be `None`")  # noqa: E501

        self._check_digit = check_digit

    @property
    def type(self):
        """Gets the type of this BusinessAccount.  # noqa: E501

        Tipos de contas. Modalidades tradicionais previstas pela Resolução 4.753, não contemplando contas vinculadas, conta de domiciliados no exterior, contas em moedas estrangeiras e conta correspondente moeda eletrônica. Vide Enum Conta de depósito à vista ou Conta corrente - é o tipo mais comum. Nela, o dinheiro fica à sua disposição para ser sacado a qualquer momento. Essa conta não gera rendimentos para o depositante Conta poupança - foi criada para estimular as pessoas a pouparem. O dinheiro que ficar na conta por trinta dias passa a gerar rendimentos, com isenção de imposto de renda para quem declara. Ou seja, o dinheiro “cresce” (rende) enquanto ficar guardado na conta. Cada depósito terá rendimentos de mês em mês, sempre no dia do mês em que o dinheiro tiver sido depositado Conta de pagamento pré-paga: segundo CIRCULAR Nº 3.680, BCB de  2013, é a 'destinada à execução de transações de pagamento em moeda eletrônica realizadas com base em fundos denominados em reais previamente aportados'. SEM_TIPO_CONTA - para reporte nos dados de identificação quando o cliente não possuir conta na instituição transmissora.   # noqa: E501

        :return: The type of this BusinessAccount.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BusinessAccount.

        Tipos de contas. Modalidades tradicionais previstas pela Resolução 4.753, não contemplando contas vinculadas, conta de domiciliados no exterior, contas em moedas estrangeiras e conta correspondente moeda eletrônica. Vide Enum Conta de depósito à vista ou Conta corrente - é o tipo mais comum. Nela, o dinheiro fica à sua disposição para ser sacado a qualquer momento. Essa conta não gera rendimentos para o depositante Conta poupança - foi criada para estimular as pessoas a pouparem. O dinheiro que ficar na conta por trinta dias passa a gerar rendimentos, com isenção de imposto de renda para quem declara. Ou seja, o dinheiro “cresce” (rende) enquanto ficar guardado na conta. Cada depósito terá rendimentos de mês em mês, sempre no dia do mês em que o dinheiro tiver sido depositado Conta de pagamento pré-paga: segundo CIRCULAR Nº 3.680, BCB de  2013, é a 'destinada à execução de transações de pagamento em moeda eletrônica realizadas com base em fundos denominados em reais previamente aportados'. SEM_TIPO_CONTA - para reporte nos dados de identificação quando o cliente não possuir conta na instituição transmissora.   # noqa: E501

        :param type: The type of this BusinessAccount.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["CONTA_DEPOSITO_A_VISTA", "CONTA_POUPANCA", "CONTA_PAGAMENTO_PRE_PAGA", "SEM_TIPO_CONTA"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(BusinessAccount, dict):
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
        if not isinstance(other, BusinessAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other