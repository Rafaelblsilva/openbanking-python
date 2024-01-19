# coding: utf-8

"""
    API Loans - Open Finance Brasil

    API de informações de operações de empréstimos do Open Finance Brasil – Fase 2. API que retorna informações de operações de crédito do tipo empréstimo, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos(ao menos para os últimos 12 meses), amortizações, garantias, encargos e taxas de juros remuneratórios. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os `endpoints.`  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.    <br> ### Observação:   - No endpoint `/contracts/{contratId}/payments` a paginação ocorrerá sob os dados contidos no campo `releases` do tipo lista.    <br> ## Permissions necessárias para a API Loans  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **LOANS_READ** ### `/contracts/{contractId}`   - permissions:     - GET **LOANS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **LOANS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **LOANS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **LOANS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 2.1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LoansListContract(object):
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
        'contract_id': 'str',
        'brand_name': 'str',
        'company_cnpj': 'str',
        'product_type': 'EnumContractProductTypeLoans',
        'product_sub_type': 'EnumContractProductSubTypeLoans',
        'ipoc_code': 'str'
    }

    attribute_map = {
        'contract_id': 'contractId',
        'brand_name': 'brandName',
        'company_cnpj': 'companyCnpj',
        'product_type': 'productType',
        'product_sub_type': 'productSubType',
        'ipoc_code': 'ipocCode'
    }

    def __init__(self, contract_id=None, brand_name=None, company_cnpj=None, product_type=None, product_sub_type=None, ipoc_code=None):  # noqa: E501
        """LoansListContract - a model defined in Swagger"""  # noqa: E501
        self._contract_id = None
        self._brand_name = None
        self._company_cnpj = None
        self._product_type = None
        self._product_sub_type = None
        self._ipoc_code = None
        self.discriminator = None
        self.contract_id = contract_id
        self.brand_name = brand_name
        self.company_cnpj = company_cnpj
        self.product_type = product_type
        self.product_sub_type = product_sub_type
        self.ipoc_code = ipoc_code

    @property
    def contract_id(self):
        """Gets the contract_id of this LoansListContract.  # noqa: E501

        Identifica de forma única o contrato da operação de crédito do cliente, mantendo as regras de imutabilidade dentro da instituição transmissora.  # noqa: E501

        :return: The contract_id of this LoansListContract.  # noqa: E501
        :rtype: str
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this LoansListContract.

        Identifica de forma única o contrato da operação de crédito do cliente, mantendo as regras de imutabilidade dentro da instituição transmissora.  # noqa: E501

        :param contract_id: The contract_id of this LoansListContract.  # noqa: E501
        :type: str
        """
        if contract_id is None:
            raise ValueError("Invalid value for `contract_id`, must not be `None`")  # noqa: E501

        self._contract_id = contract_id

    @property
    def brand_name(self):
        """Gets the brand_name of this LoansListContract.  # noqa: E501

        Nome da Marca reportada pelo participante no Open Finance. Recomenda-se utilizar, sempre que possível, o mesmo nome de marca atribuído no campo do diretório Customer Friendly Server Name (Authorisation Server).  # noqa: E501

        :return: The brand_name of this LoansListContract.  # noqa: E501
        :rtype: str
        """
        return self._brand_name

    @brand_name.setter
    def brand_name(self, brand_name):
        """Sets the brand_name of this LoansListContract.

        Nome da Marca reportada pelo participante no Open Finance. Recomenda-se utilizar, sempre que possível, o mesmo nome de marca atribuído no campo do diretório Customer Friendly Server Name (Authorisation Server).  # noqa: E501

        :param brand_name: The brand_name of this LoansListContract.  # noqa: E501
        :type: str
        """
        if brand_name is None:
            raise ValueError("Invalid value for `brand_name`, must not be `None`")  # noqa: E501

        self._brand_name = brand_name

    @property
    def company_cnpj(self):
        """Gets the company_cnpj of this LoansListContract.  # noqa: E501

        Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara.  # noqa: E501

        :return: The company_cnpj of this LoansListContract.  # noqa: E501
        :rtype: str
        """
        return self._company_cnpj

    @company_cnpj.setter
    def company_cnpj(self, company_cnpj):
        """Sets the company_cnpj of this LoansListContract.

        Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara.  # noqa: E501

        :param company_cnpj: The company_cnpj of this LoansListContract.  # noqa: E501
        :type: str
        """
        if company_cnpj is None:
            raise ValueError("Invalid value for `company_cnpj`, must not be `None`")  # noqa: E501

        self._company_cnpj = company_cnpj

    @property
    def product_type(self):
        """Gets the product_type of this LoansListContract.  # noqa: E501


        :return: The product_type of this LoansListContract.  # noqa: E501
        :rtype: EnumContractProductTypeLoans
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this LoansListContract.


        :param product_type: The product_type of this LoansListContract.  # noqa: E501
        :type: EnumContractProductTypeLoans
        """
        if product_type is None:
            raise ValueError("Invalid value for `product_type`, must not be `None`")  # noqa: E501

        self._product_type = product_type

    @property
    def product_sub_type(self):
        """Gets the product_sub_type of this LoansListContract.  # noqa: E501


        :return: The product_sub_type of this LoansListContract.  # noqa: E501
        :rtype: EnumContractProductSubTypeLoans
        """
        return self._product_sub_type

    @product_sub_type.setter
    def product_sub_type(self, product_sub_type):
        """Sets the product_sub_type of this LoansListContract.


        :param product_sub_type: The product_sub_type of this LoansListContract.  # noqa: E501
        :type: EnumContractProductSubTypeLoans
        """
        if product_sub_type is None:
            raise ValueError("Invalid value for `product_sub_type`, must not be `None`")  # noqa: E501

        self._product_sub_type = product_sub_type

    @property
    def ipoc_code(self):
        """Gets the ipoc_code of this LoansListContract.  # noqa: E501

        Número padronizado do contrato - IPOC (Identificação Padronizada da Operação de Crédito). Segundo DOC 3040, composta por: - **CNPJ da instituição:** 8 (oito) posições iniciais; - **Modalidade da operação:** 4 (quatro) posições; - **Tipo do cliente:** 1 (uma) posição( 1 = pessoa natural - CPF, 2= pessoa jurídica – CNPJ, 3 = pessoa física no exterior, 4 = pessoa jurídica no exterior, 5 = pessoa natural sem CPF e 6 = pessoa jurídica sem CNPJ); - **Código do cliente:** O número de posições varia conforme o tipo do cliente:   1. Para clientes pessoa física com CPF (tipo de cliente = 1), informar as 11 (onze) posições do CPF;   2. Para clientes pessoa jurídica com CNPJ (tipo de cliente = 2), informar as 8 (oito) posições iniciais do CNPJ;   3. Para os demais clientes (tipos de cliente 3, 4, 5 e 6), informar 14 (catorze) posições com complemento de zeros à esquerda se a identificação tiver tamanho inferior; - **Código do contrato:** 1 (uma) até 40 (quarenta) posições, sem complemento de caracteres.   # noqa: E501

        :return: The ipoc_code of this LoansListContract.  # noqa: E501
        :rtype: str
        """
        return self._ipoc_code

    @ipoc_code.setter
    def ipoc_code(self, ipoc_code):
        """Sets the ipoc_code of this LoansListContract.

        Número padronizado do contrato - IPOC (Identificação Padronizada da Operação de Crédito). Segundo DOC 3040, composta por: - **CNPJ da instituição:** 8 (oito) posições iniciais; - **Modalidade da operação:** 4 (quatro) posições; - **Tipo do cliente:** 1 (uma) posição( 1 = pessoa natural - CPF, 2= pessoa jurídica – CNPJ, 3 = pessoa física no exterior, 4 = pessoa jurídica no exterior, 5 = pessoa natural sem CPF e 6 = pessoa jurídica sem CNPJ); - **Código do cliente:** O número de posições varia conforme o tipo do cliente:   1. Para clientes pessoa física com CPF (tipo de cliente = 1), informar as 11 (onze) posições do CPF;   2. Para clientes pessoa jurídica com CNPJ (tipo de cliente = 2), informar as 8 (oito) posições iniciais do CNPJ;   3. Para os demais clientes (tipos de cliente 3, 4, 5 e 6), informar 14 (catorze) posições com complemento de zeros à esquerda se a identificação tiver tamanho inferior; - **Código do contrato:** 1 (uma) até 40 (quarenta) posições, sem complemento de caracteres.   # noqa: E501

        :param ipoc_code: The ipoc_code of this LoansListContract.  # noqa: E501
        :type: str
        """
        if ipoc_code is None:
            raise ValueError("Invalid value for `ipoc_code`, must not be `None`")  # noqa: E501

        self._ipoc_code = ipoc_code

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
        if issubclass(LoansListContract, dict):
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
        if not isinstance(other, LoansListContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
