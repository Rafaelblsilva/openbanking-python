# coding: utf-8

"""
    API Funds - Open Finance Brasil

    API de informações de operações de Fundos de Investimento Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Fundos de Investimento mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente e movimentações financeiras.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  Devem ser considerados como escopo de exposição todos os fundos de investimento classificados como: Renda Fixa, Ações, Multimercado e Cambial.  Para identificação do produto e posição do cliente, a exposição será de forma consolidada por Fundo de Investimento.  Para movimentações, a exposição se dará pela Ordem do Cliente, por exemplo, uma Ordem de Resgate é compartilhada como uma única movimentação, mesmo que esteja associada a diferentes Certificados (Cautelas).  As instituições podem apresentar cenários distintos no que diz respeito ao sincronismo entre posição `/balances` e movimentação `/transactions` e `/transactions-current` da API:  - Algumas instituições refletem movimentações ainda não convertidas na posição do cliente em seus canais eletrônicos. Isso implica que pode ocorrer compartilhamento de posição atualizada, cujas movimentações relacionadas serão expostas no ecossistema apenas após a conversão das mesmas;  - Outras instituições refletem na posição apenas movimentações convertidas nos seus canais eletrônicos. Isso implica que o compartilhamento da posição em relação às movimentações é feito de forma sincronizada no ecossistema.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc3.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseFundsProductIdentificationData(object):
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
        'name': 'str',
        'cnpj_number': 'str',
        'isin_code': 'str',
        'anbima_category': 'str',
        'anbima_class': 'str',
        'anbima_subclass': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cnpj_number': 'cnpjNumber',
        'isin_code': 'isinCode',
        'anbima_category': 'anbimaCategory',
        'anbima_class': 'anbimaClass',
        'anbima_subclass': 'anbimaSubclass'
    }

    def __init__(self, name=None, cnpj_number=None, isin_code=None, anbima_category=None, anbima_class=None, anbima_subclass=None):  # noqa: E501
        """ResponseFundsProductIdentificationData - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._cnpj_number = None
        self._isin_code = None
        self._anbima_category = None
        self._anbima_class = None
        self._anbima_subclass = None
        self.discriminator = None
        self.name = name
        self.cnpj_number = cnpj_number
        if isin_code is not None:
            self.isin_code = isin_code
        if anbima_category is not None:
            self.anbima_category = anbima_category
        if anbima_class is not None:
            self.anbima_class = anbima_class
        if anbima_subclass is not None:
            self.anbima_subclass = anbima_subclass

    @property
    def name(self):
        """Gets the name of this ResponseFundsProductIdentificationData.  # noqa: E501

        Nome oficial do fundo de investimento conforme exibido para os clientes nos canais eletrônicos.  # noqa: E501

        :return: The name of this ResponseFundsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ResponseFundsProductIdentificationData.

        Nome oficial do fundo de investimento conforme exibido para os clientes nos canais eletrônicos.  # noqa: E501

        :param name: The name of this ResponseFundsProductIdentificationData.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def cnpj_number(self):
        """Gets the cnpj_number of this ResponseFundsProductIdentificationData.  # noqa: E501

        CNPJ do fundo de investimento.  # noqa: E501

        :return: The cnpj_number of this ResponseFundsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._cnpj_number

    @cnpj_number.setter
    def cnpj_number(self, cnpj_number):
        """Sets the cnpj_number of this ResponseFundsProductIdentificationData.

        CNPJ do fundo de investimento.  # noqa: E501

        :param cnpj_number: The cnpj_number of this ResponseFundsProductIdentificationData.  # noqa: E501
        :type: str
        """
        if cnpj_number is None:
            raise ValueError("Invalid value for `cnpj_number`, must not be `None`")  # noqa: E501

        self._cnpj_number = cnpj_number

    @property
    def isin_code(self):
        """Gets the isin_code of this ResponseFundsProductIdentificationData.  # noqa: E501

        Código universal que identifica cada valor mobiliário ou instrumento financeiro, conforme Norma ISO 6166.  DEFINIÇÃO: O ISIN (International Securities Identification Number) é um código que identifica um valor mobiliário, conforme a norma ISO 6166.  ESTRUTURA: O ISIN é um código alfanumérico que possui 12 caracteres com a seguinte estrutura:   - Um prefixo, composto de 2 caracteres alfa, que identifica o código do país (Norma ISO 3166); - O número básico, composto de 9 caracteres alfabéticos ou numéricos em sua extensão; - Um dígito numérico de controle.   # noqa: E501

        :return: The isin_code of this ResponseFundsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._isin_code

    @isin_code.setter
    def isin_code(self, isin_code):
        """Sets the isin_code of this ResponseFundsProductIdentificationData.

        Código universal que identifica cada valor mobiliário ou instrumento financeiro, conforme Norma ISO 6166.  DEFINIÇÃO: O ISIN (International Securities Identification Number) é um código que identifica um valor mobiliário, conforme a norma ISO 6166.  ESTRUTURA: O ISIN é um código alfanumérico que possui 12 caracteres com a seguinte estrutura:   - Um prefixo, composto de 2 caracteres alfa, que identifica o código do país (Norma ISO 3166); - O número básico, composto de 9 caracteres alfabéticos ou numéricos em sua extensão; - Um dígito numérico de controle.   # noqa: E501

        :param isin_code: The isin_code of this ResponseFundsProductIdentificationData.  # noqa: E501
        :type: str
        """

        self._isin_code = isin_code

    @property
    def anbima_category(self):
        """Gets the anbima_category of this ResponseFundsProductIdentificationData.  # noqa: E501

        Conforme classificação ANBIMA, que segue a deliberação 77 da ANBIMA.  – Renda Fixa  – Ações  – Multimercado  – Cambial  https://www.anbima.com.br/data/files/5A/44/2C/B7/8411B510CD3B4DA568A80AC2/DeliberacaoN77-Diretriz-de-Classificacao-de-Fundos.pdf   # noqa: E501

        :return: The anbima_category of this ResponseFundsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._anbima_category

    @anbima_category.setter
    def anbima_category(self, anbima_category):
        """Sets the anbima_category of this ResponseFundsProductIdentificationData.

        Conforme classificação ANBIMA, que segue a deliberação 77 da ANBIMA.  – Renda Fixa  – Ações  – Multimercado  – Cambial  https://www.anbima.com.br/data/files/5A/44/2C/B7/8411B510CD3B4DA568A80AC2/DeliberacaoN77-Diretriz-de-Classificacao-de-Fundos.pdf   # noqa: E501

        :param anbima_category: The anbima_category of this ResponseFundsProductIdentificationData.  # noqa: E501
        :type: str
        """
        allowed_values = ["RENDA_FIXA", "ACOES", "MULTIMERCADO", "CAMBIAL"]  # noqa: E501
        if anbima_category not in allowed_values:
            raise ValueError(
                "Invalid value for `anbima_category` ({0}), must be one of {1}"  # noqa: E501
                .format(anbima_category, allowed_values)
            )

        self._anbima_category = anbima_category

    @property
    def anbima_class(self):
        """Gets the anbima_class of this ResponseFundsProductIdentificationData.  # noqa: E501

        Campo necessário para aderência a Resolução CVM175. Aguardando definições de mercado. Deve se tratar de campo do tipo enum.  # noqa: E501

        :return: The anbima_class of this ResponseFundsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._anbima_class

    @anbima_class.setter
    def anbima_class(self, anbima_class):
        """Sets the anbima_class of this ResponseFundsProductIdentificationData.

        Campo necessário para aderência a Resolução CVM175. Aguardando definições de mercado. Deve se tratar de campo do tipo enum.  # noqa: E501

        :param anbima_class: The anbima_class of this ResponseFundsProductIdentificationData.  # noqa: E501
        :type: str
        """

        self._anbima_class = anbima_class

    @property
    def anbima_subclass(self):
        """Gets the anbima_subclass of this ResponseFundsProductIdentificationData.  # noqa: E501

        Campo necessário para aderência a Resolução CVM175. Aguardando definições de mercado. Deve se tratar de campo do tipo enum.  # noqa: E501

        :return: The anbima_subclass of this ResponseFundsProductIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._anbima_subclass

    @anbima_subclass.setter
    def anbima_subclass(self, anbima_subclass):
        """Sets the anbima_subclass of this ResponseFundsProductIdentificationData.

        Campo necessário para aderência a Resolução CVM175. Aguardando definições de mercado. Deve se tratar de campo do tipo enum.  # noqa: E501

        :param anbima_subclass: The anbima_subclass of this ResponseFundsProductIdentificationData.  # noqa: E501
        :type: str
        """

        self._anbima_subclass = anbima_subclass

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
        if issubclass(ResponseFundsProductIdentificationData, dict):
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
        if not isinstance(other, ResponseFundsProductIdentificationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
