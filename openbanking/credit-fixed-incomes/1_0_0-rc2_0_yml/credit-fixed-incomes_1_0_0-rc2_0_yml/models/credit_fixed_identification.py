# coding: utf-8

"""
    API Credit Fixed Incomes - Open Finance Brasil

    API de informações de operações de Renda Fixa Crédito do Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Renda Fixa Crédito (Debêntures, CRI/CRA) mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação do produto, rentabilidade, quantidade, prazos, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. A exposição se dará por cada operação de renda fixa contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreditFixedIdentification(object):
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
        'issuer_institution_cnpj_number': 'str',
        'isin_code': 'str',
        'investment_type': 'EnumInvestimentType',
        'debtor_cnpj_number': 'str',
        'debtor_name': 'str',
        'tax_exempt_product': 'EnumTaxExemptProduct',
        'remuneration': 'Remuneration',
        'issue_unit_price': 'IssueUnitPrice',
        'issue_date': 'date',
        'due_date': 'date',
        'voucher_payment_indicator': 'VoucherPaymentIndicator',
        'voucher_payment_periodicity': 'VoucherPaymentPeriodicity',
        'voucher_payment_periodicity_additional_info': 'str',
        'clearing_code': 'str',
        'purchase_date': 'date',
        'grace_period_date': 'date'
    }

    attribute_map = {
        'issuer_institution_cnpj_number': 'issuerInstitutionCnpjNumber',
        'isin_code': 'isinCode',
        'investment_type': 'investmentType',
        'debtor_cnpj_number': 'debtorCnpjNumber',
        'debtor_name': 'debtorName',
        'tax_exempt_product': 'taxExemptProduct',
        'remuneration': 'remuneration',
        'issue_unit_price': 'issueUnitPrice',
        'issue_date': 'issueDate',
        'due_date': 'dueDate',
        'voucher_payment_indicator': 'voucherPaymentIndicator',
        'voucher_payment_periodicity': 'voucherPaymentPeriodicity',
        'voucher_payment_periodicity_additional_info': 'voucherPaymentPeriodicityAdditionalInfo',
        'clearing_code': 'clearingCode',
        'purchase_date': 'purchaseDate',
        'grace_period_date': 'gracePeriodDate'
    }

    def __init__(self, issuer_institution_cnpj_number=None, isin_code=None, investment_type=None, debtor_cnpj_number=None, debtor_name=None, tax_exempt_product=None, remuneration=None, issue_unit_price=None, issue_date=None, due_date=None, voucher_payment_indicator=None, voucher_payment_periodicity=None, voucher_payment_periodicity_additional_info=None, clearing_code=None, purchase_date=None, grace_period_date=None):  # noqa: E501
        """CreditFixedIdentification - a model defined in Swagger"""  # noqa: E501
        self._issuer_institution_cnpj_number = None
        self._isin_code = None
        self._investment_type = None
        self._debtor_cnpj_number = None
        self._debtor_name = None
        self._tax_exempt_product = None
        self._remuneration = None
        self._issue_unit_price = None
        self._issue_date = None
        self._due_date = None
        self._voucher_payment_indicator = None
        self._voucher_payment_periodicity = None
        self._voucher_payment_periodicity_additional_info = None
        self._clearing_code = None
        self._purchase_date = None
        self._grace_period_date = None
        self.discriminator = None
        self.issuer_institution_cnpj_number = issuer_institution_cnpj_number
        if isin_code is not None:
            self.isin_code = isin_code
        self.investment_type = investment_type
        if debtor_cnpj_number is not None:
            self.debtor_cnpj_number = debtor_cnpj_number
        if debtor_name is not None:
            self.debtor_name = debtor_name
        self.tax_exempt_product = tax_exempt_product
        self.remuneration = remuneration
        self.issue_unit_price = issue_unit_price
        self.issue_date = issue_date
        self.due_date = due_date
        self.voucher_payment_indicator = voucher_payment_indicator
        if voucher_payment_periodicity is not None:
            self.voucher_payment_periodicity = voucher_payment_periodicity
        if voucher_payment_periodicity_additional_info is not None:
            self.voucher_payment_periodicity_additional_info = voucher_payment_periodicity_additional_info
        if clearing_code is not None:
            self.clearing_code = clearing_code
        self.purchase_date = purchase_date
        self.grace_period_date = grace_period_date

    @property
    def issuer_institution_cnpj_number(self):
        """Gets the issuer_institution_cnpj_number of this CreditFixedIdentification.  # noqa: E501

        CNPJ da instituição emissora  # noqa: E501

        :return: The issuer_institution_cnpj_number of this CreditFixedIdentification.  # noqa: E501
        :rtype: str
        """
        return self._issuer_institution_cnpj_number

    @issuer_institution_cnpj_number.setter
    def issuer_institution_cnpj_number(self, issuer_institution_cnpj_number):
        """Sets the issuer_institution_cnpj_number of this CreditFixedIdentification.

        CNPJ da instituição emissora  # noqa: E501

        :param issuer_institution_cnpj_number: The issuer_institution_cnpj_number of this CreditFixedIdentification.  # noqa: E501
        :type: str
        """
        if issuer_institution_cnpj_number is None:
            raise ValueError("Invalid value for `issuer_institution_cnpj_number`, must not be `None`")  # noqa: E501

        self._issuer_institution_cnpj_number = issuer_institution_cnpj_number

    @property
    def isin_code(self):
        """Gets the isin_code of this CreditFixedIdentification.  # noqa: E501

        Código ISIN é um código universal que identifica cada valor mobiliário ou instrumento financeiro, conforme Norma ISO 6166. Caso a transmissora possua a informação o envio deste campo é obrigatório.  [Restrição] Deve ser preenchido nos casos em que o 'clearingCode' não seja preenchido.   # noqa: E501

        :return: The isin_code of this CreditFixedIdentification.  # noqa: E501
        :rtype: str
        """
        return self._isin_code

    @isin_code.setter
    def isin_code(self, isin_code):
        """Sets the isin_code of this CreditFixedIdentification.

        Código ISIN é um código universal que identifica cada valor mobiliário ou instrumento financeiro, conforme Norma ISO 6166. Caso a transmissora possua a informação o envio deste campo é obrigatório.  [Restrição] Deve ser preenchido nos casos em que o 'clearingCode' não seja preenchido.   # noqa: E501

        :param isin_code: The isin_code of this CreditFixedIdentification.  # noqa: E501
        :type: str
        """

        self._isin_code = isin_code

    @property
    def investment_type(self):
        """Gets the investment_type of this CreditFixedIdentification.  # noqa: E501


        :return: The investment_type of this CreditFixedIdentification.  # noqa: E501
        :rtype: EnumInvestimentType
        """
        return self._investment_type

    @investment_type.setter
    def investment_type(self, investment_type):
        """Sets the investment_type of this CreditFixedIdentification.


        :param investment_type: The investment_type of this CreditFixedIdentification.  # noqa: E501
        :type: EnumInvestimentType
        """
        if investment_type is None:
            raise ValueError("Invalid value for `investment_type`, must not be `None`")  # noqa: E501

        self._investment_type = investment_type

    @property
    def debtor_cnpj_number(self):
        """Gets the debtor_cnpj_number of this CreditFixedIdentification.  # noqa: E501

        CNPJ do devedor. Caso a transmissora possua a informação para os produtos CRI e CRA, o envio deste campo é obrigatório.   # noqa: E501

        :return: The debtor_cnpj_number of this CreditFixedIdentification.  # noqa: E501
        :rtype: str
        """
        return self._debtor_cnpj_number

    @debtor_cnpj_number.setter
    def debtor_cnpj_number(self, debtor_cnpj_number):
        """Sets the debtor_cnpj_number of this CreditFixedIdentification.

        CNPJ do devedor. Caso a transmissora possua a informação para os produtos CRI e CRA, o envio deste campo é obrigatório.   # noqa: E501

        :param debtor_cnpj_number: The debtor_cnpj_number of this CreditFixedIdentification.  # noqa: E501
        :type: str
        """

        self._debtor_cnpj_number = debtor_cnpj_number

    @property
    def debtor_name(self):
        """Gets the debtor_name of this CreditFixedIdentification.  # noqa: E501

        Nome do devedor. Caso a transmissora possua a informação para os produtos CRI e CRA, o envio deste campo é obrigatório.   # noqa: E501

        :return: The debtor_name of this CreditFixedIdentification.  # noqa: E501
        :rtype: str
        """
        return self._debtor_name

    @debtor_name.setter
    def debtor_name(self, debtor_name):
        """Sets the debtor_name of this CreditFixedIdentification.

        Nome do devedor. Caso a transmissora possua a informação para os produtos CRI e CRA, o envio deste campo é obrigatório.   # noqa: E501

        :param debtor_name: The debtor_name of this CreditFixedIdentification.  # noqa: E501
        :type: str
        """

        self._debtor_name = debtor_name

    @property
    def tax_exempt_product(self):
        """Gets the tax_exempt_product of this CreditFixedIdentification.  # noqa: E501


        :return: The tax_exempt_product of this CreditFixedIdentification.  # noqa: E501
        :rtype: EnumTaxExemptProduct
        """
        return self._tax_exempt_product

    @tax_exempt_product.setter
    def tax_exempt_product(self, tax_exempt_product):
        """Sets the tax_exempt_product of this CreditFixedIdentification.


        :param tax_exempt_product: The tax_exempt_product of this CreditFixedIdentification.  # noqa: E501
        :type: EnumTaxExemptProduct
        """
        if tax_exempt_product is None:
            raise ValueError("Invalid value for `tax_exempt_product`, must not be `None`")  # noqa: E501

        self._tax_exempt_product = tax_exempt_product

    @property
    def remuneration(self):
        """Gets the remuneration of this CreditFixedIdentification.  # noqa: E501


        :return: The remuneration of this CreditFixedIdentification.  # noqa: E501
        :rtype: Remuneration
        """
        return self._remuneration

    @remuneration.setter
    def remuneration(self, remuneration):
        """Sets the remuneration of this CreditFixedIdentification.


        :param remuneration: The remuneration of this CreditFixedIdentification.  # noqa: E501
        :type: Remuneration
        """
        if remuneration is None:
            raise ValueError("Invalid value for `remuneration`, must not be `None`")  # noqa: E501

        self._remuneration = remuneration

    @property
    def issue_unit_price(self):
        """Gets the issue_unit_price of this CreditFixedIdentification.  # noqa: E501


        :return: The issue_unit_price of this CreditFixedIdentification.  # noqa: E501
        :rtype: IssueUnitPrice
        """
        return self._issue_unit_price

    @issue_unit_price.setter
    def issue_unit_price(self, issue_unit_price):
        """Sets the issue_unit_price of this CreditFixedIdentification.


        :param issue_unit_price: The issue_unit_price of this CreditFixedIdentification.  # noqa: E501
        :type: IssueUnitPrice
        """
        if issue_unit_price is None:
            raise ValueError("Invalid value for `issue_unit_price`, must not be `None`")  # noqa: E501

        self._issue_unit_price = issue_unit_price

    @property
    def issue_date(self):
        """Gets the issue_date of this CreditFixedIdentification.  # noqa: E501

        Data de emissão do título  # noqa: E501

        :return: The issue_date of this CreditFixedIdentification.  # noqa: E501
        :rtype: date
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this CreditFixedIdentification.

        Data de emissão do título  # noqa: E501

        :param issue_date: The issue_date of this CreditFixedIdentification.  # noqa: E501
        :type: date
        """
        if issue_date is None:
            raise ValueError("Invalid value for `issue_date`, must not be `None`")  # noqa: E501

        self._issue_date = issue_date

    @property
    def due_date(self):
        """Gets the due_date of this CreditFixedIdentification.  # noqa: E501

        Data de vencimento do título  # noqa: E501

        :return: The due_date of this CreditFixedIdentification.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this CreditFixedIdentification.

        Data de vencimento do título  # noqa: E501

        :param due_date: The due_date of this CreditFixedIdentification.  # noqa: E501
        :type: date
        """
        if due_date is None:
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

    @property
    def voucher_payment_indicator(self):
        """Gets the voucher_payment_indicator of this CreditFixedIdentification.  # noqa: E501


        :return: The voucher_payment_indicator of this CreditFixedIdentification.  # noqa: E501
        :rtype: VoucherPaymentIndicator
        """
        return self._voucher_payment_indicator

    @voucher_payment_indicator.setter
    def voucher_payment_indicator(self, voucher_payment_indicator):
        """Sets the voucher_payment_indicator of this CreditFixedIdentification.


        :param voucher_payment_indicator: The voucher_payment_indicator of this CreditFixedIdentification.  # noqa: E501
        :type: VoucherPaymentIndicator
        """
        if voucher_payment_indicator is None:
            raise ValueError("Invalid value for `voucher_payment_indicator`, must not be `None`")  # noqa: E501

        self._voucher_payment_indicator = voucher_payment_indicator

    @property
    def voucher_payment_periodicity(self):
        """Gets the voucher_payment_periodicity of this CreditFixedIdentification.  # noqa: E501


        :return: The voucher_payment_periodicity of this CreditFixedIdentification.  # noqa: E501
        :rtype: VoucherPaymentPeriodicity
        """
        return self._voucher_payment_periodicity

    @voucher_payment_periodicity.setter
    def voucher_payment_periodicity(self, voucher_payment_periodicity):
        """Sets the voucher_payment_periodicity of this CreditFixedIdentification.


        :param voucher_payment_periodicity: The voucher_payment_periodicity of this CreditFixedIdentification.  # noqa: E501
        :type: VoucherPaymentPeriodicity
        """

        self._voucher_payment_periodicity = voucher_payment_periodicity

    @property
    def voucher_payment_periodicity_additional_info(self):
        """Gets the voucher_payment_periodicity_additional_info of this CreditFixedIdentification.  # noqa: E501

        Informações adicionais da periodicidade de pagamento de cupom   [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver 'Outros' no campo 'voucherPaymentPeriodicity'.   # noqa: E501

        :return: The voucher_payment_periodicity_additional_info of this CreditFixedIdentification.  # noqa: E501
        :rtype: str
        """
        return self._voucher_payment_periodicity_additional_info

    @voucher_payment_periodicity_additional_info.setter
    def voucher_payment_periodicity_additional_info(self, voucher_payment_periodicity_additional_info):
        """Sets the voucher_payment_periodicity_additional_info of this CreditFixedIdentification.

        Informações adicionais da periodicidade de pagamento de cupom   [Restrição] Campo de preenchimento obrigatório pelas participantes quando houver 'Outros' no campo 'voucherPaymentPeriodicity'.   # noqa: E501

        :param voucher_payment_periodicity_additional_info: The voucher_payment_periodicity_additional_info of this CreditFixedIdentification.  # noqa: E501
        :type: str
        """

        self._voucher_payment_periodicity_additional_info = voucher_payment_periodicity_additional_info

    @property
    def clearing_code(self):
        """Gets the clearing_code of this CreditFixedIdentification.  # noqa: E501

        Código de registro do ativo na Clearing. Caso a transmissora possua a informação o envio deste campo é obrigatório.  [Restrição] Deve ser preenchido nos casos em que o 'isinCode' não seja preenchido.   # noqa: E501

        :return: The clearing_code of this CreditFixedIdentification.  # noqa: E501
        :rtype: str
        """
        return self._clearing_code

    @clearing_code.setter
    def clearing_code(self, clearing_code):
        """Sets the clearing_code of this CreditFixedIdentification.

        Código de registro do ativo na Clearing. Caso a transmissora possua a informação o envio deste campo é obrigatório.  [Restrição] Deve ser preenchido nos casos em que o 'isinCode' não seja preenchido.   # noqa: E501

        :param clearing_code: The clearing_code of this CreditFixedIdentification.  # noqa: E501
        :type: str
        """

        self._clearing_code = clearing_code

    @property
    def purchase_date(self):
        """Gets the purchase_date of this CreditFixedIdentification.  # noqa: E501

        Data de aquisição do cliente  # noqa: E501

        :return: The purchase_date of this CreditFixedIdentification.  # noqa: E501
        :rtype: date
        """
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, purchase_date):
        """Sets the purchase_date of this CreditFixedIdentification.

        Data de aquisição do cliente  # noqa: E501

        :param purchase_date: The purchase_date of this CreditFixedIdentification.  # noqa: E501
        :type: date
        """
        if purchase_date is None:
            raise ValueError("Invalid value for `purchase_date`, must not be `None`")  # noqa: E501

        self._purchase_date = purchase_date

    @property
    def grace_period_date(self):
        """Gets the grace_period_date of this CreditFixedIdentification.  # noqa: E501

        Data até a qual o cliente não poderá resgatar antecipadamente seu investimento  # noqa: E501

        :return: The grace_period_date of this CreditFixedIdentification.  # noqa: E501
        :rtype: date
        """
        return self._grace_period_date

    @grace_period_date.setter
    def grace_period_date(self, grace_period_date):
        """Sets the grace_period_date of this CreditFixedIdentification.

        Data até a qual o cliente não poderá resgatar antecipadamente seu investimento  # noqa: E501

        :param grace_period_date: The grace_period_date of this CreditFixedIdentification.  # noqa: E501
        :type: date
        """
        if grace_period_date is None:
            raise ValueError("Invalid value for `grace_period_date`, must not be `None`")  # noqa: E501

        self._grace_period_date = grace_period_date

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
        if issubclass(CreditFixedIdentification, dict):
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
        if not isinstance(other, CreditFixedIdentification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
