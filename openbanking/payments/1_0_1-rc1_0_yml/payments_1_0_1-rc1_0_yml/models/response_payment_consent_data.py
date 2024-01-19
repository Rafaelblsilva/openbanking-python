# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora  de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:   - Certificados exigidos para assinatura de mensagens:   [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Como assinar o payload JWS: [https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload](https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload)  ## Controle de acesso    O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).    Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.       # noqa: E501

    OpenAPI spec version: 1.0.1-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponsePaymentConsentData(object):
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
        'consent_id': 'str',
        'creation_date_time': 'datetime',
        'expiration_date_time': 'datetime',
        'status_update_date_time': 'datetime',
        'status': 'EnumAuthorisationStatusType',
        'logged_user': 'LoggedUser',
        'business_entity': 'BusinessEntity',
        'creditor': 'Identification',
        'payment': 'PaymentConsent',
        'debtor_account': 'DebtorAccount'
    }

    attribute_map = {
        'consent_id': 'consentId',
        'creation_date_time': 'creationDateTime',
        'expiration_date_time': 'expirationDateTime',
        'status_update_date_time': 'statusUpdateDateTime',
        'status': 'status',
        'logged_user': 'loggedUser',
        'business_entity': 'businessEntity',
        'creditor': 'creditor',
        'payment': 'payment',
        'debtor_account': 'debtorAccount'
    }

    def __init__(self, consent_id=None, creation_date_time=None, expiration_date_time=None, status_update_date_time=None, status=None, logged_user=None, business_entity=None, creditor=None, payment=None, debtor_account=None):  # noqa: E501
        """ResponsePaymentConsentData - a model defined in Swagger"""  # noqa: E501
        self._consent_id = None
        self._creation_date_time = None
        self._expiration_date_time = None
        self._status_update_date_time = None
        self._status = None
        self._logged_user = None
        self._business_entity = None
        self._creditor = None
        self._payment = None
        self._debtor_account = None
        self.discriminator = None
        self.consent_id = consent_id
        self.creation_date_time = creation_date_time
        self.expiration_date_time = expiration_date_time
        self.status_update_date_time = status_update_date_time
        self.status = status
        self.logged_user = logged_user
        if business_entity is not None:
            self.business_entity = business_entity
        self.creditor = creditor
        self.payment = payment
        if debtor_account is not None:
            self.debtor_account = debtor_account

    @property
    def consent_id(self):
        """Gets the consent_id of this ResponsePaymentConsentData.  # noqa: E501

        Identificador único do consentimento criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).   # noqa: E501

        :return: The consent_id of this ResponsePaymentConsentData.  # noqa: E501
        :rtype: str
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this ResponsePaymentConsentData.

        Identificador único do consentimento criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).   # noqa: E501

        :param consent_id: The consent_id of this ResponsePaymentConsentData.  # noqa: E501
        :type: str
        """
        if consent_id is None:
            raise ValueError("Invalid value for `consent_id`, must not be `None`")  # noqa: E501

        self._consent_id = consent_id

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this ResponsePaymentConsentData.  # noqa: E501

        Data e hora em que o consentimento foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :return: The creation_date_time of this ResponsePaymentConsentData.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this ResponsePaymentConsentData.

        Data e hora em que o consentimento foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :param creation_date_time: The creation_date_time of this ResponsePaymentConsentData.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def expiration_date_time(self):
        """Gets the expiration_date_time of this ResponsePaymentConsentData.  # noqa: E501

        Data e hora em que o consentimento da iniciação de pagamento expira, devendo ser sempre o creationDateTime mais 5 minutos. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC (UTC time format). O consentimento é criado com o status AWAITING_AUTHORISATION, e deve assumir o status AUTHORIZED ou REJECTED antes do tempo de expiração - 5 minutos. Caso o tempo seja expirado, o status deve assumir REJECTED. Para o cenário em que o status assumiu AUTHORISED, o tempo máximo do expirationDateTime do consentimento deve assumir \"now + 60 minutos\". Este é o tempo para consumir o consentimento autorizado, mudando seu status para CONSUMED. Não é possível prorrogar este tempo e a criação de um novo consentimento será necessária para os cenários de insucesso. O tempo do expirationDateTime é garantido com os 15 minutos do access token, sendo possível utilizar mais três refresh tokens até totalizar 60 minutos.   # noqa: E501

        :return: The expiration_date_time of this ResponsePaymentConsentData.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date_time

    @expiration_date_time.setter
    def expiration_date_time(self, expiration_date_time):
        """Sets the expiration_date_time of this ResponsePaymentConsentData.

        Data e hora em que o consentimento da iniciação de pagamento expira, devendo ser sempre o creationDateTime mais 5 minutos. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC (UTC time format). O consentimento é criado com o status AWAITING_AUTHORISATION, e deve assumir o status AUTHORIZED ou REJECTED antes do tempo de expiração - 5 minutos. Caso o tempo seja expirado, o status deve assumir REJECTED. Para o cenário em que o status assumiu AUTHORISED, o tempo máximo do expirationDateTime do consentimento deve assumir \"now + 60 minutos\". Este é o tempo para consumir o consentimento autorizado, mudando seu status para CONSUMED. Não é possível prorrogar este tempo e a criação de um novo consentimento será necessária para os cenários de insucesso. O tempo do expirationDateTime é garantido com os 15 minutos do access token, sendo possível utilizar mais três refresh tokens até totalizar 60 minutos.   # noqa: E501

        :param expiration_date_time: The expiration_date_time of this ResponsePaymentConsentData.  # noqa: E501
        :type: datetime
        """
        if expiration_date_time is None:
            raise ValueError("Invalid value for `expiration_date_time`, must not be `None`")  # noqa: E501

        self._expiration_date_time = expiration_date_time

    @property
    def status_update_date_time(self):
        """Gets the status_update_date_time of this ResponsePaymentConsentData.  # noqa: E501

        Data e hora em que o recurso foi atualizado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :return: The status_update_date_time of this ResponsePaymentConsentData.  # noqa: E501
        :rtype: datetime
        """
        return self._status_update_date_time

    @status_update_date_time.setter
    def status_update_date_time(self, status_update_date_time):
        """Sets the status_update_date_time of this ResponsePaymentConsentData.

        Data e hora em que o recurso foi atualizado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :param status_update_date_time: The status_update_date_time of this ResponsePaymentConsentData.  # noqa: E501
        :type: datetime
        """
        if status_update_date_time is None:
            raise ValueError("Invalid value for `status_update_date_time`, must not be `None`")  # noqa: E501

        self._status_update_date_time = status_update_date_time

    @property
    def status(self):
        """Gets the status of this ResponsePaymentConsentData.  # noqa: E501


        :return: The status of this ResponsePaymentConsentData.  # noqa: E501
        :rtype: EnumAuthorisationStatusType
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponsePaymentConsentData.


        :param status: The status of this ResponsePaymentConsentData.  # noqa: E501
        :type: EnumAuthorisationStatusType
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def logged_user(self):
        """Gets the logged_user of this ResponsePaymentConsentData.  # noqa: E501


        :return: The logged_user of this ResponsePaymentConsentData.  # noqa: E501
        :rtype: LoggedUser
        """
        return self._logged_user

    @logged_user.setter
    def logged_user(self, logged_user):
        """Sets the logged_user of this ResponsePaymentConsentData.


        :param logged_user: The logged_user of this ResponsePaymentConsentData.  # noqa: E501
        :type: LoggedUser
        """
        if logged_user is None:
            raise ValueError("Invalid value for `logged_user`, must not be `None`")  # noqa: E501

        self._logged_user = logged_user

    @property
    def business_entity(self):
        """Gets the business_entity of this ResponsePaymentConsentData.  # noqa: E501


        :return: The business_entity of this ResponsePaymentConsentData.  # noqa: E501
        :rtype: BusinessEntity
        """
        return self._business_entity

    @business_entity.setter
    def business_entity(self, business_entity):
        """Sets the business_entity of this ResponsePaymentConsentData.


        :param business_entity: The business_entity of this ResponsePaymentConsentData.  # noqa: E501
        :type: BusinessEntity
        """

        self._business_entity = business_entity

    @property
    def creditor(self):
        """Gets the creditor of this ResponsePaymentConsentData.  # noqa: E501


        :return: The creditor of this ResponsePaymentConsentData.  # noqa: E501
        :rtype: Identification
        """
        return self._creditor

    @creditor.setter
    def creditor(self, creditor):
        """Sets the creditor of this ResponsePaymentConsentData.


        :param creditor: The creditor of this ResponsePaymentConsentData.  # noqa: E501
        :type: Identification
        """
        if creditor is None:
            raise ValueError("Invalid value for `creditor`, must not be `None`")  # noqa: E501

        self._creditor = creditor

    @property
    def payment(self):
        """Gets the payment of this ResponsePaymentConsentData.  # noqa: E501


        :return: The payment of this ResponsePaymentConsentData.  # noqa: E501
        :rtype: PaymentConsent
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this ResponsePaymentConsentData.


        :param payment: The payment of this ResponsePaymentConsentData.  # noqa: E501
        :type: PaymentConsent
        """
        if payment is None:
            raise ValueError("Invalid value for `payment`, must not be `None`")  # noqa: E501

        self._payment = payment

    @property
    def debtor_account(self):
        """Gets the debtor_account of this ResponsePaymentConsentData.  # noqa: E501


        :return: The debtor_account of this ResponsePaymentConsentData.  # noqa: E501
        :rtype: DebtorAccount
        """
        return self._debtor_account

    @debtor_account.setter
    def debtor_account(self, debtor_account):
        """Sets the debtor_account of this ResponsePaymentConsentData.


        :param debtor_account: The debtor_account of this ResponsePaymentConsentData.  # noqa: E501
        :type: DebtorAccount
        """

        self._debtor_account = debtor_account

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
        if issubclass(ResponsePaymentConsentData, dict):
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
        if not isinstance(other, ResponsePaymentConsentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
