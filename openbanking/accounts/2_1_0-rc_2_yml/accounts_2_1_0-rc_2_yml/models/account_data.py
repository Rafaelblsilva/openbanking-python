# coding: utf-8

"""
    API Accounts - Open Finance Brasil

    API de contas de depósito à vista, contas de poupança e contas pré-pagas do Open Finance Brasil – Fase 2. API que retorna informações de contas de depósito à vista, contas de poupança e contas de pagamento pré-pagas mantidas nas instituições transmissoras por seus clientes, incluindo dados de identificação da conta, saldos, limites e transações.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Accounts  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/accounts`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}`   - permissions:     - GET: **ACCOUNTS_READ** ### `/accounts/{accountId}/balances`   - permissions:     - GET: **ACCOUNTS_BALANCES_READ** ### `/accounts/{accountId}/transactions`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/transactions-current`   - permissions:     - GET: **ACCOUNTS_TRANSACTIONS_READ** ### `/accounts/{accountId}/overdraft-limits`   - permissions:     - GET: **ACCOUNTS_OVERDRAFT_LIMITS_READ**  ## Tabela: Data de imutabilidade por tipo de transação ``` |---------------------------------------|-------------------------|-----------------------| | Tipo de Transação                     | Data da Obrigatoriedade | Data da Imutabilidade | |---------------------------------------|-------------------------|-----------------------| | TED                                   | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | PIX                                   | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | TRANSFERENCIA MESMA INSTITUIÇÃO (TEF) | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | TARIFA SERVIÇOS AVULSOS               | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | FOLHA DE PAGAMENTO                    | DO                      | DO                    | |---------------------------------------|-------------------------|-----------------------| | DOC                                   | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | BOLETO                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | CONVÊNIO ARRECADAÇÃO                  | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | PACOTE TARIFA SERVIÇOS                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | DEPÓSITO                              | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | SAQUE                                 | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | CARTÃO                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | ENCARGOS JUROS CHEQUE ESPECIAL        | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | RENDIMENTO APLICAÇÃO FINANCEIRA       | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | PORTABILIDADE SALÁRIO                 | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | RESGATE APLICAÇÃO FINANCEIRA          | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | OPERAÇÃO DE CRÉDITO                   | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| | OUTROS                                | DO                      | D+1                   | |---------------------------------------|-------------------------|-----------------------| ```   # noqa: E501

    OpenAPI spec version: 2.1.0-rc.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AccountData(object):
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
        'brand_name': 'str',
        'company_cnpj': 'str',
        'type': 'EnumAccountType',
        'compe_code': 'str',
        'branch_code': 'str',
        'number': 'str',
        'check_digit': 'str',
        'account_id': 'str'
    }

    attribute_map = {
        'brand_name': 'brandName',
        'company_cnpj': 'companyCnpj',
        'type': 'type',
        'compe_code': 'compeCode',
        'branch_code': 'branchCode',
        'number': 'number',
        'check_digit': 'checkDigit',
        'account_id': 'accountId'
    }

    def __init__(self, brand_name=None, company_cnpj=None, type=None, compe_code=None, branch_code=None, number=None, check_digit=None, account_id=None):  # noqa: E501
        """AccountData - a model defined in Swagger"""  # noqa: E501
        self._brand_name = None
        self._company_cnpj = None
        self._type = None
        self._compe_code = None
        self._branch_code = None
        self._number = None
        self._check_digit = None
        self._account_id = None
        self.discriminator = None
        self.brand_name = brand_name
        self.company_cnpj = company_cnpj
        self.type = type
        self.compe_code = compe_code
        if branch_code is not None:
            self.branch_code = branch_code
        self.number = number
        self.check_digit = check_digit
        self.account_id = account_id

    @property
    def brand_name(self):
        """Gets the brand_name of this AccountData.  # noqa: E501

        Nome da Marca reportada pelo participante no Open Finance. Recomenda-se utilizar, sempre que possível, o mesmo nome de marca atribuído no campo do diretório Customer Friendly Server Name (Authorisation Server).  # noqa: E501

        :return: The brand_name of this AccountData.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this AccountData.

        Nome da Marca reportada pelo participante no Open Finance. Recomenda-se utilizar, sempre que possível, o mesmo nome de marca atribuído no campo do diretório Customer Friendly Server Name (Authorisation Server).  # noqa: E501

        :param brand_name: The brand_name of this AccountData.  # noqa: E501
        :type: str
        """
        if brand_name is None:
            raise ValueError("Invalid value for `brand_name`, must not be `None`")  # noqa: E501

        self._brand_name = brand_name

    @property
    def company_cnpj(self):
        """Gets the company_cnpj of this AccountData.  # noqa: E501

        Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara  # noqa: E501

        :return: The company_cnpj of this AccountData.  # noqa: E501
        :rtype: str
        """
        return self._company_cnpj

    @company_cnpj.setter
    def company_cnpj(self, company_cnpj):
        """Sets the company_cnpj of this AccountData.

        Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara  # noqa: E501

        :param company_cnpj: The company_cnpj of this AccountData.  # noqa: E501
        :type: str
        """
        if company_cnpj is None:
            raise ValueError("Invalid value for `company_cnpj`, must not be `None`")  # noqa: E501

        self._company_cnpj = company_cnpj

    @property
    def type(self):
        """Gets the type of this AccountData.  # noqa: E501


        :return: The type of this AccountData.  # noqa: E501
        :rtype: EnumAccountType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AccountData.


        :param type: The type of this AccountData.  # noqa: E501
        :type: EnumAccountType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def compe_code(self):
        """Gets the compe_code of this AccountData.  # noqa: E501

        Código identificador atribuído pelo Banco Central do Brasil às instituições participantes do STR (Sistema de Transferência de reservas).O Compe (Sistema de Compensação de Cheques e Outros Papéis) é um sistema que identifica e processa as compensações bancárias. Ele é representado por um código de três dígitos que serve como identificador de bancos, sendo assim, cada instituição bancária possui um número exclusivo  # noqa: E501

        :return: The compe_code of this AccountData.  # noqa: E501
        :rtype: str
        """
        return self._compe_code

    @compe_code.setter
    def compe_code(self, compe_code):
        """Sets the compe_code of this AccountData.

        Código identificador atribuído pelo Banco Central do Brasil às instituições participantes do STR (Sistema de Transferência de reservas).O Compe (Sistema de Compensação de Cheques e Outros Papéis) é um sistema que identifica e processa as compensações bancárias. Ele é representado por um código de três dígitos que serve como identificador de bancos, sendo assim, cada instituição bancária possui um número exclusivo  # noqa: E501

        :param compe_code: The compe_code of this AccountData.  # noqa: E501
        :type: str
        """
        if compe_code is None:
            raise ValueError("Invalid value for `compe_code`, must not be `None`")  # noqa: E501

        self._compe_code = compe_code

    @property
    def branch_code(self):
        """Gets the branch_code of this AccountData.  # noqa: E501

        Código da Agência detentora da conta. (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória)  [Restrição] Obrigatoriamente deve ser preenchido quando o campo \"type\" for diferente de CONTA_PAGAMENTO_PRE_PAGA.   # noqa: E501

        :return: The branch_code of this AccountData.  # noqa: E501
        :rtype: str
        """
        return self._branch_code

    @branch_code.setter
    def branch_code(self, branch_code):
        """Sets the branch_code of this AccountData.

        Código da Agência detentora da conta. (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória)  [Restrição] Obrigatoriamente deve ser preenchido quando o campo \"type\" for diferente de CONTA_PAGAMENTO_PRE_PAGA.   # noqa: E501

        :param branch_code: The branch_code of this AccountData.  # noqa: E501
        :type: str
        """

        self._branch_code = branch_code

    @property
    def number(self):
        """Gets the number of this AccountData.  # noqa: E501

        Número da conta  # noqa: E501

        :return: The number of this AccountData.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this AccountData.

        Número da conta  # noqa: E501

        :param number: The number of this AccountData.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def check_digit(self):
        """Gets the check_digit of this AccountData.  # noqa: E501

        Dígito da conta  # noqa: E501

        :return: The check_digit of this AccountData.  # noqa: E501
        :rtype: str
        """
        return self._check_digit

    @check_digit.setter
    def check_digit(self, check_digit):
        """Sets the check_digit of this AccountData.

        Dígito da conta  # noqa: E501

        :param check_digit: The check_digit of this AccountData.  # noqa: E501
        :type: str
        """
        if check_digit is None:
            raise ValueError("Invalid value for `check_digit`, must not be `None`")  # noqa: E501

        self._check_digit = check_digit

    @property
    def account_id(self):
        """Gets the account_id of this AccountData.  # noqa: E501

        Identifica de forma única  a conta do cliente, mantendo as regras de imutabilidade dentro da instituição transmissora.  # noqa: E501

        :return: The account_id of this AccountData.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AccountData.

        Identifica de forma única  a conta do cliente, mantendo as regras de imutabilidade dentro da instituição transmissora.  # noqa: E501

        :param account_id: The account_id of this AccountData.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

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
        if issubclass(AccountData, dict):
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
        if not isinstance(other, AccountData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
