# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, reponsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openId` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc2.0
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
        'end_to_end_id': 'str',
        'consent_id': 'str',
        'creation_date_time': 'datetime',
        'status_update_date_time': 'datetime',
        'proxy': 'str',
        'status': 'str',
        'rejection_reason': 'str',
        'payment': 'PaymentPix',
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
        'status': 'status',
        'rejection_reason': 'rejectionReason',
        'payment': 'payment',
        'remittance_information': 'remittanceInformation',
        'creditor_account': 'creditorAccount'
    }

    def __init__(self, payment_id=None, end_to_end_id=None, consent_id=None, creation_date_time=None, status_update_date_time=None, proxy=None, status=None, rejection_reason=None, payment=None, remittance_information=None, creditor_account=None):  # noqa: E501
        """ResponsePixPaymentData - a model defined in Swagger"""  # noqa: E501
        self._payment_id = None
        self._end_to_end_id = None
        self._consent_id = None
        self._creation_date_time = None
        self._status_update_date_time = None
        self._proxy = None
        self._status = None
        self._rejection_reason = None
        self._payment = None
        self._remittance_information = None
        self._creditor_account = None
        self.discriminator = None
        self.payment_id = payment_id
        self.end_to_end_id = end_to_end_id
        self.consent_id = consent_id
        self.creation_date_time = creation_date_time
        self.status_update_date_time = status_update_date_time
        if proxy is not None:
            self.proxy = proxy
        self.status = status
        if rejection_reason is not None:
            self.rejection_reason = rejection_reason
        self.payment = payment
        if remittance_information is not None:
            self.remittance_information = remittance_information
        if creditor_account is not None:
            self.creditor_account = creditor_account

    @property
    def payment_id(self):
        """Gets the payment_id of this ResponsePixPaymentData.  # noqa: E501

        Código ou identificador único informado pela instituição detentora da conta para representar   a iniciação de pagamento individual. O `paymentId` deve ser diferente do `endToEndId`.   Este é o identificador que deverá ser utilizado na consulta ao status da iniciação de pagamento efetuada.   # noqa: E501

        :return: The payment_id of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this ResponsePixPaymentData.

        Código ou identificador único informado pela instituição detentora da conta para representar   a iniciação de pagamento individual. O `paymentId` deve ser diferente do `endToEndId`.   Este é o identificador que deverá ser utilizado na consulta ao status da iniciação de pagamento efetuada.   # noqa: E501

        :param payment_id: The payment_id of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """
        if payment_id is None:
            raise ValueError("Invalid value for `payment_id`, must not be `None`")  # noqa: E501

        self._payment_id = payment_id

    @property
    def end_to_end_id(self):
        """Gets the end_to_end_id of this ResponsePixPaymentData.  # noqa: E501

        Código de identificação único da transação no arranjo do Pix. É usado em toda a cadeia de mensagens de uma instrução de pagamento no SPI. É um código gerado pela instituição detentora da conta que está iniciando o pagamento.   Deve ser preenchido no formato padrão ExxxxxxxxyyyyMMddHHmmkkkkkkkkkkk (32 caracteres), sendo:   • “E” – fixo (1 caractere);   • xxxxxxxx – identificação do agente que gerou o `endToEndId`, podendo ser: o ISPB do participante direto ou o ISPB do participante indireto (8 caracteres numéricos [0-9]);   • yyyyMMddHHmm – data, hora e minuto (12 caracteres), seguindo o horário UTC, da submissão da ordem de pagamento, caso a liquidação seja prioritária, ou prevista para o envio da ordem ao sistema de liquidação, caso seja realizado um agendamento. No caso de ordens prioritárias, aceita-se o preenchimento, pelo agente que gerou o <EndToEndId>, com uma tolerância máxima de 1 hora e 30 minutos, para o futuro e para o passado, em relação ao horário efetivo de processamento da ordem pelo SPI. Para ordens não prioritárias, a tolerância máxima é de 12 horas, para o futuro e para o passado;   • kkkkkkkkkkk – sequencial criado pelo agente que gerou o `endToEndId` (11 caracteres alfanuméricos [a-z|A-Z|0-9]). Deve ser único dentro de cada “yyyyMMddHHmm”.   Exemplo: E000000002020080120300000000001B   O `endToEndId` é gerado pela detentora. Ele deve ser único, não podendo ser repetido em qualquer outra operação enviada ao SPI.   # noqa: E501

        :return: The end_to_end_id of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._end_to_end_id

    @end_to_end_id.setter
    def end_to_end_id(self, end_to_end_id):
        """Sets the end_to_end_id of this ResponsePixPaymentData.

        Código de identificação único da transação no arranjo do Pix. É usado em toda a cadeia de mensagens de uma instrução de pagamento no SPI. É um código gerado pela instituição detentora da conta que está iniciando o pagamento.   Deve ser preenchido no formato padrão ExxxxxxxxyyyyMMddHHmmkkkkkkkkkkk (32 caracteres), sendo:   • “E” – fixo (1 caractere);   • xxxxxxxx – identificação do agente que gerou o `endToEndId`, podendo ser: o ISPB do participante direto ou o ISPB do participante indireto (8 caracteres numéricos [0-9]);   • yyyyMMddHHmm – data, hora e minuto (12 caracteres), seguindo o horário UTC, da submissão da ordem de pagamento, caso a liquidação seja prioritária, ou prevista para o envio da ordem ao sistema de liquidação, caso seja realizado um agendamento. No caso de ordens prioritárias, aceita-se o preenchimento, pelo agente que gerou o <EndToEndId>, com uma tolerância máxima de 1 hora e 30 minutos, para o futuro e para o passado, em relação ao horário efetivo de processamento da ordem pelo SPI. Para ordens não prioritárias, a tolerância máxima é de 12 horas, para o futuro e para o passado;   • kkkkkkkkkkk – sequencial criado pelo agente que gerou o `endToEndId` (11 caracteres alfanuméricos [a-z|A-Z|0-9]). Deve ser único dentro de cada “yyyyMMddHHmm”.   Exemplo: E000000002020080120300000000001B   O `endToEndId` é gerado pela detentora. Ele deve ser único, não podendo ser repetido em qualquer outra operação enviada ao SPI.   # noqa: E501

        :param end_to_end_id: The end_to_end_id of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """
        if end_to_end_id is None:
            raise ValueError("Invalid value for `end_to_end_id`, must not be `None`")  # noqa: E501

        self._end_to_end_id = end_to_end_id

    @property
    def consent_id(self):
        """Gets the consent_id of this ResponsePixPaymentData.  # noqa: E501

        Identificador único do consentimento.   # noqa: E501

        :return: The consent_id of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this ResponsePixPaymentData.

        Identificador único do consentimento.   # noqa: E501

        :param consent_id: The consent_id of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """
        if consent_id is None:
            raise ValueError("Invalid value for `consent_id`, must not be `None`")  # noqa: E501

        self._consent_id = consent_id

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this ResponsePixPaymentData.  # noqa: E501

        Data e hora em que o recurso foi criado.   Uma string com data e hora conforme especificação RFC-3339,   sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :return: The creation_date_time of this ResponsePixPaymentData.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this ResponsePixPaymentData.

        Data e hora em que o recurso foi criado.   Uma string com data e hora conforme especificação RFC-3339,   sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :param creation_date_time: The creation_date_time of this ResponsePixPaymentData.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def status_update_date_time(self):
        """Gets the status_update_date_time of this ResponsePixPaymentData.  # noqa: E501

        Data e hora da última atualização da iniciação de pagamento.   Uma string com data e hora conforme especificação RFC-3339,   sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :return: The status_update_date_time of this ResponsePixPaymentData.  # noqa: E501
        :rtype: datetime
        """
        return self._status_update_date_time

    @status_update_date_time.setter
    def status_update_date_time(self, status_update_date_time):
        """Sets the status_update_date_time of this ResponsePixPaymentData.

        Data e hora da última atualização da iniciação de pagamento.   Uma string com data e hora conforme especificação RFC-3339,   sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :param status_update_date_time: The status_update_date_time of this ResponsePixPaymentData.  # noqa: E501
        :type: datetime
        """
        if status_update_date_time is None:
            raise ValueError("Invalid value for `status_update_date_time`, must not be `None`")  # noqa: E501

        self._status_update_date_time = status_update_date_time

    @property
    def proxy(self):
        """Gets the proxy of this ResponsePixPaymentData.  # noqa: E501

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória.   No caso de telefone celular deve ser informado no padrão E.1641.   Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres.   No caso de CPF deverá ser informado com 11 números, sem pontos ou traços.   Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços.   No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223.   [Restrição] Preenchimento obrigatório para pagamentos via Chave.   # noqa: E501

        :return: The proxy of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this ResponsePixPaymentData.

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória.   No caso de telefone celular deve ser informado no padrão E.1641.   Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres.   No caso de CPF deverá ser informado com 11 números, sem pontos ou traços.   Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços.   No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223.   [Restrição] Preenchimento obrigatório para pagamentos via Chave.   # noqa: E501

        :param proxy: The proxy of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    @property
    def status(self):
        """Gets the status of this ResponsePixPaymentData.  # noqa: E501

        Estado atual da iniciação de pagamento. O estado evolui na seguinte ordem:   1. PDNG (PENDING) - Iniciação de pagamento ou transação de pagamento está pendente. Checagens adicionais em realização.   2. PART (PARTIALLY ACCEPTED) - Aguardando autorização múltipla alçada.   3. ACSP (ACCEPTED_SETTLEMENT_IN_PROCESS) - Iniciação de pagamento aceita e processamento do pagamento foi iniciado.   4. ACSC (ACCEPTED_SETTLEMENT_COMPLETED_DEBITOR_ACCOUNT) - Débito realizado na conta do pagador.   5. ACCC (ACCEPTED_SETTLEMENT_COMPLETED) - Crédito realizado na instituição de destino.   Em caso insucesso:   RJCT (REJECTED) - Instrução de pagamento rejeitada.   # noqa: E501

        :return: The status of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponsePixPaymentData.

        Estado atual da iniciação de pagamento. O estado evolui na seguinte ordem:   1. PDNG (PENDING) - Iniciação de pagamento ou transação de pagamento está pendente. Checagens adicionais em realização.   2. PART (PARTIALLY ACCEPTED) - Aguardando autorização múltipla alçada.   3. ACSP (ACCEPTED_SETTLEMENT_IN_PROCESS) - Iniciação de pagamento aceita e processamento do pagamento foi iniciado.   4. ACSC (ACCEPTED_SETTLEMENT_COMPLETED_DEBITOR_ACCOUNT) - Débito realizado na conta do pagador.   5. ACCC (ACCEPTED_SETTLEMENT_COMPLETED) - Crédito realizado na instituição de destino.   Em caso insucesso:   RJCT (REJECTED) - Instrução de pagamento rejeitada.   # noqa: E501

        :param status: The status of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["PDNG", "PART", "ACSP", "ACSC", "ACCC", "RJCT"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def rejection_reason(self):
        """Gets the rejection_reason of this ResponsePixPaymentData.  # noqa: E501

        Motivo da rejeição do pagamento. Informações complementares sobre o motivo do status.   ABORTED_SETTLEMENT_TIMEOUT - Liquidação da transação interrompida devido a timeout no SPI (AB03). ERROR_CREDITOR_AGENT - Transação interrompida devido a erro no participante do usuário recebedor (AB09). TIMEOUT_DEBTOR_AGENT - Timeout do participante emissor da ordem de pagamento (AB11). INVALID_CREDITOR_ACCOUNT_NUMBER - Número da conta transacional do usuário recebedor inexistente ou inválido (AC03). BLOCKED_ACCOUNT - Conta transacional do usuário recebedor encontra-se bloqueada (AC06). CLOSED_CREDITOR_ACCOUNT_NUMBER - Número da conta transacional do usuário recebedor encerrada (AC07). INVALID_CREDITOR_ACCOUNTTYPE - Tipo incorreto para a conta transacional do usuário recebedor (AC14). TRANSACTION_NOT_SUPPORTED - Tipo de transação não é suportado/autorizado na conta transacional do usuário recebedor (AG03). Exemplo: transferência para conta salário. NOT_ALLOWED_BOOK_TRANSFER - Não é permitida ordem de pagamento/devolução no SPI cujos recursos sejam transferidos de uma conta transacional para outra em uma mesma instituição participante ou entre participantes que utilizem o serviço de liquidação de um mesmo participante liquidante no SPI (booktransfer) (AG12). FORBIDDEN_RETURN_PAYMENT - Não é permitido devolver a devolução de um pagamento instantâneo (AG13). INCORRECT_AGENT - Participante direto não é liquidante do participante do usuário pagador / participante do usuário recebedor (AGNT). ZERO_AMOUNT - Ordem de pagamento instantâneo com valor zero (AM01). NOT_ALLOWED_AMOUNT - Ordem de pagamento/devolução em valor que faz superar o limite permitido para o tipo de conta transacional creditada (AM02). INSUFFICIENT_FUNDS - Saldo insuficiente na conta PI do participante do usuário pagador (AM04). WRONG_AMOUNT - Devolução de pagamento em valor que faz superar o valor da ordem de pagamento instantâneo correspondente (AM09). INVALID_AMOUNT - Divergência entre a somatória dos valores do bloco ‘valorDoDinheiroOuCompra’ e o campo ‘valor’ (AM12). INVALID_NUMBER_OF_TRANSACTIONS - Quantidade de transações inválida (AM18). INCONSISTENT_WITH_END_CUSTOMER - CPF/CNPJ do usuário recebedor não é consistente com o titular da conta transacional especificada (BE01). INVALID_IDENTIFICATION_CODE - Código de situação de pagamento ou de erro inválido (BE15). INVALID_CREDITOR_IDENTIFICATION_CODE - QR Code rejeitado pelo participante do usuário recebedor (BE17). CREDITOR_IDENTIFIER_INCORRECT - CPF/CNPJ do usuário recebedor incorreto (CH11). ELEMENT_CONTENT_FORMALLY_INCORRECT - Elemento da mensagem incorreto (CH16). ORDER_REJECTED - Ordem rejeitada pelo participante do usuário recebedor (DS04). NOT_ALLOWED_PAYMENT - Participante que assinou a mensagem não é autorizado a realizar a operação na conta PI debitada. No caso em que o participante que assinou a mensagem não é o titular da conta PI debitada nem é o liquidante no SPI do participante do usuário pagador (DS0G). NOT_ALLOWED_ACCOUNT - ISPB do participante que submeteu a resposta à ordem de pagamento/devolução diferente do ISPB do participante creditado pela ordem (DS0H). USER_NOT_YET_ACTIVATED - Participante não se encontra cadastrado ou ainda não iniciou a operação no SPI (DS27). INVALID_CREATION_DATE - Data e Hora do envio da mensagem inválida (DT02). INVALID_CUT_OFF_DATE - Transação extrapola o prazo máximo para devolução de pagamento instantâneo regulamentado pelo Arranjo PIX (DT05). SETTLEMENT_FAILED - Erro no processamento do pagamento instantâneo (ED05). INVALID_PURPOSE - Inconsistência entre a finalidade da transação e o preenchimento do bloco elementos Structured (FF07). INVALID_END_TO_END_ID - Identificador da operação mal formatado (FF08). INVALID_DEBTOR_CLEARING_SYSTEM_MEMBER_IDENTIFIER - ISPB do participante do usuário pagador inválido ou inexistente (RC09). INVALID_CREDITOR_CLEARING_SYSTEM_MEMBER_IDENTIFIER - ISPB do participante do usuário recebedor inválido ou inexistente (RC10). REGULATORY_REASON - Ordem de pagamento em que o usuário pagador é sancionado por resolução do Conselho de Segurança das Nações Unidas (CSNU). Nos casos em que o usuário recebedor for o sancionado, a ordem de pagamento não deve ser rejeitada (RR4). SPECIFIC_SERVICE_OFFERED_BY_CREDITOR_AGENT - A transação original não está relacionada ao serviço de Saque Pix (SL02). INVALID_BILL - Validação de expiração, validação de vencimento, Status Válido (INDT).   OPERATION_WINDOW - Requisição está fora da janela de funcionamento (IDEA).   INCOMPATIBLE_DATE - Data do pagamento divergente da data consentida ou divergente da data atual do QR Code (TERM).   MISMATCH_AMOUNT - O valor informado no consentimento não é o mesmo valor do informado no payload de pagamento (OB01).   OVER_LIMIT - O valor (ou quantidade de transações) ultrapassa a faixa de limite parametrizada na detentora para permitir a realização de transações pelo cliente (OB02).    INVALID_CONSENT - Consentimento inválido (status não é \"authorised\" ou está expirado) (OB03).   DENIED_MULTIPLE_AUTHORISATIONS - Um (ou mais) aprovadores na detentora recusaram a operação (OB04).   EXPIRED_MULTIPLE_AUTHORISATIONS - Um (ou mais) aprovadores na detentora não tomaram ação para aprovar a operação (OB05).   EXPIRED_BILL - O QR Code não é mais válido (OB06).   [Restrição] Esse motivo deverá ser enviado quando o campo /data/status for igual a RJCT (REJECTED).     # noqa: E501

        :return: The rejection_reason of this ResponsePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._rejection_reason

    @rejection_reason.setter
    def rejection_reason(self, rejection_reason):
        """Sets the rejection_reason of this ResponsePixPaymentData.

        Motivo da rejeição do pagamento. Informações complementares sobre o motivo do status.   ABORTED_SETTLEMENT_TIMEOUT - Liquidação da transação interrompida devido a timeout no SPI (AB03). ERROR_CREDITOR_AGENT - Transação interrompida devido a erro no participante do usuário recebedor (AB09). TIMEOUT_DEBTOR_AGENT - Timeout do participante emissor da ordem de pagamento (AB11). INVALID_CREDITOR_ACCOUNT_NUMBER - Número da conta transacional do usuário recebedor inexistente ou inválido (AC03). BLOCKED_ACCOUNT - Conta transacional do usuário recebedor encontra-se bloqueada (AC06). CLOSED_CREDITOR_ACCOUNT_NUMBER - Número da conta transacional do usuário recebedor encerrada (AC07). INVALID_CREDITOR_ACCOUNTTYPE - Tipo incorreto para a conta transacional do usuário recebedor (AC14). TRANSACTION_NOT_SUPPORTED - Tipo de transação não é suportado/autorizado na conta transacional do usuário recebedor (AG03). Exemplo: transferência para conta salário. NOT_ALLOWED_BOOK_TRANSFER - Não é permitida ordem de pagamento/devolução no SPI cujos recursos sejam transferidos de uma conta transacional para outra em uma mesma instituição participante ou entre participantes que utilizem o serviço de liquidação de um mesmo participante liquidante no SPI (booktransfer) (AG12). FORBIDDEN_RETURN_PAYMENT - Não é permitido devolver a devolução de um pagamento instantâneo (AG13). INCORRECT_AGENT - Participante direto não é liquidante do participante do usuário pagador / participante do usuário recebedor (AGNT). ZERO_AMOUNT - Ordem de pagamento instantâneo com valor zero (AM01). NOT_ALLOWED_AMOUNT - Ordem de pagamento/devolução em valor que faz superar o limite permitido para o tipo de conta transacional creditada (AM02). INSUFFICIENT_FUNDS - Saldo insuficiente na conta PI do participante do usuário pagador (AM04). WRONG_AMOUNT - Devolução de pagamento em valor que faz superar o valor da ordem de pagamento instantâneo correspondente (AM09). INVALID_AMOUNT - Divergência entre a somatória dos valores do bloco ‘valorDoDinheiroOuCompra’ e o campo ‘valor’ (AM12). INVALID_NUMBER_OF_TRANSACTIONS - Quantidade de transações inválida (AM18). INCONSISTENT_WITH_END_CUSTOMER - CPF/CNPJ do usuário recebedor não é consistente com o titular da conta transacional especificada (BE01). INVALID_IDENTIFICATION_CODE - Código de situação de pagamento ou de erro inválido (BE15). INVALID_CREDITOR_IDENTIFICATION_CODE - QR Code rejeitado pelo participante do usuário recebedor (BE17). CREDITOR_IDENTIFIER_INCORRECT - CPF/CNPJ do usuário recebedor incorreto (CH11). ELEMENT_CONTENT_FORMALLY_INCORRECT - Elemento da mensagem incorreto (CH16). ORDER_REJECTED - Ordem rejeitada pelo participante do usuário recebedor (DS04). NOT_ALLOWED_PAYMENT - Participante que assinou a mensagem não é autorizado a realizar a operação na conta PI debitada. No caso em que o participante que assinou a mensagem não é o titular da conta PI debitada nem é o liquidante no SPI do participante do usuário pagador (DS0G). NOT_ALLOWED_ACCOUNT - ISPB do participante que submeteu a resposta à ordem de pagamento/devolução diferente do ISPB do participante creditado pela ordem (DS0H). USER_NOT_YET_ACTIVATED - Participante não se encontra cadastrado ou ainda não iniciou a operação no SPI (DS27). INVALID_CREATION_DATE - Data e Hora do envio da mensagem inválida (DT02). INVALID_CUT_OFF_DATE - Transação extrapola o prazo máximo para devolução de pagamento instantâneo regulamentado pelo Arranjo PIX (DT05). SETTLEMENT_FAILED - Erro no processamento do pagamento instantâneo (ED05). INVALID_PURPOSE - Inconsistência entre a finalidade da transação e o preenchimento do bloco elementos Structured (FF07). INVALID_END_TO_END_ID - Identificador da operação mal formatado (FF08). INVALID_DEBTOR_CLEARING_SYSTEM_MEMBER_IDENTIFIER - ISPB do participante do usuário pagador inválido ou inexistente (RC09). INVALID_CREDITOR_CLEARING_SYSTEM_MEMBER_IDENTIFIER - ISPB do participante do usuário recebedor inválido ou inexistente (RC10). REGULATORY_REASON - Ordem de pagamento em que o usuário pagador é sancionado por resolução do Conselho de Segurança das Nações Unidas (CSNU). Nos casos em que o usuário recebedor for o sancionado, a ordem de pagamento não deve ser rejeitada (RR4). SPECIFIC_SERVICE_OFFERED_BY_CREDITOR_AGENT - A transação original não está relacionada ao serviço de Saque Pix (SL02). INVALID_BILL - Validação de expiração, validação de vencimento, Status Válido (INDT).   OPERATION_WINDOW - Requisição está fora da janela de funcionamento (IDEA).   INCOMPATIBLE_DATE - Data do pagamento divergente da data consentida ou divergente da data atual do QR Code (TERM).   MISMATCH_AMOUNT - O valor informado no consentimento não é o mesmo valor do informado no payload de pagamento (OB01).   OVER_LIMIT - O valor (ou quantidade de transações) ultrapassa a faixa de limite parametrizada na detentora para permitir a realização de transações pelo cliente (OB02).    INVALID_CONSENT - Consentimento inválido (status não é \"authorised\" ou está expirado) (OB03).   DENIED_MULTIPLE_AUTHORISATIONS - Um (ou mais) aprovadores na detentora recusaram a operação (OB04).   EXPIRED_MULTIPLE_AUTHORISATIONS - Um (ou mais) aprovadores na detentora não tomaram ação para aprovar a operação (OB05).   EXPIRED_BILL - O QR Code não é mais válido (OB06).   [Restrição] Esse motivo deverá ser enviado quando o campo /data/status for igual a RJCT (REJECTED).     # noqa: E501

        :param rejection_reason: The rejection_reason of this ResponsePixPaymentData.  # noqa: E501
        :type: str
        """
        allowed_values = ["ABORTED_SETTLEMENT_TIMEOUT", "ERROR_CREDITOR_AGENT", "TIMEOUT_DEBTOR_AGENT", "INVALID_CREDITOR_ACCOUNT_NUMBER", "BLOCKED_ACCOUNT", "CLOSED_CREDITOR_ACCOUNT_NUMBER", "INVALID_CREDITOR_ACCOUNTTYPE", "TRANSACTION_NOT_SUPPORTED", "NOT_ALLOWED_BOOK_TRANSFER", "FORBIDDEN_RETURN_PAYMENT", "INCORRECT_AGENT", "ZERO_AMOUNT", "NOT_ALLOWED_AMOUNT", "INSUFFICIENT_FUNDS", "WRONG_AMOUNT", "INVALID_AMOUNT", "INVALID_NUMBER_OF_TRANSACTIONS", "INCONSISTENT_WITH_END_CUSTOMER", "INVALID_IDENTIFICATION_CODE", "INVALID_CREDITOR_IDENTIFICATION_CODE", "CREDITOR_IDENTIFIER_INCORRECT", "ELEMENT_CONTENT_FORMALLY_INCORRECT", "ORDER_REJECTED", "NOT_ALLOWED_PAYMENT", "NOT_ALLOWED_ACCOUNT", "USER_NOT_YET_ACTIVATED", "INVALID_CREATION_DATE", "INVALID_CUT_OFF_DATE", "SETTLEMENT_FAILED", "INVALID_PURPOSE", "INVALID_END_TO_END_ID", "INVALID_DEBTOR_CLEARING_SYSTEM_MEMBER_IDENTIFIER", "INVALID_CREDITOR_CLEARING_SYSTEM_MEMBER_IDENTIFIER", "REGULATORY_REASON", "SPECIFIC_SERVICE_OFFERED_BY_CREDITOR_AGENT", "INVALID_BILL", "OPERATION_WINDOW", "INCOMPATIBLE_DATE", "MISMATCH_AMOUNT", "OVER_LIMIT", "INVALID_CONSENT", "DENIED_MULTIPLE_AUTHORISATIONS", "EXPIRED_MULTIPLE_AUTHORISATIONS", "EXPIRED_BILL"]  # noqa: E501
        if rejection_reason not in allowed_values:
            raise ValueError(
                "Invalid value for `rejection_reason` ({0}), must be one of {1}"  # noqa: E501
                .format(rejection_reason, allowed_values)
            )

        self._rejection_reason = rejection_reason

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
