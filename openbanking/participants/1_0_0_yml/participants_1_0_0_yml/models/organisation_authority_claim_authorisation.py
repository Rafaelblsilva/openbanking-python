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

class OrganisationAuthorityClaimAuthorisation(object):
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
        'organisation_authorisation_id': 'OrganisationAuthorisationId',
        'organisation_authority_claim_id': 'OrganisationAuthorityClaimId',
        'status': 'str',
        'member_state': 'str'
    }

    attribute_map = {
        'organisation_authorisation_id': 'OrganisationAuthorisationId',
        'organisation_authority_claim_id': 'OrganisationAuthorityClaimId',
        'status': 'Status',
        'member_state': 'MemberState'
    }

    def __init__(self, organisation_authorisation_id=None, organisation_authority_claim_id=None, status='Active', member_state=None):  # noqa: E501
        """OrganisationAuthorityClaimAuthorisation - a model defined in Swagger"""  # noqa: E501
        self._organisation_authorisation_id = None
        self._organisation_authority_claim_id = None
        self._status = None
        self._member_state = None
        self.discriminator = None
        if organisation_authorisation_id is not None:
            self.organisation_authorisation_id = organisation_authorisation_id
        if organisation_authority_claim_id is not None:
            self.organisation_authority_claim_id = organisation_authority_claim_id
        if status is not None:
            self.status = status
        if member_state is not None:
            self.member_state = member_state

    @property
    def organisation_authorisation_id(self):
        """Gets the organisation_authorisation_id of this OrganisationAuthorityClaimAuthorisation.  # noqa: E501


        :return: The organisation_authorisation_id of this OrganisationAuthorityClaimAuthorisation.  # noqa: E501
        :rtype: OrganisationAuthorisationId
        """
        return self._organisation_authorisation_id

    @organisation_authorisation_id.setter
    def organisation_authorisation_id(self, organisation_authorisation_id):
        """Sets the organisation_authorisation_id of this OrganisationAuthorityClaimAuthorisation.


        :param organisation_authorisation_id: The organisation_authorisation_id of this OrganisationAuthorityClaimAuthorisation.  # noqa: E501
        :type: OrganisationAuthorisationId
        """

        self._organisation_authorisation_id = organisation_authorisation_id

    @property
    def organisation_authority_claim_id(self):
        """Gets the organisation_authority_claim_id of this OrganisationAuthorityClaimAuthorisation.  # noqa: E501


        :return: The organisation_authority_claim_id of this OrganisationAuthorityClaimAuthorisation.  # noqa: E501
        :rtype: OrganisationAuthorityClaimId
        """
        return self._organisation_authority_claim_id

    @organisation_authority_claim_id.setter
    def organisation_authority_claim_id(self, organisation_authority_claim_id):
        """Sets the organisation_authority_claim_id of this OrganisationAuthorityClaimAuthorisation.


        :param organisation_authority_claim_id: The organisation_authority_claim_id of this OrganisationAuthorityClaimAuthorisation.  # noqa: E501
        :type: OrganisationAuthorityClaimId
        """

        self._organisation_authority_claim_id = organisation_authority_claim_id

    @property
    def status(self):
        """Gets the status of this OrganisationAuthorityClaimAuthorisation.  # noqa: E501

        Is this authority claim Active/Inactive  # noqa: E501

        :return: The status of this OrganisationAuthorityClaimAuthorisation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrganisationAuthorityClaimAuthorisation.

        Is this authority claim Active/Inactive  # noqa: E501

        :param status: The status of this OrganisationAuthorityClaimAuthorisation.  # noqa: E501
        :type: str
        """
        allowed_values = ["Active", "Inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def member_state(self):
        """Gets the member_state of this OrganisationAuthorityClaimAuthorisation.  # noqa: E501

        Abbreviated states information i.e. GB, IE, NL etc  # noqa: E501

        :return: The member_state of this OrganisationAuthorityClaimAuthorisation.  # noqa: E501
        :rtype: str
        """
        return self._member_state

    @member_state.setter
    def member_state(self, member_state):
        """Sets the member_state of this OrganisationAuthorityClaimAuthorisation.

        Abbreviated states information i.e. GB, IE, NL etc  # noqa: E501

        :param member_state: The member_state of this OrganisationAuthorityClaimAuthorisation.  # noqa: E501
        :type: str
        """

        self._member_state = member_state

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
        if issubclass(OrganisationAuthorityClaimAuthorisation, dict):
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
        if not isinstance(other, OrganisationAuthorityClaimAuthorisation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
