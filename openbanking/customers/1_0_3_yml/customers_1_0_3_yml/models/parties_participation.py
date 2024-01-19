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

class PartiesParticipation(object):
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
        'person_type': 'str',
        'type': 'str',
        'civil_name': 'str',
        'social_name': 'str',
        'company_name': 'str',
        'trade_name': 'str',
        'start_date': 'datetime',
        'shareholding': 'str',
        'document_type': 'EnumPartiesParticipationDocumentType',
        'document_number': 'str',
        'document_additional_info': 'str',
        'document_country': 'str',
        'document_expiration_date': 'date',
        'document_issue_date': 'date'
    }

    attribute_map = {
        'person_type': 'personType',
        'type': 'type',
        'civil_name': 'civilName',
        'social_name': 'socialName',
        'company_name': 'companyName',
        'trade_name': 'tradeName',
        'start_date': 'startDate',
        'shareholding': 'shareholding',
        'document_type': 'documentType',
        'document_number': 'documentNumber',
        'document_additional_info': 'documentAdditionalInfo',
        'document_country': 'documentCountry',
        'document_expiration_date': 'documentExpirationDate',
        'document_issue_date': 'documentIssueDate'
    }

    def __init__(self, person_type=None, type=None, civil_name=None, social_name=None, company_name=None, trade_name=None, start_date=None, shareholding=None, document_type=None, document_number=None, document_additional_info=None, document_country=None, document_expiration_date=None, document_issue_date=None):  # noqa: E501
        """PartiesParticipation - a model defined in Swagger"""  # noqa: E501
        self._person_type = None
        self._type = None
        self._civil_name = None
        self._social_name = None
        self._company_name = None
        self._trade_name = None
        self._start_date = None
        self._shareholding = None
        self._document_type = None
        self._document_number = None
        self._document_additional_info = None
        self._document_country = None
        self._document_expiration_date = None
        self._document_issue_date = None
        self.discriminator = None
        self.person_type = person_type
        self.type = type
        self.civil_name = civil_name
        self.social_name = social_name
        self.company_name = company_name
        if trade_name is not None:
            self.trade_name = trade_name
        self.start_date = start_date
        self.shareholding = shareholding
        self.document_type = document_type
        self.document_number = document_number
        if document_additional_info is not None:
            self.document_additional_info = document_additional_info
        self.document_country = document_country
        self.document_expiration_date = document_expiration_date
        if document_issue_date is not None:
            self.document_issue_date = document_issue_date

    @property
    def person_type(self):
        """Gets the person_type of this PartiesParticipation.  # noqa: E501

        Indica se a pessoa da parte envolvida é uma pessoa natural ou juridica  # noqa: E501

        :return: The person_type of this PartiesParticipation.  # noqa: E501
        :rtype: str
        """
        return self._person_type

    @person_type.setter
    def person_type(self, person_type):
        """Sets the person_type of this PartiesParticipation.

        Indica se a pessoa da parte envolvida é uma pessoa natural ou juridica  # noqa: E501

        :param person_type: The person_type of this PartiesParticipation.  # noqa: E501
        :type: str
        """
        if person_type is None:
            raise ValueError("Invalid value for `person_type`, must not be `None`")  # noqa: E501
        allowed_values = ["PESSOA_NATURAL", "PESSOA_JURIDICA"]  # noqa: E501
        if person_type not in allowed_values:
            raise ValueError(
                "Invalid value for `person_type` ({0}), must be one of {1}"  # noqa: E501
                .format(person_type, allowed_values)
            )

        self._person_type = person_type

    @property
    def type(self):
        """Gets the type of this PartiesParticipation.  # noqa: E501

        Indica o perfil de atuação na empresa. Vide Enum O administrador é o responsável por desempenhar todas as funções administrativas da empresa. É ele quem conduz o dia a dia do negócio, assinando documentos, respondendo legalmente pela sociedade, realizando empréstimos e outras ações gerenciais. Apesar de estar na linha de frente da empresa, ele é denominado sócio por também possuir sua parcela de participação no Capital Social. Sócio não tem qualquer envolvimento nas atividades administrativas da sociedade.   # noqa: E501

        :return: The type of this PartiesParticipation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PartiesParticipation.

        Indica o perfil de atuação na empresa. Vide Enum O administrador é o responsável por desempenhar todas as funções administrativas da empresa. É ele quem conduz o dia a dia do negócio, assinando documentos, respondendo legalmente pela sociedade, realizando empréstimos e outras ações gerenciais. Apesar de estar na linha de frente da empresa, ele é denominado sócio por também possuir sua parcela de participação no Capital Social. Sócio não tem qualquer envolvimento nas atividades administrativas da sociedade.   # noqa: E501

        :param type: The type of this PartiesParticipation.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["SOCIO", "ADMINISTRADOR"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def civil_name(self):
        """Gets the civil_name of this PartiesParticipation.  # noqa: E501

        Nome civil completo da pessoa natural (Direito fundamental da pessoa, o nome civil é aquele atribuído à pessoa natural desde o registro de seu nascimento, com o qual será identificada por toda a sua vida, bem como após a sua morte)  # noqa: E501

        :return: The civil_name of this PartiesParticipation.  # noqa: E501
        :rtype: str
        """
        return self._civil_name

    @civil_name.setter
    def civil_name(self, civil_name):
        """Sets the civil_name of this PartiesParticipation.

        Nome civil completo da pessoa natural (Direito fundamental da pessoa, o nome civil é aquele atribuído à pessoa natural desde o registro de seu nascimento, com o qual será identificada por toda a sua vida, bem como após a sua morte)  # noqa: E501

        :param civil_name: The civil_name of this PartiesParticipation.  # noqa: E501
        :type: str
        """
        if civil_name is None:
            raise ValueError("Invalid value for `civil_name`, must not be `None`")  # noqa: E501

        self._civil_name = civil_name

    @property
    def social_name(self):
        """Gets the social_name of this PartiesParticipation.  # noqa: E501

        Nome social da pessoa natural, se houver. (aquele pelo qual travestis e transexuais se reconhecem, bem como são identificados por sua comunidade e em seu meio social, conforme Decreto Local)  # noqa: E501

        :return: The social_name of this PartiesParticipation.  # noqa: E501
        :rtype: str
        """
        return self._social_name

    @social_name.setter
    def social_name(self, social_name):
        """Sets the social_name of this PartiesParticipation.

        Nome social da pessoa natural, se houver. (aquele pelo qual travestis e transexuais se reconhecem, bem como são identificados por sua comunidade e em seu meio social, conforme Decreto Local)  # noqa: E501

        :param social_name: The social_name of this PartiesParticipation.  # noqa: E501
        :type: str
        """
        if social_name is None:
            raise ValueError("Invalid value for `social_name`, must not be `None`")  # noqa: E501

        self._social_name = social_name

    @property
    def company_name(self):
        """Gets the company_name of this PartiesParticipation.  # noqa: E501

        Razão social da empresa consultada é o termo registrado sob o qual uma pessoa jurídica (PJ) se individualiza e exerce suas atividades. Também pode ser chamada por denominação social ou firma empresarial  # noqa: E501

        :return: The company_name of this PartiesParticipation.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this PartiesParticipation.

        Razão social da empresa consultada é o termo registrado sob o qual uma pessoa jurídica (PJ) se individualiza e exerce suas atividades. Também pode ser chamada por denominação social ou firma empresarial  # noqa: E501

        :param company_name: The company_name of this PartiesParticipation.  # noqa: E501
        :type: str
        """
        if company_name is None:
            raise ValueError("Invalid value for `company_name`, must not be `None`")  # noqa: E501

        self._company_name = company_name

    @property
    def trade_name(self):
        """Gets the trade_name of this PartiesParticipation.  # noqa: E501

        Nome fantasia da pessoa jurídica, se houver. (É o nome popular da empresa, utilizado para divulgação da empresa e melhor fixação com o público). De preenchimento obrigatório se houver  # noqa: E501

        :return: The trade_name of this PartiesParticipation.  # noqa: E501
        :rtype: str
        """
        return self._trade_name

    @trade_name.setter
    def trade_name(self, trade_name):
        """Sets the trade_name of this PartiesParticipation.

        Nome fantasia da pessoa jurídica, se houver. (É o nome popular da empresa, utilizado para divulgação da empresa e melhor fixação com o público). De preenchimento obrigatório se houver  # noqa: E501

        :param trade_name: The trade_name of this PartiesParticipation.  # noqa: E501
        :type: str
        """

        self._trade_name = trade_name

    @property
    def start_date(self):
        """Gets the start_date of this PartiesParticipation.  # noqa: E501

        Data de início da participação, conforme especificação RFC-3339.  # noqa: E501

        :return: The start_date of this PartiesParticipation.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PartiesParticipation.

        Data de início da participação, conforme especificação RFC-3339.  # noqa: E501

        :param start_date: The start_date of this PartiesParticipation.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def shareholding(self):
        """Gets the shareholding of this PartiesParticipation.  # noqa: E501

        Percentual de participação societária (informar com 2 casas decimais). Sócio só deve ser informado se sua participação societária for igual ou superior a 25%. p.ex: 0.25 (Este valor  representa 25%. O valor '1 'representa 100%)   # noqa: E501

        :return: The shareholding of this PartiesParticipation.  # noqa: E501
        :rtype: str
        """
        return self._shareholding

    @shareholding.setter
    def shareholding(self, shareholding):
        """Sets the shareholding of this PartiesParticipation.

        Percentual de participação societária (informar com 2 casas decimais). Sócio só deve ser informado se sua participação societária for igual ou superior a 25%. p.ex: 0.25 (Este valor  representa 25%. O valor '1 'representa 100%)   # noqa: E501

        :param shareholding: The shareholding of this PartiesParticipation.  # noqa: E501
        :type: str
        """
        if shareholding is None:
            raise ValueError("Invalid value for `shareholding`, must not be `None`")  # noqa: E501

        self._shareholding = shareholding

    @property
    def document_type(self):
        """Gets the document_type of this PartiesParticipation.  # noqa: E501


        :return: The document_type of this PartiesParticipation.  # noqa: E501
        :rtype: EnumPartiesParticipationDocumentType
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this PartiesParticipation.


        :param document_type: The document_type of this PartiesParticipation.  # noqa: E501
        :type: EnumPartiesParticipationDocumentType
        """
        if document_type is None:
            raise ValueError("Invalid value for `document_type`, must not be `None`")  # noqa: E501

        self._document_type = document_type

    @property
    def document_number(self):
        """Gets the document_number of this PartiesParticipation.  # noqa: E501

        Número do documento informado. Campo Texto Livre para preencher número e dígito do documento se houver  # noqa: E501

        :return: The document_number of this PartiesParticipation.  # noqa: E501
        :rtype: str
        """
        return self._document_number

    @document_number.setter
    def document_number(self, document_number):
        """Sets the document_number of this PartiesParticipation.

        Número do documento informado. Campo Texto Livre para preencher número e dígito do documento se houver  # noqa: E501

        :param document_number: The document_number of this PartiesParticipation.  # noqa: E501
        :type: str
        """
        if document_number is None:
            raise ValueError("Invalid value for `document_number`, must not be `None`")  # noqa: E501

        self._document_number = document_number

    @property
    def document_additional_info(self):
        """Gets the document_additional_info of this PartiesParticipation.  # noqa: E501

        Campo livre, de preenchimento obrigatório quando o documento informado tiver informações complementares relevantes para a sua identificação  # noqa: E501

        :return: The document_additional_info of this PartiesParticipation.  # noqa: E501
        :rtype: str
        """
        return self._document_additional_info

    @document_additional_info.setter
    def document_additional_info(self, document_additional_info):
        """Sets the document_additional_info of this PartiesParticipation.

        Campo livre, de preenchimento obrigatório quando o documento informado tiver informações complementares relevantes para a sua identificação  # noqa: E501

        :param document_additional_info: The document_additional_info of this PartiesParticipation.  # noqa: E501
        :type: str
        """

        self._document_additional_info = document_additional_info

    @property
    def document_country(self):
        """Gets the document_country of this PartiesParticipation.  # noqa: E501

        País de emissão do documento. Código do pais de acordo com o código alpha3 do ISO-3166.  # noqa: E501

        :return: The document_country of this PartiesParticipation.  # noqa: E501
        :rtype: str
        """
        return self._document_country

    @document_country.setter
    def document_country(self, document_country):
        """Sets the document_country of this PartiesParticipation.

        País de emissão do documento. Código do pais de acordo com o código alpha3 do ISO-3166.  # noqa: E501

        :param document_country: The document_country of this PartiesParticipation.  # noqa: E501
        :type: str
        """
        if document_country is None:
            raise ValueError("Invalid value for `document_country`, must not be `None`")  # noqa: E501

        self._document_country = document_country

    @property
    def document_expiration_date(self):
        """Gets the document_expiration_date of this PartiesParticipation.  # noqa: E501

        Data de validade do documento informado, conforme especificação RFC-3339.  # noqa: E501

        :return: The document_expiration_date of this PartiesParticipation.  # noqa: E501
        :rtype: date
        """
        return self._document_expiration_date

    @document_expiration_date.setter
    def document_expiration_date(self, document_expiration_date):
        """Sets the document_expiration_date of this PartiesParticipation.

        Data de validade do documento informado, conforme especificação RFC-3339.  # noqa: E501

        :param document_expiration_date: The document_expiration_date of this PartiesParticipation.  # noqa: E501
        :type: date
        """
        if document_expiration_date is None:
            raise ValueError("Invalid value for `document_expiration_date`, must not be `None`")  # noqa: E501

        self._document_expiration_date = document_expiration_date

    @property
    def document_issue_date(self):
        """Gets the document_issue_date of this PartiesParticipation.  # noqa: E501

        Data de emissão do documento, conforme especificação RFC-3339.  # noqa: E501

        :return: The document_issue_date of this PartiesParticipation.  # noqa: E501
        :rtype: date
        """
        return self._document_issue_date

    @document_issue_date.setter
    def document_issue_date(self, document_issue_date):
        """Sets the document_issue_date of this PartiesParticipation.

        Data de emissão do documento, conforme especificação RFC-3339.  # noqa: E501

        :param document_issue_date: The document_issue_date of this PartiesParticipation.  # noqa: E501
        :type: date
        """

        self._document_issue_date = document_issue_date

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
        if issubclass(PartiesParticipation, dict):
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
        if not isinstance(other, PartiesParticipation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
