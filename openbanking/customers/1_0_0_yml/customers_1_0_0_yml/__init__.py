# coding: utf-8

# flake8: noqa

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from customers_1_0_0_yml.api.customers_api import CustomersApi
# import ApiClient
from customers_1_0_0_yml.api_client import ApiClient
from customers_1_0_0_yml.configuration import Configuration
# import models into sdk package
from customers_1_0_0_yml.models.business_account import BusinessAccount
from customers_1_0_0_yml.models.business_contacts import BusinessContacts
from customers_1_0_0_yml.models.business_financial_relation_data import BusinessFinancialRelationData
from customers_1_0_0_yml.models.business_identification_data import BusinessIdentificationData
from customers_1_0_0_yml.models.business_informed_patrimony import BusinessInformedPatrimony
from customers_1_0_0_yml.models.business_other_document import BusinessOtherDocument
from customers_1_0_0_yml.models.business_postal_address import BusinessPostalAddress
from customers_1_0_0_yml.models.business_procurator import BusinessProcurator
from customers_1_0_0_yml.models.business_qualification_data import BusinessQualificationData
from customers_1_0_0_yml.models.business_qualification_data_informed_revenue import BusinessQualificationDataInformedRevenue
from customers_1_0_0_yml.models.customer_email import CustomerEmail
from customers_1_0_0_yml.models.customer_phone import CustomerPhone
from customers_1_0_0_yml.models.economic_activity import EconomicActivity
from customers_1_0_0_yml.models.enum_area_code import EnumAreaCode
from customers_1_0_0_yml.models.enum_country_sub_division import EnumCountrySubDivision
from customers_1_0_0_yml.models.enum_customer_phone_type import EnumCustomerPhoneType
from customers_1_0_0_yml.models.enum_filiation_type import EnumFiliationType
from customers_1_0_0_yml.models.enum_informed_income_frequency import EnumInformedIncomeFrequency
from customers_1_0_0_yml.models.enum_informed_revenue_frequency import EnumInformedRevenueFrequency
from customers_1_0_0_yml.models.enum_marital_status_code import EnumMaritalStatusCode
from customers_1_0_0_yml.models.enum_occupation_main_code_type import EnumOccupationMainCodeType
from customers_1_0_0_yml.models.enum_parties_participation_document_type import EnumPartiesParticipationDocumentType
from customers_1_0_0_yml.models.enum_personal_other_document_type import EnumPersonalOtherDocumentType
from customers_1_0_0_yml.models.enum_procurators_type_personal import EnumProcuratorsTypePersonal
from customers_1_0_0_yml.models.enum_product_service_type import EnumProductServiceType
from customers_1_0_0_yml.models.enum_sex import EnumSex
from customers_1_0_0_yml.models.geographic_coordinates import GeographicCoordinates
from customers_1_0_0_yml.models.links import Links
from customers_1_0_0_yml.models.meta import Meta
from customers_1_0_0_yml.models.nationality import Nationality
from customers_1_0_0_yml.models.nationality_other_document import NationalityOtherDocument
from customers_1_0_0_yml.models.parties_participation import PartiesParticipation
from customers_1_0_0_yml.models.personal_account import PersonalAccount
from customers_1_0_0_yml.models.personal_contacts import PersonalContacts
from customers_1_0_0_yml.models.personal_document import PersonalDocument
from customers_1_0_0_yml.models.personal_financial_relation_data import PersonalFinancialRelationData
from customers_1_0_0_yml.models.personal_identification_data import PersonalIdentificationData
from customers_1_0_0_yml.models.personal_identification_data_filiation import PersonalIdentificationDataFiliation
from customers_1_0_0_yml.models.personal_informed_patrimony import PersonalInformedPatrimony
from customers_1_0_0_yml.models.personal_other_document import PersonalOtherDocument
from customers_1_0_0_yml.models.personal_postal_address import PersonalPostalAddress
from customers_1_0_0_yml.models.personal_procurator import PersonalProcurator
from customers_1_0_0_yml.models.personal_qualification_data import PersonalQualificationData
from customers_1_0_0_yml.models.personal_qualification_data_informed_income import PersonalQualificationDataInformedIncome
from customers_1_0_0_yml.models.response_business_customers_financial_relation import ResponseBusinessCustomersFinancialRelation
from customers_1_0_0_yml.models.response_business_customers_identification import ResponseBusinessCustomersIdentification
from customers_1_0_0_yml.models.response_business_customers_qualification import ResponseBusinessCustomersQualification
from customers_1_0_0_yml.models.response_error import ResponseError
from customers_1_0_0_yml.models.response_error_errors import ResponseErrorErrors
from customers_1_0_0_yml.models.response_personal_customers_financial_relation import ResponsePersonalCustomersFinancialRelation
from customers_1_0_0_yml.models.response_personal_customers_identification import ResponsePersonalCustomersIdentification
from customers_1_0_0_yml.models.response_personal_customers_qualification import ResponsePersonalCustomersQualification
from customers_1_0_0_yml.models.x_fapi_interaction_id import XFapiInteractionId
