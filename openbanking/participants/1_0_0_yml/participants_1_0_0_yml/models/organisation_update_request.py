# coding: utf-8

"""
    Participantes Open Finance Brasil

    Informações sobre os participantes do Open Finance Brasil que estão registrados no Diretório.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OrganisationUpdateRequest(object):
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
        'status': 'str',
        'organisation_name': 'str',
        'legal_entity_name': 'str',
        'country_of_registration': 'str',
        'company_register': 'str',
        'registration_number': 'str',
        'registration_id': 'str',
        'registered_name': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'city': 'str',
        'postcode': 'str',
        'country': 'str',
        'parent_organisation_reference': 'str'
    }

    attribute_map = {
        'status': 'Status',
        'organisation_name': 'OrganisationName',
        'legal_entity_name': 'LegalEntityName',
        'country_of_registration': 'CountryOfRegistration',
        'company_register': 'CompanyRegister',
        'registration_number': 'RegistrationNumber',
        'registration_id': 'RegistrationId',
        'registered_name': 'RegisteredName',
        'address_line1': 'AddressLine1',
        'address_line2': 'AddressLine2',
        'city': 'City',
        'postcode': 'Postcode',
        'country': 'Country',
        'parent_organisation_reference': 'ParentOrganisationReference'
    }

    def __init__(self, status='Pending', organisation_name=None, legal_entity_name=None, country_of_registration=None, company_register=None, registration_number=None, registration_id=None, registered_name=None, address_line1=None, address_line2=None, city=None, postcode=None, country=None, parent_organisation_reference=None):  # noqa: E501
        """OrganisationUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._organisation_name = None
        self._legal_entity_name = None
        self._country_of_registration = None
        self._company_register = None
        self._registration_number = None
        self._registration_id = None
        self._registered_name = None
        self._address_line1 = None
        self._address_line2 = None
        self._city = None
        self._postcode = None
        self._country = None
        self._parent_organisation_reference = None
        self.discriminator = None
        if status is not None:
            self.status = status
        self.organisation_name = organisation_name
        self.legal_entity_name = legal_entity_name
        self.country_of_registration = country_of_registration
        self.company_register = company_register
        self.registration_number = registration_number
        if registration_id is not None:
            self.registration_id = registration_id
        if registered_name is not None:
            self.registered_name = registered_name
        self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        self.city = city
        self.postcode = postcode
        self.country = country
        if parent_organisation_reference is not None:
            self.parent_organisation_reference = parent_organisation_reference

    @property
    def status(self):
        """Gets the status of this OrganisationUpdateRequest.  # noqa: E501

        Status of the directory registration of an organisation  # noqa: E501

        :return: The status of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrganisationUpdateRequest.

        Status of the directory registration of an organisation  # noqa: E501

        :param status: The status of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Active", "Pending", "Withdrawn"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def organisation_name(self):
        """Gets the organisation_name of this OrganisationUpdateRequest.  # noqa: E501


        :return: The organisation_name of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._organisation_name

    @organisation_name.setter
    def organisation_name(self, organisation_name):
        """Sets the organisation_name of this OrganisationUpdateRequest.


        :param organisation_name: The organisation_name of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """
        if organisation_name is None:
            raise ValueError("Invalid value for `organisation_name`, must not be `None`")  # noqa: E501

        self._organisation_name = organisation_name

    @property
    def legal_entity_name(self):
        """Gets the legal_entity_name of this OrganisationUpdateRequest.  # noqa: E501

        Legal Entity name for the org. Usually the same as org name  # noqa: E501

        :return: The legal_entity_name of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._legal_entity_name

    @legal_entity_name.setter
    def legal_entity_name(self, legal_entity_name):
        """Sets the legal_entity_name of this OrganisationUpdateRequest.

        Legal Entity name for the org. Usually the same as org name  # noqa: E501

        :param legal_entity_name: The legal_entity_name of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """
        if legal_entity_name is None:
            raise ValueError("Invalid value for `legal_entity_name`, must not be `None`")  # noqa: E501

        self._legal_entity_name = legal_entity_name

    @property
    def country_of_registration(self):
        """Gets the country_of_registration of this OrganisationUpdateRequest.  # noqa: E501

        Country of registration for the org  # noqa: E501

        :return: The country_of_registration of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._country_of_registration

    @country_of_registration.setter
    def country_of_registration(self, country_of_registration):
        """Sets the country_of_registration of this OrganisationUpdateRequest.

        Country of registration for the org  # noqa: E501

        :param country_of_registration: The country_of_registration of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """
        if country_of_registration is None:
            raise ValueError("Invalid value for `country_of_registration`, must not be `None`")  # noqa: E501

        self._country_of_registration = country_of_registration

    @property
    def company_register(self):
        """Gets the company_register of this OrganisationUpdateRequest.  # noqa: E501

        Legal company register for the country, i.e. Companies House  # noqa: E501

        :return: The company_register of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._company_register

    @company_register.setter
    def company_register(self, company_register):
        """Sets the company_register of this OrganisationUpdateRequest.

        Legal company register for the country, i.e. Companies House  # noqa: E501

        :param company_register: The company_register of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """
        if company_register is None:
            raise ValueError("Invalid value for `company_register`, must not be `None`")  # noqa: E501

        self._company_register = company_register

    @property
    def registration_number(self):
        """Gets the registration_number of this OrganisationUpdateRequest.  # noqa: E501

        Company registration number from company register i.e. Companies House registration number  # noqa: E501

        :return: The registration_number of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._registration_number

    @registration_number.setter
    def registration_number(self, registration_number):
        """Sets the registration_number of this OrganisationUpdateRequest.

        Company registration number from company register i.e. Companies House registration number  # noqa: E501

        :param registration_number: The registration_number of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """
        if registration_number is None:
            raise ValueError("Invalid value for `registration_number`, must not be `None`")  # noqa: E501

        self._registration_number = registration_number

    @property
    def registration_id(self):
        """Gets the registration_id of this OrganisationUpdateRequest.  # noqa: E501

        Registered ID for the organisation i.e. Legal Entity identifier number  # noqa: E501

        :return: The registration_id of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._registration_id

    @registration_id.setter
    def registration_id(self, registration_id):
        """Sets the registration_id of this OrganisationUpdateRequest.

        Registered ID for the organisation i.e. Legal Entity identifier number  # noqa: E501

        :param registration_id: The registration_id of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """

        self._registration_id = registration_id

    @property
    def registered_name(self):
        """Gets the registered_name of this OrganisationUpdateRequest.  # noqa: E501

        Registered legal name  # noqa: E501

        :return: The registered_name of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._registered_name

    @registered_name.setter
    def registered_name(self, registered_name):
        """Sets the registered_name of this OrganisationUpdateRequest.

        Registered legal name  # noqa: E501

        :param registered_name: The registered_name of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """

        self._registered_name = registered_name

    @property
    def address_line1(self):
        """Gets the address_line1 of this OrganisationUpdateRequest.  # noqa: E501

        Address line 1  # noqa: E501

        :return: The address_line1 of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this OrganisationUpdateRequest.

        Address line 1  # noqa: E501

        :param address_line1: The address_line1 of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """
        if address_line1 is None:
            raise ValueError("Invalid value for `address_line1`, must not be `None`")  # noqa: E501

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this OrganisationUpdateRequest.  # noqa: E501

        Address line 2  # noqa: E501

        :return: The address_line2 of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this OrganisationUpdateRequest.

        Address line 2  # noqa: E501

        :param address_line2: The address_line2 of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def city(self):
        """Gets the city of this OrganisationUpdateRequest.  # noqa: E501

        City  # noqa: E501

        :return: The city of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this OrganisationUpdateRequest.

        City  # noqa: E501

        :param city: The city of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def postcode(self):
        """Gets the postcode of this OrganisationUpdateRequest.  # noqa: E501

        Postcode  # noqa: E501

        :return: The postcode of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this OrganisationUpdateRequest.

        Postcode  # noqa: E501

        :param postcode: The postcode of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """
        if postcode is None:
            raise ValueError("Invalid value for `postcode`, must not be `None`")  # noqa: E501

        self._postcode = postcode

    @property
    def country(self):
        """Gets the country of this OrganisationUpdateRequest.  # noqa: E501

        Country  # noqa: E501

        :return: The country of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this OrganisationUpdateRequest.

        Country  # noqa: E501

        :param country: The country of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def parent_organisation_reference(self):
        """Gets the parent_organisation_reference of this OrganisationUpdateRequest.  # noqa: E501

        Parent Organisation Reference  # noqa: E501

        :return: The parent_organisation_reference of this OrganisationUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._parent_organisation_reference

    @parent_organisation_reference.setter
    def parent_organisation_reference(self, parent_organisation_reference):
        """Sets the parent_organisation_reference of this OrganisationUpdateRequest.

        Parent Organisation Reference  # noqa: E501

        :param parent_organisation_reference: The parent_organisation_reference of this OrganisationUpdateRequest.  # noqa: E501
        :type: str
        """

        self._parent_organisation_reference = parent_organisation_reference

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
        if issubclass(OrganisationUpdateRequest, dict):
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
        if not isinstance(other, OrganisationUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
