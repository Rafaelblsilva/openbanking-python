# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    Família de API para permitir o pagamento sem redirecionamento via Open Finance Brasil.   Permite tanto o gerenciamento dos dispositivos vinculados as contas quanto a autorização de consentimentos criados via fluxo sem redirecionamento.   # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseEnrollmentData(object):
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
        'creation_date_time': 'datetime',
        'status': 'EnumEnrollmentStatus',
        'status_update_date_time': 'datetime',
        'permissions': 'list[EnumEnrollmentPermission]',
        'expiration_date_time': 'datetime',
        'logged_user': 'LoggedUser',
        'business_entity': 'BusinessEntity',
        'debtor_account': 'AllOfResponseEnrollmentDataDebtorAccount',
        'cancellation': 'ResponseEnrollmentDataCancellation',
        'transaction_limit': 'str',
        'daily_limit': 'str'
    }

    attribute_map = {
        'enrollment_id': 'enrollmentId',
        'creation_date_time': 'creationDateTime',
        'status': 'status',
        'status_update_date_time': 'statusUpdateDateTime',
        'permissions': 'permissions',
        'expiration_date_time': 'expirationDateTime',
        'logged_user': 'loggedUser',
        'business_entity': 'businessEntity',
        'debtor_account': 'debtorAccount',
        'cancellation': 'cancellation',
        'transaction_limit': 'transactionLimit',
        'daily_limit': 'dailyLimit'
    }

    def __init__(self, enrollment_id=None, creation_date_time=None, status=None, status_update_date_time=None, permissions=None, expiration_date_time=None, logged_user=None, business_entity=None, debtor_account=None, cancellation=None, transaction_limit=None, daily_limit=None):  # noqa: E501
        """ResponseEnrollmentData - a model defined in Swagger"""  # noqa: E501
        self._enrollment_id = None
        self._creation_date_time = None
        self._status = None
        self._status_update_date_time = None
        self._permissions = None
        self._expiration_date_time = None
        self._logged_user = None
        self._business_entity = None
        self._debtor_account = None
        self._cancellation = None
        self._transaction_limit = None
        self._daily_limit = None
        self.discriminator = None
        self.enrollment_id = enrollment_id
        self.creation_date_time = creation_date_time
        self.status = status
        self.status_update_date_time = status_update_date_time
        self.permissions = permissions
        self.expiration_date_time = expiration_date_time
        self.logged_user = logged_user
        if business_entity is not None:
            self.business_entity = business_entity
        if debtor_account is not None:
            self.debtor_account = debtor_account
        if cancellation is not None:
            self.cancellation = cancellation
        if transaction_limit is not None:
            self.transaction_limit = transaction_limit
        if daily_limit is not None:
            self.daily_limit = daily_limit

    @property
    def enrollment_id(self):
        """Gets the enrollment_id of this ResponseEnrollmentData.  # noqa: E501


        :return: The enrollment_id of this ResponseEnrollmentData.  # noqa: E501
        :rtype: EnrollmentId
        """
        return self._enrollment_id

    @enrollment_id.setter
    def enrollment_id(self, enrollment_id):
        """Sets the enrollment_id of this ResponseEnrollmentData.


        :param enrollment_id: The enrollment_id of this ResponseEnrollmentData.  # noqa: E501
        :type: EnrollmentId
        """
        if enrollment_id is None:
            raise ValueError("Invalid value for `enrollment_id`, must not be `None`")  # noqa: E501

        self._enrollment_id = enrollment_id

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this ResponseEnrollmentData.  # noqa: E501

        O instante em que o vínculo de conta foi criado no ambiente da detentora.  # noqa: E501

        :return: The creation_date_time of this ResponseEnrollmentData.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this ResponseEnrollmentData.

        O instante em que o vínculo de conta foi criado no ambiente da detentora.  # noqa: E501

        :param creation_date_time: The creation_date_time of this ResponseEnrollmentData.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def status(self):
        """Gets the status of this ResponseEnrollmentData.  # noqa: E501


        :return: The status of this ResponseEnrollmentData.  # noqa: E501
        :rtype: EnumEnrollmentStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseEnrollmentData.


        :param status: The status of this ResponseEnrollmentData.  # noqa: E501
        :type: EnumEnrollmentStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def status_update_date_time(self):
        """Gets the status_update_date_time of this ResponseEnrollmentData.  # noqa: E501

        O instante em que ocorreu a última alteração de status do vínculo de conta.  # noqa: E501

        :return: The status_update_date_time of this ResponseEnrollmentData.  # noqa: E501
        :rtype: datetime
        """
        return self._status_update_date_time

    @status_update_date_time.setter
    def status_update_date_time(self, status_update_date_time):
        """Sets the status_update_date_time of this ResponseEnrollmentData.

        O instante em que ocorreu a última alteração de status do vínculo de conta.  # noqa: E501

        :param status_update_date_time: The status_update_date_time of this ResponseEnrollmentData.  # noqa: E501
        :type: datetime
        """
        if status_update_date_time is None:
            raise ValueError("Invalid value for `status_update_date_time`, must not be `None`")  # noqa: E501

        self._status_update_date_time = status_update_date_time

    @property
    def permissions(self):
        """Gets the permissions of this ResponseEnrollmentData.  # noqa: E501


        :return: The permissions of this ResponseEnrollmentData.  # noqa: E501
        :rtype: list[EnumEnrollmentPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ResponseEnrollmentData.


        :param permissions: The permissions of this ResponseEnrollmentData.  # noqa: E501
        :type: list[EnumEnrollmentPermission]
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def expiration_date_time(self):
        """Gets the expiration_date_time of this ResponseEnrollmentData.  # noqa: E501

        O instante de expiração deste vínculo de conta, de acordo com a regulação vigente.  # noqa: E501

        :return: The expiration_date_time of this ResponseEnrollmentData.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date_time

    @expiration_date_time.setter
    def expiration_date_time(self, expiration_date_time):
        """Sets the expiration_date_time of this ResponseEnrollmentData.

        O instante de expiração deste vínculo de conta, de acordo com a regulação vigente.  # noqa: E501

        :param expiration_date_time: The expiration_date_time of this ResponseEnrollmentData.  # noqa: E501
        :type: datetime
        """
        if expiration_date_time is None:
            raise ValueError("Invalid value for `expiration_date_time`, must not be `None`")  # noqa: E501

        self._expiration_date_time = expiration_date_time

    @property
    def logged_user(self):
        """Gets the logged_user of this ResponseEnrollmentData.  # noqa: E501


        :return: The logged_user of this ResponseEnrollmentData.  # noqa: E501
        :rtype: LoggedUser
        """
        return self._logged_user

    @logged_user.setter
    def logged_user(self, logged_user):
        """Sets the logged_user of this ResponseEnrollmentData.


        :param logged_user: The logged_user of this ResponseEnrollmentData.  # noqa: E501
        :type: LoggedUser
        """
        if logged_user is None:
            raise ValueError("Invalid value for `logged_user`, must not be `None`")  # noqa: E501

        self._logged_user = logged_user

    @property
    def business_entity(self):
        """Gets the business_entity of this ResponseEnrollmentData.  # noqa: E501


        :return: The business_entity of this ResponseEnrollmentData.  # noqa: E501
        :rtype: BusinessEntity
        """
        return self._business_entity

    @business_entity.setter
    def business_entity(self, business_entity):
        """Sets the business_entity of this ResponseEnrollmentData.


        :param business_entity: The business_entity of this ResponseEnrollmentData.  # noqa: E501
        :type: BusinessEntity
        """

        self._business_entity = business_entity

    @property
    def debtor_account(self):
        """Gets the debtor_account of this ResponseEnrollmentData.  # noqa: E501


        :return: The debtor_account of this ResponseEnrollmentData.  # noqa: E501
        :rtype: AllOfResponseEnrollmentDataDebtorAccount
        """
        return self._debtor_account

    @debtor_account.setter
    def debtor_account(self, debtor_account):
        """Sets the debtor_account of this ResponseEnrollmentData.


        :param debtor_account: The debtor_account of this ResponseEnrollmentData.  # noqa: E501
        :type: AllOfResponseEnrollmentDataDebtorAccount
        """

        self._debtor_account = debtor_account

    @property
    def cancellation(self):
        """Gets the cancellation of this ResponseEnrollmentData.  # noqa: E501


        :return: The cancellation of this ResponseEnrollmentData.  # noqa: E501
        :rtype: ResponseEnrollmentDataCancellation
        """
        return self._cancellation

    @cancellation.setter
    def cancellation(self, cancellation):
        """Sets the cancellation of this ResponseEnrollmentData.


        :param cancellation: The cancellation of this ResponseEnrollmentData.  # noqa: E501
        :type: ResponseEnrollmentDataCancellation
        """

        self._cancellation = cancellation

    @property
    def transaction_limit(self):
        """Gets the transaction_limit of this ResponseEnrollmentData.  # noqa: E501

        Valor máximo, por transação, admitido para este vínculo de conta. Este limite não garante a autorização de iniciações de pagamento; servindo como referência para a iniciadora evitar a criação de consentimentos de valores tais que, garantidamente, não serão autorizados.  [Restrição] Campo de preenchimento obrigatório pelos participantes quando o campo `status` for preenchido com os valores `AUTHORISED` ou `AWAITING_ENROLLMENT`.   # noqa: E501

        :return: The transaction_limit of this ResponseEnrollmentData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_limit

    @transaction_limit.setter
    def transaction_limit(self, transaction_limit):
        """Sets the transaction_limit of this ResponseEnrollmentData.

        Valor máximo, por transação, admitido para este vínculo de conta. Este limite não garante a autorização de iniciações de pagamento; servindo como referência para a iniciadora evitar a criação de consentimentos de valores tais que, garantidamente, não serão autorizados.  [Restrição] Campo de preenchimento obrigatório pelos participantes quando o campo `status` for preenchido com os valores `AUTHORISED` ou `AWAITING_ENROLLMENT`.   # noqa: E501

        :param transaction_limit: The transaction_limit of this ResponseEnrollmentData.  # noqa: E501
        :type: str
        """

        self._transaction_limit = transaction_limit

    @property
    def daily_limit(self):
        """Gets the daily_limit of this ResponseEnrollmentData.  # noqa: E501

        Limite diário cumulativo para este vínculo de conta. Este limite não garante a autorização de iniciações de pagamento; servindo como referência para a iniciadora evitar a criação de consentimentos para valores tais que, garantidamente, não serão autorizados.  [Restrição] Campo de preenchimento obrigatório pelos participantes quando o campo `status` for preenchido com os valores `AUTHORISED` ou `AWAITING_ENROLLMENT`.   # noqa: E501

        :return: The daily_limit of this ResponseEnrollmentData.  # noqa: E501
        :rtype: str
        """
        return self._daily_limit

    @daily_limit.setter
    def daily_limit(self, daily_limit):
        """Sets the daily_limit of this ResponseEnrollmentData.

        Limite diário cumulativo para este vínculo de conta. Este limite não garante a autorização de iniciações de pagamento; servindo como referência para a iniciadora evitar a criação de consentimentos para valores tais que, garantidamente, não serão autorizados.  [Restrição] Campo de preenchimento obrigatório pelos participantes quando o campo `status` for preenchido com os valores `AUTHORISED` ou `AWAITING_ENROLLMENT`.   # noqa: E501

        :param daily_limit: The daily_limit of this ResponseEnrollmentData.  # noqa: E501
        :type: str
        """

        self._daily_limit = daily_limit

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
        if issubclass(ResponseEnrollmentData, dict):
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
        if not isinstance(other, ResponseEnrollmentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
