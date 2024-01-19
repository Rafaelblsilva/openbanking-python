# coding: utf-8

"""
    API Invoice-financings - Open Banking Brasil

    API de informações de operações de antecipação de recebíveis do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo antecipação de recebíveis – direitos creditórios descontados - mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Invoice-financings  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}`   - permissions:      - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **INVOICE_FINANCINGS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **INVOICE_FINANCINGS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.7
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InvoiceFinancingsContractedFee(object):
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
        'fee_charge_type': 'EnumContractFeeChargeType',
        'fee_charge': 'EnumContractFeeCharge',
        'fee_amount': 'float',
        'fee_rate': 'float'
    }

    attribute_map = {
        'fee_name': 'feeName',
        'fee_code': 'feeCode',
        'fee_charge_type': 'feeChargeType',
        'fee_charge': 'feeCharge',
        'fee_amount': 'feeAmount',
        'fee_rate': 'feeRate'
    }

    def __init__(self, fee_name=None, fee_code=None, fee_charge_type=None, fee_charge=None, fee_amount=None, fee_rate=None):  # noqa: E501
        """InvoiceFinancingsContractedFee - a model defined in Swagger"""  # noqa: E501
        self._fee_name = None
        self._fee_code = None
        self._fee_charge_type = None
        self._fee_charge = None
        self._fee_amount = None
        self._fee_rate = None
        self.discriminator = None
        self.fee_name = fee_name
        self.fee_code = fee_code
        self.fee_charge_type = fee_charge_type
        self.fee_charge = fee_charge
        self.fee_amount = fee_amount
        self.fee_rate = fee_rate

    @property
    def fee_name(self):
        """Gets the fee_name of this InvoiceFinancingsContractedFee.  # noqa: E501

        Denominação da Tarifa pactuada  # noqa: E501

        :return: The fee_name of this InvoiceFinancingsContractedFee.  # noqa: E501
        :rtype: str
        """
        return self._fee_name

    @fee_name.setter
    def fee_name(self, fee_name):
        """Sets the fee_name of this InvoiceFinancingsContractedFee.

        Denominação da Tarifa pactuada  # noqa: E501

        :param fee_name: The fee_name of this InvoiceFinancingsContractedFee.  # noqa: E501
        :type: str
        """
        if fee_name is None:
            raise ValueError("Invalid value for `fee_name`, must not be `None`")  # noqa: E501

        self._fee_name = fee_name

    @property
    def fee_code(self):
        """Gets the fee_code of this InvoiceFinancingsContractedFee.  # noqa: E501

        Sigla identificadora da tarifa pactuada  # noqa: E501

        :return: The fee_code of this InvoiceFinancingsContractedFee.  # noqa: E501
        :rtype: str
        """
        return self._fee_code

    @fee_code.setter
    def fee_code(self, fee_code):
        """Sets the fee_code of this InvoiceFinancingsContractedFee.

        Sigla identificadora da tarifa pactuada  # noqa: E501

        :param fee_code: The fee_code of this InvoiceFinancingsContractedFee.  # noqa: E501
        :type: str
        """
        if fee_code is None:
            raise ValueError("Invalid value for `fee_code`, must not be `None`")  # noqa: E501

        self._fee_code = fee_code

    @property
    def fee_charge_type(self):
        """Gets the fee_charge_type of this InvoiceFinancingsContractedFee.  # noqa: E501


        :return: The fee_charge_type of this InvoiceFinancingsContractedFee.  # noqa: E501
        :rtype: EnumContractFeeChargeType
        """
        return self._fee_charge_type

    @fee_charge_type.setter
    def fee_charge_type(self, fee_charge_type):
        """Sets the fee_charge_type of this InvoiceFinancingsContractedFee.


        :param fee_charge_type: The fee_charge_type of this InvoiceFinancingsContractedFee.  # noqa: E501
        :type: EnumContractFeeChargeType
        """
        if fee_charge_type is None:
            raise ValueError("Invalid value for `fee_charge_type`, must not be `None`")  # noqa: E501

        self._fee_charge_type = fee_charge_type

    @property
    def fee_charge(self):
        """Gets the fee_charge of this InvoiceFinancingsContractedFee.  # noqa: E501


        :return: The fee_charge of this InvoiceFinancingsContractedFee.  # noqa: E501
        :rtype: EnumContractFeeCharge
        """
        return self._fee_charge

    @fee_charge.setter
    def fee_charge(self, fee_charge):
        """Sets the fee_charge of this InvoiceFinancingsContractedFee.


        :param fee_charge: The fee_charge of this InvoiceFinancingsContractedFee.  # noqa: E501
        :type: EnumContractFeeCharge
        """
        if fee_charge is None:
            raise ValueError("Invalid value for `fee_charge`, must not be `None`")  # noqa: E501

        self._fee_charge = fee_charge

    @property
    def fee_amount(self):
        """Gets the fee_amount of this InvoiceFinancingsContractedFee.  # noqa: E501

        Valor monetário da tarifa pactuada no contrato. Preenchimento obrigatório quando a forma de cobrança for: Mínimo, Máximo ou Fixo.   # noqa: E501

        :return: The fee_amount of this InvoiceFinancingsContractedFee.  # noqa: E501
        :rtype: float
        """
        return self._fee_amount

    @fee_amount.setter
    def fee_amount(self, fee_amount):
        """Sets the fee_amount of this InvoiceFinancingsContractedFee.

        Valor monetário da tarifa pactuada no contrato. Preenchimento obrigatório quando a forma de cobrança for: Mínimo, Máximo ou Fixo.   # noqa: E501

        :param fee_amount: The fee_amount of this InvoiceFinancingsContractedFee.  # noqa: E501
        :type: float
        """
        if fee_amount is None:
            raise ValueError("Invalid value for `fee_amount`, must not be `None`")  # noqa: E501

        self._fee_amount = fee_amount

    @property
    def fee_rate(self):
        """Gets the fee_rate of this InvoiceFinancingsContractedFee.  # noqa: E501

        Percentual que representa o valor da tarifa pactuada para o contrato.  [Restrição] Preenchimento obrigatório quando a forma de cobrança por Percentual.    maxLength: 19   # noqa: E501

        :return: The fee_rate of this InvoiceFinancingsContractedFee.  # noqa: E501
        :rtype: float
        """
        return self._fee_rate

    @fee_rate.setter
    def fee_rate(self, fee_rate):
        """Sets the fee_rate of this InvoiceFinancingsContractedFee.

        Percentual que representa o valor da tarifa pactuada para o contrato.  [Restrição] Preenchimento obrigatório quando a forma de cobrança por Percentual.    maxLength: 19   # noqa: E501

        :param fee_rate: The fee_rate of this InvoiceFinancingsContractedFee.  # noqa: E501
        :type: float
        """
        if fee_rate is None:
            raise ValueError("Invalid value for `fee_rate`, must not be `None`")  # noqa: E501

        self._fee_rate = fee_rate

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
        if issubclass(InvoiceFinancingsContractedFee, dict):
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
        if not isinstance(other, InvoiceFinancingsContractedFee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
