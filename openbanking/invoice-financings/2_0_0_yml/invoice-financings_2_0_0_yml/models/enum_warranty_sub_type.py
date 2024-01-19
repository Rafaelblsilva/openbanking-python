# coding: utf-8

"""
    API Invoice-financings - Open Banking Brasil

    API de informações de operações de antecipação de recebíveis do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo antecipação de recebíveis – direitos creditórios descontados - mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ### Observação:   - No endpoint `/contracts/{contratId}/payments` a paginação ocorrerá sob os dados contidos no campo `releases` do tipo lista.     ## Permissions necessárias para a API Invoice-financings  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}`   - permissions:     - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **INVOICE_FINANCINGS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **INVOICE_FINANCINGS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EnumWarrantySubType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    ACOES_DEBENTURES = "ACOES_DEBENTURES"
    ACORDOS_COMPENSACAO_LIQUIDACAO_OBRIGACOES = "ACORDOS_COMPENSACAO_LIQUIDACAO_OBRIGACOES"
    APLICACOES_FINANCEIRAS_RENDA_FIXA = "APLICACOES_FINANCEIRAS_RENDA_FIXA"
    APLICACOES_FINANCEIRAS_RENDA_VARIAVEL = "APLICACOES_FINANCEIRAS_RENDA_VARIAVEL"
    APOLICES_CREDITO_EXPORTACAO = "APOLICES_CREDITO_EXPORTACAO"
    CCR_CONVENIO_CREDITOS_RECIPROCOS = "CCR_CONVENIO_CREDITOS_RECIPROCOS"
    CHEQUES = "CHEQUES"
    CIVIL = "CIVIL"
    DIREITOS_SOBRE_ALUGUEIS = "DIREITOS_SOBRE_ALUGUEIS"
    DEPOSITOS_A_VISTA_A_PRAZO_POUPANCA_OURO_TITULOS_PUBLICOS_FEDERAIS_ART_36 = "DEPOSITOS_A_VISTA_A_PRAZO_POUPANCA_OURO_TITULOS_PUBLICOS_FEDERAIS_ART_36"
    DEPOSITO_TITULOS_EMITIDOS_ENTIDADES_ART_23 = "DEPOSITO_TITULOS_EMITIDOS_ENTIDADES_ART_23"
    DUPLICATAS = "DUPLICATAS"
    EMD_ENTIDADES_MULTILATERAIS_DESENVOLVIMENTO_ART_37 = "EMD_ENTIDADES_MULTILATERAIS_DESENVOLVIMENTO_ART_37"
    EQUIPAMENTOS = "EQUIPAMENTOS"
    ESTADUAL_OU_DISTRITAL = "ESTADUAL_OU_DISTRITAL"
    FATURA_CARTAO_CREDITO = "FATURA_CARTAO_CREDITO"
    FEDERAL = "FEDERAL"
    FCVS_FUNDO_COMPENSACAO_VARIACOES_SALARIAIS = "FCVS_FUNDO_COMPENSACAO_VARIACOES_SALARIAIS"
    FGI_FUNDO_GARANTIDOR_INVESTIMENTOS = "FGI_FUNDO_GARANTIDOR_INVESTIMENTOS"
    FGPC_FUNDO_GARANTIA_PROMOCAO_COMPETIT = "FGPC_FUNDO_GARANTIA_PROMOCAO_COMPETIT"
    FGTS_FUNDO_GARANTIA_TEMPO_SERVICO = "FGTS_FUNDO_GARANTIA_TEMPO_SERVICO"
    FUNDO_GARANTIDOR_AVAL = "FUNDO_GARANTIDOR_AVAL"
    GARANTIA_PRESTADA_FGPC_LEI_9531_ART_37 = "GARANTIA_PRESTADA_FGPC_LEI_9531_ART_37"
    GARANTIA_PRESTADA_FUNDOS_QUAISQUER_OUTROS_MECANISMOS_COBERTURA_RISCO_CREDITO_ART_37 = "GARANTIA_PRESTADA_FUNDOS_QUAISQUER_OUTROS_MECANISMOS_COBERTURA_RISCO_CREDITO_ART_37"
    GARANTIA_PRESTADA_TESOURO_NACIONAL_OU_BACEN_ART_37_BENS_DIREITOS_INTEGRANTES_PATRIMONIO_AFETACAO = "GARANTIA_PRESTADA_TESOURO_NACIONAL_OU_BACEN_ART_37_BENS_DIREITOS_INTEGRANTES_PATRIMONIO_AFETACAO"
    IMOVEIS = "IMOVEIS"
    IMOVEIS_RESIDENCIAIS = "IMOVEIS_RESIDENCIAIS"
    MITIGADORAS = "MITIGADORAS"
    MUNICIPAL = "MUNICIPAL"
    NAO_MITIGADORAS = "NAO_MITIGADORAS"
    NOTAS_PROMISSORIAS_OUTROS_DIREITOS_CREDITO = "NOTAS_PROMISSORIAS_OUTROS_DIREITOS_CREDITO"
    OUTRAS = "OUTRAS"
    OUTROS = "OUTROS"
    OUTROS_BENS = "OUTROS_BENS"
    OUTROS_GRAUS = "OUTROS_GRAUS"
    OUTROS_IMOVEIS = "OUTROS_IMOVEIS"
    OUTROS_SEGUROS_ASSEMELHADOS = "OUTROS_SEGUROS_ASSEMELHADOS"
    PESSOA_FISICA = "PESSOA_FISICA"
    PESSOA_FISICA_EXTERIOR = "PESSOA_FISICA_EXTERIOR"
    PESSOA_JURIDICA = "PESSOA_JURIDICA"
    PESSOA_JURIDICA_EXTERIOR = "PESSOA_JURIDICA_EXTERIOR"
    PRIMEIRO_GRAU_BENS_DIREITOS_INTEGRANTES_PATRIMONIO_AFETACAO = "PRIMEIRO_GRAU_BENS_DIREITOS_INTEGRANTES_PATRIMONIO_AFETACAO"
    PRIMEIRO_GRAU_IMOVEIS_RESIDENCIAIS = "PRIMEIRO_GRAU_IMOVEIS_RESIDENCIAIS"
    PRIMEIRO_GRAU_OUTROS = "PRIMEIRO_GRAU_OUTROS"
    PROAGRO = "PROAGRO"
    PRODUTOS_AGROPECUARIOS_COM_WARRANT = "PRODUTOS_AGROPECUARIOS_COM_WARRANT"
    PRODUTOS_AGROPECUARIOS_SEM_WARRANT = "PRODUTOS_AGROPECUARIOS_SEM_WARRANT"
    SBCE_SOCIEDADE_BRASILEIRA_CREDITO_EXPORTA_O = "SBCE_SOCIEDADE_BRASILEIRA_CREDITO_EXPORTAÇÃO"
    SEGURO_RURAL = "SEGURO_RURAL"
    SEM_SUB_TIPO_GARANTIA = "SEM_SUB_TIPO_GARANTIA"
    TRIBUTOS_RECEITAS_ORCAMENTARIAS = "TRIBUTOS_RECEITAS_ORCAMENTARIAS"
    VEICULOS = "VEICULOS"
    VEICULOS_AUTOMOTORES = "VEICULOS_AUTOMOTORES"
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
        """EnumWarrantySubType - a model defined in Swagger"""  # noqa: E501
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
        if issubclass(EnumWarrantySubType, dict):
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
        if not isinstance(other, EnumWarrantySubType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
