# coding: utf-8

"""
    API Seguros - Open Finance Brasil

    As APIs descritas neste documento são referentes a API de Seguros da fase OpenInsurance do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonalCoverageItem(object):
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
        'type': 'str',
        'type_additional_infos': 'list[str]',
        'attributes': 'PersonalCoverageItemAttributes'
    }

    attribute_map = {
        'type': 'type',
        'type_additional_infos': 'typeAdditionalInfos',
        'attributes': 'attributes'
    }

    def __init__(self, type=None, type_additional_infos=None, attributes=None):  # noqa: E501
        """PersonalCoverageItem - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._type_additional_infos = None
        self._attributes = None
        self.discriminator = None
        self.type = type
        if type_additional_infos is not None:
            self.type_additional_infos = type_additional_infos
        self.attributes = attributes

    @property
    def type(self):
        """Gets the type of this PersonalCoverageItem.  # noqa: E501

        É o conjunto dos riscos cobertos elencados na apólice. (RESOLUÇÃO CNSP Nº 341/2016). Listagem de coberturas incluídas no produto que deve observar a relação discriminada de coberturas, conforme Tabela Tipo de Cobertura   # noqa: E501

        :return: The type of this PersonalCoverageItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PersonalCoverageItem.

        É o conjunto dos riscos cobertos elencados na apólice. (RESOLUÇÃO CNSP Nº 341/2016). Listagem de coberturas incluídas no produto que deve observar a relação discriminada de coberturas, conforme Tabela Tipo de Cobertura   # noqa: E501

        :param type: The type of this PersonalCoverageItem.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["ADIANTAMENTO_DOENCA_ESTAGIO_TERMINAL", "AUXILIO_CESTA_BASICA", "AUXILIO_FINANCEIRO_IMEDIATO", "CANCELAMENTO_VIAGEM", "CIRURGIA", "COBERTURA_HERNIA", "COBERTURA_LER_DORT", "CUIDADOS_PROLONGADOS_ACIDENTE", "DESEMPREGO_PERDA_RENDA", "DESPESAS_EXTRA_INVALIDEZ_PERMANENTE_TOTAL_PARCIAL_ACIDENTE_DEI", "DESPESAS_EXTRA_MORTE_DEM", "DESPESAS_MEDICAS_HOSPITALARES_ODONTOLOGICAS", "DESPESAS_MEDICAS_HOSPITALARES_ODONTOLOGICAS_BRASIL", "DESPESAS_MEDICAS_HOSPITALARES_ODONTOLOGICAS_EXTERIOR", "DIARIA_INCAPACIDADE_TOTAL_TEMPORARIA", "DIARIA_INTERNACAO_HOSPITALAR", "INTERNACAO_HOSPITALAR", "DIARIAS_INCAPACIDADE_PECUNIARIA_DIP", "DOENCA_CONGENITA_FILHOS_DCF", "FRATURA_OSSEA", "DOENCAS_TROPICAIS", "INCAPACIDADE_TOTAL_OU_TEMPORARIA", "INVALIDEZ_PERMANENTE_TOTAL_PARCIAL", "INVALIDEZ_TOTAL_ACIDENTE", "INVALIDEZ_PARCIAL_ACIDENTE", "INVALIDEZ_FUNCIONAL_PERMANENTE_DOENCA", "INVALIDEZ_LABORATIVA_DOENCA", "MORTE", "MORTE_ACIDENTAL", "MORTE_CONJUGE", "MORTE_FILHOS", "MORTE_ADIATAMENTO_DOENCA_ESTAGIO_TERMINAL", "PAGAMENTO_ANTECIPADO_ESPECIAL_DOENCA_PROFISSIONAL_PAED", "PERDA_AUTONOMIA_PESSOAL", "PERDA_INVOLUNTARIA_EMPREGO", "QUEIMADURA_GRAVE", "REGRESSO_ANTECIPADO_SANITARIO", "RENDA_INCAPACIDADE_TEMPORARIA", "RESCISAO_CONTRATUAL_CASO_MORTE_RCM", "RESCISAO_TRABALHISTA", "SERVICO_AUXILIO_FUNERAL", "SOBREVIVENCIA", "TRANSPLANTE_ORGAOS", "TRASLADO", "TRANSLADO_CORPO", "VERBA_RESCISORIA", "OUTROS"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def type_additional_infos(self):
        """Gets the type_additional_infos of this PersonalCoverageItem.  # noqa: E501

        Lista de textos para complementar informação relativa ao campo type, quando for selecionada a opção 'OUTROS'. Restrição: Campo de preenchimento obrigatório se 'type' estiver preenchida a opção 'OUTROS'   # noqa: E501

        :return: The type_additional_infos of this PersonalCoverageItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._type_additional_infos

    @type_additional_infos.setter
    def type_additional_infos(self, type_additional_infos):
        """Sets the type_additional_infos of this PersonalCoverageItem.

        Lista de textos para complementar informação relativa ao campo type, quando for selecionada a opção 'OUTROS'. Restrição: Campo de preenchimento obrigatório se 'type' estiver preenchida a opção 'OUTROS'   # noqa: E501

        :param type_additional_infos: The type_additional_infos of this PersonalCoverageItem.  # noqa: E501
        :type: list[str]
        """

        self._type_additional_infos = type_additional_infos

    @property
    def attributes(self):
        """Gets the attributes of this PersonalCoverageItem.  # noqa: E501


        :return: The attributes of this PersonalCoverageItem.  # noqa: E501
        :rtype: PersonalCoverageItemAttributes
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this PersonalCoverageItem.


        :param attributes: The attributes of this PersonalCoverageItem.  # noqa: E501
        :type: PersonalCoverageItemAttributes
        """
        if attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501

        self._attributes = attributes

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
        if issubclass(PersonalCoverageItem, dict):
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
        if not isinstance(other, PersonalCoverageItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
