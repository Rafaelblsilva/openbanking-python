# coding: utf-8

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalFinancialRelationData(object):
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
        'start_date': 'datetime',
        'products_services_type': 'list[EnumProductServiceType]',
        'products_services_type_additional_info': 'str',
        'procurators': 'list[PersonalProcurator]',
        'accounts': 'list[PersonalAccount]'
    }

    attribute_map = {
        'update_date_time': 'updateDateTime',
        'start_date': 'startDate',
        'products_services_type': 'productsServicesType',
        'products_services_type_additional_info': 'productsServicesTypeAdditionalInfo',
        'procurators': 'procurators',
        'accounts': 'accounts'
    }

    def __init__(self, update_date_time=None, start_date=None, products_services_type=None, products_services_type_additional_info=None, procurators=None, accounts=None):  # noqa: E501
        """PersonalFinancialRelationData - a model defined in Swagger"""  # noqa: E501
        self._update_date_time = None
        self._start_date = None
        self._products_services_type = None
        self._products_services_type_additional_info = None
        self._procurators = None
        self._accounts = None
        self.discriminator = None
        self.update_date_time = update_date_time
        self.start_date = start_date
        self.products_services_type = products_services_type
        if products_services_type_additional_info is not None:
            self.products_services_type_additional_info = products_services_type_additional_info
        self.procurators = procurators
        self.accounts = accounts

    @property
    def update_date_time(self):
        """Gets the update_date_time of this PersonalFinancialRelationData.  # noqa: E501

        Data e hora da atualização dos campos \\<_endpoint_\\>, conforme especificação RFC-3339, formato UTC. Quando não existente uma data vinculada especificamente ao bloco, assumir a data e hora de atualização do cadastro como um todo.   # noqa: E501

        :return: The update_date_time of this PersonalFinancialRelationData.  # noqa: E501
        :rtype: datetime
        """
        return self._update_date_time

    @update_date_time.setter
    def update_date_time(self, update_date_time):
        """Sets the update_date_time of this PersonalFinancialRelationData.

        Data e hora da atualização dos campos \\<_endpoint_\\>, conforme especificação RFC-3339, formato UTC. Quando não existente uma data vinculada especificamente ao bloco, assumir a data e hora de atualização do cadastro como um todo.   # noqa: E501

        :param update_date_time: The update_date_time of this PersonalFinancialRelationData.  # noqa: E501
        :type: datetime
        """
        if update_date_time is None:
            raise ValueError("Invalid value for `update_date_time`, must not be `None`")  # noqa: E501

        self._update_date_time = update_date_time

    @property
    def start_date(self):
        """Gets the start_date of this PersonalFinancialRelationData.  # noqa: E501

        Data de início de relacionamento com a Instituição Financeira. Deve trazer o menor valor entre a informação reportada ao BACEN pelo DOC 3040 e CCS.  # noqa: E501

        :return: The start_date of this PersonalFinancialRelationData.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this PersonalFinancialRelationData.

        Data de início de relacionamento com a Instituição Financeira. Deve trazer o menor valor entre a informação reportada ao BACEN pelo DOC 3040 e CCS.  # noqa: E501

        :param start_date: The start_date of this PersonalFinancialRelationData.  # noqa: E501
        :type: datetime
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def products_services_type(self):
        """Gets the products_services_type of this PersonalFinancialRelationData.  # noqa: E501


        :return: The products_services_type of this PersonalFinancialRelationData.  # noqa: E501
        :rtype: list[EnumProductServiceType]
        """
        return self._products_services_type

    @products_services_type.setter
    def products_services_type(self, products_services_type):
        """Sets the products_services_type of this PersonalFinancialRelationData.


        :param products_services_type: The products_services_type of this PersonalFinancialRelationData.  # noqa: E501
        :type: list[EnumProductServiceType]
        """
        if products_services_type is None:
            raise ValueError("Invalid value for `products_services_type`, must not be `None`")  # noqa: E501

        self._products_services_type = products_services_type

    @property
    def products_services_type_additional_info(self):
        """Gets the products_services_type_additional_info of this PersonalFinancialRelationData.  # noqa: E501

        Informações adicionais do tipo de serviço. [Restrição] Campo obrigatório quando productsServicesType for 'OUTROS'.   # noqa: E501

        :return: The products_services_type_additional_info of this PersonalFinancialRelationData.  # noqa: E501
        :rtype: str
        """
        return self._products_services_type_additional_info

    @products_services_type_additional_info.setter
    def products_services_type_additional_info(self, products_services_type_additional_info):
        """Sets the products_services_type_additional_info of this PersonalFinancialRelationData.

        Informações adicionais do tipo de serviço. [Restrição] Campo obrigatório quando productsServicesType for 'OUTROS'.   # noqa: E501

        :param products_services_type_additional_info: The products_services_type_additional_info of this PersonalFinancialRelationData.  # noqa: E501
        :type: str
        """

        self._products_services_type_additional_info = products_services_type_additional_info

    @property
    def procurators(self):
        """Gets the procurators of this PersonalFinancialRelationData.  # noqa: E501

        Lista dos representantes.  [Restrição] De preenchimento obrigatório se houver representante.   # noqa: E501

        :return: The procurators of this PersonalFinancialRelationData.  # noqa: E501
        :rtype: list[PersonalProcurator]
        """
        return self._procurators

    @procurators.setter
    def procurators(self, procurators):
        """Sets the procurators of this PersonalFinancialRelationData.

        Lista dos representantes.  [Restrição] De preenchimento obrigatório se houver representante.   # noqa: E501

        :param procurators: The procurators of this PersonalFinancialRelationData.  # noqa: E501
        :type: list[PersonalProcurator]
        """
        if procurators is None:
            raise ValueError("Invalid value for `procurators`, must not be `None`")  # noqa: E501

        self._procurators = procurators

    @property
    def accounts(self):
        """Gets the accounts of this PersonalFinancialRelationData.  # noqa: E501

        Lista de contas depósito à vista, poupança e pagamento pré-pagas mantidas pelo cliente na instituição transmissora.   # noqa: E501

        :return: The accounts of this PersonalFinancialRelationData.  # noqa: E501
        :rtype: list[PersonalAccount]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this PersonalFinancialRelationData.

        Lista de contas depósito à vista, poupança e pagamento pré-pagas mantidas pelo cliente na instituição transmissora.   # noqa: E501

        :param accounts: The accounts of this PersonalFinancialRelationData.  # noqa: E501
        :type: list[PersonalAccount]
        """
        if accounts is None:
            raise ValueError("Invalid value for `accounts`, must not be `None`")  # noqa: E501

        self._accounts = accounts

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
        if issubclass(PersonalFinancialRelationData, dict):
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
        if not isinstance(other, PersonalFinancialRelationData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
