# coding: utf-8

"""
    Participantes Open Finance Brasil

    Informações sobre os participantes do Open Finance Brasil que estão registrados no Diretório.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EssSignRequest(object):
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
        'tn_cid': 'TnCId',
        'no_of_signers': 'int'
    }

    attribute_map = {
        'tn_cid': 'TnCId',
        'no_of_signers': 'NoOfSigners'
    }

    def __init__(self, tn_cid=None, no_of_signers=None):  # noqa: E501
        """EssSignRequest - a model defined in Swagger"""  # noqa: E501
        self._tn_cid = None
        self._no_of_signers = None
        self.discriminator = None
        if tn_cid is not None:
            self.tn_cid = tn_cid
        if no_of_signers is not None:
            self.no_of_signers = no_of_signers

    @property
    def tn_cid(self):
        """Gets the tn_cid of this EssSignRequest.  # noqa: E501


        :return: The tn_cid of this EssSignRequest.  # noqa: E501
        :rtype: TnCId
        """
        return self._tn_cid

    @tn_cid.setter
    def tn_cid(self, tn_cid):
        """Sets the tn_cid of this EssSignRequest.


        :param tn_cid: The tn_cid of this EssSignRequest.  # noqa: E501
        :type: TnCId
        """

        self._tn_cid = tn_cid

    @property
    def no_of_signers(self):
        """Gets the no_of_signers of this EssSignRequest.  # noqa: E501


        :return: The no_of_signers of this EssSignRequest.  # noqa: E501
        :rtype: int
        """
        return self._no_of_signers

    @no_of_signers.setter
    def no_of_signers(self, no_of_signers):
        """Sets the no_of_signers of this EssSignRequest.


        :param no_of_signers: The no_of_signers of this EssSignRequest.  # noqa: E501
        :type: int
        """

        self._no_of_signers = no_of_signers

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
        if issubclass(EssSignRequest, dict):
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
        if not isinstance(other, EssSignRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
