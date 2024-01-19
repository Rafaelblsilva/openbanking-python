# coding: utf-8

"""
    API Consents - Open Finance Brasil

    API que trata da criação, consulta, renovação e revogação de consentimentos para o Open Finance Brasil Dados cadastrais e transacionais - customer-data.   Não possui segregação entre pessoa natural e pessoa jurídica.      # Orientações importantes A API Consents trata exclusivamente dos consentimentos para Dados Cadastrais e Transacionais do Open Finance Brasil. - A API consents é composta de endpoints que permitem:   - Pedido de criação do consentimento pela receptora: `POST /consents`   - Devolução do pedido de criação pela transmissora: `GET /consents/{consentId}`   - Pedido de renovação de consentimento do cliente pela receptora: `POST /consents/{consentId}/extends`   - Devolução de lista com histórico de renovações efetuadas: `GET /consents/{consentId}/extensions`   - Pedido de revogação do consentimento: `DELETE /consents/{consentId}` - Recomenda-se fortemente a leitura da seção [Orientações - [DC] Consentimento](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/219480491) para maiores detalhes, regras e restrições referente aos endpoints da API Consents - As informações da instituição receptora não trafegam na API Consents – a autenticação da receptora se dá através do [DCR](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378307/Dynamic+Client+Registration). - Na chamada para a criação, consulta e revogação do consentimento deve-se utilizar um token gerado via `client_credentials`. Na chamada para renovação do consentimento deve-se utilizar um token gerado via `authorization_code`. - Após o `POST` de criação do consentimento, o `STATUS` devolvido na resposta deverá ser `AWAITING_AUTHORISATION`. - O `STATUS` será alterado para `AUTHORISED` somente após autenticação e confirmação por parte do usuário na instituição transmissora dos dados. - Caso não haja confirmação por parte do usuário na transmissora, o status do consentimento deve ser alterado de `AWAITING_AUTHORISATION` para `REJECTED` após 60 minutos. - Todas as datas trafegadas nesta API seguem o padrão da [RFC3339](https://tools.ietf.org/html/rfc3339) e formato \"zulu\". - A descrição do fluxo de consentimento encontra-se disponível no [Portal do desenvolvedor](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17369300/Dados+Cadastrais+e+Transacionais#Fluxo-b%C3%A1sico-de-consentimento). - O arquivo com o mapeamento completo entre `Roles`, `scopes` e `permissions` está disponibilizado no Portal do desenvolvedor, no mesmo item acima - descrição do fluxo de consentimento. - A receptora deve enviar obrigatoriamente, no pedido de criação de consentimento, todas as permissions dos agrupamentos de dados as quais ela deseja consentimento, conforme tabela abaixo:    ```   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   | ROLE  | CATEGORIA DE DADOS   | AGRUPAMENTO                   | PERMISSIONS                                              | SCOPE OAUTH 2.0               |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ                  | customers                     |   |       | Cadastro             | Dados Cadastrais PF           |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           | resources                     |   |       |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CUSTOMERS_PERSONAL_ADITTIONALINFO_READ                   | customers                     |   |       | Cadastro             | Informações complementares PF |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           | resources                     |   | DADOS |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ                  | customers                     |   |       | Cadastro             | Dados Cadastrais PJ           |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           | resources                     |   |       |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CUSTOMERS_BUSINESS_ADITTIONALINFO_READ                   | customers                     |   |       | Cadastro             | Informações complementares PJ |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           | resources                     |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | ACCOUNTS_READ                                            |                               |   |       |                      |                               |----------------------------------------------------------| accounts                      |   |       | Contas               | Saldos                        | ACCOUNTS_BALANCES_READ                                   |                               |   |       |                      |                               |----------------------------------------------------------| resources                     |   |       |                      |                               | RESOURCES_READ                                           |                               |   |       |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | ACCOUNTS_READ                                            |                               |   |       |                      |                               |----------------------------------------------------------| accounts                      |   | DADOS | Contas               | Limites                       | ACCOUNTS_OVERDRAFT_LIMITS_READ                           |                               |   |       |                      |                               |----------------------------------------------------------| resources                     |   |       |                      |                               | RESOURCES_READ                                           |                               |   |       |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | ACCOUNTS_READ                                            |                               |   |       |                      |                               |----------------------------------------------------------| accounts                      |   |       | Contas               | Extratos                      | ACCOUNTS_TRANSACTIONS_READ                               |                               |   |       |                      |                               |----------------------------------------------------------| resources                     |   |       |                      |                               | RESOURCES_READ                                           |                               |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CREDIT_CARDS_ACCOUNTS_READ                               |                               |   |       |                      |                               |----------------------------------------------------------| credit-cards-accounts         |   |       | Cartão de Crédito    | Limites                       | CREDIT_CARDS_ACCOUNTS_LIMITS_READ                        |                               |   |       |                      |                               |----------------------------------------------------------| resources                     |   |       |                      |                               | RESOURCES_READ                                           |                               |   |       |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CREDIT_CARDS_ACCOUNTS_READ                               |                               |   |       |                      |                               |----------------------------------------------------------| credit-cards-accounts         |   |       | Cartão de Crédito    | Transações                    | CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ                  |                               |   | DADOS |                      |                               |----------------------------------------------------------| resources                     |   |       |                      |                               | RESOURCES_READ                                           |                               |   |       |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CREDIT_CARDS_ACCOUNTS_READ                               |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_READ                         | credit-cards-accounts         |   |       | Cartão de Crédito    | Faturas                       |----------------------------------------------------------|                               |   |       |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ            | resources                     |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           |                               |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | LOANS_READ                                               |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | LOANS_WARRANTIES_READ                                    |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | LOANS_SCHEDULED_INSTALMENTS_READ                         |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | LOANS_PAYMENTS_READ                                      |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | FINANCINGS_READ                                          |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | FINANCINGS_WARRANTIES_READ                               |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | FINANCINGS_SCHEDULED_INSTALMENTS_READ                    | loans                         |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | FINANCINGS_PAYMENTS_READ                                 | financings                    |   |       |                      |                               |----------------------------------------------------------|                               |   | DADOS | Operações de Crédito | Dados do Contrato             | UNARRANGED_ACCOUNTS_OVERDRAFT_READ                       | unarranged-accounts-overdraft |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_WARRANTIES_READ            | invoice-financings            |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_SCHEDULED_INSTALMENTS_READ | resources                     |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_PAYMENTS_READ              |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | INVOICE_FINANCINGS_READ                                  |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | INVOICE_FINANCINGS_WARRANTIES_READ                       |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ            |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | INVOICE_FINANCINGS_PAYMENTS_READ                         |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           |                               |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | BANK_FIXED_INCOMES_READ                                  | bank-fixed-incomes            |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | CREDIT_FIXED_INCOMES_READ                                | credit-fixed-incomes          |   |       |                      |                               |----------------------------------------------------------|                               |   | DADOS | Investimento         | Dados da Operação             | FUNDS_READ                                               | variable-incomes              |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | VARIABLE_INCOMES_READ                                    | treasure-titles               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | TREASURE_TITLES_READ                                     | funds                         |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           | resources                     |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | EXCHANGES_READ                                           |                               |   | DADOS | Câmbio               | Dados da Operação             |----------------------------------------------------------| exchanges                     |   |       |                      |                               | RESOURCES_READ                                           |                               |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|      ``` - A instituição transmissora deve validar o preenchimento correto dos agrupamentos acima no momento da geração do consentimento. - Caso a instiuição receptora envie permissões não existentes nos agrupamentos especificados na tabela, a transmissora deve rejeitar o pedido da receptora dando retorno HTTP Status Code 400. - A transmissora deve retornar, da lista de permissions requisitadas, apenas o subconjunto de permissions por ela suportada, removendo da lista as permissions de produtos não suportados e retornando HTTP Status Code 201. A única exceção a este comportamento são os casos de produtos agrupados, como Operações de Crédito, Investimentos e Câmbio, para os quais todas as permissões do agrupamento devem ser mantidas. Caso não restem permissões funcionais, a instituição transmissora deve retornar o erro HTTP Code \"422 Unprocessable Entity\". - A renovação de consentimento não pode ser efetuada em situações determinadas. É esperado status 401 ou 403 para situações em que o erro for tratado na camada de segurança. Para erros tratados em camada de negócio, a transmissora deve retornar 422 conforme mensagens especificadas na página [Orientações – [DC] Consentimento](https://openfinancebrasil.atlassian.net/wiki/spaces/DraftOF/pages/232915037) - Caso o método `DELETE` seja chamado para um consentimento que já se encontra no `STATUS REJECTED` deve se retornar o STATUS CODE 422. - Pedidos de renovação de consentimento somente podem alterar a data de validade (conforme as regras definidas em [Orientações – [DC] Consentimento](https://openfinancebrasil.atlassian.net/wiki/spaces/DraftOF/pages/232915037)) e a finalidade do consentimento, e aplica-se somente a consentimentos ativos (status `AUTHORISED`). - No caso de criação ou renovação de consentimentos com prazo indeterminado, a receptora não deve enviar o atributo expirationDateTime. Para prazos determinados o campo deve ser enviado. - A renovação de consentimento (`POST /consents/{consentId}/extends`) deve ser possível por apenas um cliente logado.  Isso implica que qualquer usuário (`loggedUser`) com permissão para o consentimento Pessoa Jurídica deve ser capaz de finalizar o fluxo de renovação sem redirecionamento. Para consentimentos Pessoa Natural apenas o `loggedUser` criador do consentimento consegue renovar sem redirecionamento.   # noqa: E501

    OpenAPI spec version: 3.0.0-beta.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseConsentReadExtensionsData(object):
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
        'expiration_date_time': 'datetime',
        'logged_user': 'LoggedUserExtensions',
        'request_date_time': 'datetime',
        'previous_expiration_date_time': 'datetime',
        'x_fapi_customer_ip_address': 'str',
        'x_customer_user_agent': 'str'
    }

    attribute_map = {
        'expiration_date_time': 'expirationDateTime',
        'logged_user': 'loggedUser',
        'request_date_time': 'requestDateTime',
        'previous_expiration_date_time': 'previousExpirationDateTime',
        'x_fapi_customer_ip_address': 'xFapiCustomerIpAddress',
        'x_customer_user_agent': 'xCustomerUserAgent'
    }

    def __init__(self, expiration_date_time=None, logged_user=None, request_date_time=None, previous_expiration_date_time=None, x_fapi_customer_ip_address=None, x_customer_user_agent=None):  # noqa: E501
        """ResponseConsentReadExtensionsData - a model defined in Swagger"""  # noqa: E501
        self._expiration_date_time = None
        self._logged_user = None
        self._request_date_time = None
        self._previous_expiration_date_time = None
        self._x_fapi_customer_ip_address = None
        self._x_customer_user_agent = None
        self.discriminator = None
        if expiration_date_time is not None:
            self.expiration_date_time = expiration_date_time
        self.logged_user = logged_user
        self.request_date_time = request_date_time
        if previous_expiration_date_time is not None:
            self.previous_expiration_date_time = previous_expiration_date_time
        if x_fapi_customer_ip_address is not None:
            self.x_fapi_customer_ip_address = x_fapi_customer_ip_address
        if x_customer_user_agent is not None:
            self.x_customer_user_agent = x_customer_user_agent

    @property
    def expiration_date_time(self):
        """Gets the expiration_date_time of this ResponseConsentReadExtensionsData.  # noqa: E501

        Data e hora de expiração da permissão. Reflete a data limite de validade do consentimento. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format), utilizado apenas para consulta de alterações históricas de extensão do consentimento.  [Restrição] De preenchimento obrigatório nos casos em que houver validade determinada.  Em casos de consentimento com prazo indeterminada o campo não deve ser preenchido.   # noqa: E501

        :return: The expiration_date_time of this ResponseConsentReadExtensionsData.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date_time

    @expiration_date_time.setter
    def expiration_date_time(self, expiration_date_time):
        """Sets the expiration_date_time of this ResponseConsentReadExtensionsData.

        Data e hora de expiração da permissão. Reflete a data limite de validade do consentimento. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format), utilizado apenas para consulta de alterações históricas de extensão do consentimento.  [Restrição] De preenchimento obrigatório nos casos em que houver validade determinada.  Em casos de consentimento com prazo indeterminada o campo não deve ser preenchido.   # noqa: E501

        :param expiration_date_time: The expiration_date_time of this ResponseConsentReadExtensionsData.  # noqa: E501
        :type: datetime
        """

        self._expiration_date_time = expiration_date_time

    @property
    def logged_user(self):
        """Gets the logged_user of this ResponseConsentReadExtensionsData.  # noqa: E501


        :return: The logged_user of this ResponseConsentReadExtensionsData.  # noqa: E501
        :rtype: LoggedUserExtensions
        """
        return self._logged_user

    @logged_user.setter
    def logged_user(self, logged_user):
        """Sets the logged_user of this ResponseConsentReadExtensionsData.


        :param logged_user: The logged_user of this ResponseConsentReadExtensionsData.  # noqa: E501
        :type: LoggedUserExtensions
        """
        if logged_user is None:
            raise ValueError("Invalid value for `logged_user`, must not be `None`")  # noqa: E501

        self._logged_user = logged_user

    @property
    def request_date_time(self):
        """Gets the request_date_time of this ResponseConsentReadExtensionsData.  # noqa: E501

        Data e hora em que o recurso foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :return: The request_date_time of this ResponseConsentReadExtensionsData.  # noqa: E501
        :rtype: datetime
        """
        return self._request_date_time

    @request_date_time.setter
    def request_date_time(self, request_date_time):
        """Sets the request_date_time of this ResponseConsentReadExtensionsData.

        Data e hora em que o recurso foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :param request_date_time: The request_date_time of this ResponseConsentReadExtensionsData.  # noqa: E501
        :type: datetime
        """
        if request_date_time is None:
            raise ValueError("Invalid value for `request_date_time`, must not be `None`")  # noqa: E501

        self._request_date_time = request_date_time

    @property
    def previous_expiration_date_time(self):
        """Gets the previous_expiration_date_time of this ResponseConsentReadExtensionsData.  # noqa: E501

        Data e hora de expiração anteriores a renovação. Reflete a data limite anterior de validade do consentimento. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC (UTC time format).  [Restrição] De preenchimento obrigatório nos casos em que houver validade determinada. Em casos de consentimento com prazo indeterminado, ou renovações feitas com a v2.2.0 em que não exista persistência dessa informação, o campo não deve ser preenchido.   # noqa: E501

        :return: The previous_expiration_date_time of this ResponseConsentReadExtensionsData.  # noqa: E501
        :rtype: datetime
        """
        return self._previous_expiration_date_time

    @previous_expiration_date_time.setter
    def previous_expiration_date_time(self, previous_expiration_date_time):
        """Sets the previous_expiration_date_time of this ResponseConsentReadExtensionsData.

        Data e hora de expiração anteriores a renovação. Reflete a data limite anterior de validade do consentimento. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC (UTC time format).  [Restrição] De preenchimento obrigatório nos casos em que houver validade determinada. Em casos de consentimento com prazo indeterminado, ou renovações feitas com a v2.2.0 em que não exista persistência dessa informação, o campo não deve ser preenchido.   # noqa: E501

        :param previous_expiration_date_time: The previous_expiration_date_time of this ResponseConsentReadExtensionsData.  # noqa: E501
        :type: datetime
        """

        self._previous_expiration_date_time = previous_expiration_date_time

    @property
    def x_fapi_customer_ip_address(self):
        """Gets the x_fapi_customer_ip_address of this ResponseConsentReadExtensionsData.  # noqa: E501

        O endereço IP do usuário logado com o receptor que solicitou a renovação sem redirecionamento.  [Restrição] De preenchimento obrigatório a partir da v3.0.0. Opcional para renovações feitas com a v2.2.0 quando não existir persistência dessa informação.   # noqa: E501

        :return: The x_fapi_customer_ip_address of this ResponseConsentReadExtensionsData.  # noqa: E501
        :rtype: str
        """
        return self._x_fapi_customer_ip_address

    @x_fapi_customer_ip_address.setter
    def x_fapi_customer_ip_address(self, x_fapi_customer_ip_address):
        """Sets the x_fapi_customer_ip_address of this ResponseConsentReadExtensionsData.

        O endereço IP do usuário logado com o receptor que solicitou a renovação sem redirecionamento.  [Restrição] De preenchimento obrigatório a partir da v3.0.0. Opcional para renovações feitas com a v2.2.0 quando não existir persistência dessa informação.   # noqa: E501

        :param x_fapi_customer_ip_address: The x_fapi_customer_ip_address of this ResponseConsentReadExtensionsData.  # noqa: E501
        :type: str
        """

        self._x_fapi_customer_ip_address = x_fapi_customer_ip_address

    @property
    def x_customer_user_agent(self):
        """Gets the x_customer_user_agent of this ResponseConsentReadExtensionsData.  # noqa: E501

        Indica o user-agent que o usuário utilizou quando solicitou a renovação sem redirecionamento.  [Restrição] De preenchimento obrigatório a partir da v3.0.0. Opcional para renovações feitas com a v2.2.0 quando não existir persistência dessa informação.   # noqa: E501

        :return: The x_customer_user_agent of this ResponseConsentReadExtensionsData.  # noqa: E501
        :rtype: str
        """
        return self._x_customer_user_agent

    @x_customer_user_agent.setter
    def x_customer_user_agent(self, x_customer_user_agent):
        """Sets the x_customer_user_agent of this ResponseConsentReadExtensionsData.

        Indica o user-agent que o usuário utilizou quando solicitou a renovação sem redirecionamento.  [Restrição] De preenchimento obrigatório a partir da v3.0.0. Opcional para renovações feitas com a v2.2.0 quando não existir persistência dessa informação.   # noqa: E501

        :param x_customer_user_agent: The x_customer_user_agent of this ResponseConsentReadExtensionsData.  # noqa: E501
        :type: str
        """

        self._x_customer_user_agent = x_customer_user_agent

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
        if issubclass(ResponseConsentReadExtensionsData, dict):
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
        if not isinstance(other, ResponseConsentReadExtensionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
