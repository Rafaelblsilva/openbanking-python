# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    Família de API para permitir o pagamento sem redirecionamento via Open Finance Brasil.   Permite tanto o gerenciamento dos dispositivos vinculados as contas quanto a autorização de consentimentos criados via fluxo sem redirecionamento.   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EnrollmentFidoSignOptionsData(object):
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
        'challenge': 'str',
        'timeout': 'int',
        'rp_id': 'str',
        'allow_credentials': 'list[FidoPublicKeyCredentialDescriptor]',
        'user_verification': 'str',
        'extensions': 'dict(str, str)'
    }

    attribute_map = {
        'challenge': 'challenge',
        'timeout': 'timeout',
        'rp_id': 'rpId',
        'allow_credentials': 'allowCredentials',
        'user_verification': 'userVerification',
        'extensions': 'extensions'
    }

    def __init__(self, challenge=None, timeout=None, rp_id=None, allow_credentials=None, user_verification=None, extensions=None):  # noqa: E501
        """EnrollmentFidoSignOptionsData - a model defined in Swagger"""  # noqa: E501
        self._challenge = None
        self._timeout = None
        self._rp_id = None
        self._allow_credentials = None
        self._user_verification = None
        self._extensions = None
        self.discriminator = None
        self.challenge = challenge
        if timeout is not None:
            self.timeout = timeout
        if rp_id is not None:
            self.rp_id = rp_id
        if allow_credentials is not None:
            self.allow_credentials = allow_credentials
        if user_verification is not None:
            self.user_verification = user_verification
        if extensions is not None:
            self.extensions = extensions

    @property
    def challenge(self):
        """Gets the challenge of this EnrollmentFidoSignOptionsData.  # noqa: E501

        Sequência de bytes aleatórios gerados pelo servidor FIDO2, codificados em base64.  # noqa: E501

        :return: The challenge of this EnrollmentFidoSignOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this EnrollmentFidoSignOptionsData.

        Sequência de bytes aleatórios gerados pelo servidor FIDO2, codificados em base64.  # noqa: E501

        :param challenge: The challenge of this EnrollmentFidoSignOptionsData.  # noqa: E501
        :type: str
        """
        if challenge is None:
            raise ValueError("Invalid value for `challenge`, must not be `None`")  # noqa: E501

        self._challenge = challenge

    @property
    def timeout(self):
        """Gets the timeout of this EnrollmentFidoSignOptionsData.  # noqa: E501

        Expiração, em milissegundos, do challenge.  # noqa: E501

        :return: The timeout of this EnrollmentFidoSignOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this EnrollmentFidoSignOptionsData.

        Expiração, em milissegundos, do challenge.  # noqa: E501

        :param timeout: The timeout of this EnrollmentFidoSignOptionsData.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def rp_id(self):
        """Gets the rp_id of this EnrollmentFidoSignOptionsData.  # noqa: E501

        Identificador da Relying Party.  # noqa: E501

        :return: The rp_id of this EnrollmentFidoSignOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._rp_id

    @rp_id.setter
    def rp_id(self, rp_id):
        """Sets the rp_id of this EnrollmentFidoSignOptionsData.

        Identificador da Relying Party.  # noqa: E501

        :param rp_id: The rp_id of this EnrollmentFidoSignOptionsData.  # noqa: E501
        :type: str
        """

        self._rp_id = rp_id

    @property
    def allow_credentials(self):
        """Gets the allow_credentials of this EnrollmentFidoSignOptionsData.  # noqa: E501


        :return: The allow_credentials of this EnrollmentFidoSignOptionsData.  # noqa: E501
        :rtype: list[FidoPublicKeyCredentialDescriptor]
        """
        return self._allow_credentials

    @allow_credentials.setter
    def allow_credentials(self, allow_credentials):
        """Sets the allow_credentials of this EnrollmentFidoSignOptionsData.


        :param allow_credentials: The allow_credentials of this EnrollmentFidoSignOptionsData.  # noqa: E501
        :type: list[FidoPublicKeyCredentialDescriptor]
        """

        self._allow_credentials = allow_credentials

    @property
    def user_verification(self):
        """Gets the user_verification of this EnrollmentFidoSignOptionsData.  # noqa: E501


        :return: The user_verification of this EnrollmentFidoSignOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._user_verification

    @user_verification.setter
    def user_verification(self, user_verification):
        """Sets the user_verification of this EnrollmentFidoSignOptionsData.


        :param user_verification: The user_verification of this EnrollmentFidoSignOptionsData.  # noqa: E501
        :type: str
        """

        self._user_verification = user_verification

    @property
    def extensions(self):
        """Gets the extensions of this EnrollmentFidoSignOptionsData.  # noqa: E501

        Campo de extensão com opções que variam por plataforma.  # noqa: E501

        :return: The extensions of this EnrollmentFidoSignOptionsData.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this EnrollmentFidoSignOptionsData.

        Campo de extensão com opções que variam por plataforma.  # noqa: E501

        :param extensions: The extensions of this EnrollmentFidoSignOptionsData.  # noqa: E501
        :type: dict(str, str)
        """

        self._extensions = extensions

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
        if issubclass(EnrollmentFidoSignOptionsData, dict):
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
        if not isinstance(other, EnrollmentFidoSignOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
