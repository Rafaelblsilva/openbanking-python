# coding: utf-8

# flake8: noqa

"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from insurances_1_0_0_yml.api.seguros_api import SegurosApi
# import ApiClient
from insurances_1_0_0_yml.api_client import ApiClient
from insurances_1_0_0_yml.configuration import Configuration
# import models into sdk package
from insurances_1_0_0_yml.models.age_adjustment import AgeAdjustment
from insurances_1_0_0_yml.models.benefit_recalculation import BenefitRecalculation
from insurances_1_0_0_yml.models.cnpj_number import CnpjNumber
from insurances_1_0_0_yml.models.currency_code import CurrencyCode
from insurances_1_0_0_yml.models.enum_contract_type_personal import EnumContractTypePersonal
from insurances_1_0_0_yml.models.enum_excluded_risks import EnumExcludedRisks
from insurances_1_0_0_yml.models.enum_grace_period_unit import EnumGracePeriodUnit
from insurances_1_0_0_yml.models.enum_insurance_personal_benefit_recalculation_update_index import EnumInsurancePersonalBenefitRecalculationUpdateIndex
from insurances_1_0_0_yml.models.enum_insurance_personal_coverage_type_personal import EnumInsurancePersonalCoverageTypePersonal
from insurances_1_0_0_yml.models.enum_personal_indemnity_payment_frequency_type import EnumPersonalIndemnityPaymentFrequencyType
from insurances_1_0_0_yml.models.enum_personal_insurance_indemnity_payment_income import EnumPersonalInsuranceIndemnityPaymentIncome
from insurances_1_0_0_yml.models.enum_personal_insurance_indemnity_payment_method import EnumPersonalInsuranceIndemnityPaymentMethod
from insurances_1_0_0_yml.models.enum_personal_insurance_other_guaranteed_values import EnumPersonalInsuranceOtherGuaranteedValues
from insurances_1_0_0_yml.models.enum_personal_insurance_premium_payment_frequency import EnumPersonalInsurancePremiumPaymentFrequency
from insurances_1_0_0_yml.models.enum_personal_update_index import EnumPersonalUpdateIndex
from insurances_1_0_0_yml.models.enum_premium_payment_method_type_personal import EnumPremiumPaymentMethodTypePersonal
from insurances_1_0_0_yml.models.enum_product_modality import EnumProductModality
from insurances_1_0_0_yml.models.grace_period import GracePeriod
from insurances_1_0_0_yml.models.inline_response529 import InlineResponse529
from insurances_1_0_0_yml.models.inline_response529_errors import InlineResponse529Errors
from insurances_1_0_0_yml.models.inline_response529_meta import InlineResponse529Meta
from insurances_1_0_0_yml.models.insurance_pension_enum_financial_regime import InsurancePensionEnumFinancialRegime
from insurances_1_0_0_yml.models.insurance_pension_enum_pmbac_remuneration import InsurancePensionEnumPmbacRemuneration
from insurances_1_0_0_yml.models.insurance_pension_max_value import InsurancePensionMaxValue
from insurances_1_0_0_yml.models.insurance_pension_min_value import InsurancePensionMinValue
from insurances_1_0_0_yml.models.links import Links
from insurances_1_0_0_yml.models.meta import Meta
from insurances_1_0_0_yml.models.ok_response_personal_insurance_list import OKResponsePersonalInsuranceList
from insurances_1_0_0_yml.models.open_data_meta import OpenDataMeta
from insurances_1_0_0_yml.models.participant import Participant
from insurances_1_0_0_yml.models.personal_coverage_item import PersonalCoverageItem
from insurances_1_0_0_yml.models.personal_coverage_item_attributes import PersonalCoverageItemAttributes
from insurances_1_0_0_yml.models.personal_coverage_item_attributes_deductible import PersonalCoverageItemAttributesDeductible
from insurances_1_0_0_yml.models.personal_coverage_item_attributes_differentiated_deductible import PersonalCoverageItemAttributesDifferentiatedDeductible
from insurances_1_0_0_yml.models.personal_insurance_data import PersonalInsuranceData
from insurances_1_0_0_yml.models.personal_insurance_grace_period import PersonalInsuranceGracePeriod
from insurances_1_0_0_yml.models.personal_insurance_minimum_requirement import PersonalInsuranceMinimumRequirement
from insurances_1_0_0_yml.models.personal_insurance_portability_grace_time import PersonalInsurancePortabilityGraceTime
from insurances_1_0_0_yml.models.personal_insurance_premium_payment import PersonalInsurancePremiumPayment
from insurances_1_0_0_yml.models.personal_insurance_reclaim import PersonalInsuranceReclaim
from insurances_1_0_0_yml.models.personal_insurance_reclaim_table_item import PersonalInsuranceReclaimTableItem
from insurances_1_0_0_yml.models.personal_insurance_society import PersonalInsuranceSociety
from insurances_1_0_0_yml.models.response_error import ResponseError
from insurances_1_0_0_yml.models.response_error_errors import ResponseErrorErrors
from insurances_1_0_0_yml.models.terms_and_conditions_item import TermsAndConditionsItem
