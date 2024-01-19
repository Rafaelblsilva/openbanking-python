# coding: utf-8

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.6
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalIdentificationData(object):
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
        'personal_id': 'str',
        'brand_name': 'str',
        'civil_name': 'str',
        'social_name': 'str',
        'birth_date': 'date',
        'marital_status_code': 'EnumMaritalStatusCode',
        'marital_status_additional_info': 'str',
        'sex': 'EnumSex',
        'company_cnpj': 'list[str]',
        'documents': 'PersonalDocument',
        'other_documents': 'list[PersonalOtherDocument]',
        'has_brazilian_nationality': 'bool',
        'nationality': 'list[Nationality]',
        'filiation': 'list[PersonalIdentificationDataFiliation]',
        'contacts': 'PersonalContacts'
    }

    attribute_map = {
        'update_date_time': 'updateDateTime',
        'personal_id': 'personalId',
        'brand_name': 'brandName',
        'civil_name': 'civilName',
        'social_name': 'socialName',
        'birth_date': 'birthDate',
        'marital_status_code': 'maritalStatusCode',
        'marital_status_additional_info': 'maritalStatusAdditionalInfo',
        'sex': 'sex',
        'company_cnpj': 'companyCnpj',
        'documents': 'documents',
        'other_documents': 'otherDocuments',
        'has_brazilian_nationality': 'hasBrazilianNationality',
        'nationality': 'nationality',
        'filiation': 'filiation',
        'contacts': 'contacts'
    }

    def __init__(self, update_date_time=None, personal_id=None, brand_name=None, civil_name=None, social_name=None, birth_date=None, marital_status_code=None, marital_status_additional_info=None, sex=None, company_cnpj=None, documents=None, other_documents=None, has_brazilian_nationality=None, nationality=None, filiation=None, contacts=None):  # noqa: E501
        """PersonalIdentificationData - a model defined in Swagger"""  # noqa: E501
        self._update_date_time = None
        self._personal_id = None
        self._brand_name = None
        self._civil_name = None
        self._social_name = None
        self._birth_date = None
        self._marital_status_code = None
        self._marital_status_additional_info = None
        self._sex = None
        self._company_cnpj = None
        self._documents = None
        self._other_documents = None
        self._has_brazilian_nationality = None
        self._nationality = None
        self._filiation = None
        self._contacts = None
        self.discriminator = None
        self.update_date_time = update_date_time
        self.personal_id = personal_id
        self.brand_name = brand_name
        self.civil_name = civil_name
        self.social_name = social_name
        self.birth_date = birth_date
        self.marital_status_code = marital_status_code
        if marital_status_additional_info is not None:
            self.marital_status_additional_info = marital_status_additional_info
        self.sex = sex
        self.company_cnpj = company_cnpj
        self.documents = documents
        self.other_documents = other_documents
        self.has_brazilian_nationality = has_brazilian_nationality
        self.nationality = nationality
        self.filiation = filiation
        self.contacts = contacts

    @property
    def update_date_time(self):
        """Gets the update_date_time of this PersonalIdentificationData.  # noqa: E501


        :return: The update_date_time of this PersonalIdentificationData.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date_time

    @update_date_time.setter
    def update_date_time(self, update_date_time):
        """Sets the update_date_time of this PersonalIdentificationData.


        :param update_date_time: The update_date_time of this PersonalIdentificationData.  # noqa: E501
        :type: datetime
        """
        if update_date_time is None:
            raise ValueError("Invalid value for `update_date_time`, must not be `None`")  # noqa: E501

        self._update_date_time = update_date_time

    @property
    def personal_id(self):
        """Gets the personal_id of this PersonalIdentificationData.  # noqa: E501

        Um identificador único e imutável usado para identificar o recurso cliente pessoa natural. Este identificador não tem significado para o cliente que deu o consentimento  # noqa: E501

        :return: The personal_id of this PersonalIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._personal_id

    @personal_id.setter
    def personal_id(self, personal_id):
        """Sets the personal_id of this PersonalIdentificationData.

        Um identificador único e imutável usado para identificar o recurso cliente pessoa natural. Este identificador não tem significado para o cliente que deu o consentimento  # noqa: E501

        :param personal_id: The personal_id of this PersonalIdentificationData.  # noqa: E501
        :type: str
        """
        if personal_id is None:
            raise ValueError("Invalid value for `personal_id`, must not be `None`")  # noqa: E501

        self._personal_id = personal_id

    @property
    def brand_name(self):
        """Gets the brand_name of this PersonalIdentificationData.  # noqa: E501

        Nome da Marca reportada pelo participante do Open Banking. O conceito a que se refere a 'marca' é em essência uma promessa da empresa em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes  # noqa: E501

        :return: The brand_name of this PersonalIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this PersonalIdentificationData.

        Nome da Marca reportada pelo participante do Open Banking. O conceito a que se refere a 'marca' é em essência uma promessa da empresa em fornecer uma série específica de atributos, benefícios e serviços uniformes aos clientes  # noqa: E501

        :param brand_name: The brand_name of this PersonalIdentificationData.  # noqa: E501
        :type: str
        """
        if brand_name is None:
            raise ValueError("Invalid value for `brand_name`, must not be `None`")  # noqa: E501

        self._brand_name = brand_name

    @property
    def civil_name(self):
        """Gets the civil_name of this PersonalIdentificationData.  # noqa: E501

        Nome civil completo da pessoa natural (Direito fundamental da pessoa, o nome civil é aquele atribuído à pessoa natural desde o registro de seu nascimento, com o qual será identificada por toda a sua vida, bem como após a sua morte)  # noqa: E501

        :return: The civil_name of this PersonalIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._civil_name

    @civil_name.setter
    def civil_name(self, civil_name):
        """Sets the civil_name of this PersonalIdentificationData.

        Nome civil completo da pessoa natural (Direito fundamental da pessoa, o nome civil é aquele atribuído à pessoa natural desde o registro de seu nascimento, com o qual será identificada por toda a sua vida, bem como após a sua morte)  # noqa: E501

        :param civil_name: The civil_name of this PersonalIdentificationData.  # noqa: E501
        :type: str
        """
        if civil_name is None:
            raise ValueError("Invalid value for `civil_name`, must not be `None`")  # noqa: E501

        self._civil_name = civil_name

    @property
    def social_name(self):
        """Gets the social_name of this PersonalIdentificationData.  # noqa: E501

        Nome social da pessoa natural, se houver. (aquele pelo qual travestis e transexuais se reconhecem, bem como são identificados por sua comunidade e em seu meio social, conforme Decreto Local)  # noqa: E501

        :return: The social_name of this PersonalIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._social_name

    @social_name.setter
    def social_name(self, social_name):
        """Sets the social_name of this PersonalIdentificationData.

        Nome social da pessoa natural, se houver. (aquele pelo qual travestis e transexuais se reconhecem, bem como são identificados por sua comunidade e em seu meio social, conforme Decreto Local)  # noqa: E501

        :param social_name: The social_name of this PersonalIdentificationData.  # noqa: E501
        :type: str
        """
        if social_name is None:
            raise ValueError("Invalid value for `social_name`, must not be `None`")  # noqa: E501

        self._social_name = social_name

    @property
    def birth_date(self):
        """Gets the birth_date of this PersonalIdentificationData.  # noqa: E501

        Data de nascimento, conforme especificação RFC-3339  # noqa: E501

        :return: The birth_date of this PersonalIdentificationData.  # noqa: E501
        :rtype: date
        """
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        """Sets the birth_date of this PersonalIdentificationData.

        Data de nascimento, conforme especificação RFC-3339  # noqa: E501

        :param birth_date: The birth_date of this PersonalIdentificationData.  # noqa: E501
        :type: date
        """
        if birth_date is None:
            raise ValueError("Invalid value for `birth_date`, must not be `None`")  # noqa: E501

        self._birth_date = birth_date

    @property
    def marital_status_code(self):
        """Gets the marital_status_code of this PersonalIdentificationData.  # noqa: E501


        :return: The marital_status_code of this PersonalIdentificationData.  # noqa: E501
        :rtype: EnumMaritalStatusCode
        """
        return self._marital_status_code

    @marital_status_code.setter
    def marital_status_code(self, marital_status_code):
        """Sets the marital_status_code of this PersonalIdentificationData.


        :param marital_status_code: The marital_status_code of this PersonalIdentificationData.  # noqa: E501
        :type: EnumMaritalStatusCode
        """
        if marital_status_code is None:
            raise ValueError("Invalid value for `marital_status_code`, must not be `None`")  # noqa: E501

        self._marital_status_code = marital_status_code

    @property
    def marital_status_additional_info(self):
        """Gets the marital_status_additional_info of this PersonalIdentificationData.  # noqa: E501

        Campo livre para complementar a informação relativa ao estado marital, quando selecionada a opção 'OUTROS'  # noqa: E501

        :return: The marital_status_additional_info of this PersonalIdentificationData.  # noqa: E501
        :rtype: str
        """
        return self._marital_status_additional_info

    @marital_status_additional_info.setter
    def marital_status_additional_info(self, marital_status_additional_info):
        """Sets the marital_status_additional_info of this PersonalIdentificationData.

        Campo livre para complementar a informação relativa ao estado marital, quando selecionada a opção 'OUTROS'  # noqa: E501

        :param marital_status_additional_info: The marital_status_additional_info of this PersonalIdentificationData.  # noqa: E501
        :type: str
        """

        self._marital_status_additional_info = marital_status_additional_info

    @property
    def sex(self):
        """Gets the sex of this PersonalIdentificationData.  # noqa: E501


        :return: The sex of this PersonalIdentificationData.  # noqa: E501
        :rtype: EnumSex
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        """Sets the sex of this PersonalIdentificationData.


        :param sex: The sex of this PersonalIdentificationData.  # noqa: E501
        :type: EnumSex
        """
        if sex is None:
            raise ValueError("Invalid value for `sex`, must not be `None`")  # noqa: E501

        self._sex = sex

    @property
    def company_cnpj(self):
        """Gets the company_cnpj of this PersonalIdentificationData.  # noqa: E501

        Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica.  Deve-se ter apenas os números do CNPJ, sem máscara   # noqa: E501

        :return: The company_cnpj of this PersonalIdentificationData.  # noqa: E501
        :rtype: list[str]
        """
        return self._company_cnpj

    @company_cnpj.setter
    def company_cnpj(self, company_cnpj):
        """Sets the company_cnpj of this PersonalIdentificationData.

        Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica.  Deve-se ter apenas os números do CNPJ, sem máscara   # noqa: E501

        :param company_cnpj: The company_cnpj of this PersonalIdentificationData.  # noqa: E501
        :type: list[str]
        """
        if company_cnpj is None:
            raise ValueError("Invalid value for `company_cnpj`, must not be `None`")  # noqa: E501

        self._company_cnpj = company_cnpj

    @property
    def documents(self):
        """Gets the documents of this PersonalIdentificationData.  # noqa: E501


        :return: The documents of this PersonalIdentificationData.  # noqa: E501
        :rtype: PersonalDocument
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this PersonalIdentificationData.


        :param documents: The documents of this PersonalIdentificationData.  # noqa: E501
        :type: PersonalDocument
        """
        if documents is None:
            raise ValueError("Invalid value for `documents`, must not be `None`")  # noqa: E501

        self._documents = documents

    @property
    def other_documents(self):
        """Gets the other_documents of this PersonalIdentificationData.  # noqa: E501

        Relação dos demais documentos  # noqa: E501

        :return: The other_documents of this PersonalIdentificationData.  # noqa: E501
        :rtype: list[PersonalOtherDocument]
        """
        return self._other_documents

    @other_documents.setter
    def other_documents(self, other_documents):
        """Sets the other_documents of this PersonalIdentificationData.

        Relação dos demais documentos  # noqa: E501

        :param other_documents: The other_documents of this PersonalIdentificationData.  # noqa: E501
        :type: list[PersonalOtherDocument]
        """
        if other_documents is None:
            raise ValueError("Invalid value for `other_documents`, must not be `None`")  # noqa: E501

        self._other_documents = other_documents

    @property
    def has_brazilian_nationality(self):
        """Gets the has_brazilian_nationality of this PersonalIdentificationData.  # noqa: E501

        Informa se o Cliente tem nacionalidade brasileira.  # noqa: E501

        :return: The has_brazilian_nationality of this PersonalIdentificationData.  # noqa: E501
        :rtype: bool
        """
        return self._has_brazilian_nationality

    @has_brazilian_nationality.setter
    def has_brazilian_nationality(self, has_brazilian_nationality):
        """Sets the has_brazilian_nationality of this PersonalIdentificationData.

        Informa se o Cliente tem nacionalidade brasileira.  # noqa: E501

        :param has_brazilian_nationality: The has_brazilian_nationality of this PersonalIdentificationData.  # noqa: E501
        :type: bool
        """
        if has_brazilian_nationality is None:
            raise ValueError("Invalid value for `has_brazilian_nationality`, must not be `None`")  # noqa: E501

        self._has_brazilian_nationality = has_brazilian_nationality

    @property
    def nationality(self):
        """Gets the nationality of this PersonalIdentificationData.  # noqa: E501


        :return: The nationality of this PersonalIdentificationData.  # noqa: E501
        :rtype: list[Nationality]
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this PersonalIdentificationData.


        :param nationality: The nationality of this PersonalIdentificationData.  # noqa: E501
        :type: list[Nationality]
        """
        if nationality is None:
            raise ValueError("Invalid value for `nationality`, must not be `None`")  # noqa: E501

        self._nationality = nationality

    @property
    def filiation(self):
        """Gets the filiation of this PersonalIdentificationData.  # noqa: E501


        :return: The filiation of this PersonalIdentificationData.  # noqa: E501
        :rtype: list[PersonalIdentificationDataFiliation]
        """
        return self._filiation

    @filiation.setter
    def filiation(self, filiation):
        """Sets the filiation of this PersonalIdentificationData.


        :param filiation: The filiation of this PersonalIdentificationData.  # noqa: E501
        :type: list[PersonalIdentificationDataFiliation]
        """
        if filiation is None:
            raise ValueError("Invalid value for `filiation`, must not be `None`")  # noqa: E501

        self._filiation = filiation

    @property
    def contacts(self):
        """Gets the contacts of this PersonalIdentificationData.  # noqa: E501


        :return: The contacts of this PersonalIdentificationData.  # noqa: E501
        :rtype: PersonalContacts
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this PersonalIdentificationData.


        :param contacts: The contacts of this PersonalIdentificationData.  # noqa: E501
        :type: PersonalContacts
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
        if issubclass(PersonalIdentificationData, dict):
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
        if not isinstance(other, PersonalIdentificationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other