# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    API de Dispositivo Vínculado para suportar Iniciação de Pagamentos na Jornada Sem Redirecionamento do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc.2
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreateEnrollmentData(object):
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
        'logged_user': 'LoggedUser',
        'permissions': 'list[EnumEnrollmentPermission]',
        'business_entity': 'BusinessEntity',
        'debtor_account': 'DebtorAccount'
    }

    attribute_map = {
        'logged_user': 'loggedUser',
        'permissions': 'permissions',
        'business_entity': 'businessEntity',
        'debtor_account': 'debtorAccount'
    }

    def __init__(self, logged_user=None, permissions=None, business_entity=None, debtor_account=None):  # noqa: E501
        """CreateEnrollmentData - a model defined in Swagger"""  # noqa: E501
        self._logged_user = None
        self._permissions = None
        self._business_entity = None
        self._debtor_account = None
        self.discriminator = None
        self.logged_user = logged_user
        self.permissions = permissions
        if business_entity is not None:
            self.business_entity = business_entity
        if debtor_account is not None:
            self.debtor_account = debtor_account

    @property
    def logged_user(self):
        """Gets the logged_user of this CreateEnrollmentData.  # noqa: E501


        :return: The logged_user of this CreateEnrollmentData.  # noqa: E501
        :rtype: LoggedUser
        """
        return self._logged_user

    @logged_user.setter
    def logged_user(self, logged_user):
        """Sets the logged_user of this CreateEnrollmentData.


        :param logged_user: The logged_user of this CreateEnrollmentData.  # noqa: E501
        :type: LoggedUser
        """
        if logged_user is None:
            raise ValueError("Invalid value for `logged_user`, must not be `None`")  # noqa: E501

        self._logged_user = logged_user

    @property
    def permissions(self):
        """Gets the permissions of this CreateEnrollmentData.  # noqa: E501


        :return: The permissions of this CreateEnrollmentData.  # noqa: E501
        :rtype: list[EnumEnrollmentPermission]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this CreateEnrollmentData.


        :param permissions: The permissions of this CreateEnrollmentData.  # noqa: E501
        :type: list[EnumEnrollmentPermission]
        """
        if permissions is None:
            raise ValueError("Invalid value for `permissions`, must not be `None`")  # noqa: E501

        self._permissions = permissions

    @property
    def business_entity(self):
        """Gets the business_entity of this CreateEnrollmentData.  # noqa: E501


        :return: The business_entity of this CreateEnrollmentData.  # noqa: E501
        :rtype: BusinessEntity
        """
        return self._business_entity

    @business_entity.setter
    def business_entity(self, business_entity):
        """Sets the business_entity of this CreateEnrollmentData.


        :param business_entity: The business_entity of this CreateEnrollmentData.  # noqa: E501
        :type: BusinessEntity
        """

        self._business_entity = business_entity

    @property
    def debtor_account(self):
        """Gets the debtor_account of this CreateEnrollmentData.  # noqa: E501


        :return: The debtor_account of this CreateEnrollmentData.  # noqa: E501
        :rtype: DebtorAccount
        """
        return self._debtor_account

    @debtor_account.setter
    def debtor_account(self, debtor_account):
        """Sets the debtor_account of this CreateEnrollmentData.


        :param debtor_account: The debtor_account of this CreateEnrollmentData.  # noqa: E501
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
        if issubclass(CreateEnrollmentData, dict):
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
        if not isinstance(other, CreateEnrollmentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other