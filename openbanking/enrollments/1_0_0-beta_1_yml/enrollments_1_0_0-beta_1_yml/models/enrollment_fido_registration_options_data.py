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

class EnrollmentFidoRegistrationOptionsData(object):
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
        'enrollment_id': 'EnrollmentId',
        'rp': 'FidoRelyingParty',
        'user': 'FidoUser',
        'challenge': 'str',
        'pub_key_cred_params': 'list[FidoPublicKeyCredentialCreationOptions]',
        'timeout': 'int',
        'exclude_credentials': 'list[FidoPublicKeyCredentialDescriptor]',
        'authenticator_selection': 'FidoAuthenticatorSelectionCriteria',
        'attestation': 'str',
        'attestation_formats': 'list[str]',
        'extensions': 'dict(str, str)'
    }

    attribute_map = {
        'enrollment_id': 'enrollmentId',
        'rp': 'rp',
        'user': 'user',
        'challenge': 'challenge',
        'pub_key_cred_params': 'pubKeyCredParams',
        'timeout': 'timeout',
        'exclude_credentials': 'excludeCredentials',
        'authenticator_selection': 'authenticatorSelection',
        'attestation': 'attestation',
        'attestation_formats': 'attestationFormats',
        'extensions': 'extensions'
    }

    def __init__(self, enrollment_id=None, rp=None, user=None, challenge=None, pub_key_cred_params=None, timeout=None, exclude_credentials=None, authenticator_selection=None, attestation=None, attestation_formats=None, extensions=None):  # noqa: E501
        """EnrollmentFidoRegistrationOptionsData - a model defined in Swagger"""  # noqa: E501
        self._enrollment_id = None
        self._rp = None
        self._user = None
        self._challenge = None
        self._pub_key_cred_params = None
        self._timeout = None
        self._exclude_credentials = None
        self._authenticator_selection = None
        self._attestation = None
        self._attestation_formats = None
        self._extensions = None
        self.discriminator = None
        self.enrollment_id = enrollment_id
        self.rp = rp
        self.user = user
        self.challenge = challenge
        self.pub_key_cred_params = pub_key_cred_params
        if timeout is not None:
            self.timeout = timeout
        if exclude_credentials is not None:
            self.exclude_credentials = exclude_credentials
        if authenticator_selection is not None:
            self.authenticator_selection = authenticator_selection
        if attestation is not None:
            self.attestation = attestation
        if attestation_formats is not None:
            self.attestation_formats = attestation_formats
        if extensions is not None:
            self.extensions = extensions

    @property
    def enrollment_id(self):
        """Gets the enrollment_id of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501


        :return: The enrollment_id of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :rtype: EnrollmentId
        """
        return self._enrollment_id

    @enrollment_id.setter
    def enrollment_id(self, enrollment_id):
        """Sets the enrollment_id of this EnrollmentFidoRegistrationOptionsData.


        :param enrollment_id: The enrollment_id of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :type: EnrollmentId
        """
        if enrollment_id is None:
            raise ValueError("Invalid value for `enrollment_id`, must not be `None`")  # noqa: E501

        self._enrollment_id = enrollment_id

    @property
    def rp(self):
        """Gets the rp of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501


        :return: The rp of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :rtype: FidoRelyingParty
        """
        return self._rp

    @rp.setter
    def rp(self, rp):
        """Sets the rp of this EnrollmentFidoRegistrationOptionsData.


        :param rp: The rp of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :type: FidoRelyingParty
        """
        if rp is None:
            raise ValueError("Invalid value for `rp`, must not be `None`")  # noqa: E501

        self._rp = rp

    @property
    def user(self):
        """Gets the user of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501


        :return: The user of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :rtype: FidoUser
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this EnrollmentFidoRegistrationOptionsData.


        :param user: The user of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :type: FidoUser
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def challenge(self):
        """Gets the challenge of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501

        Sequência de bytes aleatórios gerados pelo servidor FIDO2, codificados em base64.  # noqa: E501

        :return: The challenge of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this EnrollmentFidoRegistrationOptionsData.

        Sequência de bytes aleatórios gerados pelo servidor FIDO2, codificados em base64.  # noqa: E501

        :param challenge: The challenge of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :type: str
        """
        if challenge is None:
            raise ValueError("Invalid value for `challenge`, must not be `None`")  # noqa: E501

        self._challenge = challenge

    @property
    def pub_key_cred_params(self):
        """Gets the pub_key_cred_params of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501


        :return: The pub_key_cred_params of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :rtype: list[FidoPublicKeyCredentialCreationOptions]
        """
        return self._pub_key_cred_params

    @pub_key_cred_params.setter
    def pub_key_cred_params(self, pub_key_cred_params):
        """Sets the pub_key_cred_params of this EnrollmentFidoRegistrationOptionsData.


        :param pub_key_cred_params: The pub_key_cred_params of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :type: list[FidoPublicKeyCredentialCreationOptions]
        """
        if pub_key_cred_params is None:
            raise ValueError("Invalid value for `pub_key_cred_params`, must not be `None`")  # noqa: E501

        self._pub_key_cred_params = pub_key_cred_params

    @property
    def timeout(self):
        """Gets the timeout of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501

        Timeout, em milissegundos, para registro da credencial FIDO2.  # noqa: E501

        :return: The timeout of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this EnrollmentFidoRegistrationOptionsData.

        Timeout, em milissegundos, para registro da credencial FIDO2.  # noqa: E501

        :param timeout: The timeout of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    @property
    def exclude_credentials(self):
        """Gets the exclude_credentials of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501


        :return: The exclude_credentials of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :rtype: list[FidoPublicKeyCredentialDescriptor]
        """
        return self._exclude_credentials

    @exclude_credentials.setter
    def exclude_credentials(self, exclude_credentials):
        """Sets the exclude_credentials of this EnrollmentFidoRegistrationOptionsData.


        :param exclude_credentials: The exclude_credentials of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :type: list[FidoPublicKeyCredentialDescriptor]
        """

        self._exclude_credentials = exclude_credentials

    @property
    def authenticator_selection(self):
        """Gets the authenticator_selection of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501


        :return: The authenticator_selection of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :rtype: FidoAuthenticatorSelectionCriteria
        """
        return self._authenticator_selection

    @authenticator_selection.setter
    def authenticator_selection(self, authenticator_selection):
        """Sets the authenticator_selection of this EnrollmentFidoRegistrationOptionsData.


        :param authenticator_selection: The authenticator_selection of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :type: FidoAuthenticatorSelectionCriteria
        """

        self._authenticator_selection = authenticator_selection

    @property
    def attestation(self):
        """Gets the attestation of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501

        Indica o tipo de attestation que o autenticador pode utilizar.  # noqa: E501

        :return: The attestation of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :rtype: str
        """
        return self._attestation

    @attestation.setter
    def attestation(self, attestation):
        """Sets the attestation of this EnrollmentFidoRegistrationOptionsData.

        Indica o tipo de attestation que o autenticador pode utilizar.  # noqa: E501

        :param attestation: The attestation of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :type: str
        """

        self._attestation = attestation

    @property
    def attestation_formats(self):
        """Gets the attestation_formats of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501

        Indica as preferências de formato sobre o campo attestation.  # noqa: E501

        :return: The attestation_formats of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :rtype: list[str]
        """
        return self._attestation_formats

    @attestation_formats.setter
    def attestation_formats(self, attestation_formats):
        """Sets the attestation_formats of this EnrollmentFidoRegistrationOptionsData.

        Indica as preferências de formato sobre o campo attestation.  # noqa: E501

        :param attestation_formats: The attestation_formats of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :type: list[str]
        """

        self._attestation_formats = attestation_formats

    @property
    def extensions(self):
        """Gets the extensions of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501

        Campo de extensão com opções que variam por plataforma.  # noqa: E501

        :return: The extensions of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._extensions

    @extensions.setter
    def extensions(self, extensions):
        """Sets the extensions of this EnrollmentFidoRegistrationOptionsData.

        Campo de extensão com opções que variam por plataforma.  # noqa: E501

        :param extensions: The extensions of this EnrollmentFidoRegistrationOptionsData.  # noqa: E501
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
        if issubclass(EnrollmentFidoRegistrationOptionsData, dict):
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
        if not isinstance(other, EnrollmentFidoRegistrationOptionsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
