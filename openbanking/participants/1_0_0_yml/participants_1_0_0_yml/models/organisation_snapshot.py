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

class OrganisationSnapshot(object):
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
        'organisation_details': 'Organisation',
        'contacts': 'Contacts',
        'authorisation_servers': 'AuthorisationServers',
        'org_domain_claims': 'OrganisationAuthorityDomainClaims',
        'org_domain_role_claims': 'OrganisationAuthorityClaims',
        'software_statements': 'dict(str, OrganisationSnapshotSoftwareStatements)'
    }

    attribute_map = {
        'organisation_details': 'OrganisationDetails',
        'contacts': 'Contacts',
        'authorisation_servers': 'AuthorisationServers',
        'org_domain_claims': 'OrgDomainClaims',
        'org_domain_role_claims': 'OrgDomainRoleClaims',
        'software_statements': 'SoftwareStatements'
    }

    def __init__(self, organisation_details=None, contacts=None, authorisation_servers=None, org_domain_claims=None, org_domain_role_claims=None, software_statements=None):  # noqa: E501
        """OrganisationSnapshot - a model defined in Swagger"""  # noqa: E501
        self._organisation_details = None
        self._contacts = None
        self._authorisation_servers = None
        self._org_domain_claims = None
        self._org_domain_role_claims = None
        self._software_statements = None
        self.discriminator = None
        if organisation_details is not None:
            self.organisation_details = organisation_details
        if contacts is not None:
            self.contacts = contacts
        if authorisation_servers is not None:
            self.authorisation_servers = authorisation_servers
        if org_domain_claims is not None:
            self.org_domain_claims = org_domain_claims
        if org_domain_role_claims is not None:
            self.org_domain_role_claims = org_domain_role_claims
        if software_statements is not None:
            self.software_statements = software_statements

    @property
    def organisation_details(self):
        """Gets the organisation_details of this OrganisationSnapshot.  # noqa: E501


        :return: The organisation_details of this OrganisationSnapshot.  # noqa: E501
        :rtype: Organisation
        """
        return self._organisation_details

    @organisation_details.setter
    def organisation_details(self, organisation_details):
        """Sets the organisation_details of this OrganisationSnapshot.


        :param organisation_details: The organisation_details of this OrganisationSnapshot.  # noqa: E501
        :type: Organisation
        """

        self._organisation_details = organisation_details

    @property
    def contacts(self):
        """Gets the contacts of this OrganisationSnapshot.  # noqa: E501


        :return: The contacts of this OrganisationSnapshot.  # noqa: E501
        :rtype: Contacts
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this OrganisationSnapshot.


        :param contacts: The contacts of this OrganisationSnapshot.  # noqa: E501
        :type: Contacts
        """

        self._contacts = contacts

    @property
    def authorisation_servers(self):
        """Gets the authorisation_servers of this OrganisationSnapshot.  # noqa: E501


        :return: The authorisation_servers of this OrganisationSnapshot.  # noqa: E501
        :rtype: AuthorisationServers
        """
        return self._authorisation_servers

    @authorisation_servers.setter
    def authorisation_servers(self, authorisation_servers):
        """Sets the authorisation_servers of this OrganisationSnapshot.


        :param authorisation_servers: The authorisation_servers of this OrganisationSnapshot.  # noqa: E501
        :type: AuthorisationServers
        """

        self._authorisation_servers = authorisation_servers

    @property
    def org_domain_claims(self):
        """Gets the org_domain_claims of this OrganisationSnapshot.  # noqa: E501


        :return: The org_domain_claims of this OrganisationSnapshot.  # noqa: E501
        :rtype: OrganisationAuthorityDomainClaims
        """
        return self._org_domain_claims

    @org_domain_claims.setter
    def org_domain_claims(self, org_domain_claims):
        """Sets the org_domain_claims of this OrganisationSnapshot.


        :param org_domain_claims: The org_domain_claims of this OrganisationSnapshot.  # noqa: E501
        :type: OrganisationAuthorityDomainClaims
        """

        self._org_domain_claims = org_domain_claims

    @property
    def org_domain_role_claims(self):
        """Gets the org_domain_role_claims of this OrganisationSnapshot.  # noqa: E501


        :return: The org_domain_role_claims of this OrganisationSnapshot.  # noqa: E501
        :rtype: OrganisationAuthorityClaims
        """
        return self._org_domain_role_claims

    @org_domain_role_claims.setter
    def org_domain_role_claims(self, org_domain_role_claims):
        """Sets the org_domain_role_claims of this OrganisationSnapshot.


        :param org_domain_role_claims: The org_domain_role_claims of this OrganisationSnapshot.  # noqa: E501
        :type: OrganisationAuthorityClaims
        """

        self._org_domain_role_claims = org_domain_role_claims

    @property
    def software_statements(self):
        """Gets the software_statements of this OrganisationSnapshot.  # noqa: E501


        :return: The software_statements of this OrganisationSnapshot.  # noqa: E501
        :rtype: dict(str, OrganisationSnapshotSoftwareStatements)
        """
        return self._software_statements

    @software_statements.setter
    def software_statements(self, software_statements):
        """Sets the software_statements of this OrganisationSnapshot.


        :param software_statements: The software_statements of this OrganisationSnapshot.  # noqa: E501
        :type: dict(str, OrganisationSnapshotSoftwareStatements)
        """

        self._software_statements = software_statements

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
        if issubclass(OrganisationSnapshot, dict):
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
        if not isinstance(other, OrganisationSnapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other