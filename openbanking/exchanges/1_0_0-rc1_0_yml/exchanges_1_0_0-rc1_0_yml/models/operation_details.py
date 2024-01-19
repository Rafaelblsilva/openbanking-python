# coding: utf-8

"""
    API Exchanges - Open Finance Brasil

    API de informações de operações de Câmbio Open Finance Brasil – Fase 4.  API que retorna informações de operações de Câmbio realizadas nas instituições transmissoras por seus clientes, incluindo dados como informações da operação contratada, valor da operação em moeda nacional e moeda estrangeira, classificação da operação, forma de entrega, VET e, quando aplicável, valor a liquidar.  Também serão compartilhados os eventos de alteração da operação, caso existam, com as informações modificadas.  Não possui segregação entre pessoa natural e pessoa jurídica.  Requer consentimento do cliente para todos os endpoints.  __São escopo de compartilhamento as operações de compra e venda de moeda estrangeira de liquidação pronta ou futura, inclusive com adiantamento.  Operações de câmbio anuladas não são escopo de exposição, bem como eventos de vinculação de operações.  A exposição se dará por cada operação de câmbio contratada pelo cliente.__   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class OperationDetails(object):
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
        'authorized_institution_cnpj_number': 'str',
        'authorized_institution_name': 'str',
        'intermediary_institution_cnpj_number': 'str',
        'intemediary_institution_name': 'str',
        'operation_number': 'str',
        'operation_type': 'EnumExchangesOperationType',
        'operation_date': 'datetime',
        'due_date': 'date',
        'local_currency_operation_tax': 'OperationDetailsLocalCurrencyOperationTax',
        'local_currency_operation_value': 'OperationDetailsLocalCurrencyOperationValue',
        'foreign_operation_value': 'OperationDetailsForeignOperationValue',
        'operation_outstanding_balance': 'OperationDetailsOperationOutstandingBalance',
        'vet_amount': 'OperationDetailsVetAmount',
        'local_currency_advance_percentage': 'str',
        'delivery_foreign_currency': 'EnumExchangesDeliveryForeignCurrency',
        'operation_category_code': 'str',
        'relationship_code': 'str',
        'foreign_partie_name': 'str',
        'foreign_partie_country_code': 'str'
    }

    attribute_map = {
        'authorized_institution_cnpj_number': 'authorizedInstitutionCnpjNumber',
        'authorized_institution_name': 'authorizedInstitutionName',
        'intermediary_institution_cnpj_number': 'intermediaryInstitutionCnpjNumber',
        'intemediary_institution_name': 'intemediaryInstitutionName',
        'operation_number': 'operationNumber',
        'operation_type': 'operationType',
        'operation_date': 'operationDate',
        'due_date': 'dueDate',
        'local_currency_operation_tax': 'localCurrencyOperationTax',
        'local_currency_operation_value': 'localCurrencyOperationValue',
        'foreign_operation_value': 'foreignOperationValue',
        'operation_outstanding_balance': 'operationOutstandingBalance',
        'vet_amount': 'vetAmount',
        'local_currency_advance_percentage': 'localCurrencyAdvancePercentage',
        'delivery_foreign_currency': 'deliveryForeignCurrency',
        'operation_category_code': 'operationCategoryCode',
        'relationship_code': 'relationshipCode',
        'foreign_partie_name': 'foreignPartieName',
        'foreign_partie_country_code': 'foreignPartieCountryCode'
    }

    def __init__(self, authorized_institution_cnpj_number=None, authorized_institution_name=None, intermediary_institution_cnpj_number=None, intemediary_institution_name=None, operation_number=None, operation_type=None, operation_date=None, due_date=None, local_currency_operation_tax=None, local_currency_operation_value=None, foreign_operation_value=None, operation_outstanding_balance=None, vet_amount=None, local_currency_advance_percentage=None, delivery_foreign_currency=None, operation_category_code=None, relationship_code=None, foreign_partie_name=None, foreign_partie_country_code=None):  # noqa: E501
        """OperationDetails - a model defined in Swagger"""  # noqa: E501
        self._authorized_institution_cnpj_number = None
        self._authorized_institution_name = None
        self._intermediary_institution_cnpj_number = None
        self._intemediary_institution_name = None
        self._operation_number = None
        self._operation_type = None
        self._operation_date = None
        self._due_date = None
        self._local_currency_operation_tax = None
        self._local_currency_operation_value = None
        self._foreign_operation_value = None
        self._operation_outstanding_balance = None
        self._vet_amount = None
        self._local_currency_advance_percentage = None
        self._delivery_foreign_currency = None
        self._operation_category_code = None
        self._relationship_code = None
        self._foreign_partie_name = None
        self._foreign_partie_country_code = None
        self.discriminator = None
        self.authorized_institution_cnpj_number = authorized_institution_cnpj_number
        self.authorized_institution_name = authorized_institution_name
        if intermediary_institution_cnpj_number is not None:
            self.intermediary_institution_cnpj_number = intermediary_institution_cnpj_number
        if intemediary_institution_name is not None:
            self.intemediary_institution_name = intemediary_institution_name
        if operation_number is not None:
            self.operation_number = operation_number
        self.operation_type = operation_type
        self.operation_date = operation_date
        self.due_date = due_date
        self.local_currency_operation_tax = local_currency_operation_tax
        self.local_currency_operation_value = local_currency_operation_value
        self.foreign_operation_value = foreign_operation_value
        if operation_outstanding_balance is not None:
            self.operation_outstanding_balance = operation_outstanding_balance
        if vet_amount is not None:
            self.vet_amount = vet_amount
        if local_currency_advance_percentage is not None:
            self.local_currency_advance_percentage = local_currency_advance_percentage
        self.delivery_foreign_currency = delivery_foreign_currency
        self.operation_category_code = operation_category_code
        if relationship_code is not None:
            self.relationship_code = relationship_code
        if foreign_partie_name is not None:
            self.foreign_partie_name = foreign_partie_name
        if foreign_partie_country_code is not None:
            self.foreign_partie_country_code = foreign_partie_country_code

    @property
    def authorized_institution_cnpj_number(self):
        """Gets the authorized_institution_cnpj_number of this OperationDetails.  # noqa: E501

        CNPJ da instituição autorizada a operar no mercado de câmbio.  # noqa: E501

        :return: The authorized_institution_cnpj_number of this OperationDetails.  # noqa: E501
        :rtype: str
        """
        return self._authorized_institution_cnpj_number

    @authorized_institution_cnpj_number.setter
    def authorized_institution_cnpj_number(self, authorized_institution_cnpj_number):
        """Sets the authorized_institution_cnpj_number of this OperationDetails.

        CNPJ da instituição autorizada a operar no mercado de câmbio.  # noqa: E501

        :param authorized_institution_cnpj_number: The authorized_institution_cnpj_number of this OperationDetails.  # noqa: E501
        :type: str
        """
        if authorized_institution_cnpj_number is None:
            raise ValueError("Invalid value for `authorized_institution_cnpj_number`, must not be `None`")  # noqa: E501

        self._authorized_institution_cnpj_number = authorized_institution_cnpj_number

    @property
    def authorized_institution_name(self):
        """Gets the authorized_institution_name of this OperationDetails.  # noqa: E501

        Nome da Instituição Financeira no Brasil.  # noqa: E501

        :return: The authorized_institution_name of this OperationDetails.  # noqa: E501
        :rtype: str
        """
        return self._authorized_institution_name

    @authorized_institution_name.setter
    def authorized_institution_name(self, authorized_institution_name):
        """Sets the authorized_institution_name of this OperationDetails.

        Nome da Instituição Financeira no Brasil.  # noqa: E501

        :param authorized_institution_name: The authorized_institution_name of this OperationDetails.  # noqa: E501
        :type: str
        """
        if authorized_institution_name is None:
            raise ValueError("Invalid value for `authorized_institution_name`, must not be `None`")  # noqa: E501

        self._authorized_institution_name = authorized_institution_name

    @property
    def intermediary_institution_cnpj_number(self):
        """Gets the intermediary_institution_cnpj_number of this OperationDetails.  # noqa: E501

        CNPJ da instituição intermediadora autorizada a operar no mercado de câmbio.  Campo de envio obrigatório nos casos em que houver instituição intermediadora.   # noqa: E501

        :return: The intermediary_institution_cnpj_number of this OperationDetails.  # noqa: E501
        :rtype: str
        """
        return self._intermediary_institution_cnpj_number

    @intermediary_institution_cnpj_number.setter
    def intermediary_institution_cnpj_number(self, intermediary_institution_cnpj_number):
        """Sets the intermediary_institution_cnpj_number of this OperationDetails.

        CNPJ da instituição intermediadora autorizada a operar no mercado de câmbio.  Campo de envio obrigatório nos casos em que houver instituição intermediadora.   # noqa: E501

        :param intermediary_institution_cnpj_number: The intermediary_institution_cnpj_number of this OperationDetails.  # noqa: E501
        :type: str
        """

        self._intermediary_institution_cnpj_number = intermediary_institution_cnpj_number

    @property
    def intemediary_institution_name(self):
        """Gets the intemediary_institution_name of this OperationDetails.  # noqa: E501

        Nome da corretora interveniente autorizada a operar no mercado de câmbio.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo 'intermediaryInstitutionCnpjNumber' for informado.   # noqa: E501

        :return: The intemediary_institution_name of this OperationDetails.  # noqa: E501
        :rtype: str
        """
        return self._intemediary_institution_name

    @intemediary_institution_name.setter
    def intemediary_institution_name(self, intemediary_institution_name):
        """Sets the intemediary_institution_name of this OperationDetails.

        Nome da corretora interveniente autorizada a operar no mercado de câmbio.  [Restrição] Campo de preenchimento obrigatório pelas participantes quando o campo 'intermediaryInstitutionCnpjNumber' for informado.   # noqa: E501

        :param intemediary_institution_name: The intemediary_institution_name of this OperationDetails.  # noqa: E501
        :type: str
        """

        self._intemediary_institution_name = intemediary_institution_name

    @property
    def operation_number(self):
        """Gets the operation_number of this OperationDetails.  # noqa: E501

        Número do registro da operação no Bacen. Deve ser preenchido no compartilhamento, após registro no Sistema de Câmbio e número disponível na transmissora/detentora.  # noqa: E501

        :return: The operation_number of this OperationDetails.  # noqa: E501
        :rtype: str
        """
        return self._operation_number

    @operation_number.setter
    def operation_number(self, operation_number):
        """Sets the operation_number of this OperationDetails.

        Número do registro da operação no Bacen. Deve ser preenchido no compartilhamento, após registro no Sistema de Câmbio e número disponível na transmissora/detentora.  # noqa: E501

        :param operation_number: The operation_number of this OperationDetails.  # noqa: E501
        :type: str
        """

        self._operation_number = operation_number

    @property
    def operation_type(self):
        """Gets the operation_type of this OperationDetails.  # noqa: E501


        :return: The operation_type of this OperationDetails.  # noqa: E501
        :rtype: EnumExchangesOperationType
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this OperationDetails.


        :param operation_type: The operation_type of this OperationDetails.  # noqa: E501
        :type: EnumExchangesOperationType
        """
        if operation_type is None:
            raise ValueError("Invalid value for `operation_type`, must not be `None`")  # noqa: E501

        self._operation_type = operation_type

    @property
    def operation_date(self):
        """Gets the operation_date of this OperationDetails.  # noqa: E501

        Data do fechamento do contrato de câmbio.  # noqa: E501

        :return: The operation_date of this OperationDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._operation_date

    @operation_date.setter
    def operation_date(self, operation_date):
        """Sets the operation_date of this OperationDetails.

        Data do fechamento do contrato de câmbio.  # noqa: E501

        :param operation_date: The operation_date of this OperationDetails.  # noqa: E501
        :type: datetime
        """
        if operation_date is None:
            raise ValueError("Invalid value for `operation_date`, must not be `None`")  # noqa: E501

        self._operation_date = operation_date

    @property
    def due_date(self):
        """Gets the due_date of this OperationDetails.  # noqa: E501

        Data em que a operação (compra ou venda) está prevista para ser liquidada.  # noqa: E501

        :return: The due_date of this OperationDetails.  # noqa: E501
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this OperationDetails.

        Data em que a operação (compra ou venda) está prevista para ser liquidada.  # noqa: E501

        :param due_date: The due_date of this OperationDetails.  # noqa: E501
        :type: date
        """
        if due_date is None:
            raise ValueError("Invalid value for `due_date`, must not be `None`")  # noqa: E501

        self._due_date = due_date

    @property
    def local_currency_operation_tax(self):
        """Gets the local_currency_operation_tax of this OperationDetails.  # noqa: E501


        :return: The local_currency_operation_tax of this OperationDetails.  # noqa: E501
        :rtype: OperationDetailsLocalCurrencyOperationTax
        """
        return self._local_currency_operation_tax

    @local_currency_operation_tax.setter
    def local_currency_operation_tax(self, local_currency_operation_tax):
        """Sets the local_currency_operation_tax of this OperationDetails.


        :param local_currency_operation_tax: The local_currency_operation_tax of this OperationDetails.  # noqa: E501
        :type: OperationDetailsLocalCurrencyOperationTax
        """
        if local_currency_operation_tax is None:
            raise ValueError("Invalid value for `local_currency_operation_tax`, must not be `None`")  # noqa: E501

        self._local_currency_operation_tax = local_currency_operation_tax

    @property
    def local_currency_operation_value(self):
        """Gets the local_currency_operation_value of this OperationDetails.  # noqa: E501


        :return: The local_currency_operation_value of this OperationDetails.  # noqa: E501
        :rtype: OperationDetailsLocalCurrencyOperationValue
        """
        return self._local_currency_operation_value

    @local_currency_operation_value.setter
    def local_currency_operation_value(self, local_currency_operation_value):
        """Sets the local_currency_operation_value of this OperationDetails.


        :param local_currency_operation_value: The local_currency_operation_value of this OperationDetails.  # noqa: E501
        :type: OperationDetailsLocalCurrencyOperationValue
        """
        if local_currency_operation_value is None:
            raise ValueError("Invalid value for `local_currency_operation_value`, must not be `None`")  # noqa: E501

        self._local_currency_operation_value = local_currency_operation_value

    @property
    def foreign_operation_value(self):
        """Gets the foreign_operation_value of this OperationDetails.  # noqa: E501


        :return: The foreign_operation_value of this OperationDetails.  # noqa: E501
        :rtype: OperationDetailsForeignOperationValue
        """
        return self._foreign_operation_value

    @foreign_operation_value.setter
    def foreign_operation_value(self, foreign_operation_value):
        """Sets the foreign_operation_value of this OperationDetails.


        :param foreign_operation_value: The foreign_operation_value of this OperationDetails.  # noqa: E501
        :type: OperationDetailsForeignOperationValue
        """
        if foreign_operation_value is None:
            raise ValueError("Invalid value for `foreign_operation_value`, must not be `None`")  # noqa: E501

        self._foreign_operation_value = foreign_operation_value

    @property
    def operation_outstanding_balance(self):
        """Gets the operation_outstanding_balance of this OperationDetails.  # noqa: E501


        :return: The operation_outstanding_balance of this OperationDetails.  # noqa: E501
        :rtype: OperationDetailsOperationOutstandingBalance
        """
        return self._operation_outstanding_balance

    @operation_outstanding_balance.setter
    def operation_outstanding_balance(self, operation_outstanding_balance):
        """Sets the operation_outstanding_balance of this OperationDetails.


        :param operation_outstanding_balance: The operation_outstanding_balance of this OperationDetails.  # noqa: E501
        :type: OperationDetailsOperationOutstandingBalance
        """

        self._operation_outstanding_balance = operation_outstanding_balance

    @property
    def vet_amount(self):
        """Gets the vet_amount of this OperationDetails.  # noqa: E501


        :return: The vet_amount of this OperationDetails.  # noqa: E501
        :rtype: OperationDetailsVetAmount
        """
        return self._vet_amount

    @vet_amount.setter
    def vet_amount(self, vet_amount):
        """Sets the vet_amount of this OperationDetails.


        :param vet_amount: The vet_amount of this OperationDetails.  # noqa: E501
        :type: OperationDetailsVetAmount
        """

        self._vet_amount = vet_amount

    @property
    def local_currency_advance_percentage(self):
        """Gets the local_currency_advance_percentage of this OperationDetails.  # noqa: E501

        Percentual do valor de moeda nacional concedido ao cliente antecipadamente. p.ex. 0.014500.  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%). Campos de envio obrigatório no caso de operações de câmbio com liquidação futura.   # noqa: E501

        :return: The local_currency_advance_percentage of this OperationDetails.  # noqa: E501
        :rtype: str
        """
        return self._local_currency_advance_percentage

    @local_currency_advance_percentage.setter
    def local_currency_advance_percentage(self, local_currency_advance_percentage):
        """Sets the local_currency_advance_percentage of this OperationDetails.

        Percentual do valor de moeda nacional concedido ao cliente antecipadamente. p.ex. 0.014500.  O preenchimento deve respeitar as 6 casas decimais, mesmo que venham preenchidas com zeros(representação de porcentagem p.ex: 0.150000. Este valor representa 15%. O valor 1 representa 100%). Campos de envio obrigatório no caso de operações de câmbio com liquidação futura.   # noqa: E501

        :param local_currency_advance_percentage: The local_currency_advance_percentage of this OperationDetails.  # noqa: E501
        :type: str
        """

        self._local_currency_advance_percentage = local_currency_advance_percentage

    @property
    def delivery_foreign_currency(self):
        """Gets the delivery_foreign_currency of this OperationDetails.  # noqa: E501


        :return: The delivery_foreign_currency of this OperationDetails.  # noqa: E501
        :rtype: EnumExchangesDeliveryForeignCurrency
        """
        return self._delivery_foreign_currency

    @delivery_foreign_currency.setter
    def delivery_foreign_currency(self, delivery_foreign_currency):
        """Sets the delivery_foreign_currency of this OperationDetails.


        :param delivery_foreign_currency: The delivery_foreign_currency of this OperationDetails.  # noqa: E501
        :type: EnumExchangesDeliveryForeignCurrency
        """
        if delivery_foreign_currency is None:
            raise ValueError("Invalid value for `delivery_foreign_currency`, must not be `None`")  # noqa: E501

        self._delivery_foreign_currency = delivery_foreign_currency

    @property
    def operation_category_code(self):
        """Gets the operation_category_code of this OperationDetails.  # noqa: E501

        Código da natureza fato do fechamento da operação. Deve respeitar os códigos de natureza referenciados na resolução 277 ou na Circular 3690, conforme se aplicar ao contrato de câmbio.  # noqa: E501

        :return: The operation_category_code of this OperationDetails.  # noqa: E501
        :rtype: str
        """
        return self._operation_category_code

    @operation_category_code.setter
    def operation_category_code(self, operation_category_code):
        """Sets the operation_category_code of this OperationDetails.

        Código da natureza fato do fechamento da operação. Deve respeitar os códigos de natureza referenciados na resolução 277 ou na Circular 3690, conforme se aplicar ao contrato de câmbio.  # noqa: E501

        :param operation_category_code: The operation_category_code of this OperationDetails.  # noqa: E501
        :type: str
        """
        if operation_category_code is None:
            raise ValueError("Invalid value for `operation_category_code`, must not be `None`")  # noqa: E501

        self._operation_category_code = operation_category_code

    @property
    def relationship_code(self):
        """Gets the relationship_code of this OperationDetails.  # noqa: E501

        Código de Relação de vínculo entre o Cliente e o Pagador/Recebedor no Exterior. Deve respeitar os códigos de vínculo referenciados na resolução 277 ou na Circular 3690, conforme se aplicar ao contrato de câmbio.  [Restrição] Campo de preenchimento opcional pelas participantes quando o campo 'deliveryForeignCurrency ' for igual EM ESPÉCIE E/OU CHEQUES DE VIAGEM.   # noqa: E501

        :return: The relationship_code of this OperationDetails.  # noqa: E501
        :rtype: str
        """
        return self._relationship_code

    @relationship_code.setter
    def relationship_code(self, relationship_code):
        """Sets the relationship_code of this OperationDetails.

        Código de Relação de vínculo entre o Cliente e o Pagador/Recebedor no Exterior. Deve respeitar os códigos de vínculo referenciados na resolução 277 ou na Circular 3690, conforme se aplicar ao contrato de câmbio.  [Restrição] Campo de preenchimento opcional pelas participantes quando o campo 'deliveryForeignCurrency ' for igual EM ESPÉCIE E/OU CHEQUES DE VIAGEM.   # noqa: E501

        :param relationship_code: The relationship_code of this OperationDetails.  # noqa: E501
        :type: str
        """

        self._relationship_code = relationship_code

    @property
    def foreign_partie_name(self):
        """Gets the foreign_partie_name of this OperationDetails.  # noqa: E501

        Nome do pagador ou recebedor no exterior.  [Restrição] Campo de preenchimento opcional pelas participantes quando o campo 'deliveryForeignCurrency ' for igual EM ESPÉCIE E/OU CHEQUES DE VIAGEM.   # noqa: E501

        :return: The foreign_partie_name of this OperationDetails.  # noqa: E501
        :rtype: str
        """
        return self._foreign_partie_name

    @foreign_partie_name.setter
    def foreign_partie_name(self, foreign_partie_name):
        """Sets the foreign_partie_name of this OperationDetails.

        Nome do pagador ou recebedor no exterior.  [Restrição] Campo de preenchimento opcional pelas participantes quando o campo 'deliveryForeignCurrency ' for igual EM ESPÉCIE E/OU CHEQUES DE VIAGEM.   # noqa: E501

        :param foreign_partie_name: The foreign_partie_name of this OperationDetails.  # noqa: E501
        :type: str
        """

        self._foreign_partie_name = foreign_partie_name

    @property
    def foreign_partie_country_code(self):
        """Gets the foreign_partie_country_code of this OperationDetails.  # noqa: E501

        País do pagador ou recebedor. Código do país segundo a norma ISO 3166-1.  [Restrição] Campo de preenchimento opcional pelas participantes quando o campo 'deliveryForeignCurrency ' for igual EM ESPÉCIE E/OU CHEQUES DE VIAGEM.   # noqa: E501

        :return: The foreign_partie_country_code of this OperationDetails.  # noqa: E501
        :rtype: str
        """
        return self._foreign_partie_country_code

    @foreign_partie_country_code.setter
    def foreign_partie_country_code(self, foreign_partie_country_code):
        """Sets the foreign_partie_country_code of this OperationDetails.

        País do pagador ou recebedor. Código do país segundo a norma ISO 3166-1.  [Restrição] Campo de preenchimento opcional pelas participantes quando o campo 'deliveryForeignCurrency ' for igual EM ESPÉCIE E/OU CHEQUES DE VIAGEM.   # noqa: E501

        :param foreign_partie_country_code: The foreign_partie_country_code of this OperationDetails.  # noqa: E501
        :type: str
        """

        self._foreign_partie_country_code = foreign_partie_country_code

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
        if issubclass(OperationDetails, dict):
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
        if not isinstance(other, OperationDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
