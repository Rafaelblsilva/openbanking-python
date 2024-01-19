# coding: utf-8

# flake8: noqa
"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.2
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from products-services_1_0_0-rc5_2_yml.models.account_fee import AccountFee
from products-services_1_0_0-rc5_2_yml.models.account_other_service import AccountOtherService
from products-services_1_0_0-rc5_2_yml.models.account_priority_service import AccountPriorityService
from products-services_1_0_0-rc5_2_yml.models.account_priority_service_code import AccountPriorityServiceCode
from products-services_1_0_0-rc5_2_yml.models.account_type import AccountType
from products-services_1_0_0-rc5_2_yml.models.accounts_income_rate import AccountsIncomeRate
from products-services_1_0_0-rc5_2_yml.models.accounts_terms_conditions import AccountsTermsConditions
from products-services_1_0_0-rc5_2_yml.models.application_intervals import ApplicationIntervals
from products-services_1_0_0-rc5_2_yml.models.application_rate import ApplicationRate
from products-services_1_0_0-rc5_2_yml.models.brand import Brand
from products-services_1_0_0-rc5_2_yml.models.business_accounts import BusinessAccounts
from products-services_1_0_0-rc5_2_yml.models.business_accounts_brand import BusinessAccountsBrand
from products-services_1_0_0-rc5_2_yml.models.business_accounts_company import BusinessAccountsCompany
from products-services_1_0_0-rc5_2_yml.models.business_accounts_fees import BusinessAccountsFees
from products-services_1_0_0-rc5_2_yml.models.business_accounts_service import BusinessAccountsService
from products-services_1_0_0-rc5_2_yml.models.business_credit_card import BusinessCreditCard
from products-services_1_0_0-rc5_2_yml.models.business_credit_card_brand import BusinessCreditCardBrand
from products-services_1_0_0-rc5_2_yml.models.business_credit_card_company import BusinessCreditCardCompany
from products-services_1_0_0-rc5_2_yml.models.business_credit_card_response import BusinessCreditCardResponse
from products-services_1_0_0-rc5_2_yml.models.business_credit_card_response_data import BusinessCreditCardResponseData
from products-services_1_0_0-rc5_2_yml.models.business_financing import BusinessFinancing
from products-services_1_0_0-rc5_2_yml.models.business_financing_brand import BusinessFinancingBrand
from products-services_1_0_0-rc5_2_yml.models.business_financing_company import BusinessFinancingCompany
from products-services_1_0_0-rc5_2_yml.models.business_financing_fee import BusinessFinancingFee
from products-services_1_0_0-rc5_2_yml.models.business_invoice_financings import BusinessInvoiceFinancings
from products-services_1_0_0-rc5_2_yml.models.business_invoice_financings_brand import BusinessInvoiceFinancingsBrand
from products-services_1_0_0-rc5_2_yml.models.business_invoice_financings_companies import BusinessInvoiceFinancingsCompanies
from products-services_1_0_0-rc5_2_yml.models.business_invoice_financings_fees import BusinessInvoiceFinancingsFees
from products-services_1_0_0-rc5_2_yml.models.business_invoice_financings_interest_rates import BusinessInvoiceFinancingsInterestRates
from products-services_1_0_0-rc5_2_yml.models.business_loan import BusinessLoan
from products-services_1_0_0-rc5_2_yml.models.business_loan_brand import BusinessLoanBrand
from products-services_1_0_0-rc5_2_yml.models.business_loan_company import BusinessLoanCompany
from products-services_1_0_0-rc5_2_yml.models.business_unarranged_account_overdraft import BusinessUnarrangedAccountOverdraft
from products-services_1_0_0-rc5_2_yml.models.business_unarranged_account_overdraft_brand import BusinessUnarrangedAccountOverdraftBrand
from products-services_1_0_0-rc5_2_yml.models.business_unarranged_account_overdraft_company import BusinessUnarrangedAccountOverdraftCompany
from products-services_1_0_0-rc5_2_yml.models.business_unarranged_account_overdraft_fee import BusinessUnarrangedAccountOverdraftFee
from products-services_1_0_0-rc5_2_yml.models.cnpj import CNPJ
from products-services_1_0_0-rc5_2_yml.models.company import Company
from products-services_1_0_0-rc5_2_yml.models.credit_card_identification import CreditCardIdentification
from products-services_1_0_0-rc5_2_yml.models.credit_card_identification_credit_card import CreditCardIdentificationCreditCard
from products-services_1_0_0-rc5_2_yml.models.credit_card_identification_product import CreditCardIdentificationProduct
from products-services_1_0_0-rc5_2_yml.models.credit_card_interest import CreditCardInterest
from products-services_1_0_0-rc5_2_yml.models.credit_card_interest_rate import CreditCardInterestRate
from products-services_1_0_0-rc5_2_yml.models.credit_card_rewards_program import CreditCardRewardsProgram
from products-services_1_0_0-rc5_2_yml.models.credit_card_service import CreditCardService
from products-services_1_0_0-rc5_2_yml.models.credit_card_terms_conditions import CreditCardTermsConditions
from products-services_1_0_0-rc5_2_yml.models.currency import Currency
from products-services_1_0_0-rc5_2_yml.models.customer import Customer
from products-services_1_0_0-rc5_2_yml.models.fee_referential_rate_indexer import FeeReferentialRateIndexer
from products-services_1_0_0-rc5_2_yml.models.financing_interest_rate import FinancingInterestRate
from products-services_1_0_0-rc5_2_yml.models.financing_service import FinancingService
from products-services_1_0_0-rc5_2_yml.models.indexer import Indexer
from products-services_1_0_0-rc5_2_yml.models.interest_rate import InterestRate
from products-services_1_0_0-rc5_2_yml.models.interest_rate_fee import InterestRateFee
from products-services_1_0_0-rc5_2_yml.models.invoice_financings_service import InvoiceFinancingsService
from products-services_1_0_0-rc5_2_yml.models.links import Links
from products-services_1_0_0-rc5_2_yml.models.loan_fees import LoanFees
from products-services_1_0_0-rc5_2_yml.models.loan_interest_rate import LoanInterestRate
from products-services_1_0_0-rc5_2_yml.models.loan_service import LoanService
from products-services_1_0_0-rc5_2_yml.models.maximum_price import MaximumPrice
from products-services_1_0_0-rc5_2_yml.models.meta import Meta
from products-services_1_0_0-rc5_2_yml.models.minimum_balance import MinimumBalance
from products-services_1_0_0-rc5_2_yml.models.minimum_price import MinimumPrice
from products-services_1_0_0-rc5_2_yml.models.monthly_price import MonthlyPrice
from products-services_1_0_0-rc5_2_yml.models.opening_closing_channels import OpeningClosingChannels
from products-services_1_0_0-rc5_2_yml.models.personal_account import PersonalAccount
from products-services_1_0_0-rc5_2_yml.models.personal_account_brand import PersonalAccountBrand
from products-services_1_0_0-rc5_2_yml.models.personal_account_company import PersonalAccountCompany
from products-services_1_0_0-rc5_2_yml.models.personal_credit_card import PersonalCreditCard
from products-services_1_0_0-rc5_2_yml.models.personal_credit_card_brand import PersonalCreditCardBrand
from products-services_1_0_0-rc5_2_yml.models.personal_credit_card_company import PersonalCreditCardCompany
from products-services_1_0_0-rc5_2_yml.models.personal_credit_card_fees import PersonalCreditCardFees
from products-services_1_0_0-rc5_2_yml.models.personal_credit_card_response import PersonalCreditCardResponse
from products-services_1_0_0-rc5_2_yml.models.personal_credit_card_response_data import PersonalCreditCardResponseData
from products-services_1_0_0-rc5_2_yml.models.personal_financing import PersonalFinancing
from products-services_1_0_0-rc5_2_yml.models.personal_financing_brand import PersonalFinancingBrand
from products-services_1_0_0-rc5_2_yml.models.personal_financing_company import PersonalFinancingCompany
from products-services_1_0_0-rc5_2_yml.models.personal_financing_fee import PersonalFinancingFee
from products-services_1_0_0-rc5_2_yml.models.personal_invoice_financings import PersonalInvoiceFinancings
from products-services_1_0_0-rc5_2_yml.models.personal_invoice_financings_brand import PersonalInvoiceFinancingsBrand
from products-services_1_0_0-rc5_2_yml.models.personal_invoice_financings_companies import PersonalInvoiceFinancingsCompanies
from products-services_1_0_0-rc5_2_yml.models.personal_invoice_financings_fees import PersonalInvoiceFinancingsFees
from products-services_1_0_0-rc5_2_yml.models.personal_invoice_financings_interest_rates import PersonalInvoiceFinancingsInterestRates
from products-services_1_0_0-rc5_2_yml.models.personal_loan import PersonalLoan
from products-services_1_0_0-rc5_2_yml.models.personal_loan_brand import PersonalLoanBrand
from products-services_1_0_0-rc5_2_yml.models.personal_loan_company import PersonalLoanCompany
from products-services_1_0_0-rc5_2_yml.models.personal_unarranged_account_overdraft import PersonalUnarrangedAccountOverdraft
from products-services_1_0_0-rc5_2_yml.models.personal_unarranged_account_overdraft_brand import PersonalUnarrangedAccountOverdraftBrand
from products-services_1_0_0-rc5_2_yml.models.personal_unarranged_account_overdraft_company import PersonalUnarrangedAccountOverdraftCompany
from products-services_1_0_0-rc5_2_yml.models.personal_unarranged_account_overdraft_fee import PersonalUnarrangedAccountOverdraftFee
from products-services_1_0_0-rc5_2_yml.models.price import Price
from products-services_1_0_0-rc5_2_yml.models.price_intervals import PriceIntervals
from products-services_1_0_0-rc5_2_yml.models.priority_service_name import PriorityServiceName
from products-services_1_0_0-rc5_2_yml.models.referential_rate_indexer import ReferentialRateIndexer
from products-services_1_0_0-rc5_2_yml.models.required_warranty import RequiredWarranty
from products-services_1_0_0-rc5_2_yml.models.response_business_accounts import ResponseBusinessAccounts
from products-services_1_0_0-rc5_2_yml.models.response_business_accounts_data import ResponseBusinessAccountsData
from products-services_1_0_0-rc5_2_yml.models.response_business_financings import ResponseBusinessFinancings
from products-services_1_0_0-rc5_2_yml.models.response_business_financings_data import ResponseBusinessFinancingsData
from products-services_1_0_0-rc5_2_yml.models.response_business_invoice_financings import ResponseBusinessInvoiceFinancings
from products-services_1_0_0-rc5_2_yml.models.response_business_invoice_financings_data import ResponseBusinessInvoiceFinancingsData
from products-services_1_0_0-rc5_2_yml.models.response_business_loans import ResponseBusinessLoans
from products-services_1_0_0-rc5_2_yml.models.response_business_loans_data import ResponseBusinessLoansData
from products-services_1_0_0-rc5_2_yml.models.response_business_unarranged_account_overdraft import ResponseBusinessUnarrangedAccountOverdraft
from products-services_1_0_0-rc5_2_yml.models.response_business_unarranged_account_overdraft_data import ResponseBusinessUnarrangedAccountOverdraftData
from products-services_1_0_0-rc5_2_yml.models.response_personal_accounts import ResponsePersonalAccounts
from products-services_1_0_0-rc5_2_yml.models.response_personal_accounts_data import ResponsePersonalAccountsData
from products-services_1_0_0-rc5_2_yml.models.response_personal_financings import ResponsePersonalFinancings
from products-services_1_0_0-rc5_2_yml.models.response_personal_financings_data import ResponsePersonalFinancingsData
from products-services_1_0_0-rc5_2_yml.models.response_personal_invoice_financings import ResponsePersonalInvoiceFinancings
from products-services_1_0_0-rc5_2_yml.models.response_personal_invoice_financings_data import ResponsePersonalInvoiceFinancingsData
from products-services_1_0_0-rc5_2_yml.models.response_personal_loans import ResponsePersonalLoans
from products-services_1_0_0-rc5_2_yml.models.response_personal_loans_data import ResponsePersonalLoansData
from products-services_1_0_0-rc5_2_yml.models.response_personal_unarranged_account_overdraft import ResponsePersonalUnarrangedAccountOverdraft
from products-services_1_0_0-rc5_2_yml.models.response_personal_unarranged_account_overdraft_data import ResponsePersonalUnarrangedAccountOverdraftData
from products-services_1_0_0-rc5_2_yml.models.service_bundle import ServiceBundle
from products-services_1_0_0-rc5_2_yml.models.service_bundle_service_detail import ServiceBundleServiceDetail
from products-services_1_0_0-rc5_2_yml.models.transaction_methods import TransactionMethods
from products-services_1_0_0-rc5_2_yml.models.unarranged_account_overdraft_rate import UnarrangedAccountOverdraftRate
from products-services_1_0_0-rc5_2_yml.models.unarranged_account_overdraft_service import UnarrangedAccountOverdraftService