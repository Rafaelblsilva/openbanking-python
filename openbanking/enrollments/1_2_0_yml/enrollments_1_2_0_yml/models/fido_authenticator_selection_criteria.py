# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    Família de API para permitir o pagamento sem redirecionamento via Open Finance Brasil.   Permite tanto o gerenciamento dos dispositivos vinculados as contas quanto a autorização de consentimentos criados via fluxo sem redirecionamento.   # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FidoAuthenticatorSelectionCriteria(object):
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
        'authenticator_attachment': 'str',
        'user_verification': 'str',
        'require_resident_key': 'bool',
        'resident_key': 'str'
    }

    attribute_map = {
        'authenticator_attachment': 'authenticatorAttachment',
        'user_verification': 'userVerification',
        'require_resident_key': 'requireResidentKey',
        'resident_key': 'residentKey'
    }

    def __init__(self, authenticator_attachment=None, user_verification=None, require_resident_key=None, resident_key=None):  # noqa: E501
        """FidoAuthenticatorSelectionCriteria - a model defined in Swagger"""  # noqa: E501
        self._authenticator_attachment = None
        self._user_verification = None
        self._require_resident_key = None
        self._resident_key = None
        self.discriminator = None
        if authenticator_attachment is not None:
            self.authenticator_attachment = authenticator_attachment
        if user_verification is not None:
            self.user_verification = user_verification
        if require_resident_key is not None:
            self.require_resident_key = require_resident_key
        if resident_key is not None:
            self.resident_key = resident_key

    @property
    def authenticator_attachment(self):
        """Gets the authenticator_attachment of this FidoAuthenticatorSelectionCriteria.  # noqa: E501

        Indica os tipos de autenticadores suportados (ex: Sistema Operacional ou Cross-Platform como uma chave USB)  # noqa: E501

        :return: The authenticator_attachment of this FidoAuthenticatorSelectionCriteria.  # noqa: E501
        :rtype: str
        """
        return self._authenticator_attachment

    @authenticator_attachment.setter
    def authenticator_attachment(self, authenticator_attachment):
        """Sets the authenticator_attachment of this FidoAuthenticatorSelectionCriteria.

        Indica os tipos de autenticadores suportados (ex: Sistema Operacional ou Cross-Platform como uma chave USB)  # noqa: E501

        :param authenticator_attachment: The authenticator_attachment of this FidoAuthenticatorSelectionCriteria.  # noqa: E501
        :type: str
        """

        self._authenticator_attachment = authenticator_attachment

    @property
    def user_verification(self):
        """Gets the user_verification of this FidoAuthenticatorSelectionCriteria.  # noqa: E501

        Indica o tipo de \"discoverability\" da credencial.  # noqa: E501

        :return: The user_verification of this FidoAuthenticatorSelectionCriteria.  # noqa: E501
        :rtype: str
        """
        return self._user_verification

    @user_verification.setter
    def user_verification(self, user_verification):
        """Sets the user_verification of this FidoAuthenticatorSelectionCriteria.

        Indica o tipo de \"discoverability\" da credencial.  # noqa: E501

        :param user_verification: The user_verification of this FidoAuthenticatorSelectionCriteria.  # noqa: E501
        :type: str
        """

        self._user_verification = user_verification

    @property
    def require_resident_key(self):
        """Gets the require_resident_key of this FidoAuthenticatorSelectionCriteria.  # noqa: E501

        Indica o requisito de verificação do usuário.  # noqa: E501

        :return: The require_resident_key of this FidoAuthenticatorSelectionCriteria.  # noqa: E501
        :rtype: bool
        """
        return self._require_resident_key

    @require_resident_key.setter
    def require_resident_key(self, require_resident_key):
        """Sets the require_resident_key of this FidoAuthenticatorSelectionCriteria.

        Indica o requisito de verificação do usuário.  # noqa: E501

        :param require_resident_key: The require_resident_key of this FidoAuthenticatorSelectionCriteria.  # noqa: E501
        :type: bool
        """

        self._require_resident_key = require_resident_key

    @property
    def resident_key(self):
        """Gets the resident_key of this FidoAuthenticatorSelectionCriteria.  # noqa: E501

        Indica o requisito de verificação do usuário.  # noqa: E501

        :return: The resident_key of this FidoAuthenticatorSelectionCriteria.  # noqa: E501
        :rtype: str
        """
        return self._resident_key

    @resident_key.setter
    def resident_key(self, resident_key):
        """Sets the resident_key of this FidoAuthenticatorSelectionCriteria.

        Indica o requisito de verificação do usuário.  # noqa: E501

        :param resident_key: The resident_key of this FidoAuthenticatorSelectionCriteria.  # noqa: E501
        :type: str
        """

        self._resident_key = resident_key

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
        if issubclass(FidoAuthenticatorSelectionCriteria, dict):
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
        if not isinstance(other, FidoAuthenticatorSelectionCriteria):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
