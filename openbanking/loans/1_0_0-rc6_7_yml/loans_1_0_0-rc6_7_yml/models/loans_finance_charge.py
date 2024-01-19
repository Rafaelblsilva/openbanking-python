# coding: utf-8

"""
    API Loans - Open Banking Brasil

    API de informações de operações de empréstimos do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo empréstimo, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Loans  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **LOANS_READ** ### `/contracts/{contractId}`   - permissions:      - GET **LOANS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **LOANS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **LOANS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **LOANS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.7
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LoansFinanceCharge(object):
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
        'charge_type': 'EnumContractFinanceChargeType',
        'charge_additional_info': 'str',
        'charge_rate': 'float'
    }

    attribute_map = {
        'charge_type': 'chargeType',
        'charge_additional_info': 'chargeAdditionalInfo',
        'charge_rate': 'chargeRate'
    }

    def __init__(self, charge_type=None, charge_additional_info=None, charge_rate=None):  # noqa: E501
        """LoansFinanceCharge - a model defined in Swagger"""  # noqa: E501
        self._charge_type = None
        self._charge_additional_info = None
        self._charge_rate = None
        self.discriminator = None
        self.charge_type = charge_type
        self.charge_additional_info = charge_additional_info
        if charge_rate is not None:
            self.charge_rate = charge_rate

    @property
    def charge_type(self):
        """Gets the charge_type of this LoansFinanceCharge.  # noqa: E501


        :return: The charge_type of this LoansFinanceCharge.  # noqa: E501
        :rtype: EnumContractFinanceChargeType
        """
        return self._charge_type

    @charge_type.setter
    def charge_type(self, charge_type):
        """Sets the charge_type of this LoansFinanceCharge.


        :param charge_type: The charge_type of this LoansFinanceCharge.  # noqa: E501
        :type: EnumContractFinanceChargeType
        """
        if charge_type is None:
            raise ValueError("Invalid value for `charge_type`, must not be `None`")  # noqa: E501

        self._charge_type = charge_type

    @property
    def charge_additional_info(self):
        """Gets the charge_additional_info of this LoansFinanceCharge.  # noqa: E501

        Campo de preenchimento obrigatório se selecionada a opção 'OUTROS' em Tipo de encargo pactuado no contrato. [Restrição] Obrigatório se selecionada a opção 'OUTROS' em Tipo de encargo pactuado no contrato.   # noqa: E501

        :return: The charge_additional_info of this LoansFinanceCharge.  # noqa: E501
        :rtype: str
        """
        return self._charge_additional_info

    @charge_additional_info.setter
    def charge_additional_info(self, charge_additional_info):
        """Sets the charge_additional_info of this LoansFinanceCharge.

        Campo de preenchimento obrigatório se selecionada a opção 'OUTROS' em Tipo de encargo pactuado no contrato. [Restrição] Obrigatório se selecionada a opção 'OUTROS' em Tipo de encargo pactuado no contrato.   # noqa: E501

        :param charge_additional_info: The charge_additional_info of this LoansFinanceCharge.  # noqa: E501
        :type: str
        """
        if charge_additional_info is None:
            raise ValueError("Invalid value for `charge_additional_info`, must not be `None`")  # noqa: E501

        self._charge_additional_info = charge_additional_info

    @property
    def charge_rate(self):
        """Gets the charge_rate of this LoansFinanceCharge.  # noqa: E501

        Representa o valor do encargo em percentual pactuado no contrato. Exemplo: 0.0210 (=2.1%).   # noqa: E501

        :return: The charge_rate of this LoansFinanceCharge.  # noqa: E501
        :rtype: float
        """
        return self._charge_rate

    @charge_rate.setter
    def charge_rate(self, charge_rate):
        """Sets the charge_rate of this LoansFinanceCharge.

        Representa o valor do encargo em percentual pactuado no contrato. Exemplo: 0.0210 (=2.1%).   # noqa: E501

        :param charge_rate: The charge_rate of this LoansFinanceCharge.  # noqa: E501
        :type: float
        """

        self._charge_rate = charge_rate

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
        if issubclass(LoansFinanceCharge, dict):
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
        if not isinstance(other, LoansFinanceCharge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
