# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    API de Dispositivo Vínculado para suportar Iniciação de Pagamentos na Jornada Sem Redirecionamento do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-beta.1
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from enrollments_1_0_0-beta_1_yml.models.enrollment_fido_options_input import EnrollmentFidoOptionsInput  # noqa: F401,E501

class EnrollmentIdFidosignoptionsBody(EnrollmentFidoOptionsInput):
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
        'data': 'EnrollmentsenrollmentIdfidosignoptionsData'
    }
    if hasattr(EnrollmentFidoOptionsInput, "swagger_types"):
        swagger_types.update(EnrollmentFidoOptionsInput.swagger_types)

    attribute_map = {
        'data': 'data'
    }
    if hasattr(EnrollmentFidoOptionsInput, "attribute_map"):
        attribute_map.update(EnrollmentFidoOptionsInput.attribute_map)

    def __init__(self, data=None, *args, **kwargs):  # noqa: E501
        """EnrollmentIdFidosignoptionsBody - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self.discriminator = None
        self.data = data
        EnrollmentFidoOptionsInput.__init__(self, *args, **kwargs)

    @property
    def data(self):
        """Gets the data of this EnrollmentIdFidosignoptionsBody.  # noqa: E501


        :return: The data of this EnrollmentIdFidosignoptionsBody.  # noqa: E501
        :rtype: EnrollmentsenrollmentIdfidosignoptionsData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this EnrollmentIdFidosignoptionsBody.


        :param data: The data of this EnrollmentIdFidosignoptionsBody.  # noqa: E501
        :type: EnrollmentsenrollmentIdfidosignoptionsData
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

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
        if issubclass(EnrollmentIdFidosignoptionsBody, dict):
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
        if not isinstance(other, EnrollmentIdFidosignoptionsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
