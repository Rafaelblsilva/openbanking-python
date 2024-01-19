# coding: utf-8

"""
    API Consents - Open Finance Brasil

    API que trata da criação, consulta e revogação de consentimentos para o Open Finance Brasil Fase 2 - customer-data.   Não possui segregação entre pessoa natural e pessoa jurídica.      # Orientações importantes A API Consents trata dos consentimentos exclusivamente para a fase 2 do Open Finance Brasil. - As informações da instituição receptora não trafegam na API Consents – a autenticação da receptora se dá através do [DCR](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378307/Dynamic+Client+Registration).    - Na chamada para a criação do consentimento deve-se utilizar um token gerado via `client_credentials`. - Após o `POST` de criação do consentimento, o `STATUS` devolvido na resposta deverá ser `AWAITING_AUTHORISATION`. - O `STATUS` será alterado para `AUTHORISED` somente após autenticação e confirmação por parte do usuário na instituição transmissora dos dados. - Alteração obrigatória do status `AWAITING_AUTHORISATION` para `REVOKED` após 60 minutos. - Todas as datas trafegadas nesta API seguem o padrão da [RFC3339](https://tools.ietf.org/html/rfc3339) e formato \"zulu\". - A descrição do fluxo de consentimento encontra-se disponível no [Portal do desenvolvedor](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17369300/Dados+Cadastrais+e+Transacionais#Fluxo-b%C3%A1sico-de-consentimento). - O arquivo com o mapeamento completo entre `Roles`, `scopes` e `permissions` está disponibilizado no Portal do desenvolvedor, no mesmo item acima - descrição do fluxo de consentimento. - A receptora deve enviar obrigatoriamente, no pedido de criação de consentimento, todas as permissions dos agrupamentos de dados as quais ela deseja consentimento, conforme tabela abaixo:      ```   |----------------------|-------------------------------|----------------------------------------------------------|   | CATEGORIA DE DADOS   | AGRUPAMENTO                   | PERMISSIONS                                              |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Dados Cadastrais PF           | CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Informações complementares PF | CUSTOMERS_PERSONAL_ADITTIONALINFO_READ                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Dados Cadastrais PJ           | CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Informações complementares PJ | CUSTOMERS_BUSINESS_ADITTIONALINFO_READ                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Saldos                        | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_BALANCES_READ                                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Limites                       | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_OVERDRAFT_LIMITS_READ                           |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Extratos                      | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_TRANSACTIONS_READ                               |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Limites                       | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_LIMITS_READ                        |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Transações                    | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Faturas                       | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_READ                         |   |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ            |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Operações de Crédito | Dados do Contrato             | LOANS_READ                                               |   |                      |                               | LOANS_WARRANTIES_READ                                    |   |                      |                               | LOANS_SCHEDULED_INSTALMENTS_READ                         |   |                      |                               | LOANS_PAYMENTS_READ                                      |   |                      |                               | FINANCINGS_READ                                          |   |                      |                               | FINANCINGS_WARRANTIES_READ                               |   |                      |                               | FINANCINGS_SCHEDULED_INSTALMENTS_READ                    |   |                      |                               | FINANCINGS_PAYMENTS_READ                                 |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_READ                       |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_WARRANTIES_READ            |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_SCHEDULED_INSTALMENTS_READ |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_PAYMENTS_READ              |   |                      |                               | INVOICE_FINANCINGS_READ                                  |   |                      |                               | INVOICE_FINANCINGS_WARRANTIES_READ                       |   |                      |                               | INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ            |   |                      |                               | INVOICE_FINANCINGS_PAYMENTS_READ                         |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   ``` - A instituição transmissora deve validar o preenchimento correto desses agrupamentos no momento da geração do consentimento. - Caso a instiuição receptora envie permissões divergentes ao agrupamento especificado na tabela, a transmissora deve rejeitar o pedido da receptora dando retorno HTTP Status Code 400. - A transmissora deve retornar, da lista de permissions requisitadas, apenas o subconjunto de permissions por ela suportada, removendo da lista as permissions de produtos não suportados e retornando HTTP Status Code 201. Caso não restem permissões funcionais, a instituição transmissora deve retornar o erro HTTP Code \"422 Unprocessable Entity\".   # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseErrorErrors(object):
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
        'code': 'str',
        'title': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'code': 'code',
        'title': 'title',
        'detail': 'detail'
    }

    def __init__(self, code=None, title=None, detail=None):  # noqa: E501
        """ResponseErrorErrors - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._title = None
        self._detail = None
        self.discriminator = None
        self.code = code
        self.title = title
        self.detail = detail

    @property
    def code(self):
        """Gets the code of this ResponseErrorErrors.  # noqa: E501

        Código de erro específico do endpoint  # noqa: E501

        :return: The code of this ResponseErrorErrors.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ResponseErrorErrors.

        Código de erro específico do endpoint  # noqa: E501

        :param code: The code of this ResponseErrorErrors.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def title(self):
        """Gets the title of this ResponseErrorErrors.  # noqa: E501

        Título legível por humanos deste erro específico  # noqa: E501

        :return: The title of this ResponseErrorErrors.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ResponseErrorErrors.

        Título legível por humanos deste erro específico  # noqa: E501

        :param title: The title of this ResponseErrorErrors.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def detail(self):
        """Gets the detail of this ResponseErrorErrors.  # noqa: E501

        Descrição legível por humanos deste erro específico  # noqa: E501

        :return: The detail of this ResponseErrorErrors.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ResponseErrorErrors.

        Descrição legível por humanos deste erro específico  # noqa: E501

        :param detail: The detail of this ResponseErrorErrors.  # noqa: E501
        :type: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

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
        if issubclass(ResponseErrorErrors, dict):
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
        if not isinstance(other, ResponseErrorErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
