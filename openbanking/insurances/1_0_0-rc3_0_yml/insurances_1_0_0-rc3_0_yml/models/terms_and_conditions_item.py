# coding: utf-8

"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc3.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TermsAndConditionsItem(object):
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
        'susep_process_number': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'susep_process_number': 'susepProcessNumber',
        'detail': 'detail'
    }

    def __init__(self, susep_process_number=None, detail=None):  # noqa: E501
        """TermsAndConditionsItem - a model defined in Swagger"""  # noqa: E501
        self._susep_process_number = None
        self._detail = None
        self.discriminator = None
        self.susep_process_number = susep_process_number
        self.detail = detail

    @property
    def susep_process_number(self):
        """Gets the susep_process_number of this TermsAndConditionsItem.  # noqa: E501

        Sequência numérica utilizada para consulta dos processos eletrônicos na SUSEP, com caracteres especiais, conforme campo de consulta no site da SUSEP (XXXXX.XXXXXX/XXXX-XX)<br>Observação&#58; Mascaras da SUSEP – Serão permitidos todas as máscaras de Produtos. Limitar pelos códigos das Máscaras.  # noqa: E501

        :return: The susep_process_number of this TermsAndConditionsItem.  # noqa: E501
        :rtype: str
        """
        return self._susep_process_number

    @susep_process_number.setter
    def susep_process_number(self, susep_process_number):
        """Sets the susep_process_number of this TermsAndConditionsItem.

        Sequência numérica utilizada para consulta dos processos eletrônicos na SUSEP, com caracteres especiais, conforme campo de consulta no site da SUSEP (XXXXX.XXXXXX/XXXX-XX)<br>Observação&#58; Mascaras da SUSEP – Serão permitidos todas as máscaras de Produtos. Limitar pelos códigos das Máscaras.  # noqa: E501

        :param susep_process_number: The susep_process_number of this TermsAndConditionsItem.  # noqa: E501
        :type: str
        """
        if susep_process_number is None:
            raise ValueError("Invalid value for `susep_process_number`, must not be `None`")  # noqa: E501

        self._susep_process_number = susep_process_number

    @property
    def detail(self):
        """Gets the detail of this TermsAndConditionsItem.  # noqa: E501

        Representam as Condições Gerais, Condições Especiais e Condições ou Cláusulas Particulares de um mesmo produto. (Circular SUSEP 321/06). Campo aberto (possibilidade de incluir URL)  # noqa: E501

        :return: The detail of this TermsAndConditionsItem.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this TermsAndConditionsItem.

        Representam as Condições Gerais, Condições Especiais e Condições ou Cláusulas Particulares de um mesmo produto. (Circular SUSEP 321/06). Campo aberto (possibilidade de incluir URL)  # noqa: E501

        :param detail: The detail of this TermsAndConditionsItem.  # noqa: E501
        :type: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail

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
        if issubclass(TermsAndConditionsItem, dict):
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
        if not isinstance(other, TermsAndConditionsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
