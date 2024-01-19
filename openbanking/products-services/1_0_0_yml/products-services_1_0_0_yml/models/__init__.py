# coding: utf-8

# flake8: noqa
"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from products-services_1_0_0_yml.models.account_other_services_price import AccountOtherServicesPrice
from products-services_1_0_0_yml.models.account_other_services_price_maximum import AccountOtherServicesPriceMaximum
from products-services_1_0_0_yml.models.account_other_services_price_minimum import AccountOtherServicesPriceMinimum
from products-services_1_0_0_yml.models.accounts_terms_conditions import AccountsTermsConditions
from products-services_1_0_0_yml.models.accounts_terms_conditions_minimum_balance import AccountsTermsConditionsMinimumBalance
from products-services_1_0_0_yml.models.application_rate import ApplicationRate
from products-services_1_0_0_yml.models.business_accounts_services import BusinessAccountsServices
from products-services_1_0_0_yml.models.business_accounts_services_maximum import BusinessAccountsServicesMaximum
from products-services_1_0_0_yml.models.business_accounts_services_minimum import BusinessAccountsServicesMinimum
from products-services_1_0_0_yml.models.business_credit_card_response import BusinessCreditCardResponse
from products-services_1_0_0_yml.models.business_credit_card_response_data import BusinessCreditCardResponseData
from products-services_1_0_0_yml.models.business_credit_card_response_data_brand import BusinessCreditCardResponseDataBrand
from products-services_1_0_0_yml.models.business_credit_card_response_data_brand_business_credit_cards import BusinessCreditCardResponseDataBrandBusinessCreditCards
from products-services_1_0_0_yml.models.business_credit_card_response_data_brand_companies import BusinessCreditCardResponseDataBrandCompanies
from products-services_1_0_0_yml.models.business_credit_card_response_data_brand_fees import BusinessCreditCardResponseDataBrandFees
from products-services_1_0_0_yml.models.business_financing import BusinessFinancing
from products-services_1_0_0_yml.models.business_financing_brand import BusinessFinancingBrand
from products-services_1_0_0_yml.models.business_financing_company import BusinessFinancingCompany
from products-services_1_0_0_yml.models.business_financing_fee import BusinessFinancingFee
from products-services_1_0_0_yml.models.business_invoice_financings import BusinessInvoiceFinancings
from products-services_1_0_0_yml.models.business_invoice_financings_brand import BusinessInvoiceFinancingsBrand
from products-services_1_0_0_yml.models.business_invoice_financings_companies import BusinessInvoiceFinancingsCompanies
from products-services_1_0_0_yml.models.business_invoice_financings_fees import BusinessInvoiceFinancingsFees
from products-services_1_0_0_yml.models.business_invoice_financings_fees_service import BusinessInvoiceFinancingsFeesService
from products-services_1_0_0_yml.models.business_invoice_financings_interest_rates import BusinessInvoiceFinancingsInterestRates
from products-services_1_0_0_yml.models.business_loan import BusinessLoan
from products-services_1_0_0_yml.models.business_loan_brand import BusinessLoanBrand
from products-services_1_0_0_yml.models.business_loan_company import BusinessLoanCompany
from products-services_1_0_0_yml.models.cnpj import CNPJ
from products-services_1_0_0_yml.models.credit_card_indentification import CreditCardIndentification
from products-services_1_0_0_yml.models.credit_card_indentification_credit_card import CreditCardIndentificationCreditCard
from products-services_1_0_0_yml.models.credit_card_indentification_product import CreditCardIndentificationProduct
from products-services_1_0_0_yml.models.credit_card_interest import CreditCardInterest
from products-services_1_0_0_yml.models.credit_card_interest_interest_rates import CreditCardInterestInterestRates
from products-services_1_0_0_yml.models.credit_card_interest_prices import CreditCardInterestPrices
from products-services_1_0_0_yml.models.credit_card_rewards_program import CreditCardRewardsProgram
from products-services_1_0_0_yml.models.credit_card_service import CreditCardService
from products-services_1_0_0_yml.models.credit_card_terms_conditions import CreditCardTermsConditions
from products-services_1_0_0_yml.models.financing_interest_rate import FinancingInterestRate
from products-services_1_0_0_yml.models.financing_service import FinancingService
from products-services_1_0_0_yml.models.interest_rate import InterestRate
from products-services_1_0_0_yml.models.interest_rate_prices import InterestRatePrices
from products-services_1_0_0_yml.models.intervals import Intervals
from products-services_1_0_0_yml.models.links import Links
from products-services_1_0_0_yml.models.loan_fee import LoanFee
from products-services_1_0_0_yml.models.loan_interest_rate import LoanInterestRate
from products-services_1_0_0_yml.models.loan_service import LoanService
from products-services_1_0_0_yml.models.maximum_price import MaximumPrice
from products-services_1_0_0_yml.models.meta import Meta
from products-services_1_0_0_yml.models.minimum_price import MinimumPrice
from products-services_1_0_0_yml.models.personal_accounts_income_rates import PersonalAccountsIncomeRates
from products-services_1_0_0_yml.models.personal_accounts_income_rates_prepaid_payment_account import PersonalAccountsIncomeRatesPrepaidPaymentAccount
from products-services_1_0_0_yml.models.personal_accounts_other_services import PersonalAccountsOtherServices
from products-services_1_0_0_yml.models.personal_accounts_other_services_minimum import PersonalAccountsOtherServicesMinimum
from products-services_1_0_0_yml.models.personal_accounts_priority_services import PersonalAccountsPriorityServices
from products-services_1_0_0_yml.models.personal_accounts_priority_services_maximum import PersonalAccountsPriorityServicesMaximum
from products-services_1_0_0_yml.models.personal_accounts_priority_services_minimum import PersonalAccountsPriorityServicesMinimum
from products-services_1_0_0_yml.models.personal_accounts_priority_services_prices import PersonalAccountsPriorityServicesPrices
from products-services_1_0_0_yml.models.personal_accounts_response import PersonalAccountsResponse
from products-services_1_0_0_yml.models.personal_accounts_response_data import PersonalAccountsResponseData
from products-services_1_0_0_yml.models.personal_accounts_response_data_brand import PersonalAccountsResponseDataBrand
from products-services_1_0_0_yml.models.personal_accounts_response_data_brand_companies import PersonalAccountsResponseDataBrandCompanies
from products-services_1_0_0_yml.models.personal_accounts_response_data_brand_fees import PersonalAccountsResponseDataBrandFees
from products-services_1_0_0_yml.models.personal_accounts_response_data_brand_maximum import PersonalAccountsResponseDataBrandMaximum
from products-services_1_0_0_yml.models.personal_accounts_response_data_brand_minimum import PersonalAccountsResponseDataBrandMinimum
from products-services_1_0_0_yml.models.personal_accounts_response_data_brand_personal_accounts import PersonalAccountsResponseDataBrandPersonalAccounts
from products-services_1_0_0_yml.models.personal_accounts_response_data_brand_prices import PersonalAccountsResponseDataBrandPrices
from products-services_1_0_0_yml.models.personal_accounts_response_data_brand_service_bundles import PersonalAccountsResponseDataBrandServiceBundles
from products-services_1_0_0_yml.models.personal_accounts_response_data_brand_services import PersonalAccountsResponseDataBrandServices
from products-services_1_0_0_yml.models.personal_credit_card_response import PersonalCreditCardResponse
from products-services_1_0_0_yml.models.personal_credit_card_response_data import PersonalCreditCardResponseData
from products-services_1_0_0_yml.models.personal_credit_card_response_data_brand import PersonalCreditCardResponseDataBrand
from products-services_1_0_0_yml.models.personal_credit_card_response_data_brand_companies import PersonalCreditCardResponseDataBrandCompanies
from products-services_1_0_0_yml.models.personal_credit_card_response_data_brand_personal_credit_cards import PersonalCreditCardResponseDataBrandPersonalCreditCards
from products-services_1_0_0_yml.models.personal_financing import PersonalFinancing
from products-services_1_0_0_yml.models.personal_financing_brand import PersonalFinancingBrand
from products-services_1_0_0_yml.models.personal_financing_company import PersonalFinancingCompany
from products-services_1_0_0_yml.models.personal_financing_fee import PersonalFinancingFee
from products-services_1_0_0_yml.models.personal_invoice_financings import PersonalInvoiceFinancings
from products-services_1_0_0_yml.models.personal_invoice_financings_brand import PersonalInvoiceFinancingsBrand
from products-services_1_0_0_yml.models.personal_invoice_financings_companies import PersonalInvoiceFinancingsCompanies
from products-services_1_0_0_yml.models.personal_invoice_financings_fees import PersonalInvoiceFinancingsFees
from products-services_1_0_0_yml.models.personal_invoice_financings_fees_service import PersonalInvoiceFinancingsFeesService
from products-services_1_0_0_yml.models.personal_invoice_financings_interest_rates import PersonalInvoiceFinancingsInterestRates
from products-services_1_0_0_yml.models.personal_invoice_financings_interest_rates_applications import PersonalInvoiceFinancingsInterestRatesApplications
from products-services_1_0_0_yml.models.personal_loan import PersonalLoan
from products-services_1_0_0_yml.models.personal_loan_brand import PersonalLoanBrand
from products-services_1_0_0_yml.models.personal_loan_company import PersonalLoanCompany
from products-services_1_0_0_yml.models.price import Price
from products-services_1_0_0_yml.models.required_warranty import RequiredWarranty
from products-services_1_0_0_yml.models.response_business_accounts import ResponseBusinessAccounts
from products-services_1_0_0_yml.models.response_business_accounts_data import ResponseBusinessAccountsData
from products-services_1_0_0_yml.models.response_business_accounts_data_brand import ResponseBusinessAccountsDataBrand
from products-services_1_0_0_yml.models.response_business_accounts_data_brand_business_accounts import ResponseBusinessAccountsDataBrandBusinessAccounts
from products-services_1_0_0_yml.models.response_business_accounts_data_brand_companies import ResponseBusinessAccountsDataBrandCompanies
from products-services_1_0_0_yml.models.response_business_accounts_data_brand_fees import ResponseBusinessAccountsDataBrandFees
from products-services_1_0_0_yml.models.response_business_accounts_data_brand_income_rates import ResponseBusinessAccountsDataBrandIncomeRates
from products-services_1_0_0_yml.models.response_business_accounts_data_brand_prepaid_payment_account import ResponseBusinessAccountsDataBrandPrepaidPaymentAccount
from products-services_1_0_0_yml.models.response_business_accounts_data_brand_prepaid_payment_account_applications import ResponseBusinessAccountsDataBrandPrepaidPaymentAccountApplications
from products-services_1_0_0_yml.models.response_business_accounts_data_brand_prices import ResponseBusinessAccountsDataBrandPrices
from products-services_1_0_0_yml.models.response_business_accounts_data_brand_service import ResponseBusinessAccountsDataBrandService
from products-services_1_0_0_yml.models.response_business_accounts_data_brand_service_bundles import ResponseBusinessAccountsDataBrandServiceBundles
from products-services_1_0_0_yml.models.response_business_financings_list import ResponseBusinessFinancingsList
from products-services_1_0_0_yml.models.response_business_financings_list_data import ResponseBusinessFinancingsListData
from products-services_1_0_0_yml.models.response_business_invoice_financings_list import ResponseBusinessInvoiceFinancingsList
from products-services_1_0_0_yml.models.response_business_invoice_financings_list_data import ResponseBusinessInvoiceFinancingsListData
from products-services_1_0_0_yml.models.response_business_loans_list import ResponseBusinessLoansList
from products-services_1_0_0_yml.models.response_business_loans_list_data import ResponseBusinessLoansListData
from products-services_1_0_0_yml.models.response_personal_financings_list import ResponsePersonalFinancingsList
from products-services_1_0_0_yml.models.response_personal_financings_list_data import ResponsePersonalFinancingsListData
from products-services_1_0_0_yml.models.response_personal_invoice_financings_list import ResponsePersonalInvoiceFinancingsList
from products-services_1_0_0_yml.models.response_personal_invoice_financings_list_data import ResponsePersonalInvoiceFinancingsListData
from products-services_1_0_0_yml.models.response_personal_loans_list import ResponsePersonalLoansList
from products-services_1_0_0_yml.models.response_personal_loans_list_data import ResponsePersonalLoansListData
