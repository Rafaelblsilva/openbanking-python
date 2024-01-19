# coding: utf-8

"""
    API Consents - Open Finance Brasil

    API que trata da criação, consulta e revogação de consentimentos para o Open Finance Brasil Dados cadastrais e transacionais - customer-data.   Não possui segregação entre pessoa natural e pessoa jurídica.      # Orientações importantes A API Consents trata dos consentimentos exclusivamente para a Dados cadastrais e transacionais do Open Finance Brasil. - As informações da instituição receptora não trafegam na API Consents – a autenticação da receptora se dá através do [DCR](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378307/Dynamic+Client+Registration).    - Na chamada para a criação do consentimento deve-se utilizar um token gerado via `client_credentials`. - Após o `POST` de criação do consentimento, o `STATUS` devolvido na resposta deverá ser `AWAITING_AUTHORISATION`. - O `STATUS` será alterado para `AUTHORISED` somente após autenticação e confirmação por parte do usuário na instituição transmissora dos dados. - Alteração obrigatória do status `AWAITING_AUTHORISATION` para `REVOKED` após 60 minutos. - Todas as datas trafegadas nesta API seguem o padrão da [RFC3339](https://tools.ietf.org/html/rfc3339) e formato \"zulu\". - A descrição do fluxo de consentimento encontra-se disponível no [Portal do desenvolvedor](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17369300/Dados+Cadastrais+e+Transacionais#Fluxo-b%C3%A1sico-de-consentimento). - O arquivo com o mapeamento completo entre `Roles`, `scopes` e `permissions` está disponibilizado no Portal do desenvolvedor, no mesmo item acima - descrição do fluxo de consentimento. - A receptora deve enviar obrigatoriamente, no pedido de criação de consentimento, todas as permissions dos agrupamentos de dados as quais ela deseja consentimento, conforme tabela abaixo:      ```   |----------------------|-------------------------------|----------------------------------------------------------|   | CATEGORIA DE DADOS   | AGRUPAMENTO                   | PERMISSIONS                                              |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Dados Cadastrais PF           | CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Informações complementares PF | CUSTOMERS_PERSONAL_ADITTIONALINFO_READ                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Dados Cadastrais PJ           | CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Informações complementares PJ | CUSTOMERS_BUSINESS_ADITTIONALINFO_READ                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Saldos                        | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_BALANCES_READ                                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Limites                       | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_OVERDRAFT_LIMITS_READ                           |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Extratos                      | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_TRANSACTIONS_READ                               |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Limites                       | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_LIMITS_READ                        |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Transações                    | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Faturas                       | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_READ                         |   |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ            |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Operações de Crédito | Dados do Contrato             | LOANS_READ                                               |   |                      |                               | LOANS_WARRANTIES_READ                                    |   |                      |                               | LOANS_SCHEDULED_INSTALMENTS_READ                         |   |                      |                               | LOANS_PAYMENTS_READ                                      |   |                      |                               | FINANCINGS_READ                                          |   |                      |                               | FINANCINGS_WARRANTIES_READ                               |   |                      |                               | FINANCINGS_SCHEDULED_INSTALMENTS_READ                    |   |                      |                               | FINANCINGS_PAYMENTS_READ                                 |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_READ                       |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_WARRANTIES_READ            |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_SCHEDULED_INSTALMENTS_READ |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_PAYMENTS_READ              |   |                      |                               | INVOICE_FINANCINGS_READ                                  |   |                      |                               | INVOICE_FINANCINGS_WARRANTIES_READ                       |   |                      |                               | INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ            |   |                      |                               | INVOICE_FINANCINGS_PAYMENTS_READ                         |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Investimento         | Dados da Operação             | BANK_FIXED_INCOMES_READ                                  |   |                      |                               | CREDIT_FIXED_INCOMES_READ                                |   |                      |                               | FUNDS_READ                                               |   |                      |                               | VARIABLE_INCOMES_READ                                    |   |                      |                               | TREASURE_TITLES_READ                                     |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   ``` - A instituição transmissora deve validar o preenchimento correto desses agrupamentos no momento da geração do consentimento. - Caso a instiuição receptora envie permissões divergentes ao agrupamento especificado na tabela, a transmissora deve rejeitar o pedido da receptora dando retorno HTTP Status Code 400. - A transmissora deve retornar, da lista de permissions requisitadas, apenas o subconjunto de permissions por ela suportada, removendo da lista as permissions de produtos não suportados e retornando HTTP Status Code 201. Caso não restem permissões funcionais, a instituição transmissora deve retornar o erro HTTP Code \"422 Unprocessable Entity\". - O endpoint `POST /consents/{consentId}/extends` é utilizado para renovação de consentimento ativo do cliente.  Ou seja, quando a receptora recebe pedido de renovação de consentimento com status ainda ativo para a transmissora, ela deve requisitar este endpoint. - Apenas consentimentos autorizados (status AUTHORISED) podem ser renovados pelo uso do endpoint `POST /consents/{consentId}/extends`. Essa renovação é feita exclusivamente via backende resulta em:   - Alteração do `expirationDateTime` do consentimento vigente;   - Persistência de informações para listar histórico de alterações que podem ser acessadas via endpoint `GET /consents/{consentId}/extends`. - A data de expiração `2300-01-01T00:00:00Z` (`expirationDateTime= 2300-01-01T00:00:00Z`) é a representação técnica de um consentimento com prazo de expiração indeterminado.  Ou seja, sempre que o cliente escolher prazo indeterminado para expiração de consentimento, a instituição receptora deve preencher `expirationDateTime= 2300-01-01T00:00:00Z` e assim informá-la para à instituição transmissora.  De igual forma, a instituição transmissora deve entender e representar consentimento com `expirationDateTime= 2300-01-01T00:00:00Z` como um consentimento com prazo de expiração indeterminado. - Os consentimentos em estado expirado ou cancelado não podem ser renovados sem redirecionamento.  Ou seja, não é possível utilizar o endpoint `POST /consents/{consentId}/extends` para consentimentos nesses estados (status REJECTED).  A transmissora deve retornar status de erro 422 (`ESTADO_CONSENTIMENTO_INVALIDO`) para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) deve ser possível por apenas um cliente logado.  Isso implica que qualquer usuário (`loggedUser`) com permissão para o consentimento associado deve ser capaz de finalizar o fluxo de renovação sem redirecionamento.   A transmissora deve retornar status de erro 422 (DEPENDE_MULTIPLA_ALCADA) para requisições que necessitam de múltipla alçada. - Para consentimentos Pessoa Natural apenas o loggedUser criador do consentimento consegue renovar sem redirecionamento (`POST /consents/{consentId}/extends`). A transmissora deve retornar status de erro 403 para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) deve ser possível para consentimento para o qual foi emitido um refresh token opaco.  Não deve ser possível quando o consentimento está vinculado a um refresh token do tipo JWT (com prazo não prorrogável).  A transmissora deve retornar status de erro 422 (`REFRESH_TOKEN_JWT`) para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) deve ocorrer apenas até o período de 12 meses após a data de requisição (`current_datetime<= expirationDateTime<= current_datetime+12meses`), ou com prazo de expiração indeterminado (`expirationDateTime=2300-01-01T00:00:00Z`).  A transmissora deve retornar status de erro 422 (`DATA_EXPIRACAO_INVALIDA`) para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) sempre aumenta a data de expiração final do consentimento em relação à data de expiração vigente.  Ou seja, um consentimento com prazo de expiração para 6 meses no futuro não pode ter sua data de expiração alterada para apenas 3 meses no futuro.  A transmissora deve retornar status de erro 422 (`DATA_EXPIRACAO_INVALIDA`) para requisições que não seguem essa definição. - A renovação de consentimento ativo do cliente somente poderá ser aceita pela transmissora para um usuário logado na receptora, identificado por seu documento (`loggedUser`; `businessEntity` quando aplicável) e permitido a partir de token de acesso (informado no cabeçalho `Authorization`) conseguido anteriormente durante a criação e confirmação do consentimento vigente.  A transmissora deve validar documento fornecido (`loggedUser`; `businessEntity` quando aplicável) e token de acesso para executar a renovação de consentimento. Caso a transmissora detecte que trata-se de acesso inválido por questões de segurança, é esperado status de erro 401 ou 403. - Após a renovação de consentimento (`POST /consents/{consentId}/extends`) a transmissora deve garantir que a data de expiração do refresh token opaco, ao qual o consentimento está associado, seja:   - sem expiração: refresh token permanece ativo, desde que o consentimento associado permaneça ativo (status AUTHORIZED);   - com expiração: desde que, no mínimo, a nova data de expiração do refreshtoken seja igual à nova data do consentimento. - A lista do payload de resposta do endpoint de histórico de renovações feitas (`GET /consents/{consentId}/extends`) deve ser entregue em ordem decrescente pela data de requisição (`data[].requestDateTime`).  Dessa forma, o primeiro item da lista apresentará a mesma data de expiração do consentimento vigente, pois foi a última renovação feita.   # noqa: E501

    OpenAPI spec version: 2.2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Links(object):
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
        '_self': 'str',
        'first': 'str',
        'prev': 'str',
        'next': 'str',
        'last': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'first': 'first',
        'prev': 'prev',
        'next': 'next',
        'last': 'last'
    }

    def __init__(self, _self=None, first=None, prev=None, next=None, last=None):  # noqa: E501
        """Links - a model defined in Swagger"""  # noqa: E501
        self.__self = None
        self._first = None
        self._prev = None
        self._next = None
        self._last = None
        self.discriminator = None
        self._self = _self
        if first is not None:
            self.first = first
        if prev is not None:
            self.prev = prev
        if next is not None:
            self.next = next
        if last is not None:
            self.last = last

    @property
    def _self(self):
        """Gets the _self of this Links.  # noqa: E501

        URI completo que gerou a resposta atual.  # noqa: E501

        :return: The _self of this Links.  # noqa: E501
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Sets the _self of this Links.

        URI completo que gerou a resposta atual.  # noqa: E501

        :param _self: The _self of this Links.  # noqa: E501
        :type: str
        """
        if _self is None:
            raise ValueError("Invalid value for `_self`, must not be `None`")  # noqa: E501

        self.__self = _self

    @property
    def first(self):
        """Gets the first of this Links.  # noqa: E501

        URI da primeira página que originou essa lista de resultados. Restrição - Obrigatório quando não for a primeira página da resposta  # noqa: E501

        :return: The first of this Links.  # noqa: E501
        :rtype: str
        """
        return self._first

    @first.setter
    def first(self, first):
        """Sets the first of this Links.

        URI da primeira página que originou essa lista de resultados. Restrição - Obrigatório quando não for a primeira página da resposta  # noqa: E501

        :param first: The first of this Links.  # noqa: E501
        :type: str
        """

        self._first = first

    @property
    def prev(self):
        """Gets the prev of this Links.  # noqa: E501

        URI da página anterior dessa lista de resultados. Restrição -  Obrigatório quando não for a primeira página da resposta  # noqa: E501

        :return: The prev of this Links.  # noqa: E501
        :rtype: str
        """
        return self._prev

    @prev.setter
    def prev(self, prev):
        """Sets the prev of this Links.

        URI da página anterior dessa lista de resultados. Restrição -  Obrigatório quando não for a primeira página da resposta  # noqa: E501

        :param prev: The prev of this Links.  # noqa: E501
        :type: str
        """

        self._prev = prev

    @property
    def next(self):
        """Gets the next of this Links.  # noqa: E501

        URI da próxima página dessa lista de resultados. Restrição - Obrigatório quando não for a última página da resposta  # noqa: E501

        :return: The next of this Links.  # noqa: E501
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next):
        """Sets the next of this Links.

        URI da próxima página dessa lista de resultados. Restrição - Obrigatório quando não for a última página da resposta  # noqa: E501

        :param next: The next of this Links.  # noqa: E501
        :type: str
        """

        self._next = next

    @property
    def last(self):
        """Gets the last of this Links.  # noqa: E501

        URI da última página dessa lista de resultados. Restrição - Obrigatório quando não for a última página da resposta  # noqa: E501

        :return: The last of this Links.  # noqa: E501
        :rtype: str
        """
        return self._last

    @last.setter
    def last(self, last):
        """Sets the last of this Links.

        URI da última página dessa lista de resultados. Restrição - Obrigatório quando não for a última página da resposta  # noqa: E501

        :param last: The last of this Links.  # noqa: E501
        :type: str
        """

        self._last = last

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
        if issubclass(Links, dict):
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
        if not isinstance(other, Links):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
