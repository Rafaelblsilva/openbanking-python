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

class LoansContract(object):
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
        'contract_number': 'str',
        'ipoc_code': 'str',
        'product_name': 'str',
        'product_type': 'EnumContractProductTypeLoans',
        'product_sub_type': 'EnumContractProductSubTypeLoans',
        'contract_date': 'date',
        'disbursement_date': 'date',
        'settlement_date': 'date',
        'contract_amount': 'float',
        'currency': 'str',
        'due_date': 'date',
        'instalment_periodicity': 'EnumContractInstalmentPeriodicity',
        'instalment_periodicity_additional_info': 'str',
        'first_instalment_due_date': 'date',
        'cet': 'float',
        'amortization_scheduled': 'EnumContractAmortizationScheduled',
        'amortization_scheduled_additional_info': 'str',
        'cnpj_consignee': 'str',
        'interest_rates': 'list[LoansContractInterestRate]',
        'contracted_fees': 'list[LoansContractedFee]',
        'contracted_finance_charges': 'list[LoansFinanceCharge]'
    }

    attribute_map = {
        'contract_number': 'contractNumber',
        'ipoc_code': 'ipocCode',
        'product_name': 'productName',
        'product_type': 'productType',
        'product_sub_type': 'productSubType',
        'contract_date': 'contractDate',
        'disbursement_date': 'disbursementDate',
        'settlement_date': 'settlementDate',
        'contract_amount': 'contractAmount',
        'currency': 'currency',
        'due_date': 'dueDate',
        'instalment_periodicity': 'instalmentPeriodicity',
        'instalment_periodicity_additional_info': 'instalmentPeriodicityAdditionalInfo',
        'first_instalment_due_date': 'firstInstalmentDueDate',
        'cet': 'CET',
        'amortization_scheduled': 'amortizationScheduled',
        'amortization_scheduled_additional_info': 'amortizationScheduledAdditionalInfo',
        'cnpj_consignee': 'cnpjConsignee',
        'interest_rates': 'interestRates',
        'contracted_fees': 'contractedFees',
        'contracted_finance_charges': 'contractedFinanceCharges'
    }

    def __init__(self, contract_number=None, ipoc_code=None, product_name=None, product_type=None, product_sub_type=None, contract_date=None, disbursement_date=None, settlement_date=None, contract_amount=None, currency=None, due_date=None, instalment_periodicity=None, instalment_periodicity_additional_info=None, first_instalment_due_date=None, cet=None, amortization_scheduled=None, amortization_scheduled_additional_info=None, cnpj_consignee=None, interest_rates=None, contracted_fees=None, contracted_finance_charges=None):  # noqa: E501
        """LoansContract - a model defined in Swagger"""  # noqa: E501
        self._contract_number = None
        self._ipoc_code = None
        self._product_name = None
        self._product_type = None
        self._product_sub_type = None
        self._contract_date = None
        self._disbursement_date = None
        self._settlement_date = None
        self._contract_amount = None
        self._currency = None
        self._due_date = None
        self._instalment_periodicity = None
        self._instalment_periodicity_additional_info = None
        self._first_instalment_due_date = None
        self._cet = None
        self._amortization_scheduled = None
        self._amortization_scheduled_additional_info = None
        self._cnpj_consignee = None
        self._interest_rates = None
        self._contracted_fees = None
        self._contracted_finance_charges = None
        self.discriminator = None
        self.contract_number = contract_number
        self.ipoc_code = ipoc_code
        self.product_name = product_name
        self.product_type = product_type
        self.product_sub_type = product_sub_type
        self.contract_date = contract_date
        if disbursement_date is not None:
            self.disbursement_date = disbursement_date
        self.settlement_date = settlement_date
        self.contract_amount = contract_amount
        self.currency = currency
        self.due_date = due_date
        self.instalment_periodicity = instalment_periodicity
        self.instalment_periodicity_additional_info = instalment_periodicity_additional_info
        self.first_instalment_due_date = first_instalment_due_date
        self.cet = cet
        self.amortization_scheduled = amortization_scheduled
        self.amortization_scheduled_additional_info = amortization_scheduled_additional_info
        self.cnpj_consignee = cnpj_consignee
        self.interest_rates = interest_rates
        self.contracted_fees = contracted_fees
        self.contracted_finance_charges = contracted_finance_charges

    @property
    def contract_number(self):
        """Gets the contract_number of this LoansContract.  # noqa: E501

        Número do contrato dado pela instituição contratante.  # noqa: E501

        :return: The contract_number of this LoansContract.  # noqa: E501
        :rtype: str
        """
        return self._contract_number

    @contract_number.setter
    def contract_number(self, contract_number):
        """Sets the contract_number of this LoansContract.

        Número do contrato dado pela instituição contratante.  # noqa: E501

        :param contract_number: The contract_number of this LoansContract.  # noqa: E501
        :type: str
        """
        if contract_number is None:
            raise ValueError("Invalid value for `contract_number`, must not be `None`")  # noqa: E501

        self._contract_number = contract_number

    @property
    def ipoc_code(self):
        """Gets the ipoc_code of this LoansContract.  # noqa: E501

        Número padronizado do contrato - IPOC (Identificação Padronizada da Operação de Crédito). Segundo DOC 3040, composta por: - **CNPJ da instituição:** 8 (oito) posições iniciais; - **Modalidade da operação:** 4 (quatro) posições; - **Tipo do cliente:** 1 (uma) posição( 1 = pessoa natural - CPF, 2= pessoa jurídica – CNPJ, 3 = pessoa física no exterior, 4 = pessoa jurídica no exterior, 5 = pessoa natural sem CPF e 6 = pessoa jurídica sem CNPJ); - **Código do cliente:** O número de posições varia conforme o tipo do cliente:   1. Para clientes pessoa física com CPF (tipo de cliente = 1), informar as 11 (onze) posições do CPF;   2. Para clientes pessoa jurídica com CNPJ (tipo de cliente = 2), informar as 8 (oito) posições iniciais do CNPJ;   3. Para os demais clientes (tipos de cliente 3, 4, 5 e 6), informar 14 (catorze) posições com complemento de zeros à esquerda se a identificação tiver tamanho inferior; - **Código do contrato:** 1 (uma) até 40 (quarenta) posições, sem complemento de caracteres.   # noqa: E501

        :return: The ipoc_code of this LoansContract.  # noqa: E501
        :rtype: str
        """
        return self._ipoc_code

    @ipoc_code.setter
    def ipoc_code(self, ipoc_code):
        """Sets the ipoc_code of this LoansContract.

        Número padronizado do contrato - IPOC (Identificação Padronizada da Operação de Crédito). Segundo DOC 3040, composta por: - **CNPJ da instituição:** 8 (oito) posições iniciais; - **Modalidade da operação:** 4 (quatro) posições; - **Tipo do cliente:** 1 (uma) posição( 1 = pessoa natural - CPF, 2= pessoa jurídica – CNPJ, 3 = pessoa física no exterior, 4 = pessoa jurídica no exterior, 5 = pessoa natural sem CPF e 6 = pessoa jurídica sem CNPJ); - **Código do cliente:** O número de posições varia conforme o tipo do cliente:   1. Para clientes pessoa física com CPF (tipo de cliente = 1), informar as 11 (onze) posições do CPF;   2. Para clientes pessoa jurídica com CNPJ (tipo de cliente = 2), informar as 8 (oito) posições iniciais do CNPJ;   3. Para os demais clientes (tipos de cliente 3, 4, 5 e 6), informar 14 (catorze) posições com complemento de zeros à esquerda se a identificação tiver tamanho inferior; - **Código do contrato:** 1 (uma) até 40 (quarenta) posições, sem complemento de caracteres.   # noqa: E501

        :param ipoc_code: The ipoc_code of this LoansContract.  # noqa: E501
        :type: str
        """
        if ipoc_code is None:
            raise ValueError("Invalid value for `ipoc_code`, must not be `None`")  # noqa: E501

        self._ipoc_code = ipoc_code

    @property
    def product_name(self):
        """Gets the product_name of this LoansContract.  # noqa: E501

        Denominação/Identificação do nome da Modalidade da Operação de Crédito divulgado ao cliente   # noqa: E501

        :return: The product_name of this LoansContract.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this LoansContract.

        Denominação/Identificação do nome da Modalidade da Operação de Crédito divulgado ao cliente   # noqa: E501

        :param product_name: The product_name of this LoansContract.  # noqa: E501
        :type: str
        """
        if product_name is None:
            raise ValueError("Invalid value for `product_name`, must not be `None`")  # noqa: E501

        self._product_name = product_name

    @property
    def product_type(self):
        """Gets the product_type of this LoansContract.  # noqa: E501


        :return: The product_type of this LoansContract.  # noqa: E501
        :rtype: EnumContractProductTypeLoans
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this LoansContract.


        :param product_type: The product_type of this LoansContract.  # noqa: E501
        :type: EnumContractProductTypeLoans
        """
        if product_type is None:
            raise ValueError("Invalid value for `product_type`, must not be `None`")  # noqa: E501

        self._product_type = product_type

    @property
    def product_sub_type(self):
        """Gets the product_sub_type of this LoansContract.  # noqa: E501


        :return: The product_sub_type of this LoansContract.  # noqa: E501
        :rtype: EnumContractProductSubTypeLoans
        """
        return self._product_sub_type

    @product_sub_type.setter
    def product_sub_type(self, product_sub_type):
        """Sets the product_sub_type of this LoansContract.


        :param product_sub_type: The product_sub_type of this LoansContract.  # noqa: E501
        :type: EnumContractProductSubTypeLoans
        """
        if product_sub_type is None:
            raise ValueError("Invalid value for `product_sub_type`, must not be `None`")  # noqa: E501

        self._product_sub_type = product_sub_type

    @property
    def contract_date(self):
        """Gets the contract_date of this LoansContract.  # noqa: E501

        Data de contratação da operação de crédito. Especificação RFC-3339  # noqa: E501

        :return: The contract_date of this LoansContract.  # noqa: E501
        :rtype: date
        """
        return self._contract_date

    @contract_date.setter
    def contract_date(self, contract_date):
        """Sets the contract_date of this LoansContract.

        Data de contratação da operação de crédito. Especificação RFC-3339  # noqa: E501

        :param contract_date: The contract_date of this LoansContract.  # noqa: E501
        :type: date
        """
        if contract_date is None:
            raise ValueError("Invalid value for `contract_date`, must not be `None`")  # noqa: E501

        self._contract_date = contract_date

    @property
    def disbursement_date(self):
        """Gets the disbursement_date of this LoansContract.  # noqa: E501

        Data do Desembolso do valor contratado. Especificação RFC-3339  # noqa: E501

        :return: The disbursement_date of this LoansContract.  # noqa: E501
        :rtype: date
        """
        return self._disbursement_date

    @disbursement_date.setter
    def disbursement_date(self, disbursement_date):
        """Sets the disbursement_date of this LoansContract.

        Data do Desembolso do valor contratado. Especificação RFC-3339  # noqa: E501

        :param disbursement_date: The disbursement_date of this LoansContract.  # noqa: E501
        :type: date
        """

        self._disbursement_date = disbursement_date

    @property
    def settlement_date(self):
        """Gets the settlement_date of this LoansContract.  # noqa: E501

        Data de liquidação da operação. [Restrição] Deve aceitar NA caso não seja retornado pela instituição.   # noqa: E501

        :return: The settlement_date of this LoansContract.  # noqa: E501
        :rtype: date
        """
        return self._settlement_date

    @settlement_date.setter
    def settlement_date(self, settlement_date):
        """Sets the settlement_date of this LoansContract.

        Data de liquidação da operação. [Restrição] Deve aceitar NA caso não seja retornado pela instituição.   # noqa: E501

        :param settlement_date: The settlement_date of this LoansContract.  # noqa: E501
        :type: date
        """
        if settlement_date is None:
            raise ValueError("Invalid value for `settlement_date`, must not be `None`")  # noqa: E501

        self._settlement_date = settlement_date

    @property
    def contract_amount(self):
        """Gets the contract_amount of this LoansContract.  # noqa: E501

        Valor contratado da operação. Expresso em valor monetário com até 4 casas decimais  # noqa: E501

        :return: The contract_amount of this LoansContract.  # noqa: E501
        :rtype: float
        """
        return self._contract_amount

    @contract_amount.setter
    def contract_amount(self, contract_amount):
        """Sets the contract_amount of this LoansContract.

        Valor contratado da operação. Expresso em valor monetário com até 4 casas decimais  # noqa: E501

        :param contract_amount: The contract_amount of this LoansContract.  # noqa: E501
        :type: float
        """
        if contract_amount is None:
            raise ValueError("Invalid value for `contract_amount`, must not be `None`")  # noqa: E501

        self._contract_amount = contract_amount

    @property
    def currency(self):
        """Gets the currency of this LoansContract.  # noqa: E501

        Moeda referente ao valor da garantia, segundo modelo ISO-4217. p.ex. 'BRL' Todos os valores monetários informados estão representados com a moeda vigente do Brasil   # noqa: E501

        :return: The currency of this LoansContract.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this LoansContract.

        Moeda referente ao valor da garantia, segundo modelo ISO-4217. p.ex. 'BRL' Todos os valores monetários informados estão representados com a moeda vigente do Brasil   # noqa: E501

        :param currency: The currency of this LoansContract.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def due_date(self):
        """Gets the due_date of this LoansContract.  # noqa: E501

        Data de vencimento Final da operação. Especificação RFC-3339  # noqa: E501

        :return: The due_date of this LoansContract.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this LoansContract.

        Data de vencimento Final da operação. Especificação RFC-3339  # noqa: E501

        :param due_date: The due_date of this LoansContract.  # noqa: E501
        :type: date
        """
        if due_date is None:
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

    @property
    def instalment_periodicity(self):
        """Gets the instalment_periodicity of this LoansContract.  # noqa: E501


        :return: The instalment_periodicity of this LoansContract.  # noqa: E501
        :rtype: EnumContractInstalmentPeriodicity
        """
        return self._instalment_periodicity

    @instalment_periodicity.setter
    def instalment_periodicity(self, instalment_periodicity):
        """Sets the instalment_periodicity of this LoansContract.


        :param instalment_periodicity: The instalment_periodicity of this LoansContract.  # noqa: E501
        :type: EnumContractInstalmentPeriodicity
        """
        if instalment_periodicity is None:
            raise ValueError("Invalid value for `instalment_periodicity`, must not be `None`")  # noqa: E501

        self._instalment_periodicity = instalment_periodicity

    @property
    def instalment_periodicity_additional_info(self):
        """Gets the instalment_periodicity_additional_info of this LoansContract.  # noqa: E501

        Campo obrigatório para complementar a informação relativa à periodicidade de pagamento regular quando tiver a opção OUTROS. [Restrição] Obrigatório para complementar a informação relativa da periodicidade de pagamento regular, quando selecionada o tipo ou subtipo OUTRO.          # noqa: E501

        :return: The instalment_periodicity_additional_info of this LoansContract.  # noqa: E501
        :rtype: str
        """
        return self._instalment_periodicity_additional_info

    @instalment_periodicity_additional_info.setter
    def instalment_periodicity_additional_info(self, instalment_periodicity_additional_info):
        """Sets the instalment_periodicity_additional_info of this LoansContract.

        Campo obrigatório para complementar a informação relativa à periodicidade de pagamento regular quando tiver a opção OUTROS. [Restrição] Obrigatório para complementar a informação relativa da periodicidade de pagamento regular, quando selecionada o tipo ou subtipo OUTRO.          # noqa: E501

        :param instalment_periodicity_additional_info: The instalment_periodicity_additional_info of this LoansContract.  # noqa: E501
        :type: str
        """
        if instalment_periodicity_additional_info is None:
            raise ValueError("Invalid value for `instalment_periodicity_additional_info`, must not be `None`")  # noqa: E501

        self._instalment_periodicity_additional_info = instalment_periodicity_additional_info

    @property
    def first_instalment_due_date(self):
        """Gets the first_instalment_due_date of this LoansContract.  # noqa: E501

        Data de vencimento primeira parcela do principal  # noqa: E501

        :return: The first_instalment_due_date of this LoansContract.  # noqa: E501
        :rtype: date
        """
        return self._first_instalment_due_date

    @first_instalment_due_date.setter
    def first_instalment_due_date(self, first_instalment_due_date):
        """Sets the first_instalment_due_date of this LoansContract.

        Data de vencimento primeira parcela do principal  # noqa: E501

        :param first_instalment_due_date: The first_instalment_due_date of this LoansContract.  # noqa: E501
        :type: date
        """
        if first_instalment_due_date is None:
            raise ValueError("Invalid value for `first_instalment_due_date`, must not be `None`")  # noqa: E501

        self._first_instalment_due_date = first_instalment_due_date

    @property
    def cet(self):
        """Gets the cet of this LoansContract.  # noqa: E501

        CET – Custo Efetivo Total deve ser expresso na forma de taxa percentual anual e   incorpora todos os encargos e despesas incidentes nas operações de crédito (taxa de juro, mas também tarifas, tributos, seguros e outras despesas cobradas). O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)   # noqa: E501

        :return: The cet of this LoansContract.  # noqa: E501
        :rtype: float
        """
        return self._cet

    @cet.setter
    def cet(self, cet):
        """Sets the cet of this LoansContract.

        CET – Custo Efetivo Total deve ser expresso na forma de taxa percentual anual e   incorpora todos os encargos e despesas incidentes nas operações de crédito (taxa de juro, mas também tarifas, tributos, seguros e outras despesas cobradas). O preenchimento deve respeitar as 4 casas decimais, mesmo que venham preenchidas com zeros (representação de porcentagem p.ex: 0.1500. Este valor representa 15%. O valor 1 representa 100%)   # noqa: E501

        :param cet: The cet of this LoansContract.  # noqa: E501
        :type: float
        """
        if cet is None:
            raise ValueError("Invalid value for `cet`, must not be `None`")  # noqa: E501

        self._cet = cet

    @property
    def amortization_scheduled(self):
        """Gets the amortization_scheduled of this LoansContract.  # noqa: E501


        :return: The amortization_scheduled of this LoansContract.  # noqa: E501
        :rtype: EnumContractAmortizationScheduled
        """
        return self._amortization_scheduled

    @amortization_scheduled.setter
    def amortization_scheduled(self, amortization_scheduled):
        """Sets the amortization_scheduled of this LoansContract.


        :param amortization_scheduled: The amortization_scheduled of this LoansContract.  # noqa: E501
        :type: EnumContractAmortizationScheduled
        """
        if amortization_scheduled is None:
            raise ValueError("Invalid value for `amortization_scheduled`, must not be `None`")  # noqa: E501

        self._amortization_scheduled = amortization_scheduled

    @property
    def amortization_scheduled_additional_info(self):
        """Gets the amortization_scheduled_additional_info of this LoansContract.  # noqa: E501

        Campo obrigatório para complementar a informação relativa à amortização quando selecionada a opção OUTROS. [Restrição] Obrigatório para complementar a informação relativa à amortização quando selecionada a opção OUTROS, para os demais casos informar \"NA\".          # noqa: E501

        :return: The amortization_scheduled_additional_info of this LoansContract.  # noqa: E501
        :rtype: str
        """
        return self._amortization_scheduled_additional_info

    @amortization_scheduled_additional_info.setter
    def amortization_scheduled_additional_info(self, amortization_scheduled_additional_info):
        """Sets the amortization_scheduled_additional_info of this LoansContract.

        Campo obrigatório para complementar a informação relativa à amortização quando selecionada a opção OUTROS. [Restrição] Obrigatório para complementar a informação relativa à amortização quando selecionada a opção OUTROS, para os demais casos informar \"NA\".          # noqa: E501

        :param amortization_scheduled_additional_info: The amortization_scheduled_additional_info of this LoansContract.  # noqa: E501
        :type: str
        """
        if amortization_scheduled_additional_info is None:
            raise ValueError("Invalid value for `amortization_scheduled_additional_info`, must not be `None`")  # noqa: E501

        self._amortization_scheduled_additional_info = amortization_scheduled_additional_info

    @property
    def cnpj_consignee(self):
        """Gets the cnpj_consignee of this LoansContract.  # noqa: E501

        CNPJ do consignante (CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica). Deve-se ter apenas os números do CNPJ, sem máscara. Informação adicional específica para Modalidade de Crédito: Empréstimo-Crédito Pessoal Consignado   # noqa: E501

        :return: The cnpj_consignee of this LoansContract.  # noqa: E501
        :rtype: str
        """
        return self._cnpj_consignee

    @cnpj_consignee.setter
    def cnpj_consignee(self, cnpj_consignee):
        """Sets the cnpj_consignee of this LoansContract.

        CNPJ do consignante (CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica). Deve-se ter apenas os números do CNPJ, sem máscara. Informação adicional específica para Modalidade de Crédito: Empréstimo-Crédito Pessoal Consignado   # noqa: E501

        :param cnpj_consignee: The cnpj_consignee of this LoansContract.  # noqa: E501
        :type: str
        """
        if cnpj_consignee is None:
            raise ValueError("Invalid value for `cnpj_consignee`, must not be `None`")  # noqa: E501

        self._cnpj_consignee = cnpj_consignee

    @property
    def interest_rates(self):
        """Gets the interest_rates of this LoansContract.  # noqa: E501


        :return: The interest_rates of this LoansContract.  # noqa: E501
        :rtype: list[LoansContractInterestRate]
        """
        return self._interest_rates

    @interest_rates.setter
    def interest_rates(self, interest_rates):
        """Sets the interest_rates of this LoansContract.


        :param interest_rates: The interest_rates of this LoansContract.  # noqa: E501
        :type: list[LoansContractInterestRate]
        """
        if interest_rates is None:
            raise ValueError("Invalid value for `interest_rates`, must not be `None`")  # noqa: E501

        self._interest_rates = interest_rates

    @property
    def contracted_fees(self):
        """Gets the contracted_fees of this LoansContract.  # noqa: E501


        :return: The contracted_fees of this LoansContract.  # noqa: E501
        :rtype: list[LoansContractedFee]
        """
        return self._contracted_fees

    @contracted_fees.setter
    def contracted_fees(self, contracted_fees):
        """Sets the contracted_fees of this LoansContract.


        :param contracted_fees: The contracted_fees of this LoansContract.  # noqa: E501
        :type: list[LoansContractedFee]
        """
        if contracted_fees is None:
            raise ValueError("Invalid value for `contracted_fees`, must not be `None`")  # noqa: E501

        self._contracted_fees = contracted_fees

    @property
    def contracted_finance_charges(self):
        """Gets the contracted_finance_charges of this LoansContract.  # noqa: E501

        Lista que traz os encargos pactuados no contrato  # noqa: E501

        :return: The contracted_finance_charges of this LoansContract.  # noqa: E501
        :rtype: list[LoansFinanceCharge]
        """
        return self._contracted_finance_charges

    @contracted_finance_charges.setter
    def contracted_finance_charges(self, contracted_finance_charges):
        """Sets the contracted_finance_charges of this LoansContract.

        Lista que traz os encargos pactuados no contrato  # noqa: E501

        :param contracted_finance_charges: The contracted_finance_charges of this LoansContract.  # noqa: E501
        :type: list[LoansFinanceCharge]
        """
        if contracted_finance_charges is None:
            raise ValueError("Invalid value for `contracted_finance_charges`, must not be `None`")  # noqa: E501

        self._contracted_finance_charges = contracted_finance_charges

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
        if issubclass(LoansContract, dict):
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
        if not isinstance(other, LoansContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
