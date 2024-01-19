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

class ResponseRecurringConsentData(object):
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
        'recurring_consent_id': 'str',
        'status_update_date_time': 'datetime',
        'logged_user': 'LoggedUser',
        'business_entity': 'BusinessEntity',
        'status': 'EnumAuthorisationStatusType',
        'creditors': 'Creditors',
        'start_date_time': 'datetime',
        'creation_date_time': 'datetime',
        'expiration_date_time': 'datetime',
        'additional_information': 'str',
        'debtor_account': 'ConsentsDebtorAccount',
        'rejection': 'Rejection',
        'revocation': 'ResponsePostRecurringConsentDataRevocation',
        'recurring_configuration': 'RecurringConfiguration',
        'risk_signals': 'RiskSignalsConsents'
    }

    attribute_map = {
        'recurring_consent_id': 'recurringConsentId',
        'status_update_date_time': 'statusUpdateDateTime',
        'logged_user': 'loggedUser',
        'business_entity': 'businessEntity',
        'status': 'status',
        'creditors': 'creditors',
        'start_date_time': 'startDateTime',
        'creation_date_time': 'creationDateTime',
        'expiration_date_time': 'expirationDateTime',
        'additional_information': 'additionalInformation',
        'debtor_account': 'debtorAccount',
        'rejection': 'rejection',
        'revocation': 'revocation',
        'recurring_configuration': 'recurringConfiguration',
        'risk_signals': 'riskSignals'
    }

    def __init__(self, recurring_consent_id=None, status_update_date_time=None, logged_user=None, business_entity=None, status=None, creditors=None, start_date_time=None, creation_date_time=None, expiration_date_time=None, additional_information=None, debtor_account=None, rejection=None, revocation=None, recurring_configuration=None, risk_signals=None):  # noqa: E501
        """ResponseRecurringConsentData - a model defined in Swagger"""  # noqa: E501
        self._recurring_consent_id = None
        self._status_update_date_time = None
        self._logged_user = None
        self._business_entity = None
        self._status = None
        self._creditors = None
        self._start_date_time = None
        self._creation_date_time = None
        self._expiration_date_time = None
        self._additional_information = None
        self._debtor_account = None
        self._rejection = None
        self._revocation = None
        self._recurring_configuration = None
        self._risk_signals = None
        self.discriminator = None
        self.recurring_consent_id = recurring_consent_id
        self.status_update_date_time = status_update_date_time
        self.logged_user = logged_user
        self.business_entity = business_entity
        self.status = status
        self.creditors = creditors
        self.start_date_time = start_date_time
        self.creation_date_time = creation_date_time
        if expiration_date_time is not None:
            self.expiration_date_time = expiration_date_time
        if additional_information is not None:
            self.additional_information = additional_information
        if debtor_account is not None:
            self.debtor_account = debtor_account
        if rejection is not None:
            self.rejection = rejection
        if revocation is not None:
            self.revocation = revocation
        self.recurring_configuration = recurring_configuration
        if risk_signals is not None:
            self.risk_signals = risk_signals

    @property
    def recurring_consent_id(self):
        """Gets the recurring_consent_id of this ResponseRecurringConsentData.  # noqa: E501

        Identificador único do consentimento de longa duração criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://datatracker.ietf.org/doc/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para `recurringConsentId` temos:   - o namespace(urn)   - o identificador associado ao namespace da instituição transmissora (bancoex)   - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://datatracker.ietf.org/doc/html/rfc8141).   # noqa: E501

        :return: The recurring_consent_id of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: str
        """
        return self._recurring_consent_id

    @recurring_consent_id.setter
    def recurring_consent_id(self, recurring_consent_id):
        """Sets the recurring_consent_id of this ResponseRecurringConsentData.

        Identificador único do consentimento de longa duração criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://datatracker.ietf.org/doc/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para `recurringConsentId` temos:   - o namespace(urn)   - o identificador associado ao namespace da instituição transmissora (bancoex)   - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://datatracker.ietf.org/doc/html/rfc8141).   # noqa: E501

        :param recurring_consent_id: The recurring_consent_id of this ResponseRecurringConsentData.  # noqa: E501
        :type: str
        """
        if recurring_consent_id is None:
            raise ValueError("Invalid value for `recurring_consent_id`, must not be `None`")  # noqa: E501

        self._recurring_consent_id = recurring_consent_id

    @property
    def status_update_date_time(self):
        """Gets the status_update_date_time of this ResponseRecurringConsentData.  # noqa: E501

        Data e hora em que o consentimento teve o status atualizado. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :return: The status_update_date_time of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: datetime
        """
        return self._status_update_date_time

    @status_update_date_time.setter
    def status_update_date_time(self, status_update_date_time):
        """Sets the status_update_date_time of this ResponseRecurringConsentData.

        Data e hora em que o consentimento teve o status atualizado. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :param status_update_date_time: The status_update_date_time of this ResponseRecurringConsentData.  # noqa: E501
        :type: datetime
        """
        if status_update_date_time is None:
            raise ValueError("Invalid value for `status_update_date_time`, must not be `None`")  # noqa: E501

        self._status_update_date_time = status_update_date_time

    @property
    def logged_user(self):
        """Gets the logged_user of this ResponseRecurringConsentData.  # noqa: E501


        :return: The logged_user of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: LoggedUser
        """
        return self._logged_user

    @logged_user.setter
    def logged_user(self, logged_user):
        """Sets the logged_user of this ResponseRecurringConsentData.


        :param logged_user: The logged_user of this ResponseRecurringConsentData.  # noqa: E501
        :type: LoggedUser
        """
        if logged_user is None:
            raise ValueError("Invalid value for `logged_user`, must not be `None`")  # noqa: E501

        self._logged_user = logged_user

    @property
    def business_entity(self):
        """Gets the business_entity of this ResponseRecurringConsentData.  # noqa: E501


        :return: The business_entity of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: BusinessEntity
        """
        return self._business_entity

    @business_entity.setter
    def business_entity(self, business_entity):
        """Sets the business_entity of this ResponseRecurringConsentData.


        :param business_entity: The business_entity of this ResponseRecurringConsentData.  # noqa: E501
        :type: BusinessEntity
        """
        if business_entity is None:
            raise ValueError("Invalid value for `business_entity`, must not be `None`")  # noqa: E501

        self._business_entity = business_entity

    @property
    def status(self):
        """Gets the status of this ResponseRecurringConsentData.  # noqa: E501


        :return: The status of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: EnumAuthorisationStatusType
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseRecurringConsentData.


        :param status: The status of this ResponseRecurringConsentData.  # noqa: E501
        :type: EnumAuthorisationStatusType
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def creditors(self):
        """Gets the creditors of this ResponseRecurringConsentData.  # noqa: E501


        :return: The creditors of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: Creditors
        """
        return self._creditors

    @creditors.setter
    def creditors(self, creditors):
        """Sets the creditors of this ResponseRecurringConsentData.


        :param creditors: The creditors of this ResponseRecurringConsentData.  # noqa: E501
        :type: Creditors
        """
        if creditors is None:
            raise ValueError("Invalid value for `creditors`, must not be `None`")  # noqa: E501

        self._creditors = creditors

    @property
    def start_date_time(self):
        """Gets the start_date_time of this ResponseRecurringConsentData.  # noqa: E501

        Data e hora em que o consentimento deve passar a ser válido. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :return: The start_date_time of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_time

    @start_date_time.setter
    def start_date_time(self, start_date_time):
        """Sets the start_date_time of this ResponseRecurringConsentData.

        Data e hora em que o consentimento deve passar a ser válido. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :param start_date_time: The start_date_time of this ResponseRecurringConsentData.  # noqa: E501
        :type: datetime
        """
        if start_date_time is None:
            raise ValueError("Invalid value for `start_date_time`, must not be `None`")  # noqa: E501

        self._start_date_time = start_date_time

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this ResponseRecurringConsentData.  # noqa: E501

        Data e hora em que o consentimento foi criado. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :return: The creation_date_time of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this ResponseRecurringConsentData.

        Data e hora em que o consentimento foi criado. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :param creation_date_time: The creation_date_time of this ResponseRecurringConsentData.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def expiration_date_time(self):
        """Gets the expiration_date_time of this ResponseRecurringConsentData.  # noqa: E501

        Data e hora em que o consentimento deve deixar de ser válido. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :return: The expiration_date_time of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: datetime
        """
        return self._expiration_date_time

    @expiration_date_time.setter
    def expiration_date_time(self, expiration_date_time):
        """Sets the expiration_date_time of this ResponseRecurringConsentData.

        Data e hora em que o consentimento deve deixar de ser válido. Uma string com data e hora conforme especificação [RFC-3339](https://datatracker.ietf.org/doc/html/rfc3339), sempre com a utilização de timezone UTC(UTC time format).  # noqa: E501

        :param expiration_date_time: The expiration_date_time of this ResponseRecurringConsentData.  # noqa: E501
        :type: datetime
        """

        self._expiration_date_time = expiration_date_time

    @property
    def additional_information(self):
        """Gets the additional_information of this ResponseRecurringConsentData.  # noqa: E501

        Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional no consentimento  # noqa: E501

        :return: The additional_information of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: str
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this ResponseRecurringConsentData.

        Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional no consentimento  # noqa: E501

        :param additional_information: The additional_information of this ResponseRecurringConsentData.  # noqa: E501
        :type: str
        """

        self._additional_information = additional_information

    @property
    def debtor_account(self):
        """Gets the debtor_account of this ResponseRecurringConsentData.  # noqa: E501


        :return: The debtor_account of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: ConsentsDebtorAccount
        """
        return self._debtor_account

    @debtor_account.setter
    def debtor_account(self, debtor_account):
        """Sets the debtor_account of this ResponseRecurringConsentData.


        :param debtor_account: The debtor_account of this ResponseRecurringConsentData.  # noqa: E501
        :type: ConsentsDebtorAccount
        """

        self._debtor_account = debtor_account

    @property
    def rejection(self):
        """Gets the rejection of this ResponseRecurringConsentData.  # noqa: E501


        :return: The rejection of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: Rejection
        """
        return self._rejection

    @rejection.setter
    def rejection(self, rejection):
        """Sets the rejection of this ResponseRecurringConsentData.


        :param rejection: The rejection of this ResponseRecurringConsentData.  # noqa: E501
        :type: Rejection
        """

        self._rejection = rejection

    @property
    def revocation(self):
        """Gets the revocation of this ResponseRecurringConsentData.  # noqa: E501


        :return: The revocation of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: ResponsePostRecurringConsentDataRevocation
        """
        return self._revocation

    @revocation.setter
    def revocation(self, revocation):
        """Sets the revocation of this ResponseRecurringConsentData.


        :param revocation: The revocation of this ResponseRecurringConsentData.  # noqa: E501
        :type: ResponsePostRecurringConsentDataRevocation
        """

        self._revocation = revocation

    @property
    def recurring_configuration(self):
        """Gets the recurring_configuration of this ResponseRecurringConsentData.  # noqa: E501


        :return: The recurring_configuration of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: RecurringConfiguration
        """
        return self._recurring_configuration

    @recurring_configuration.setter
    def recurring_configuration(self, recurring_configuration):
        """Sets the recurring_configuration of this ResponseRecurringConsentData.


        :param recurring_configuration: The recurring_configuration of this ResponseRecurringConsentData.  # noqa: E501
        :type: RecurringConfiguration
        """
        if recurring_configuration is None:
            raise ValueError("Invalid value for `recurring_configuration`, must not be `None`")  # noqa: E501

        self._recurring_configuration = recurring_configuration

    @property
    def risk_signals(self):
        """Gets the risk_signals of this ResponseRecurringConsentData.  # noqa: E501


        :return: The risk_signals of this ResponseRecurringConsentData.  # noqa: E501
        :rtype: RiskSignalsConsents
        """
        return self._risk_signals

    @risk_signals.setter
    def risk_signals(self, risk_signals):
        """Sets the risk_signals of this ResponseRecurringConsentData.


        :param risk_signals: The risk_signals of this ResponseRecurringConsentData.  # noqa: E501
        :type: RiskSignalsConsents
        """

        self._risk_signals = risk_signals

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
        if issubclass(ResponseRecurringConsentData, dict):
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
        if not isinstance(other, ResponseRecurringConsentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
