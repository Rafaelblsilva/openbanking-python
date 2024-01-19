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

class OrganisationAuthorityClaimAuthorisationRequest(object):
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
        'member_state': 'str'
    }

    attribute_map = {
        'status': 'Status',
        'member_state': 'MemberState'
    }

    def __init__(self, status='Active', member_state=None):  # noqa: E501
        """OrganisationAuthorityClaimAuthorisationRequest - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._member_state = None
        self.discriminator = None
        self.status = status
        self.member_state = member_state

    @property
    def status(self):
        """Gets the status of this OrganisationAuthorityClaimAuthorisationRequest.  # noqa: E501

        Is this Active/Inactive - default is Active  # noqa: E501

        :return: The status of this OrganisationAuthorityClaimAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this OrganisationAuthorityClaimAuthorisationRequest.

        Is this Active/Inactive - default is Active  # noqa: E501

        :param status: The status of this OrganisationAuthorityClaimAuthorisationRequest.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["Active", "Inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def member_state(self):
        """Gets the member_state of this OrganisationAuthorityClaimAuthorisationRequest.  # noqa: E501

        Abbreviated states information i.e. GB, IE, NL etc  # noqa: E501

        :return: The member_state of this OrganisationAuthorityClaimAuthorisationRequest.  # noqa: E501
        :rtype: str
        """
        return self._member_state

    @member_state.setter
    def member_state(self, member_state):
        """Sets the member_state of this OrganisationAuthorityClaimAuthorisationRequest.

        Abbreviated states information i.e. GB, IE, NL etc  # noqa: E501

        :param member_state: The member_state of this OrganisationAuthorityClaimAuthorisationRequest.  # noqa: E501
        :type: str
        """
        if member_state is None:
            raise ValueError("Invalid value for `member_state`, must not be `None`")  # noqa: E501

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
        if issubclass(OrganisationAuthorityClaimAuthorisationRequest, dict):
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
        if not isinstance(other, OrganisationAuthorityClaimAuthorisationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
