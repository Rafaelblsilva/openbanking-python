# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil. Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API: - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil. Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`. Esta API não requer a implementação de `permissions` para sua utilização. Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:  - Certificados exigidos para assinatura de mensagens: [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Como assinar o payload JWS: [https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload](https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload)  ## Controle de acesso  O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).  Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.   # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponsePixPaymentData(object):
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
        'payment_id': 'str',
        'end_to_end_id': 'EndToEndId',
        'consent_id': 'str',
        'creation_date_time': 'datetime',
        'status_update_date_time': 'datetime',
        'proxy': 'str',
        'ibge_town_code': 'str',
        'status': 'EnumPaymentStatusType',
        'rejection_reason': 'EnumRejectionReasonType',
        'local_instrument': 'CreatePixPaymentDatapropertieslocalInstrument',
        'cnpj_initiator': 'str',
        'payment': 'PaymentPix',
        'transaction_identification': 'str',
        'remittance_information': 'str',
        'creditor_account': 'CreditorAccount'
    }

    attribute_map = {
        'payment_id': 'paymentId',
        'end_to_end_id': 'endToEndId',
        'consent_id': 'consentId',
        'creation_date_time': 'creationDateTime',
        'status_update_date_time': 'statusUpdateDateTime',
        'proxy': 'proxy',
        'ibge_town_code': 'ibgeTownCode',
        'status': 'status',
        'rejection_reason': 'rejectionReason',
        'local_instrument': 'localInstrument',
        'cnpj_initiator': 'cnpjInitiator',
        'payment': 'payment',
        'transaction_identification': 'transactionIdentification',
        'remittance_information': 'remittanceInformation',
        'creditor_account': 'creditorAccount'
    }

    def __init__(self, payment_id=None, end_to_end_id=None, consent_id=None, creation_date_time=None, status_update_date_time=None, proxy=None, ibge_town_code=None, status=None, rejection_reason=None, local_instrument=None, cnpj_initiator=None, payment=None, transaction_identification=None, remittance_information=None, creditor_account=None):  # noqa: E501
        """ResponsePixPaymentData - a model defined in Swagger"""  # noqa: E501
        self._payment_id = None
        self._end_to_end_id = None
        self._consent_id = None
        self._creation_date_time = None
        self._status_update_date_time = None
        self._proxy = None
        self._ibge_town_code = None
        self._status = None
        self._rejection_reason = None
        self._local_instrument = None
        self._cnpj_initiator = None
        self._payment = None
        self._transaction_identification = None
        self._remittance_information = None
        self._creditor_account = None
        self.discriminator = None
        self.payment_id = payment_id
        if end_to_end_id is not None:
            self.end_to_end_id = end_to_end_id
        self.consent_id = consent_id
        self.creation_date_time = creation_date_time
        self.status_update_date_time = status_update_date_time
        if proxy is not None:
            self.proxy = proxy
        if ibge_town_code is not None:
            self.ibge_town_code = ibge_town_code
        self.status = status
        if rejection_reason is not None:
            self.rejection_reason = rejection_reason
        self.local_instrument = local_instrument
        self.cnpj_initiator = cnpj_initiator
        self.payment = payment
        if transaction_identification is not None:
            self.transaction_identification = transaction_identification
        if remittance_information is not None:
            self.remittance_information = remittance_information
        self.creditor_account = creditor_account

    @property
    def payment_id(self):
        """Gets the payment_id of this ResponsePixPaymentData.  # noqa: E501

        Código ou identificador único informado pela instituição detentora da conta para representar a iniciação de pagamento individual. O `paymentId` deve ser diferente do `endToEndId`. Este é o identificador que deverá ser utilizado na consulta ao status da iniciação de pagamento efetuada.   # noqa: E501

        :return: The payment_id of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this ResponsePixPaymentData.

        Código ou identificador único informado pela instituição detentora da conta para representar a iniciação de pagamento individual. O `paymentId` deve ser diferente do `endToEndId`. Este é o identificador que deverá ser utilizado na consulta ao status da iniciação de pagamento efetuada.   # noqa: E501

        :param payment_id: The payment_id of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """
        if payment_id is None:
            raise ValueError("Invalid value for `payment_id`, must not be `None`")  # noqa: E501

        self._payment_id = payment_id

    @property
    def end_to_end_id(self):
        """Gets the end_to_end_id of this ResponsePixPaymentData.  # noqa: E501


        :return: The end_to_end_id of this ResponsePixPaymentData.  # noqa: E501
        :rtype: EndToEndId
        """
        return self._end_to_end_id

    @end_to_end_id.setter
    def end_to_end_id(self, end_to_end_id):
        """Sets the end_to_end_id of this ResponsePixPaymentData.


        :param end_to_end_id: The end_to_end_id of this ResponsePixPaymentData.  # noqa: E501
        :type: EndToEndId
        """

        self._end_to_end_id = end_to_end_id

    @property
    def consent_id(self):
        """Gets the consent_id of this ResponsePixPaymentData.  # noqa: E501

        Identificador único do consentimento criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).   # noqa: E501

        :return: The consent_id of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this ResponsePixPaymentData.

        Identificador único do consentimento criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).   # noqa: E501

        :param consent_id: The consent_id of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """
        if consent_id is None:
            raise ValueError("Invalid value for `consent_id`, must not be `None`")  # noqa: E501

        self._consent_id = consent_id

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this ResponsePixPaymentData.  # noqa: E501

        Data e hora em que o recurso foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :return: The creation_date_time of this ResponsePixPaymentData.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this ResponsePixPaymentData.

        Data e hora em que o recurso foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :param creation_date_time: The creation_date_time of this ResponsePixPaymentData.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def status_update_date_time(self):
        """Gets the status_update_date_time of this ResponsePixPaymentData.  # noqa: E501

        Data e hora da última atualização da iniciação de pagamento. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :return: The status_update_date_time of this ResponsePixPaymentData.  # noqa: E501
        :rtype: datetime
        """
        return self._status_update_date_time

    @status_update_date_time.setter
    def status_update_date_time(self, status_update_date_time):
        """Sets the status_update_date_time of this ResponsePixPaymentData.

        Data e hora da última atualização da iniciação de pagamento. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :param status_update_date_time: The status_update_date_time of this ResponsePixPaymentData.  # noqa: E501
        :type: datetime
        """
        if status_update_date_time is None:
            raise ValueError("Invalid value for `status_update_date_time`, must not be `None`")  # noqa: E501

        self._status_update_date_time = status_update_date_time

    @property
    def proxy(self):
        """Gets the proxy of this ResponsePixPaymentData.  # noqa: E501

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória. No caso de telefone celular deve ser informado no padrão E.1641. Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres. No caso de CPF deverá ser informado com 11 números, sem pontos ou traços. Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços. No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223. Se informado, a detentora da conta deve validar o proxy no DICT quando localInstrument for igual a DICT, QRDN ou QRES e validar o campo creditorAccount. Esta validação é opcional caso o localInstrument for igual a INIC. [Restrição] Se localInstrument for igual a MANU, o campo proxy não deve ser preenchido. Se localInstrument for igual INIC, DICT, QRDN ou QRES, o campo proxy deve ser sempre preenchido com a chave Pix.   # noqa: E501

        :return: The proxy of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this ResponsePixPaymentData.

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória. No caso de telefone celular deve ser informado no padrão E.1641. Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres. No caso de CPF deverá ser informado com 11 números, sem pontos ou traços. Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços. No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223. Se informado, a detentora da conta deve validar o proxy no DICT quando localInstrument for igual a DICT, QRDN ou QRES e validar o campo creditorAccount. Esta validação é opcional caso o localInstrument for igual a INIC. [Restrição] Se localInstrument for igual a MANU, o campo proxy não deve ser preenchido. Se localInstrument for igual INIC, DICT, QRDN ou QRES, o campo proxy deve ser sempre preenchido com a chave Pix.   # noqa: E501

        :param proxy: The proxy of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    @property
    def ibge_town_code(self):
        """Gets the ibge_town_code of this ResponsePixPaymentData.  # noqa: E501

        Traz o código da cidade segundo o IBGE (Instituto Brasileiro de Geografia e Estatística). Para o preenchimento deste campo, o Iniciador de Pagamentos deve seguir a orientação do arranjo da forma de pagamento. O preenchimento do campo tanto em pix/payments quanto /consents deve ser igual. Caso haja divergência dos valores, a instituição deve retornar HTTP 422 com o código de erro PAGAMENTO_DIVERGENTE_DO_CONSENTIMENTO. Este campo faz referência ao campo CodMun do arranjo Pix.   # noqa: E501

        :return: The ibge_town_code of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._ibge_town_code

    @ibge_town_code.setter
    def ibge_town_code(self, ibge_town_code):
        """Sets the ibge_town_code of this ResponsePixPaymentData.

        Traz o código da cidade segundo o IBGE (Instituto Brasileiro de Geografia e Estatística). Para o preenchimento deste campo, o Iniciador de Pagamentos deve seguir a orientação do arranjo da forma de pagamento. O preenchimento do campo tanto em pix/payments quanto /consents deve ser igual. Caso haja divergência dos valores, a instituição deve retornar HTTP 422 com o código de erro PAGAMENTO_DIVERGENTE_DO_CONSENTIMENTO. Este campo faz referência ao campo CodMun do arranjo Pix.   # noqa: E501

        :param ibge_town_code: The ibge_town_code of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """

        self._ibge_town_code = ibge_town_code

    @property
    def status(self):
        """Gets the status of this ResponsePixPaymentData.  # noqa: E501


        :return: The status of this ResponsePixPaymentData.  # noqa: E501
        :rtype: EnumPaymentStatusType
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponsePixPaymentData.


        :param status: The status of this ResponsePixPaymentData.  # noqa: E501
        :type: EnumPaymentStatusType
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def rejection_reason(self):
        """Gets the rejection_reason of this ResponsePixPaymentData.  # noqa: E501


        :return: The rejection_reason of this ResponsePixPaymentData.  # noqa: E501
        :rtype: EnumRejectionReasonType
        """
        return self._rejection_reason

    @rejection_reason.setter
    def rejection_reason(self, rejection_reason):
        """Sets the rejection_reason of this ResponsePixPaymentData.


        :param rejection_reason: The rejection_reason of this ResponsePixPaymentData.  # noqa: E501
        :type: EnumRejectionReasonType
        """

        self._rejection_reason = rejection_reason

    @property
    def local_instrument(self):
        """Gets the local_instrument of this ResponsePixPaymentData.  # noqa: E501


        :return: The local_instrument of this ResponsePixPaymentData.  # noqa: E501
        :rtype: CreatePixPaymentDatapropertieslocalInstrument
        """
        return self._local_instrument

    @local_instrument.setter
    def local_instrument(self, local_instrument):
        """Sets the local_instrument of this ResponsePixPaymentData.


        :param local_instrument: The local_instrument of this ResponsePixPaymentData.  # noqa: E501
        :type: CreatePixPaymentDatapropertieslocalInstrument
        """
        if local_instrument is None:
            raise ValueError("Invalid value for `local_instrument`, must not be `None`")  # noqa: E501

        self._local_instrument = local_instrument

    @property
    def cnpj_initiator(self):
        """Gets the cnpj_initiator of this ResponsePixPaymentData.  # noqa: E501

        CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix.  # noqa: E501

        :return: The cnpj_initiator of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._cnpj_initiator

    @cnpj_initiator.setter
    def cnpj_initiator(self, cnpj_initiator):
        """Sets the cnpj_initiator of this ResponsePixPaymentData.

        CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix.  # noqa: E501

        :param cnpj_initiator: The cnpj_initiator of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """
        if cnpj_initiator is None:
            raise ValueError("Invalid value for `cnpj_initiator`, must not be `None`")  # noqa: E501

        self._cnpj_initiator = cnpj_initiator

    @property
    def payment(self):
        """Gets the payment of this ResponsePixPaymentData.  # noqa: E501


        :return: The payment of this ResponsePixPaymentData.  # noqa: E501
        :rtype: PaymentPix
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this ResponsePixPaymentData.


        :param payment: The payment of this ResponsePixPaymentData.  # noqa: E501
        :type: PaymentPix
        """
        if payment is None:
            raise ValueError("Invalid value for `payment`, must not be `None`")  # noqa: E501

        self._payment = payment

    @property
    def transaction_identification(self):
        """Gets the transaction_identification of this ResponsePixPaymentData.  # noqa: E501

        Trata-se de um identificador de transação que deve ser retransmitido intacto pelo PSP do pagador ao gerar a ordem de pagamento. Essa informação permitirá ao recebedor identificar e correlacionar a transferência, quando recebida, com a apresentação das instruções ao pagador. Os caracteres permitidos no contexto do Pix para o campo txid (EMV 62-05) são: - Letras minúsculas, de ‘a’ a ‘z’ - Letras maiúsculas, de ‘A’ a ‘z’ - Dígitos decimais, de ‘0’ a ‘9’  [Restrição] Se localInstrument for igual a INIC, o campo transactionIdentification deve ser preenchido obrigatoriamente. Se localInstrument for igual a MANU ou DICT, o campo transactionIdentification não deve ser preenchido. A detentora de conta deve validar se a condicionalidade do campo foi atendida pela iniciadora de pagamento.   # noqa: E501

        :return: The transaction_identification of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_identification

    @transaction_identification.setter
    def transaction_identification(self, transaction_identification):
        """Sets the transaction_identification of this ResponsePixPaymentData.

        Trata-se de um identificador de transação que deve ser retransmitido intacto pelo PSP do pagador ao gerar a ordem de pagamento. Essa informação permitirá ao recebedor identificar e correlacionar a transferência, quando recebida, com a apresentação das instruções ao pagador. Os caracteres permitidos no contexto do Pix para o campo txid (EMV 62-05) são: - Letras minúsculas, de ‘a’ a ‘z’ - Letras maiúsculas, de ‘A’ a ‘z’ - Dígitos decimais, de ‘0’ a ‘9’  [Restrição] Se localInstrument for igual a INIC, o campo transactionIdentification deve ser preenchido obrigatoriamente. Se localInstrument for igual a MANU ou DICT, o campo transactionIdentification não deve ser preenchido. A detentora de conta deve validar se a condicionalidade do campo foi atendida pela iniciadora de pagamento.   # noqa: E501

        :param transaction_identification: The transaction_identification of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """

        self._transaction_identification = transaction_identification

    @property
    def remittance_information(self):
        """Gets the remittance_information of this ResponsePixPaymentData.  # noqa: E501

        Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.   # noqa: E501

        :return: The remittance_information of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._remittance_information

    @remittance_information.setter
    def remittance_information(self, remittance_information):
        """Sets the remittance_information of this ResponsePixPaymentData.

        Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.   # noqa: E501

        :param remittance_information: The remittance_information of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """

        self._remittance_information = remittance_information

    @property
    def creditor_account(self):
        """Gets the creditor_account of this ResponsePixPaymentData.  # noqa: E501


        :return: The creditor_account of this ResponsePixPaymentData.  # noqa: E501
        :rtype: CreditorAccount
        """
        return self._creditor_account

    @creditor_account.setter
    def creditor_account(self, creditor_account):
        """Sets the creditor_account of this ResponsePixPaymentData.


        :param creditor_account: The creditor_account of this ResponsePixPaymentData.  # noqa: E501
        :type: CreditorAccount
        """
        if creditor_account is None:
            raise ValueError("Invalid value for `creditor_account`, must not be `None`")  # noqa: E501

        self._creditor_account = creditor_account

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
        if issubclass(ResponsePixPaymentData, dict):
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
        if not isinstance(other, ResponsePixPaymentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
