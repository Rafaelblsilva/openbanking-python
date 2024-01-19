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

class ResponseEnrollmentDataCancellation(object):
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
        'cancelled_by': 'EnrollmentsenrollmentIdDataCancellationCancelledBy',
        'reason': 'OneOfResponseEnrollmentDataCancellationReason',
        'additional_information': 'str',
        'cancelled_from': 'EnumEnrollmentCancelledFrom',
        'rejected_at': 'datetime'
    }

    attribute_map = {
        'cancelled_by': 'cancelledBy',
        'reason': 'reason',
        'additional_information': 'additionalInformation',
        'cancelled_from': 'cancelledFrom',
        'rejected_at': 'rejectedAt'
    }

    def __init__(self, cancelled_by=None, reason=None, additional_information=None, cancelled_from=None, rejected_at=None):  # noqa: E501
        """ResponseEnrollmentDataCancellation - a model defined in Swagger"""  # noqa: E501
        self._cancelled_by = None
        self._reason = None
        self._additional_information = None
        self._cancelled_from = None
        self._rejected_at = None
        self.discriminator = None
        if cancelled_by is not None:
            self.cancelled_by = cancelled_by
        self.reason = reason
        if additional_information is not None:
            self.additional_information = additional_information
        self.cancelled_from = cancelled_from
        if rejected_at is not None:
            self.rejected_at = rejected_at

    @property
    def cancelled_by(self):
        """Gets the cancelled_by of this ResponseEnrollmentDataCancellation.  # noqa: E501


        :return: The cancelled_by of this ResponseEnrollmentDataCancellation.  # noqa: E501
        :rtype: EnrollmentsenrollmentIdDataCancellationCancelledBy
        """
        return self._cancelled_by

    @cancelled_by.setter
    def cancelled_by(self, cancelled_by):
        """Sets the cancelled_by of this ResponseEnrollmentDataCancellation.


        :param cancelled_by: The cancelled_by of this ResponseEnrollmentDataCancellation.  # noqa: E501
        :type: EnrollmentsenrollmentIdDataCancellationCancelledBy
        """

        self._cancelled_by = cancelled_by

    @property
    def reason(self):
        """Gets the reason of this ResponseEnrollmentDataCancellation.  # noqa: E501


        :return: The reason of this ResponseEnrollmentDataCancellation.  # noqa: E501
        :rtype: OneOfResponseEnrollmentDataCancellationReason
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ResponseEnrollmentDataCancellation.


        :param reason: The reason of this ResponseEnrollmentDataCancellation.  # noqa: E501
        :type: OneOfResponseEnrollmentDataCancellationReason
        """
        if reason is None:
            raise ValueError("Invalid value for `reason`, must not be `None`")  # noqa: E501

        self._reason = reason

    @property
    def additional_information(self):
        """Gets the additional_information of this ResponseEnrollmentDataCancellation.  # noqa: E501


        :return: The additional_information of this ResponseEnrollmentDataCancellation.  # noqa: E501
        :rtype: str
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this ResponseEnrollmentDataCancellation.


        :param additional_information: The additional_information of this ResponseEnrollmentDataCancellation.  # noqa: E501
        :type: str
        """

        self._additional_information = additional_information

    @property
    def cancelled_from(self):
        """Gets the cancelled_from of this ResponseEnrollmentDataCancellation.  # noqa: E501


        :return: The cancelled_from of this ResponseEnrollmentDataCancellation.  # noqa: E501
        :rtype: EnumEnrollmentCancelledFrom
        """
        return self._cancelled_from

    @cancelled_from.setter
    def cancelled_from(self, cancelled_from):
        """Sets the cancelled_from of this ResponseEnrollmentDataCancellation.


        :param cancelled_from: The cancelled_from of this ResponseEnrollmentDataCancellation.  # noqa: E501
        :type: EnumEnrollmentCancelledFrom
        """
        if cancelled_from is None:
            raise ValueError("Invalid value for `cancelled_from`, must not be `None`")  # noqa: E501

        self._cancelled_from = cancelled_from

    @property
    def rejected_at(self):
        """Gets the rejected_at of this ResponseEnrollmentDataCancellation.  # noqa: E501

        Instante de rejeição do vínculo de conta no ambiente da detentora.  # noqa: E501

        :return: The rejected_at of this ResponseEnrollmentDataCancellation.  # noqa: E501
        :rtype: datetime
        """
        return self._rejected_at

    @rejected_at.setter
    def rejected_at(self, rejected_at):
        """Sets the rejected_at of this ResponseEnrollmentDataCancellation.

        Instante de rejeição do vínculo de conta no ambiente da detentora.  # noqa: E501

        :param rejected_at: The rejected_at of this ResponseEnrollmentDataCancellation.  # noqa: E501
        :type: datetime
        """

        self._rejected_at = rejected_at

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
        if issubclass(ResponseEnrollmentDataCancellation, dict):
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
        if not isinstance(other, ResponseEnrollmentDataCancellation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
