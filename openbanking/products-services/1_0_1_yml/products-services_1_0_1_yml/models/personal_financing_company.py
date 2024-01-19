# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from products-services_1_0_1_yml.models.company import Company  # noqa: F401,E501

class PersonalFinancingCompany(Company):
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
        'personal_financings': 'list[PersonalFinancing]'
    }
    if hasattr(Company, "swagger_types"):
        swagger_types.update(Company.swagger_types)

    attribute_map = {
        'personal_financings': 'personalFinancings'
    }
    if hasattr(Company, "attribute_map"):
        attribute_map.update(Company.attribute_map)

    def __init__(self, personal_financings=None, *args, **kwargs):  # noqa: E501
        """PersonalFinancingCompany - a model defined in Swagger"""  # noqa: E501
        self._personal_financings = None
        self.discriminator = None
        self.personal_financings = personal_financings
        Company.__init__(self, *args, **kwargs)

    @property
    def personal_financings(self):
        """Gets the personal_financings of this PersonalFinancingCompany.  # noqa: E501

        Lista de financiamentos  # noqa: E501

        :return: The personal_financings of this PersonalFinancingCompany.  # noqa: E501
        :rtype: list[PersonalFinancing]
        """
        return self._personal_financings

    @personal_financings.setter
    def personal_financings(self, personal_financings):
        """Sets the personal_financings of this PersonalFinancingCompany.

        Lista de financiamentos  # noqa: E501

        :param personal_financings: The personal_financings of this PersonalFinancingCompany.  # noqa: E501
        :type: list[PersonalFinancing]
        """
        if personal_financings is None:
            raise ValueError("Invalid value for `personal_financings`, must not be `None`")  # noqa: E501

        self._personal_financings = personal_financings

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
        if issubclass(PersonalFinancingCompany, dict):
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
        if not isinstance(other, PersonalFinancingCompany):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
