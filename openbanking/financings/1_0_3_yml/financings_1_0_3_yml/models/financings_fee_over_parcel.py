# coding: utf-8

"""
    API Financings - Open Banking Brasil

    API de informações de operações de financiamentos do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo financiamento, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Financings  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **FINANCINGS_READ** ### `/contracts/{contractId}`   - permissions:     - GET **FINANCINGS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **FINANCINGS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **FINANCINGS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **FINANCINGS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.3
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FinancingsFeeOverParcel(object):
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
        'fee_name': 'str',
        'fee_code': 'str',
        'fee_amount': 'float'
    }

    attribute_map = {
        'fee_name': 'feeName',
        'fee_code': 'feeCode',
        'fee_amount': 'feeAmount'
    }

    def __init__(self, fee_name=None, fee_code=None, fee_amount=None):  # noqa: E501
        """FinancingsFeeOverParcel - a model defined in Swagger"""  # noqa: E501
        self._fee_name = None
        self._fee_code = None
        self._fee_amount = None
        self.discriminator = None
        self.fee_name = fee_name
        self.fee_code = fee_code
        self.fee_amount = fee_amount

    @property
    def fee_name(self):
        """Gets the fee_name of this FinancingsFeeOverParcel.  # noqa: E501

        Denominação da Tarifa pactuada  # noqa: E501

        :return: The fee_name of this FinancingsFeeOverParcel.  # noqa: E501
        :rtype: str
        """
        return self._fee_name

    @fee_name.setter
    def fee_name(self, fee_name):
        """Sets the fee_name of this FinancingsFeeOverParcel.

        Denominação da Tarifa pactuada  # noqa: E501

        :param fee_name: The fee_name of this FinancingsFeeOverParcel.  # noqa: E501
        :type: str
        """
        if fee_name is None:
            raise ValueError("Invalid value for `fee_name`, must not be `None`")  # noqa: E501

        self._fee_name = fee_name

    @property
    def fee_code(self):
        """Gets the fee_code of this FinancingsFeeOverParcel.  # noqa: E501

        Sigla identificadora da tarifa pactuada  # noqa: E501

        :return: The fee_code of this FinancingsFeeOverParcel.  # noqa: E501
        :rtype: str
        """
        return self._fee_code

    @fee_code.setter
    def fee_code(self, fee_code):
        """Sets the fee_code of this FinancingsFeeOverParcel.

        Sigla identificadora da tarifa pactuada  # noqa: E501

        :param fee_code: The fee_code of this FinancingsFeeOverParcel.  # noqa: E501
        :type: str
        """
        if fee_code is None:
            raise ValueError("Invalid value for `fee_code`, must not be `None`")  # noqa: E501

        self._fee_code = fee_code

    @property
    def fee_amount(self):
        """Gets the fee_amount of this FinancingsFeeOverParcel.  # noqa: E501

        Valor monetário da tarifa pactuada no contrato. [Restrição] Preenchimento obrigatório quando a forma de cobrança for: Mínimo, Máximo ou Fixo   # noqa: E501

        :return: The fee_amount of this FinancingsFeeOverParcel.  # noqa: E501
        :rtype: float
        """
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """Sets the fee_amount of this FinancingsFeeOverParcel.

        Valor monetário da tarifa pactuada no contrato. [Restrição] Preenchimento obrigatório quando a forma de cobrança for: Mínimo, Máximo ou Fixo   # noqa: E501

        :param fee_amount: The fee_amount of this FinancingsFeeOverParcel.  # noqa: E501
        :type: float
        """
        if fee_amount is None:
            raise ValueError("Invalid value for `fee_amount`, must not be `None`")  # noqa: E501

        self._fee_amount = fee_amount

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
        if issubclass(FinancingsFeeOverParcel, dict):
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
        if not isinstance(other, FinancingsFeeOverParcel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
