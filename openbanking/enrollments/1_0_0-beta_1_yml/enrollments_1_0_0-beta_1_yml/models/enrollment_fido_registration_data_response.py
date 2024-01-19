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

class EnrollmentFidoRegistrationDataResponse(object):
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
        'client_data_json': 'str',
        'attestation_object': 'str'
    }

    attribute_map = {
        'client_data_json': 'clientDataJSON',
        'attestation_object': 'attestationObject'
    }

    def __init__(self, client_data_json=None, attestation_object=None):  # noqa: E501
        """EnrollmentFidoRegistrationDataResponse - a model defined in Swagger"""  # noqa: E501
        self._client_data_json = None
        self._attestation_object = None
        self.discriminator = None
        self.client_data_json = client_data_json
        self.attestation_object = attestation_object

    @property
    def client_data_json(self):
        """Gets the client_data_json of this EnrollmentFidoRegistrationDataResponse.  # noqa: E501

        Agrega as informações do aplicativo que gerou a credencial.  # noqa: E501

        :return: The client_data_json of this EnrollmentFidoRegistrationDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._client_data_json

    @client_data_json.setter
    def client_data_json(self, client_data_json):
        """Sets the client_data_json of this EnrollmentFidoRegistrationDataResponse.

        Agrega as informações do aplicativo que gerou a credencial.  # noqa: E501

        :param client_data_json: The client_data_json of this EnrollmentFidoRegistrationDataResponse.  # noqa: E501
        :type: str
        """
        if client_data_json is None:
            raise ValueError("Invalid value for `client_data_json`, must not be `None`")  # noqa: E501

        self._client_data_json = client_data_json

    @property
    def attestation_object(self):
        """Gets the attestation_object of this EnrollmentFidoRegistrationDataResponse.  # noqa: E501

        Agrega as informações da chave pública da credencial.  # noqa: E501

        :return: The attestation_object of this EnrollmentFidoRegistrationDataResponse.  # noqa: E501
        :rtype: str
        """
        return self._attestation_object

    @attestation_object.setter
    def attestation_object(self, attestation_object):
        """Sets the attestation_object of this EnrollmentFidoRegistrationDataResponse.

        Agrega as informações da chave pública da credencial.  # noqa: E501

        :param attestation_object: The attestation_object of this EnrollmentFidoRegistrationDataResponse.  # noqa: E501
        :type: str
        """
        if attestation_object is None:
            raise ValueError("Invalid value for `attestation_object`, must not be `None`")  # noqa: E501

        self._attestation_object = attestation_object

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
        if issubclass(EnrollmentFidoRegistrationDataResponse, dict):
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
        if not isinstance(other, EnrollmentFidoRegistrationDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
