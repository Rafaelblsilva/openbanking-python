# coding: utf-8

# flake8: noqa
"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from channels_2_0_0_yml.models.availability import Availability
from channels_2_0_0_yml.models.availability_standards import AvailabilityStandards
from channels_2_0_0_yml.models.banking_agent import BankingAgent
from channels_2_0_0_yml.models.banking_agent_identification import BankingAgentIdentification
from channels_2_0_0_yml.models.banking_agent_location import BankingAgentLocation
from channels_2_0_0_yml.models.banking_agent_postal_address import BankingAgentPostalAddress
from channels_2_0_0_yml.models.banking_agent_service import BankingAgentService
from channels_2_0_0_yml.models.banking_agents_brand import BankingAgentsBrand
from channels_2_0_0_yml.models.banking_agents_companies import BankingAgentsCompanies
from channels_2_0_0_yml.models.banking_agents_contractor import BankingAgentsContractor
from channels_2_0_0_yml.models.branch import Branch
from channels_2_0_0_yml.models.branch_availability import BranchAvailability
from channels_2_0_0_yml.models.branch_availability_standards import BranchAvailabilityStandards
from channels_2_0_0_yml.models.branch_identification import BranchIdentification
from channels_2_0_0_yml.models.branch_postal_address import BranchPostalAddress
from channels_2_0_0_yml.models.branch_services import BranchServices
from channels_2_0_0_yml.models.branches_brand import BranchesBrand
from channels_2_0_0_yml.models.branches_company import BranchesCompany
from channels_2_0_0_yml.models.brand import Brand
from channels_2_0_0_yml.models.cnpj import CNPJ
from channels_2_0_0_yml.models.electronic_channel import ElectronicChannel
from channels_2_0_0_yml.models.electronic_channel_identification import ElectronicChannelIdentification
from channels_2_0_0_yml.models.electronic_channel_service import ElectronicChannelService
from channels_2_0_0_yml.models.electronic_channel_url import ElectronicChannelUrl
from channels_2_0_0_yml.models.electronic_channels_brand import ElectronicChannelsBrand
from channels_2_0_0_yml.models.electronic_channels_companies import ElectronicChannelsCompanies
from channels_2_0_0_yml.models.geographic_coordinates import GeographicCoordinates
from channels_2_0_0_yml.models.links import Links
from channels_2_0_0_yml.models.meta import Meta
from channels_2_0_0_yml.models.phone import Phone
from channels_2_0_0_yml.models.phone_channel import PhoneChannel
from channels_2_0_0_yml.models.phone_channel_identification import PhoneChannelIdentification
from channels_2_0_0_yml.models.phone_channel_phone import PhoneChannelPhone
from channels_2_0_0_yml.models.phone_channel_service import PhoneChannelService
from channels_2_0_0_yml.models.phone_channels_brand import PhoneChannelsBrand
from channels_2_0_0_yml.models.phone_channels_company import PhoneChannelsCompany
from channels_2_0_0_yml.models.postal_address import PostalAddress
from channels_2_0_0_yml.models.response_banking_agents_list import ResponseBankingAgentsList
from channels_2_0_0_yml.models.response_banking_agents_list_data import ResponseBankingAgentsListData
from channels_2_0_0_yml.models.response_branches_list import ResponseBranchesList
from channels_2_0_0_yml.models.response_branches_list_data import ResponseBranchesListData
from channels_2_0_0_yml.models.response_electronic_channels_list import ResponseElectronicChannelsList
from channels_2_0_0_yml.models.response_electronic_channels_list_data import ResponseElectronicChannelsListData
from channels_2_0_0_yml.models.response_phone_channels_list import ResponsePhoneChannelsList
from channels_2_0_0_yml.models.response_phone_channels_list_data import ResponsePhoneChannelsListData
from channels_2_0_0_yml.models.response_shared_automated_teller_machines_list import ResponseSharedAutomatedTellerMachinesList
from channels_2_0_0_yml.models.response_shared_automated_teller_machines_list_data import ResponseSharedAutomatedTellerMachinesListData
from channels_2_0_0_yml.models.shared_automated_teller_machines import SharedAutomatedTellerMachines
from channels_2_0_0_yml.models.shared_automated_teller_machines_availability import SharedAutomatedTellerMachinesAvailability
from channels_2_0_0_yml.models.shared_automated_teller_machines_availability_standards import SharedAutomatedTellerMachinesAvailabilityStandards
from channels_2_0_0_yml.models.shared_automated_teller_machines_brand import SharedAutomatedTellerMachinesBrand
from channels_2_0_0_yml.models.shared_automated_teller_machines_companies import SharedAutomatedTellerMachinesCompanies
from channels_2_0_0_yml.models.shared_automated_teller_machines_company import SharedAutomatedTellerMachinesCompany
from channels_2_0_0_yml.models.shared_automated_teller_machines_identification import SharedAutomatedTellerMachinesIdentification
from channels_2_0_0_yml.models.shared_automated_teller_machines_postal_address import SharedAutomatedTellerMachinesPostalAddress
from channels_2_0_0_yml.models.shared_automated_teller_machines_services import SharedAutomatedTellerMachinesServices
