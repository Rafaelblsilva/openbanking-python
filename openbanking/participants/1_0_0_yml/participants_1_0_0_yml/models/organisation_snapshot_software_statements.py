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

class OrganisationSnapshotSoftwareStatements(object):
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
        'software_details': 'SoftwareStatement',
        'software_authority_claims': 'SoftwareAuthorityClaims',
        'software_certificates': 'CertificatesOrKeys'
    }

    attribute_map = {
        'software_details': 'SoftwareDetails',
        'software_authority_claims': 'SoftwareAuthorityClaims',
        'software_certificates': 'SoftwareCertificates'
    }

    def __init__(self, software_details=None, software_authority_claims=None, software_certificates=None):  # noqa: E501
        """OrganisationSnapshotSoftwareStatements - a model defined in Swagger"""  # noqa: E501
        self._software_details = None
        self._software_authority_claims = None
        self._software_certificates = None
        self.discriminator = None
        if software_details is not None:
            self.software_details = software_details
        if software_authority_claims is not None:
            self.software_authority_claims = software_authority_claims
        if software_certificates is not None:
            self.software_certificates = software_certificates

    @property
    def software_details(self):
        """Gets the software_details of this OrganisationSnapshotSoftwareStatements.  # noqa: E501


        :return: The software_details of this OrganisationSnapshotSoftwareStatements.  # noqa: E501
        :rtype: SoftwareStatement
        """
        return self._software_details

    @software_details.setter
    def software_details(self, software_details):
        """Sets the software_details of this OrganisationSnapshotSoftwareStatements.


        :param software_details: The software_details of this OrganisationSnapshotSoftwareStatements.  # noqa: E501
        :type: SoftwareStatement
        """

        self._software_details = software_details

    @property
    def software_authority_claims(self):
        """Gets the software_authority_claims of this OrganisationSnapshotSoftwareStatements.  # noqa: E501


        :return: The software_authority_claims of this OrganisationSnapshotSoftwareStatements.  # noqa: E501
        :rtype: SoftwareAuthorityClaims
        """
        return self._software_authority_claims

    @software_authority_claims.setter
    def software_authority_claims(self, software_authority_claims):
        """Sets the software_authority_claims of this OrganisationSnapshotSoftwareStatements.


        :param software_authority_claims: The software_authority_claims of this OrganisationSnapshotSoftwareStatements.  # noqa: E501
        :type: SoftwareAuthorityClaims
        """

        self._software_authority_claims = software_authority_claims

    @property
    def software_certificates(self):
        """Gets the software_certificates of this OrganisationSnapshotSoftwareStatements.  # noqa: E501


        :return: The software_certificates of this OrganisationSnapshotSoftwareStatements.  # noqa: E501
        :rtype: CertificatesOrKeys
        """
        return self._software_certificates

    @software_certificates.setter
    def software_certificates(self, software_certificates):
        """Sets the software_certificates of this OrganisationSnapshotSoftwareStatements.


        :param software_certificates: The software_certificates of this OrganisationSnapshotSoftwareStatements.  # noqa: E501
        :type: CertificatesOrKeys
        """

        self._software_certificates = software_certificates

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
        if issubclass(OrganisationSnapshotSoftwareStatements, dict):
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
        if not isinstance(other, OrganisationSnapshotSoftwareStatements):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
