# coding: utf-8

# flake8: noqa
"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.5
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from insurances_1_0_0-rc1_5_yml.models.age_adjustment import AgeAdjustment
from insurances_1_0_0-rc1_5_yml.models.assistance_services_item import AssistanceServicesItem
from insurances_1_0_0-rc1_5_yml.models.automotive_coverage_item import AutomotiveCoverageItem
from insurances_1_0_0-rc1_5_yml.models.automotive_coverage_item_attributes import AutomotiveCoverageItemAttributes
from insurances_1_0_0-rc1_5_yml.models.automotive_geo_graphic_scope import AutomotiveGeoGraphicScope
from insurances_1_0_0-rc1_5_yml.models.automotive_insurance_data import AutomotiveInsuranceData
from insurances_1_0_0-rc1_5_yml.models.automotive_insurance_determined_value import AutomotiveInsuranceDeterminedValue
from insurances_1_0_0-rc1_5_yml.models.automotive_insurance_market_value_percentage import AutomotiveInsuranceMarketValuePercentage
from insurances_1_0_0-rc1_5_yml.models.automotive_model import AutomotiveModel
from insurances_1_0_0-rc1_5_yml.models.automotive_parts_item import AutomotivePartsItem
from insurances_1_0_0-rc1_5_yml.models.cnpj_number import CnpjNumber
from insurances_1_0_0-rc1_5_yml.models.contract_base import ContractBase
from insurances_1_0_0-rc1_5_yml.models.contract_base_determined_value import ContractBaseDeterminedValue
from insurances_1_0_0-rc1_5_yml.models.coverage_item_attributes_max_lmi import CoverageItemAttributesMaxLMI
from insurances_1_0_0-rc1_5_yml.models.coverage_item_attributes_min_lmi import CoverageItemAttributesMinLMI
from insurances_1_0_0-rc1_5_yml.models.currency_code import CurrencyCode
from insurances_1_0_0-rc1_5_yml.models.enum_assistance_services_package_type import EnumAssistanceServicesPackageType
from insurances_1_0_0-rc1_5_yml.models.enum_automotive_coverage_type import EnumAutomotiveCoverageType
from insurances_1_0_0-rc1_5_yml.models.enum_automotive_part_type import EnumAutomotivePartType
from insurances_1_0_0-rc1_5_yml.models.enum_charge_type_signaling_type import EnumChargeTypeSignalingType
from insurances_1_0_0-rc1_5_yml.models.enum_coverage_item_deductible_type import EnumCoverageItemDeductibleType
from insurances_1_0_0-rc1_5_yml.models.enum_coverage_item_geographic_scope_type import EnumCoverageItemGeographicScopeType
from insurances_1_0_0-rc1_5_yml.models.enum_customer_service_type import EnumCustomerServiceType
from insurances_1_0_0-rc1_5_yml.models.enum_grace_period_unit import EnumGracePeriodUnit
from insurances_1_0_0-rc1_5_yml.models.enum_home_coverage_type import EnumHomeCoverageType
from insurances_1_0_0-rc1_5_yml.models.enum_home_importance_insured_type import EnumHomeImportanceInsuredType
from insurances_1_0_0-rc1_5_yml.models.enum_home_property_build_type import EnumHomePropertyBuildType
from insurances_1_0_0-rc1_5_yml.models.enum_home_property_type import EnumHomePropertyType
from insurances_1_0_0-rc1_5_yml.models.enum_home_property_usage_type import EnumHomePropertyUsageType
from insurances_1_0_0-rc1_5_yml.models.enum_insurance_additional_type import EnumInsuranceAdditionalType
from insurances_1_0_0-rc1_5_yml.models.enum_insurance_personal_benefit_recalculation_update_index import EnumInsurancePersonalBenefitRecalculationUpdateIndex
from insurances_1_0_0-rc1_5_yml.models.enum_insurance_term_type import EnumInsuranceTermType
from insurances_1_0_0-rc1_5_yml.models.enum_personal_update_index import EnumPersonalUpdateIndex
from insurances_1_0_0-rc1_5_yml.models.enum_premium_payment_method_type import EnumPremiumPaymentMethodType
from insurances_1_0_0-rc1_5_yml.models.enum_premium_payment_type import EnumPremiumPaymentType
from insurances_1_0_0-rc1_5_yml.models.enum_product_modality import EnumProductModality
from insurances_1_0_0-rc1_5_yml.models.enum_target_audience import EnumTargetAudience
from insurances_1_0_0-rc1_5_yml.models.grace_period import GracePeriod
from insurances_1_0_0-rc1_5_yml.models.home_coverage_item import HomeCoverageItem
from insurances_1_0_0-rc1_5_yml.models.home_coverage_item_attributes import HomeCoverageItemAttributes
from insurances_1_0_0-rc1_5_yml.models.home_insurance_data import HomeInsuranceData
from insurances_1_0_0-rc1_5_yml.models.home_min_deductible_amount import HomeMinDeductibleAmount
from insurances_1_0_0-rc1_5_yml.models.home_property_characteristics import HomePropertyCharacteristics
from insurances_1_0_0-rc1_5_yml.models.inline_response529 import InlineResponse529
from insurances_1_0_0-rc1_5_yml.models.inline_response529_errors import InlineResponse529Errors
from insurances_1_0_0-rc1_5_yml.models.inline_response529_meta import InlineResponse529Meta
from insurances_1_0_0-rc1_5_yml.models.insurance_minimum_requirement import InsuranceMinimumRequirement
from insurances_1_0_0-rc1_5_yml.models.insurance_pension_benefit_recalculation import InsurancePensionBenefitRecalculation
from insurances_1_0_0-rc1_5_yml.models.insurance_pension_coverage_deductible import InsurancePensionCoverageDeductible
from insurances_1_0_0-rc1_5_yml.models.insurance_pension_coverage_differentiated_deductible import InsurancePensionCoverageDifferentiatedDeductible
from insurances_1_0_0-rc1_5_yml.models.insurance_pension_enum_financial_regime import InsurancePensionEnumFinancialRegime
from insurances_1_0_0-rc1_5_yml.models.insurance_pension_enum_pmbac_remuneration import InsurancePensionEnumPmbacRemuneration
from insurances_1_0_0-rc1_5_yml.models.insurance_pension_max_value import InsurancePensionMaxValue
from insurances_1_0_0-rc1_5_yml.models.insurance_pension_min_value import InsurancePensionMinValue
from insurances_1_0_0-rc1_5_yml.models.links import Links
from insurances_1_0_0-rc1_5_yml.models.meta import Meta
from insurances_1_0_0-rc1_5_yml.models.new_car import NewCar
from insurances_1_0_0-rc1_5_yml.models.ok_response_automotive_insurance_list import OKResponseAutomotiveInsuranceList
from insurances_1_0_0-rc1_5_yml.models.ok_response_home_insurance_list import OKResponseHomeInsuranceList
from insurances_1_0_0-rc1_5_yml.models.open_data_meta import OpenDataMeta
from insurances_1_0_0-rc1_5_yml.models.participant import Participant
from insurances_1_0_0-rc1_5_yml.models.premium_payment import PremiumPayment
from insurances_1_0_0-rc1_5_yml.models.response_error import ResponseError
from insurances_1_0_0-rc1_5_yml.models.response_error_errors import ResponseErrorErrors
from insurances_1_0_0-rc1_5_yml.models.society import Society
from insurances_1_0_0-rc1_5_yml.models.terms_and_conditions_item import TermsAndConditionsItem
