# coding: utf-8

"""
    API Automatic Payments - Open Finance Brasil

    API de Iniciação de Pagamentos automáticos, responsável por viabilizar as operações de iniciação de pagamentos automáticos (Pix automático e Sweeping Accounts) para o Open Finance Brasil.  Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos endpoints dedicados ao consentimento nesta API.  # Orientações - `CONTA`, referente às instituições detentoras de conta participantes do Open Finance Brasil; - `PAGTO`, referente às instituições iniciadoras de pagamento participantes do Open Finance Brasil.  Os tokens utilizados para consumo nos endpoints de consentimentos devem possuir o scope payments e os endpoints de pagamentos recorrentes devem possuir os scopes openid e payments.  Esta API não requer a implementação de permissions para sua utilização.  Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão Assinaturas do guia de segurança.  ## Orientações gerais sobre os consentimentos de pagamentos automáticos - Duração e reutilização do consentimento: A utilização das credenciais geradas a partir de uma autorização de um consentimento recorrente deve durar até que o consentimento recorrente atinja o fim do seu ciclo de vida, conforme detalhado na sua [máquina de estados](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/198410647).  - Credenciais: As credenciais (authorization_code) geradas na autorização do consentimento devem ser utilizadas para criação dos pagamentos subsequentes utilizando o mecanismo de refresh, caso necessário. Maiores informações através do link [[PT] Open Finance Brasil Financial-grade API Security Profile 1.0 Implementers Draft 3 - Área do Desenvolvedor -Open Finance Brasil - Área do Desenvolvedor (atlassian.net)](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/82051180/PT+Open+Finance+Brasil+Financial-grade+API+Security+Profile+1.0+Implementers+Draft+3#7.2.2.-Servidor-de-autorização)  ## Regras do arranjo Pix A implementação e o uso da API de Pagamentos Automáticos (Pix) devem seguir as regras do arranjo Pix do Banco Central, que podem ser encontradas no link abaixo:   [Banco Central do Brasil](https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix)  ## Assinatura de payloads No contexto da API de Pagamentos Automáticos, os payloads de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora de conta devem estar assinados.  Para o processo de assinatura destes payloads, as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor.  ## Controle de acesso - Os endpoints de consulta de pagamentos GET /pix/recurring-payments/{recurringPaymentId} e GET /pix/recurring-payments devem suportar acesso a partir de access_token emitido por meio de um grant_type do tipo client credentials, como opção do uso do token vinculado ao consentimento (hybrid flow). - Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.  ## Aprovações de múltipla alçada  Todas as aprovações devem ser realizadas até a data/hora limite suportada pela detentora e em tempo hábil para realizar o primeiro pagamento.  ## Validações da edição do consentimento recorrente para o produto Pix Automático  Para permitir a edição dos campos de um consentimento na iniciadora sem que se faça necessário o redirecionamento para o  ambiente da detentora de conta, é necessário o envio de indicadores de risco.  Esta medida visa proporcionar à detentora de conta as informações necessárias para decidir sobre os ajustes no consentimento de forma segura  ## Validações  Durante a jornada de iniciação de pagamento, diferentes validações são necessárias pela instituição detentora de conta e devem ocorrer conforme a seguir:  1. **Validações na criação do consentimento de longa duração (_POST /recurring-consents_)**     1.1 **Orientações Iniciais**       &ensp;1.1.1 Não devem ser retornadas na resposta deste endpoint informações associadas ao usuário/cliente (ex. insuficiência de saldo, conta inexistente/bloqueada).       &ensp;1.1.2 Não devem ser realizadas validações de informações sobre o usuário/cliente durante a criação do consentimento.     1.2 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;1.2.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;1.2.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;1.2.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;1.2.4 Validação de Claims (exceto data);         &emsp;1.2.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;1.2.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     1.3 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**        &ensp;1.3.1 **Sintáticos**         &emsp;1.3.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios foram informados (PARAMETRO_NAO_INFORMADO);         &emsp;1.3.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;1.3.2 **Semânticos**         &emsp;1.3.2.1 Data de pagamento: Valida se a data de pagamento enviada é válida para a forma de pagamento selecionada (DATA_PAGAMENTO_INVALIDA);         &emsp;1.3.2.2 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;1.3.2.3 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;1.3.2.4 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA);         &emsp;1.3.2.5 Funcionalidade não habilitada: A detentora de conta não oferece o serviço nessa modalidade (FUNCIONALIDADE_NAO_HABILITADA).    2. **Demais validações executadas durante o processamento assíncrono do consentimento pela detentora poderão ser consultados pela iniciadora através do endpoint GET /recurring-consents/{recurringConsentId} previstos com retorno HTTP Code 200 – OK com status REJECTED e rejectionReason conforme abaixo:**     2.1 **Validações durante o processamento assíncrono do consentimento**       &ensp;2.1.1 Falha de infraestrutura: Ocorreu algum erro interno na detentora durante processamento da criação do consentimento (FALHA_INFRAESTRUTURA);       &ensp;2.1.2 Tempo de autorização expirado: O usuário não confirmou o consentimento e o mesmo expirou (TEMPO_EXPIRADO_AUTORIZACAO);       &ensp;2.1.3 Rejeitado pelo usuário: O usuário explicitamente rejeitou a autorização do consentimento (REJEITADO_USUARIO);       &ensp;2.1.4 Mesma conta origem/destino: A conta indicada pelo usuário para recebimento é a mesma selecionada para o pagamento (CONTAS_ORIGEM_DESTINO_IGUAIS);       &ensp;2.1.5 Tipo de conta inválida: A conta indicada não permite operações de pagamento (CONTA_NAO_PERMITE_PAGAMENTO);       &ensp;2.1.6 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);       &ensp;2.1.7 Limites da transação: Valida se o valor ultrapassa o limite estabelecido [na instituição/no arranjo/outro] para permitir a realização de transações pelo cliente (VALOR_ACIMA_LIMITE);    3. **Demais validações executadas durante o processamento assíncrono do consentimento pela detentora, poderão ser consultados pela iniciadora através dos endpoints GET /recurring-consents/{recurringConsentId} previstos com retorno HTTP Code 200 - OK com status REVOKED e revocationReason conforme abaixo (detalhamento adicional na documentação técnica da API).**     3.1 **Demais validações durante o processamento assíncrono:**       &ensp;3.1.1 Nao informado: Validações não explicitamente informadas (ex. suspeita de fraude) (NAO_INFORMADO);       &ensp;3.1.2 Revogado pelo recebedor: O usuário recebedor solicitou explicitamente ao iniciador a revogação do consentimento (ex: término de contrato) (REVOGADO_RECEBEDOR);       &ensp;3.1.3 Revogado pelo pagador: O usuário pagador solicitou explicitamente a revogação do consentimento (REVOGADO_USUARIO).    4. **Validações na criação do pagamento - Síncrono (_POST /pix/recurring-payments_)**     4.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;4.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;4.1.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;4.1.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;4.1.4 Validação de Claims (exceto data);         &emsp;4.1.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;4.1.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     4.2 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**       &ensp;4.2.1 Sintáticos         &emsp;4.2.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios são informados (PARAMETRO_NAO_INFORMADO);         &emsp;4.2.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;4.2.2 Semânticos         &emsp;4.2.2.1 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);         &emsp;4.2.2.2 Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora na conta do cliente pagador (VALOR_ACIMA_LIMITE);         &emsp;4.2.2.3 Valor informado: Valida se valor enviado é válido para o consentimento associado ao pagamento (VALOR_INVALIDO);         &emsp;4.2.2.4 Status Consentimento: Valida se status de consentimento é diferente de “AUTHORISED” (CONSENTIMENTO_INVALIDO);         &emsp;4.2.2.5 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;4.2.2.6 Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO)         &emsp;4.2.2.7 Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa;         &emsp;4.2.2.8 Detalhes do pagamento: Valida se determinado parâmetro informado obedece as regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;4.2.2.9 Pagamento recusado no Sistema de Pagamentos Instantâneos (SPI) (PAGAMENTO_RECUSADO_SPI);         &emsp;4.2.2.10 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA);         &emsp;4.2.2.11 Limite valor excedido por período: Foi atingido o valor limite permitido pelo usuário por um determinado período de tempo no consentimento do pagamento (LIMITE_PERIODO_VALOR_EXCEDIDO);         &emsp;4.2.2.12 Limite quantidade excedida por período: A quantidade de cobranças atingiu o limite determinado pelo usuário na criação do consentimento (LIMITE_PERIODO_QUANTIDADE_EXCEDIDO).    5. **Validações na consulta do pagamento (_GET /pix/recurring-payments/{recurringPaymentId}_ e _GET /pix/recurring-payments_)**     5.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token)**       &ensp;5.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;5.1.2 Validações de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED).  6. **Demais validações executadas durante o processamento assíncrono do pagamento pela detentora, poderão ser consultados pela iniciadora através dos endpoints _GET /pix/recurring-payments/{recurringPaymentId}_ e _GET /pix/recurring-payments_ previstos com retorno HTTP Code 200 - OK com status RJCT (Rejected) e rejectionReason conforme abaixo (detalhamento adicional na documentação técnica da API):**     6.1 **Demais validações durante o processamento assíncrono:**       &ensp;6.1.1 - Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);       &ensp;6.1.2 - Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora (VALOR_ACIMA_LIMITE);       &ensp;6.1.3 - Valor informado: Valida se valor enviado é válido para o consentimento do pagamento (VALOR_INVALIDO);       &ensp;6.1.4 - Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);       &ensp;6.1.5 - Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO);       &ensp;6.1.6 - Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa;       &ensp;6.1.7 - Pagamento recusado no Sistema de Pagamentos Instantâneos (SPI) (PAGAMENTO_RECUSADO_SPI);       &ensp;6.1.8 - Erro de infraestrutura na consulta ao SPI: Ocorreu uma falha de infraestrutura durante a consulta ao SPI(FALHA_INFRAESTRUTURA_SPI);       &ensp;6.1.9 - Erro de infraestrutura na consulta ao ICP: Ocorreu uma falha de infraestrutura durante a consulta ao ICP (FALHA_INFRAESTRUTURA_ICP);       &ensp;6.1.10 - Erro de infraestrutura na comunicação com o PSP do recebedor: Ocorreu uma falha de infraestrutura durante a comunicação com o PSP do recebedor (FALHA_INFRAESTRUTURA_PSP_RECEBEDOR);       &ensp;6.1.11 - Erro de infraestrutura interno na detentora: Ocorreu uma falha de infraestrutura interna na detentora durante o processamento do pagamento (FALHA_INFRAESTRUTURA_DETENTORA);       &ensp;6.1.12 - Status Consentimento: Valida se status de consentimento é diferente de “AUTHORISED” (CONSENTIMENTO_INVALIDO);    ## Validações antifraude do Sweeping accounts  - Afim de garantir a mesma titularidade e aumentar a segurança das transações do produto Sweeping Accounts, as validações abaixo poderão ser realizadas pela detetora de conta e pela iniciadora, quando localinstrument for igual a DICT ou INIC. A detentora PODE usar a API Consultar Vinculo (DICT API) do arranjo Pix e validar no momento de transação ao menos os atributos abaixo mencionados:   - se o valor dos atributos de fraude abaixo são iguais a 0, de modo a evitar que contas criadas especificamente para uso indevido do Sweeping accounts impactem o ecossistema      - OwnerStatistics.Spi.FraudMarkers.ApplicationFrauds.d90     - OwnerStatistics.Spi.FraudMarkers.MuleAccounts.d90     - OwnerStatistics.Spi.FraudMarkers.ScammerAccounts.d90     - OwnerStatistics.Spi.FraudMarkers.OtherFrauds.d90     - OwnerStatistics.Spi.FraudMarkers.UnknownFrauds.d90   # noqa: E501

    OpenAPI spec version: 1.0.0-beta.4
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseRecurringPaymentsPostData(object):
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
        'recurring_payment_id': 'str',
        'recurring_consent_id': 'str',
        'end_to_end_id': 'EndToEndId',
        '_date': 'str',
        'creation_date_time': 'datetime',
        'status_update_date_time': 'datetime',
        'ibge_town_code': 'str',
        'status': 'EnumPaymentStatusType',
        'rejection_reason': 'RejectionReason',
        'cnpj_initiator': 'str',
        'payment': 'PaymentPix',
        'remittance_information': 'str',
        'creditor_account': 'CreditorAccountPost',
        'debtor_account': 'DebtorAccount',
        'cancellation': 'PixPaymentCancellation',
        'authorisation_flow': 'str',
        'local_instrument': 'str',
        'proxy': 'str',
        'transaction_identification': 'str'
    }

    attribute_map = {
        'recurring_payment_id': 'recurringPaymentId',
        'recurring_consent_id': 'recurringConsentId',
        'end_to_end_id': 'endToEndId',
        '_date': 'date',
        'creation_date_time': 'creationDateTime',
        'status_update_date_time': 'statusUpdateDateTime',
        'ibge_town_code': 'ibgeTownCode',
        'status': 'status',
        'rejection_reason': 'rejectionReason',
        'cnpj_initiator': 'cnpjInitiator',
        'payment': 'payment',
        'remittance_information': 'remittanceInformation',
        'creditor_account': 'creditorAccount',
        'debtor_account': 'debtorAccount',
        'cancellation': 'cancellation',
        'authorisation_flow': 'authorisationFlow',
        'local_instrument': 'localInstrument',
        'proxy': 'proxy',
        'transaction_identification': 'transactionIdentification'
    }

    def __init__(self, recurring_payment_id=None, recurring_consent_id=None, end_to_end_id=None, _date=None, creation_date_time=None, status_update_date_time=None, ibge_town_code=None, status=None, rejection_reason=None, cnpj_initiator=None, payment=None, remittance_information=None, creditor_account=None, debtor_account=None, cancellation=None, authorisation_flow=None, local_instrument=None, proxy=None, transaction_identification=None):  # noqa: E501
        """ResponseRecurringPaymentsPostData - a model defined in Swagger"""  # noqa: E501
        self._recurring_payment_id = None
        self._recurring_consent_id = None
        self._end_to_end_id = None
        self.__date = None
        self._creation_date_time = None
        self._status_update_date_time = None
        self._ibge_town_code = None
        self._status = None
        self._rejection_reason = None
        self._cnpj_initiator = None
        self._payment = None
        self._remittance_information = None
        self._creditor_account = None
        self._debtor_account = None
        self._cancellation = None
        self._authorisation_flow = None
        self._local_instrument = None
        self._proxy = None
        self._transaction_identification = None
        self.discriminator = None
        self.recurring_payment_id = recurring_payment_id
        if recurring_consent_id is not None:
            self.recurring_consent_id = recurring_consent_id
        self.end_to_end_id = end_to_end_id
        self._date = _date
        self.creation_date_time = creation_date_time
        self.status_update_date_time = status_update_date_time
        self.ibge_town_code = ibge_town_code
        self.status = status
        if rejection_reason is not None:
            self.rejection_reason = rejection_reason
        self.cnpj_initiator = cnpj_initiator
        self.payment = payment
        if remittance_information is not None:
            self.remittance_information = remittance_information
        if creditor_account is not None:
            self.creditor_account = creditor_account
        if debtor_account is not None:
            self.debtor_account = debtor_account
        if cancellation is not None:
            self.cancellation = cancellation
        if authorisation_flow is not None:
            self.authorisation_flow = authorisation_flow
        self.local_instrument = local_instrument
        if proxy is not None:
            self.proxy = proxy
        if transaction_identification is not None:
            self.transaction_identification = transaction_identification

    @property
    def recurring_payment_id(self):
        """Gets the recurring_payment_id of this ResponseRecurringPaymentsPostData.  # noqa: E501

        Código ou identificador único informado pela instituição detentora da conta para representar a iniciação de pagamento. O `recurringPaymentId` deve ser diferente do `endToEndId`.  Este é o identificador que deverá ser utilizado na consulta ao status da iniciação de pagamento efetuada.   # noqa: E501

        :return: The recurring_payment_id of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: str
        """
        return self._recurring_payment_id

    @recurring_payment_id.setter
    def recurring_payment_id(self, recurring_payment_id):
        """Sets the recurring_payment_id of this ResponseRecurringPaymentsPostData.

        Código ou identificador único informado pela instituição detentora da conta para representar a iniciação de pagamento. O `recurringPaymentId` deve ser diferente do `endToEndId`.  Este é o identificador que deverá ser utilizado na consulta ao status da iniciação de pagamento efetuada.   # noqa: E501

        :param recurring_payment_id: The recurring_payment_id of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: str
        """
        if recurring_payment_id is None:
            raise ValueError("Invalid value for `recurring_payment_id`, must not be `None`")  # noqa: E501

        self._recurring_payment_id = recurring_payment_id

    @property
    def recurring_consent_id(self):
        """Gets the recurring_consent_id of this ResponseRecurringPaymentsPostData.  # noqa: E501

        Identificador único do consentimento criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para `recurringConsentId` temos: - o namespace(urn) - o identificador associado ao namespace da instituição transmissora (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  [Restrição] Este campo é de preenchimento obrigatório quando o valor do campo authorisationFlow for igual a FIDO_FLOW.   # noqa: E501

        :return: The recurring_consent_id of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: str
        """
        return self._recurring_consent_id

    @recurring_consent_id.setter
    def recurring_consent_id(self, recurring_consent_id):
        """Sets the recurring_consent_id of this ResponseRecurringPaymentsPostData.

        Identificador único do consentimento criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para `recurringConsentId` temos: - o namespace(urn) - o identificador associado ao namespace da instituição transmissora (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  [Restrição] Este campo é de preenchimento obrigatório quando o valor do campo authorisationFlow for igual a FIDO_FLOW.   # noqa: E501

        :param recurring_consent_id: The recurring_consent_id of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: str
        """

        self._recurring_consent_id = recurring_consent_id

    @property
    def end_to_end_id(self):
        """Gets the end_to_end_id of this ResponseRecurringPaymentsPostData.  # noqa: E501


        :return: The end_to_end_id of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: EndToEndId
        """
        return self._end_to_end_id

    @end_to_end_id.setter
    def end_to_end_id(self, end_to_end_id):
        """Sets the end_to_end_id of this ResponseRecurringPaymentsPostData.


        :param end_to_end_id: The end_to_end_id of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: EndToEndId
        """
        if end_to_end_id is None:
            raise ValueError("Invalid value for `end_to_end_id`, must not be `None`")  # noqa: E501

        self._end_to_end_id = end_to_end_id

    @property
    def _date(self):
        """Gets the _date of this ResponseRecurringPaymentsPostData.  # noqa: E501

        Data em que o recurso foi criado. Uma string com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :return: The _date of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ResponseRecurringPaymentsPostData.

        Data em que o recurso foi criado. Uma string com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :param _date: The _date of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this ResponseRecurringPaymentsPostData.  # noqa: E501

        Data e hora em que o pagamento foi criado.  Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339),  sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :return: The creation_date_time of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this ResponseRecurringPaymentsPostData.

        Data e hora em que o pagamento foi criado.  Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339),  sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :param creation_date_time: The creation_date_time of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def status_update_date_time(self):
        """Gets the status_update_date_time of this ResponseRecurringPaymentsPostData.  # noqa: E501

        Data e hora em que o pagamento teve o status atualizado.  Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339),  sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :return: The status_update_date_time of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: datetime
        """
        return self._status_update_date_time

    @status_update_date_time.setter
    def status_update_date_time(self, status_update_date_time):
        """Sets the status_update_date_time of this ResponseRecurringPaymentsPostData.

        Data e hora em que o pagamento teve o status atualizado.  Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339),  sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :param status_update_date_time: The status_update_date_time of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: datetime
        """
        if status_update_date_time is None:
            raise ValueError("Invalid value for `status_update_date_time`, must not be `None`")  # noqa: E501

        self._status_update_date_time = status_update_date_time

    @property
    def ibge_town_code(self):
        """Gets the ibge_town_code of this ResponseRecurringPaymentsPostData.  # noqa: E501

        O campo ibgeTownCode no arranjo Pix tem o mesmo comportamento que o campo codMun descrito no item 1.6.6 do manual do Pix.  1. Caso a informação referente ao município não seja enviada, o PSP do recebedor assumirá que não existem feriados estaduais e municipais no período em questão;   # noqa: E501

        :return: The ibge_town_code of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: str
        """
        return self._ibge_town_code

    @ibge_town_code.setter
    def ibge_town_code(self, ibge_town_code):
        """Sets the ibge_town_code of this ResponseRecurringPaymentsPostData.

        O campo ibgeTownCode no arranjo Pix tem o mesmo comportamento que o campo codMun descrito no item 1.6.6 do manual do Pix.  1. Caso a informação referente ao município não seja enviada, o PSP do recebedor assumirá que não existem feriados estaduais e municipais no período em questão;   # noqa: E501

        :param ibge_town_code: The ibge_town_code of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: str
        """
        if ibge_town_code is None:
            raise ValueError("Invalid value for `ibge_town_code`, must not be `None`")  # noqa: E501

        self._ibge_town_code = ibge_town_code

    @property
    def status(self):
        """Gets the status of this ResponseRecurringPaymentsPostData.  # noqa: E501


        :return: The status of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: EnumPaymentStatusType
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseRecurringPaymentsPostData.


        :param status: The status of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: EnumPaymentStatusType
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def rejection_reason(self):
        """Gets the rejection_reason of this ResponseRecurringPaymentsPostData.  # noqa: E501


        :return: The rejection_reason of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: RejectionReason
        """
        return self._rejection_reason

    @rejection_reason.setter
    def rejection_reason(self, rejection_reason):
        """Sets the rejection_reason of this ResponseRecurringPaymentsPostData.


        :param rejection_reason: The rejection_reason of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: RejectionReason
        """

        self._rejection_reason = rejection_reason

    @property
    def cnpj_initiator(self):
        """Gets the cnpj_initiator of this ResponseRecurringPaymentsPostData.  # noqa: E501

        CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix.  # noqa: E501

        :return: The cnpj_initiator of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: str
        """
        return self._cnpj_initiator

    @cnpj_initiator.setter
    def cnpj_initiator(self, cnpj_initiator):
        """Sets the cnpj_initiator of this ResponseRecurringPaymentsPostData.

        CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix.  # noqa: E501

        :param cnpj_initiator: The cnpj_initiator of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: str
        """
        if cnpj_initiator is None:
            raise ValueError("Invalid value for `cnpj_initiator`, must not be `None`")  # noqa: E501

        self._cnpj_initiator = cnpj_initiator

    @property
    def payment(self):
        """Gets the payment of this ResponseRecurringPaymentsPostData.  # noqa: E501


        :return: The payment of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: PaymentPix
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this ResponseRecurringPaymentsPostData.


        :param payment: The payment of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: PaymentPix
        """
        if payment is None:
            raise ValueError("Invalid value for `payment`, must not be `None`")  # noqa: E501

        self._payment = payment

    @property
    def remittance_information(self):
        """Gets the remittance_information of this ResponseRecurringPaymentsPostData.  # noqa: E501

        Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.   # noqa: E501

        :return: The remittance_information of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: str
        """
        return self._remittance_information

    @remittance_information.setter
    def remittance_information(self, remittance_information):
        """Sets the remittance_information of this ResponseRecurringPaymentsPostData.

        Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.   # noqa: E501

        :param remittance_information: The remittance_information of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: str
        """

        self._remittance_information = remittance_information

    @property
    def creditor_account(self):
        """Gets the creditor_account of this ResponseRecurringPaymentsPostData.  # noqa: E501


        :return: The creditor_account of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: CreditorAccountPost
        """
        return self._creditor_account

    @creditor_account.setter
    def creditor_account(self, creditor_account):
        """Sets the creditor_account of this ResponseRecurringPaymentsPostData.


        :param creditor_account: The creditor_account of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: CreditorAccountPost
        """

        self._creditor_account = creditor_account

    @property
    def debtor_account(self):
        """Gets the debtor_account of this ResponseRecurringPaymentsPostData.  # noqa: E501


        :return: The debtor_account of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: DebtorAccount
        """
        return self._debtor_account

    @debtor_account.setter
    def debtor_account(self, debtor_account):
        """Sets the debtor_account of this ResponseRecurringPaymentsPostData.


        :param debtor_account: The debtor_account of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: DebtorAccount
        """

        self._debtor_account = debtor_account

    @property
    def cancellation(self):
        """Gets the cancellation of this ResponseRecurringPaymentsPostData.  # noqa: E501


        :return: The cancellation of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: PixPaymentCancellation
        """
        return self._cancellation

    @cancellation.setter
    def cancellation(self, cancellation):
        """Sets the cancellation of this ResponseRecurringPaymentsPostData.


        :param cancellation: The cancellation of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: PixPaymentCancellation
        """

        self._cancellation = cancellation

    @property
    def authorisation_flow(self):
        """Gets the authorisation_flow of this ResponseRecurringPaymentsPostData.  # noqa: E501

        Campo condicional utilizado para identificar o fluxo de autorização em que o pagamento foi solicitado.  [Restrição] Se CIBA ou FIDO, preenchimento obrigatório. Caso o campo não esteja presente no payload, subentende-se que o fluxo de autorização utilizado é o HYBRID_FLOW.   # noqa: E501

        :return: The authorisation_flow of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_flow

    @authorisation_flow.setter
    def authorisation_flow(self, authorisation_flow):
        """Sets the authorisation_flow of this ResponseRecurringPaymentsPostData.

        Campo condicional utilizado para identificar o fluxo de autorização em que o pagamento foi solicitado.  [Restrição] Se CIBA ou FIDO, preenchimento obrigatório. Caso o campo não esteja presente no payload, subentende-se que o fluxo de autorização utilizado é o HYBRID_FLOW.   # noqa: E501

        :param authorisation_flow: The authorisation_flow of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: str
        """
        allowed_values = ["HYBRID_FLOW", "CIBA_FLOW", "FIDO_FLOW"]  # noqa: E501
        if authorisation_flow not in allowed_values:
            raise ValueError(
                "Invalid value for `authorisation_flow` ({0}), must be one of {1}"  # noqa: E501
                .format(authorisation_flow, allowed_values)
            )

        self._authorisation_flow = authorisation_flow

    @property
    def local_instrument(self):
        """Gets the local_instrument of this ResponseRecurringPaymentsPostData.  # noqa: E501

        Especifica a forma de iniciação do pagamento - MANU - Inserção manual de dados da conta transacional - DICT - Inserção manual de chave Pix - INIC - Indica que o recebedor (creditor) contratou o Iniciador de Pagamentos especificamente para realizar iniciações de pagamento em que o beneficiário é previamente conhecido   # noqa: E501

        :return: The local_instrument of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: str
        """
        return self._local_instrument

    @local_instrument.setter
    def local_instrument(self, local_instrument):
        """Sets the local_instrument of this ResponseRecurringPaymentsPostData.

        Especifica a forma de iniciação do pagamento - MANU - Inserção manual de dados da conta transacional - DICT - Inserção manual de chave Pix - INIC - Indica que o recebedor (creditor) contratou o Iniciador de Pagamentos especificamente para realizar iniciações de pagamento em que o beneficiário é previamente conhecido   # noqa: E501

        :param local_instrument: The local_instrument of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: str
        """
        if local_instrument is None:
            raise ValueError("Invalid value for `local_instrument`, must not be `None`")  # noqa: E501
        allowed_values = ["MANU", "DICT", "INIC"]  # noqa: E501
        if local_instrument not in allowed_values:
            raise ValueError(
                "Invalid value for `local_instrument` ({0}), must be one of {1}"  # noqa: E501
                .format(local_instrument, allowed_values)
            )

        self._local_instrument = local_instrument

    @property
    def proxy(self):
        """Gets the proxy of this ResponseRecurringPaymentsPostData.  # noqa: E501

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória.  No caso de telefone celular deve ser informado no padrão E.1641. Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres.  No caso de CPF deverá ser informado com 11 números, sem pontos ou traços. Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços.  No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na [RFC4122](https://tools.ietf.org/html/rfc4122).  Se informado, a detentora da conta deve validar o proxy no DICT quando localInstrument for igual a DICT e validar o campo creditorAccount.  Esta validação é opcional caso o localInstrument for igual a INIC.  [Restrição] Se localInstrument for igual a DICT, o campo proxy deve ser preenchido.   # noqa: E501

        :return: The proxy of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this ResponseRecurringPaymentsPostData.

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória.  No caso de telefone celular deve ser informado no padrão E.1641. Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres.  No caso de CPF deverá ser informado com 11 números, sem pontos ou traços. Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços.  No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na [RFC4122](https://tools.ietf.org/html/rfc4122).  Se informado, a detentora da conta deve validar o proxy no DICT quando localInstrument for igual a DICT e validar o campo creditorAccount.  Esta validação é opcional caso o localInstrument for igual a INIC.  [Restrição] Se localInstrument for igual a DICT, o campo proxy deve ser preenchido.   # noqa: E501

        :param proxy: The proxy of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    @property
    def transaction_identification(self):
        """Gets the transaction_identification of this ResponseRecurringPaymentsPostData.  # noqa: E501

        Trata-se de um identificador de transação que deve ser retransmitido intacto pelo PSP do pagador ao gerar a ordem de pagamento.  Essa informação permitirá ao recebedor identificar e correlacionar a transferência, quando recebida, com a apresentação das instruções ao pagador.  Os caracteres permitidos no contexto do Pix para o campo txid (EMV 62-05) são:Letras minúsculas, de 'a' a 'z' Letras maiúsculas, de 'A' a 'z' Dígitos decimais, de '0' a '9'.   # noqa: E501

        :return: The transaction_identification of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_identification

    @transaction_identification.setter
    def transaction_identification(self, transaction_identification):
        """Sets the transaction_identification of this ResponseRecurringPaymentsPostData.

        Trata-se de um identificador de transação que deve ser retransmitido intacto pelo PSP do pagador ao gerar a ordem de pagamento.  Essa informação permitirá ao recebedor identificar e correlacionar a transferência, quando recebida, com a apresentação das instruções ao pagador.  Os caracteres permitidos no contexto do Pix para o campo txid (EMV 62-05) são:Letras minúsculas, de 'a' a 'z' Letras maiúsculas, de 'A' a 'z' Dígitos decimais, de '0' a '9'.   # noqa: E501

        :param transaction_identification: The transaction_identification of this ResponseRecurringPaymentsPostData.  # noqa: E501
        :type: str
        """

        self._transaction_identification = transaction_identification

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
        if issubclass(ResponseRecurringPaymentsPostData, dict):
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
        if not isinstance(other, ResponseRecurringPaymentsPostData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
