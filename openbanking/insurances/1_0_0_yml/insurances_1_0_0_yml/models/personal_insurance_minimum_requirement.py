# coding: utf-8

"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalInsuranceMinimumRequirement(object):
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
        'contract_type': 'EnumContractTypePersonal',
        'contracting_min_requirement': 'str'
    }

    attribute_map = {
        'contract_type': 'contractType',
        'contracting_min_requirement': 'contractingMinRequirement'
    }

    def __init__(self, contract_type=None, contracting_min_requirement=None):  # noqa: E501
        """PersonalInsuranceMinimumRequirement - a model defined in Swagger"""  # noqa: E501
        self._contract_type = None
        self._contracting_min_requirement = None
        self.discriminator = None
        self.contract_type = contract_type
        self.contracting_min_requirement = contracting_min_requirement

    @property
    def contract_type(self):
        """Gets the contract_type of this PersonalInsuranceMinimumRequirement.  # noqa: E501


        :return: The contract_type of this PersonalInsuranceMinimumRequirement.  # noqa: E501
        :rtype: EnumContractTypePersonal
        """
        return self._contract_type

    @contract_type.setter
    def contract_type(self, contract_type):
        """Sets the contract_type of this PersonalInsuranceMinimumRequirement.


        :param contract_type: The contract_type of this PersonalInsuranceMinimumRequirement.  # noqa: E501
        :type: EnumContractTypePersonal
        """
        if contract_type is None:
            raise ValueError("Invalid value for `contract_type`, must not be `None`")  # noqa: E501

        self._contract_type = contract_type

    @property
    def contracting_min_requirement(self):
        """Gets the contracting_min_requirement of this PersonalInsuranceMinimumRequirement.  # noqa: E501

        Campo aberto (possibilidade de incluir URL)  # noqa: E501

        :return: The contracting_min_requirement of this PersonalInsuranceMinimumRequirement.  # noqa: E501
        :rtype: str
        """
        return self._contracting_min_requirement

    @contracting_min_requirement.setter
    def contracting_min_requirement(self, contracting_min_requirement):
        """Sets the contracting_min_requirement of this PersonalInsuranceMinimumRequirement.

        Campo aberto (possibilidade de incluir URL)  # noqa: E501

        :param contracting_min_requirement: The contracting_min_requirement of this PersonalInsuranceMinimumRequirement.  # noqa: E501
        :type: str
        """
        if contracting_min_requirement is None:
            raise ValueError("Invalid value for `contracting_min_requirement`, must not be `None`")  # noqa: E501

        self._contracting_min_requirement = contracting_min_requirement

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
        if issubclass(PersonalInsuranceMinimumRequirement, dict):
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
        if not isinstance(other, PersonalInsuranceMinimumRequirement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
