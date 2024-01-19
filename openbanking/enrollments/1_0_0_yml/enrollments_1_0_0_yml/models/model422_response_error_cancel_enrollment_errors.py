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

class Model422ResponseErrorCancelEnrollmentErrors(object):
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
        'code': 'str',
        'title': 'str',
        'detail': 'str'
    }

    attribute_map = {
        'code': 'code',
        'title': 'title',
        'detail': 'detail'
    }

    def __init__(self, code=None, title=None, detail=None):  # noqa: E501
        """Model422ResponseErrorCancelEnrollmentErrors - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._title = None
        self._detail = None
        self.discriminator = None
        self.code = code
        self.title = title
        self.detail = detail

    @property
    def code(self):
        """Gets the code of this Model422ResponseErrorCancelEnrollmentErrors.  # noqa: E501

        Códigos de erros previstos no cancelamento do vínculo de conta:  • STATUS_INVALIDO: O status do vínculo de conta não permite cancelamento.  • MOTIVO_REJEICAO: A rejeição do vínculo de conta exige um motivo associado.  • REJEITADO_OUTRO_SEM_DETALHES: O uso do motivo REJEITADO_OUTRO, deve estar acompanhado de descrição (additionalInformation).  • MOTIVO_REVOGACAO: A revogação do vínculo de conta exige um motivo associado.  • REVOGADO_OUTRO_SEM_DETALHES: O uso do motivo REVOGADO_OUTRO deve estar acompanhado de descrição (additionalInformation)   # noqa: E501

        :return: The code of this Model422ResponseErrorCancelEnrollmentErrors.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Model422ResponseErrorCancelEnrollmentErrors.

        Códigos de erros previstos no cancelamento do vínculo de conta:  • STATUS_INVALIDO: O status do vínculo de conta não permite cancelamento.  • MOTIVO_REJEICAO: A rejeição do vínculo de conta exige um motivo associado.  • REJEITADO_OUTRO_SEM_DETALHES: O uso do motivo REJEITADO_OUTRO, deve estar acompanhado de descrição (additionalInformation).  • MOTIVO_REVOGACAO: A revogação do vínculo de conta exige um motivo associado.  • REVOGADO_OUTRO_SEM_DETALHES: O uso do motivo REVOGADO_OUTRO deve estar acompanhado de descrição (additionalInformation)   # noqa: E501

        :param code: The code of this Model422ResponseErrorCancelEnrollmentErrors.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        allowed_values = ["STATUS_INVALIDO", "MOTIVO_REJEICAO", "REJEITADO_OUTRO_SEM_DETALHES", "MOTIVO_REVOGACAO", "REVOGADO_OUTRO_SEM_DETALHES"]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def title(self):
        """Gets the title of this Model422ResponseErrorCancelEnrollmentErrors.  # noqa: E501

        Título específico do erro reportado, de acordo com o código enviado:  • STATUS_INVALIDO: Status inválido.  • MOTIVO_REJEICAO: Motivo de rejeição não especificado.  • REJEITADO_OUTRO_SEM_DETALHES: O campo additionalInformation é obrigatório.  • MOTIVO_REVOGACAO: Motivo de revogação não especificado.  • REVOGADO_OUTRO_SEM_DETALHES: O campo additionalInformation é obrigatório.   # noqa: E501

        :return: The title of this Model422ResponseErrorCancelEnrollmentErrors.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Model422ResponseErrorCancelEnrollmentErrors.

        Título específico do erro reportado, de acordo com o código enviado:  • STATUS_INVALIDO: Status inválido.  • MOTIVO_REJEICAO: Motivo de rejeição não especificado.  • REJEITADO_OUTRO_SEM_DETALHES: O campo additionalInformation é obrigatório.  • MOTIVO_REVOGACAO: Motivo de revogação não especificado.  • REVOGADO_OUTRO_SEM_DETALHES: O campo additionalInformation é obrigatório.   # noqa: E501

        :param title: The title of this Model422ResponseErrorCancelEnrollmentErrors.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def detail(self):
        """Gets the detail of this Model422ResponseErrorCancelEnrollmentErrors.  # noqa: E501

        Descrição específica do erro de acordo com o código reportado:  • STATUS_INVALIDO: O status do vínculo de conta não permite cancelamento.  • MOTIVO_REJEICAO: A rejeição do vínculo de conta deve estar associada a um motivo de rejeição.  • REJEITADO_OUTRO_SEM_DETALHES: O uso do motivo REJEITADO_OUTRO, deve estar acompanhado de descrição (additionalInformation).  • MOTIVO_REVOGACAO: A revogação do vínculo de conta deve estar associada a um motivo de revogação.  • REVOGADO_OUTRO_SEM_DETALHES: O uso do motivo REVOGADO_OUTRO deve estar acompanhado de descrição (additionalInformation)   # noqa: E501

        :return: The detail of this Model422ResponseErrorCancelEnrollmentErrors.  # noqa: E501
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Model422ResponseErrorCancelEnrollmentErrors.

        Descrição específica do erro de acordo com o código reportado:  • STATUS_INVALIDO: O status do vínculo de conta não permite cancelamento.  • MOTIVO_REJEICAO: A rejeição do vínculo de conta deve estar associada a um motivo de rejeição.  • REJEITADO_OUTRO_SEM_DETALHES: O uso do motivo REJEITADO_OUTRO, deve estar acompanhado de descrição (additionalInformation).  • MOTIVO_REVOGACAO: A revogação do vínculo de conta deve estar associada a um motivo de revogação.  • REVOGADO_OUTRO_SEM_DETALHES: O uso do motivo REVOGADO_OUTRO deve estar acompanhado de descrição (additionalInformation)   # noqa: E501

        :param detail: The detail of this Model422ResponseErrorCancelEnrollmentErrors.  # noqa: E501
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
        if issubclass(Model422ResponseErrorCancelEnrollmentErrors, dict):
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
        if not isinstance(other, Model422ResponseErrorCancelEnrollmentErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
