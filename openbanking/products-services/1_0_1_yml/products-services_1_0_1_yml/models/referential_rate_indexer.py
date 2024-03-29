# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReferentialRateIndexer(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    SEM_INDEXADOR_TAXA = "SEM_INDEXADOR_TAXA"
    PRE_FIXADO = "PRE_FIXADO"
    POS_FIXADO_TR_TBF = "POS_FIXADO_TR_TBF"
    POS_FIXADO_TJLP = "POS_FIXADO_TJLP"
    POS_FIXADO_LIBOR = "POS_FIXADO_LIBOR"
    POS_FIXADO_TLP = "POS_FIXADO_TLP"
    OUTRAS_TAXAS_POS_FIXADAS = "OUTRAS_TAXAS_POS_FIXADAS"
    FLUTUANTES_CDI = "FLUTUANTES_CDI"
    FLUTUANTES_SELIC = "FLUTUANTES_SELIC"
    OUTRAS_TAXAS_FLUTUANTES = "OUTRAS_TAXAS_FLUTUANTES"
    INDICES_PRECOS_IGPM = "INDICES_PRECOS_IGPM"
    INDICES_PRECOS_IPCA = "INDICES_PRECOS_IPCA"
    INDICES_PRECOS_IPCC = "INDICES_PRECOS_IPCC"
    OUTROS_INDICES_PRECO = "OUTROS_INDICES_PRECO"
    CREDITO_RURAL_TCR_PRE = "CREDITO_RURAL_TCR_PRE"
    CREDITO_RURAL_TCR_POS = "CREDITO_RURAL_TCR_POS"
    CREDITO_RURAL_TRFC_PRE = "CREDITO_RURAL_TRFC_PRE"
    CREDITO_RURAL_TRFC_POS = "CREDITO_RURAL_TRFC_POS"
    OUTROS_INDEXADORES = "OUTROS_INDEXADORES"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """ReferentialRateIndexer - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(ReferentialRateIndexer, dict):
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
        if not isinstance(other, ReferentialRateIndexer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
