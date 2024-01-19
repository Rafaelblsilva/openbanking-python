# coding: utf-8

"""
    API Financings - Open Banking Brasil

    API de informações de operações de financiamentos do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo financiamento, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Financings  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **FINANCINGS_READ** ### `/contracts/{contractId}`   - permissions:     - GET **FINANCINGS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **FINANCINGS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **FINANCINGS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **FINANCINGS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FinancingsWarranties(object):
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
        'currency': 'str',
        'warranty_type': 'str',
        'warranty_sub_type': 'str',
        'warranty_amount': 'float'
    }

    attribute_map = {
        'currency': 'currency',
        'warranty_type': 'warrantyType',
        'warranty_sub_type': 'warrantySubType',
        'warranty_amount': 'warrantyAmount'
    }

    def __init__(self, currency=None, warranty_type=None, warranty_sub_type=None, warranty_amount=None):  # noqa: E501
        """FinancingsWarranties - a model defined in Swagger"""  # noqa: E501
        self._currency = None
        self._warranty_type = None
        self._warranty_sub_type = None
        self._warranty_amount = None
        self.discriminator = None
        self.currency = currency
        self.warranty_type = warranty_type
        self.warranty_sub_type = warranty_sub_type
        if warranty_amount is not None:
            self.warranty_amount = warranty_amount

    @property
    def currency(self):
        """Gets the currency of this FinancingsWarranties.  # noqa: E501

        Moeda referente ao valor da garantia, segundo modelo ISO-4217. p.ex. 'BRL'. Todos os valores monetários informados estão representados com a moeda vigente do Brasil  # noqa: E501

        :return: The currency of this FinancingsWarranties.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this FinancingsWarranties.

        Moeda referente ao valor da garantia, segundo modelo ISO-4217. p.ex. 'BRL'. Todos os valores monetários informados estão representados com a moeda vigente do Brasil  # noqa: E501

        :param currency: The currency of this FinancingsWarranties.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def warranty_type(self):
        """Gets the warranty_type of this FinancingsWarranties.  # noqa: E501

        Denominação/Identificação do tipo da garantia que avaliza a Modalidade da Operação de Crédito contratada  (Doc 3040, Anexo 12)  # noqa: E501

        :return: The warranty_type of this FinancingsWarranties.  # noqa: E501
        :rtype: str
        """
        return self._warranty_type

    @warranty_type.setter
    def warranty_type(self, warranty_type):
        """Sets the warranty_type of this FinancingsWarranties.

        Denominação/Identificação do tipo da garantia que avaliza a Modalidade da Operação de Crédito contratada  (Doc 3040, Anexo 12)  # noqa: E501

        :param warranty_type: The warranty_type of this FinancingsWarranties.  # noqa: E501
        :type: str
        """
        if warranty_type is None:
            raise ValueError("Invalid value for `warranty_type`, must not be `None`")  # noqa: E501
        allowed_values = ["SEM_TIPO_GARANTIA", "CESSAO_DIREITOS_CREDITORIOS", "CAUCAO", "PENHOR", "ALIENACAO_FIDUCIARIA", "HIPOTECA", "OPERACOES_GARANTIDAS_PELO_GOVERNO", "OUTRAS_GARANTIAS_NAO_FIDEJUSSORIAS", "SEGUROS_ASSEMELHADOS", "GARANTIA_FIDEJUSSORIA", "BENS_ARRENDADOS", "GARANTIAS_INTERNACIONAIS", "OPERACOES_GARANTIDAS_OUTRAS_ENTIDADES", "ACORDOS_COMPENSACAO"]  # noqa: E501
        if warranty_type not in allowed_values:
            raise ValueError(
                "Invalid value for `warranty_type` ({0}), must be one of {1}"  # noqa: E501
                .format(warranty_type, allowed_values)
            )

        self._warranty_type = warranty_type

    @property
    def warranty_sub_type(self):
        """Gets the warranty_sub_type of this FinancingsWarranties.  # noqa: E501

        Denominação/Identificação do sub tipo da garantia que avaliza a Modalidade da Operação de Crédito contratada (Doc 3040, Anexo 12).   # noqa: E501

        :return: The warranty_sub_type of this FinancingsWarranties.  # noqa: E501
        :rtype: str
        """
        return self._warranty_sub_type

    @warranty_sub_type.setter
    def warranty_sub_type(self, warranty_sub_type):
        """Sets the warranty_sub_type of this FinancingsWarranties.

        Denominação/Identificação do sub tipo da garantia que avaliza a Modalidade da Operação de Crédito contratada (Doc 3040, Anexo 12).   # noqa: E501

        :param warranty_sub_type: The warranty_sub_type of this FinancingsWarranties.  # noqa: E501
        :type: str
        """
        if warranty_sub_type is None:
            raise ValueError("Invalid value for `warranty_sub_type`, must not be `None`")  # noqa: E501
        allowed_values = ["ACOES_DEBENTURES", "APLICACOES_FINANCEIRAS_RENDA_FIXA", "APLICACOES_FINANCEIRAS_RENDA_VARIAVEL", "APOLICES_CREDITO_EXPORTACAO", "CCR_CONVENIO_CREDITOS_RECIPROCOS", "CHEQUES", "CIVIL", "DIREITOS_SOBRE_ALUGUEIS", "DEPOSITOS_A_VISTA_A_PRAZO_POUPANCA_OURO_TITULOS_PUBLICOS_FEDERAIS_ART_36", "DEPOSITO_TITULOS_EMITIDOS_ENTIDADES_ART_23", "DUPLICATAS", "EMD_ENTIDADES_MULTILATERAIS_DESENVOLVIMENTO_ART_37", "EQUIPAMENTOS FATURA_CARTAO_CREDITO", "ESTADUAL_OU_DISTRITAL", "FATURA_CARTAO_CREDITO", "FEDERAL", "FCVS_FUNDO_COMPENSACAO_VARIACOES_SALARIAIS", "FGI_FUNDO_GARANTIDOR_INVESTIMENTOS", "FGPC_FUNDO_GARANTIA_PROMOCAO_COMPETIT", "FGTS_FUNDO_GARANTIA_TEMPO_SERVICO", "FUNDO_GARANTIDOR_AVAL", "GARANTIA_PRESTADA_FGPC_LEI_9531_ART_37", "GARANTIA_PRESTADA_FUNDOS_QUAISQUER_OUTROS_MECANISMOS_COBERTURA_RISCO_CREDITO_ART_37", "GARANTIA_PRESTADA_TESOURO_NACIONAL_OU_BACEN_ART_37_BENS_DIREITOS_INTEGRANTES_PATRIMONIO_AFETACAO", "IMOVEIS", "IMOVEIS_RESIDENCIAIS", "MITIGADORAS", "MUNICIPAL", "NAO_MITIGADORAS", "NOTAS_PROMISSORIAS_OUTROS_DIREITOS_CREDITO", "OUTRAS", "OUTROS", "OUTROS_BENS", "OUTROS_GRAUS", "OUTROS_IMOVEIS", "OUTROS_SEGUROS_ASSEMELHADOS", "PESSOA_FISICA", "PESSOA_FISICA_EXTERIOR", "PESSOA_JURIDICA", "PESSOA_JURIDICA_EXTERIOR", "PRIMEIRO_GRAU_BENS_DIREITOS_INTEGRANTES_PATRIMONIO_AFETACAO", "PRIMEIRO_GRAU_IMOVEIS_RESIDENCIAIS", "PRIMEIRO_GRAU_OUTROS", "PRODUTOS_AGROPECUARIOS_COM_WARRANT", "PRODUTOS_AGROPECUARIOS_SEM_WARRANT", "SBCE_SOCIEDADE_BRASILEIRA_CREDITO_EXPORTAÇÃO", "SEGURO_RURAL", "TRIBUTOS_RECEITAS_ORCAMENTARIAS", "VEICULOS", "VEICULOS_AUTOMOTORES"]  # noqa: E501
        if warranty_sub_type not in allowed_values:
            raise ValueError(
                "Invalid value for `warranty_sub_type` ({0}), must be one of {1}"  # noqa: E501
                .format(warranty_sub_type, allowed_values)
            )

        self._warranty_sub_type = warranty_sub_type

    @property
    def warranty_amount(self):
        """Gets the warranty_amount of this FinancingsWarranties.  # noqa: E501

        Valor original da garantia. Valor monetário, expresso com até 4 casas decimais.   # noqa: E501

        :return: The warranty_amount of this FinancingsWarranties.  # noqa: E501
        :rtype: float
        """
        return self._warranty_amount

    @warranty_amount.setter
    def warranty_amount(self, warranty_amount):
        """Sets the warranty_amount of this FinancingsWarranties.

        Valor original da garantia. Valor monetário, expresso com até 4 casas decimais.   # noqa: E501

        :param warranty_amount: The warranty_amount of this FinancingsWarranties.  # noqa: E501
        :type: float
        """

        self._warranty_amount = warranty_amount

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
        if issubclass(FinancingsWarranties, dict):
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
        if not isinstance(other, FinancingsWarranties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
