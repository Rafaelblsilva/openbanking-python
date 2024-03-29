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

class BusinessIdentificationData(object):
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
        'update_date_time': 'datetime',
        'business_id': 'str',
        'brand_name': 'str',
        'company_name': 'str',
        'trade_name': 'str',
        'incorporation_date': 'datetime',
        'cnpj_number': 'str',
        'company_cnpj_number': 'list[str]',
        'other_documents': 'list[BusinessOtherDocument]',
        'parties': 'list[PartiesParticipation]',
        'contacts': 'BusinessContacts'
    }

    attribute_map = {
        'update_date_time': 'updateDateTime',
        'business_id': 'businessId',
        'brand_name': 'brandName',
        'company_name': 'companyName',
        'trade_name': 'tradeName',
        'incorporation_date': 'incorporationDate',
        'cnpj_number': 'cnpjNumber',
        'company_cnpj_number': 'companyCnpjNumber',
        'other_documents': 'otherDocuments',
        'parties': 'parties',
        'contacts': 'contacts'
    }

    def __init__(self, update_date_time=None, business_id=None, brand_name=None, company_name=None, trade_name=None, incorporation_date=None, cnpj_number=None, company_cnpj_number=None, other_documents=None, parties=None, contacts=None):  # noqa: E501
        """BusinessIdentificationData - a model defined in Swagger"""  # noqa: E501
        self._update_date_time = None
        self._business_id = None
        self._brand_name = None
        self._company_name = None
        self._trade_name = None
        self._incorporation_date = None
        self._cnpj_number = None
        self._company_cnpj_number = None
        self._other_documents = None
        self._parties = None
        self._contacts = None
        self.discriminator = None
        self.update_date_time = update_date_time
        self.business_id = business_id
        self.brand_name = brand_name
        self.company_name = company_name
        self.trade_name = trade_name
        self.incorporation_date = incorporation_date
        self.cnpj_number = cnpj_number
        self.company_cnpj_number = company_cnpj_number
        if other_documents is not None:
            self.other_documents = other_documents
        self.parties = parties
        self.contacts = contacts

    @property
    def update_date_time(self):
        """Gets the update_date_time of this BusinessIdentificationData.  # noqa: E501

        Data e hora da atualização do bloco, conforme especificação RFC-3339  # noqa: E501

        :return: The update_date_time of this BusinessIdentificationData.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date_time

    @update_date_time.setter
    def update_date_time(self, update_date_time):
        """Sets the update_date_time of this BusinessIdentificationData.

        Data e hora da atualização do bloco, conforme especificação RFC-3339  # noqa: E501

        :param update_date_time: The update_date_time of this BusinessIdentificationData.  # noqa: E501
        :type: datetime
        """
        if update_date_time is None:
            raise ValueError("Invalid value for `update_date_time`, must not be `None`")  # noqa: E501

        self._update_date_time = update_date_time

    @property
    def business_id(self):
        """Gets the business_id of this BusinessIdentificationData.  # noqa: E501

        Um identificador único e imutável usado para identificar o recurso cliente pessoa jurídica. Este identificador não tem significado para o cliente que deu o consentimento  # noqa: E501

        :return: The business_id of this BusinessIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this BusinessIdentificationData.

        Um identificador único e imutável usado para identificar o recurso cliente pessoa jurídica. Este identificador não tem significado para o cliente que deu o consentimento  # noqa: E501

        :param business_id: The business_id of this BusinessIdentificationData.  # noqa: E501
        :type: str
        """
        if business_id is None:
            raise ValueError("Invalid value for `business_id`, must not be `None`")  # noqa: E501

        self._business_id = business_id

    @property
    def brand_name(self):
        """Gets the brand_name of this BusinessIdentificationData.  # noqa: E501

        Nome da Marca reportada pelo participante do Open Banking. O conceito a que se refere a 'marca' é em essência uma promessa da empresa em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes   # noqa: E501

        :return: The brand_name of this BusinessIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this BusinessIdentificationData.

        Nome da Marca reportada pelo participante do Open Banking. O conceito a que se refere a 'marca' é em essência uma promessa da empresa em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes   # noqa: E501

        :param brand_name: The brand_name of this BusinessIdentificationData.  # noqa: E501
        :type: str
        """
        if brand_name is None:
            raise ValueError("Invalid value for `brand_name`, must not be `None`")  # noqa: E501

        self._brand_name = brand_name

    @property
    def company_name(self):
        """Gets the company_name of this BusinessIdentificationData.  # noqa: E501

        Razão social da empresa consultada é o termo registrado sob o qual uma pessoa jurídica (PJ) se individualiza e exerce suas atividades. Também pode ser chamada por denominação social ou firma empresarial  # noqa: E501

        :return: The company_name of this BusinessIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this BusinessIdentificationData.

        Razão social da empresa consultada é o termo registrado sob o qual uma pessoa jurídica (PJ) se individualiza e exerce suas atividades. Também pode ser chamada por denominação social ou firma empresarial  # noqa: E501

        :param company_name: The company_name of this BusinessIdentificationData.  # noqa: E501
        :type: str
        """
        if company_name is None:
            raise ValueError("Invalid value for `company_name`, must not be `None`")  # noqa: E501

        self._company_name = company_name

    @property
    def trade_name(self):
        """Gets the trade_name of this BusinessIdentificationData.  # noqa: E501

        Nome fantasia da pessoa jurídica, se houver. (É o nome popular da empresa, utilizado para divulgação da empresa e melhor fixação com o público). De preenchimento obrigatório se houver  # noqa: E501

        :return: The trade_name of this BusinessIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._trade_name

    @trade_name.setter
    def trade_name(self, trade_name):
        """Sets the trade_name of this BusinessIdentificationData.

        Nome fantasia da pessoa jurídica, se houver. (É o nome popular da empresa, utilizado para divulgação da empresa e melhor fixação com o público). De preenchimento obrigatório se houver  # noqa: E501

        :param trade_name: The trade_name of this BusinessIdentificationData.  # noqa: E501
        :type: str
        """
        if trade_name is None:
            raise ValueError("Invalid value for `trade_name`, must not be `None`")  # noqa: E501

        self._trade_name = trade_name

    @property
    def incorporation_date(self):
        """Gets the incorporation_date of this BusinessIdentificationData.  # noqa: E501

        Data de constituição da empresa, conforme especificação RFC-3339.  # noqa: E501

        :return: The incorporation_date of this BusinessIdentificationData.  # noqa: E501
        :rtype: datetime
        """
        return self._incorporation_date

    @incorporation_date.setter
    def incorporation_date(self, incorporation_date):
        """Sets the incorporation_date of this BusinessIdentificationData.

        Data de constituição da empresa, conforme especificação RFC-3339.  # noqa: E501

        :param incorporation_date: The incorporation_date of this BusinessIdentificationData.  # noqa: E501
        :type: datetime
        """
        if incorporation_date is None:
            raise ValueError("Invalid value for `incorporation_date`, must not be `None`")  # noqa: E501

        self._incorporation_date = incorporation_date

    @property
    def cnpj_number(self):
        """Gets the cnpj_number of this BusinessIdentificationData.  # noqa: E501

        Número completo do CNPJ da Empresa consultada  - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara  # noqa: E501

        :return: The cnpj_number of this BusinessIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._cnpj_number

    @cnpj_number.setter
    def cnpj_number(self, cnpj_number):
        """Sets the cnpj_number of this BusinessIdentificationData.

        Número completo do CNPJ da Empresa consultada  - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara  # noqa: E501

        :param cnpj_number: The cnpj_number of this BusinessIdentificationData.  # noqa: E501
        :type: str
        """
        if cnpj_number is None:
            raise ValueError("Invalid value for `cnpj_number`, must not be `None`")  # noqa: E501

        self._cnpj_number = cnpj_number

    @property
    def company_cnpj_number(self):
        """Gets the company_cnpj_number of this BusinessIdentificationData.  # noqa: E501

        Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica.  Deve-se ter apenas os números do CNPJ, sem máscara   # noqa: E501

        :return: The company_cnpj_number of this BusinessIdentificationData.  # noqa: E501
        :rtype: list[str]
        """
        return self._company_cnpj_number

    @company_cnpj_number.setter
    def company_cnpj_number(self, company_cnpj_number):
        """Sets the company_cnpj_number of this BusinessIdentificationData.

        Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica.  Deve-se ter apenas os números do CNPJ, sem máscara   # noqa: E501

        :param company_cnpj_number: The company_cnpj_number of this BusinessIdentificationData.  # noqa: E501
        :type: list[str]
        """
        if company_cnpj_number is None:
            raise ValueError("Invalid value for `company_cnpj_number`, must not be `None`")  # noqa: E501

        self._company_cnpj_number = company_cnpj_number

    @property
    def other_documents(self):
        """Gets the other_documents of this BusinessIdentificationData.  # noqa: E501

        Relação dos demais documentos  # noqa: E501

        :return: The other_documents of this BusinessIdentificationData.  # noqa: E501
        :rtype: list[BusinessOtherDocument]
        """
        return self._other_documents

    @other_documents.setter
    def other_documents(self, other_documents):
        """Sets the other_documents of this BusinessIdentificationData.

        Relação dos demais documentos  # noqa: E501

        :param other_documents: The other_documents of this BusinessIdentificationData.  # noqa: E501
        :type: list[BusinessOtherDocument]
        """

        self._other_documents = other_documents

    @property
    def parties(self):
        """Gets the parties of this BusinessIdentificationData.  # noqa: E501

        Lista relativa às informações das partes envolvidas, como: sócio e /ou administrador   # noqa: E501

        :return: The parties of this BusinessIdentificationData.  # noqa: E501
        :rtype: list[PartiesParticipation]
        """
        return self._parties

    @parties.setter
    def parties(self, parties):
        """Sets the parties of this BusinessIdentificationData.

        Lista relativa às informações das partes envolvidas, como: sócio e /ou administrador   # noqa: E501

        :param parties: The parties of this BusinessIdentificationData.  # noqa: E501
        :type: list[PartiesParticipation]
        """
        if parties is None:
            raise ValueError("Invalid value for `parties`, must not be `None`")  # noqa: E501

        self._parties = parties

    @property
    def contacts(self):
        """Gets the contacts of this BusinessIdentificationData.  # noqa: E501


        :return: The contacts of this BusinessIdentificationData.  # noqa: E501
        :rtype: BusinessContacts
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this BusinessIdentificationData.


        :param contacts: The contacts of this BusinessIdentificationData.  # noqa: E501
        :type: BusinessContacts
        """
        if contacts is None:
            raise ValueError("Invalid value for `contacts`, must not be `None`")  # noqa: E501

        self._contacts = contacts

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
        if issubclass(BusinessIdentificationData, dict):
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
        if not isinstance(other, BusinessIdentificationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
