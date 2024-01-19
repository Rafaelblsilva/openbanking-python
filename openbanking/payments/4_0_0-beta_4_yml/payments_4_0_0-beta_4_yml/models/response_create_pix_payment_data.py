# coding: utf-8

"""
    API Payment Initiation - Open Finance Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Finance Brasil. Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API: - `CONTA`, referente às instituições detentoras de conta participantes do Open Finance Brasil; - `PAGTO`, referente às instituições iniciadoras de pagamento participantes do Open Finance Brasil.  Os tokens utilizados para consumo nos endpoints de consentimentos devem possuir o scope `payments` e os `endpoints` de pagamentos devem possuir os `scopes`, `openid` e `payments`.  Esta API não requer a implementação de `permissions` para sua utilização. Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Regras do arranjo Pix A implementação e o uso da API de Pagamentos Pix devem seguir as regras do arranjo Pix do Banco Central, que podem ser encontradas no link abaixo:    [https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix](https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix)  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:  - Certificados exigidos para assinatura de mensagens: [[EN] Padrão de Certificados Open Finance Brasil 2.1](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/82084176/EN+Padr+o+de+Certificados+Open+Finance+Brasil+2.1%20%E2%80%8B)  - Como assinar o payload JWS: [Como Assinar o Payload](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/180061175/Como+Assinar+o+Payload+-+v3.0.0+-+Pagamentos)  ## Controle de acesso  Os endpoints de consulta e cancelamento devem suportar somente acesso a partir de access_token emitido por meio de um grant_type do tipo client_credentials.  Para a criação do consentimento deve-se utilizar client_credentials e para criação de pagamentos deve-se utilizar authorization_code.  ## Aprovações de múltipla alçada  Para o caso de Pix imediato, todas as aprovações necessárias devem ser realizadas nos canais da detentora até às 23:59 (horário de Brasília) da data de solicitação do pagamento. Já para o caso de Pix agendado, todas as aprovações devem ser realizadas até a data/hora limite suportada pela detentora.  ## Validações para pagamentos recorrentes  - Caso a data de liquidação enviada pela iniciadora no endToEndId seja de um dia inexistente, (ex.: 31/02) a detentora deve  rejeitar com erro 422 com código PARAMETRO_INVALIDO e detalhe “Data de liquidação inválida“. A iniciadora deverá solicitar um novo consentimento ao usuário e corrigir as datas de liquidação.  - Quando o detentor receber mais de um item na lista de pagamentos enviados pelo iniciador e optar por responder  assincronamente, é de responsabilidade do detentor realizar a transição para o status SCHD de todos os itens enviados na  lista de pagamentos em até 60 minutos (contados a partir da resposta de sucesso da solicitação).  Caso não seja possível realizar a transição de todos os pagamentos para SCHD, o detentor deverá mover todos os pagamentos  enviados pelo iniciador naquela mesma requisição para RJCT e preencher o motivo de rejeição correspondente,  FALHA_AGENDAMENTO_PAGAMENTOS. O consentimento irá para CONSUMED.  ## Validações **Validações** (*após o processo de DCR e obtenção de token client credential*– não escopo dessa documentação)   Durante a jornada de iniciação de pagamento, diferentes validações são necessárias pela instituição detentora  de conta e devem ocorrer conforme a seguir:   1. Na criação do consentimento (*POST /consents*);  2. Na criação do pagamento - Síncrono (*POST /payments*);  3. Validações na consulta do pagamento (*GET /pix/payments/{paymentId}*); 4. Demais validações executadas durante o processamento assíncrono do pagamento pela detentora, poderão ser consultados pela iniciadora através do endpoint (*GET /pix/payments/{paymentId}*) previstos com retorno HTTP Code 200 - OK com status RJCT (Rejected) e rejectionReason; 5. Demais validações executadas durante o processamento assíncrono do consentimento pela detentora poderão ser consultados pela iniciadora através do endpoint (*GET /consents/{consentId}*) previstos com retorno HTTP Code 200 – OK com status REJECTED e rejectionReason  **Os tipos de validações dispostas abaixo não determinam a ordem em que as instituições devem implementá-las**  1. **Validações na criação do consentimento (_POST /consents_)**     1.1 **Orientações Iniciais**       &ensp;1.1.1 Não devem ser retornadas na resposta deste endpointinformações associadas ao usuário/cliente (ex.  insuficiência de saldo, conta inexistente/bloqueada).       &ensp;1.1.2 Não devem ser executadas validações no DICT (Diretório de Identificadores de Contas Transacionais do Pix), a partir dos dados compartilhados nesse *endpoint*. Tais  validações podem ocorrer somente na criação do pagamento;        &ensp;1.1.3 Não devem ser realizadas validações de informações sobre o usuário/cliente durante a criação do consentimento.   1.2 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;1.2.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;1.2.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;1.2.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;1.2.4 Validação de Claims (exceto data);         &emsp;1.2.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;1.2.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     1.3 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**        &ensp;1.3.1 **Sintáticos**         &emsp;1.3.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios são informados (PARAMETRO_NAO_INFORMADO);         &emsp;1.3.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;1.3.2 **Semânticos**         &emsp;1.3.2.1 Forma de pagamento: Valida se a forma de pagamento é suportada pela detentora (FORMA_PAGAMENTO_INVALIDA) **Obs. No detalhe do erro, a variável “modalidade” deve ser comunicada pela detentora da forma mais clara possível - ex. modalidade de pagamento não suportada (_localInstrument_ - QRES) ou tipo de arranjo pagamento não suportado (_type_ – ex. Pix / TED – previsto para inclusão futura);**         &emsp;1.3.2.2 Data de pagamento: Valida se a data de pagamento enviada é válida para a forma de pagamento selecionada (DATA_PAGAMENTO_INVALIDA);         &emsp;1.3.2.3 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;1.3.2.4 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;1.3.2.5 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA).    2. **Validações na criação do pagamento - Síncrono (_POST /payments_)**     2.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;2.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;2.1.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;2.1.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;2.1.4 Validação de Claims (exceto data);         &emsp;2.1.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;2.1.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     2.2 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**       &ensp;2.2.1 **Sintáticos**         &emsp;2.3.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios são informados (PARAMETRO_NAO_INFORMADO);         &emsp;2.3.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;2.2.2 **Semânticos**         &emsp;2.2.2.1 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);         &emsp;2.2.2.2 Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora (VALOR_ACIMA_LIMITE);         &emsp;2.2.2.3 Valor informado (QR Code): Valida se valor enviado é válido para o QR Code informado (VALOR_INVALIDO);         &emsp;2.2.2.4 Cobrança inválida: Valida expiração, vencimento e status (COBRANCA_INVALIDA);         &emsp;2.2.2.5 Status Consentimento: Valida se o consentimento encontra-se em um dos estados finais “CONSUMED” ou “REJECTED\" (CONSENTIMENTO_INVALIDO);         &emsp;2.2.2.6 Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO)         &emsp;2.2.2.7 Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa (ex. chave Pix inválida, QRCode inválido, conta bloqueada);         &emsp;2.2.2.8 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;2.2.2.9 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;2.2.2.10 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA);         &emsp;2.2.2.11 Consentimento pendente de autorização: Em `PARTIALLY_ACCEPTED` aguardando aprovação de múltiplas alçadas. Não consome nem invalida o consentimento (CONSENTIMENTO_PENDENTE_AUTORIZACAO).     2.3 **Casos de erro para validações síncronas no DICT**       &ensp;Nesse cenário, o pagamento não é criado, porém o consentimento deve ser alterado para o status CONSUMED Retorno esperado do endpoint POST/Payments: HTTP Code 422 - Unprocessable Entity:       &ensp;• Erro por dados inválidos: Conforme item **2.2.2.8**       &ensp;• Erro por suspeita de fraude: Conforme item **2.2.2.9**    3. **Validações na consulta do pagamento (_GET /pix/payments/{paymentId}_)**     3.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token)**       &ensp;3.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;3.1.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED).    4. **Demais validações executadas durante o processamento assíncrono do pagamento pela detentora, poderão ser consultados pela iniciadora através do endpoint _GET /pix/payments/{paymentId}_ previstos com retorno HTTP Code 200 - OK com status RJCT (Rejected) e rejectionReason conforme abaixo (detalhamento adicional na documentação técnica da API):**     4.1 **Demais validações durante processamento assíncrono**       &ensp;4.1.1 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento. No caso de um pagamento agendado, a validação só ocorre na tentativa de liquidação do pagamento (SALDO_INSUFICIENTE);       &ensp;4.1.2 Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora (VALOR_ACIMA_LIMITE);       &ensp;4.1.3 Valor informado (QR Code): Valida se valor enviado é válido para o QR Code informado (VALOR_INVALIDO);       &ensp;4.1.4 Cobrança inválida: Valida expiração, vencimento e status (COBRANCA_INVALIDA);       &ensp;4.1.5 Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO);       &ensp;4.1.6 Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa (ex. chave Pix inválida, QRCode inválido, conta bloqueada);       &ensp;4.1.7 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);       &ensp;4.1.8 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);       &ensp;4.1.9 Validação SPI: Externaliza validações no SPI (PAGAMENTO_RECUSADO_SPI);       &ensp;4.1.10 Falha em agendamentos: Uma ou mais incidências de pagamento não foram possíveis de ser agendadas (FALHA_AGENDAMENTO_PAGAMENTOS);     4.2 **Casos de erro para validações assíncronas no DICT**       &ensp;Neste cenário o pagamento é criado com sucesso (status RCVD) e o consentimento é consumido (status CONSUMED), porém, as validações contra o DICT só ocorrerão de forma assíncrona e em caso de negativa será percebido pela iniciadora na consulta do pagamento (GET /Payments).       &ensp;Retorno esperado do endpoint GET /Payments: HTTP Code 200 - OK.       &ensp;Status do Pagamento: RJCT (Rejected), com as seguintes opções rejectionReason:       &ensp;• Erro por dados inválidos: Conforme item **4.1.7**;       &ensp;• Erro por suspeita de fraude: Conforme item **4.1.8**.  5. **Demais validações executadas durante o processamento assíncrono do consentimento pela detentora poderão ser consultados pela iniciadora através do endpoint _GET /consents/{consentId}_ previstos com retorno HTTP Code 200 – OK com status REJECTED e rejectionReason conforme abaixo:**     5.1 **Validações durante o processamento assíncrono**       &ensp;5.1.1 - Falha de infraestrutura: Ocorreu algum erro interno na detentora durante processamento da criação do consentimento (FALHA_INFRAESTRUTURA)       &ensp;5.1.2 - Tempo de autorização expirado: O usuário não confirmou o consentimento e o mesmo expirou (TEMPO_EXPIRADO_AUTORIZACAO);       &ensp;5.1.3 - Rejeitado pelo usuário: O usuário explicitamente rejeitou a autorização do consentimento (REJEITADO_USUARIO);       &ensp;5.1.4 - Mesma conta origem/destino: A conta indicada pelo usuário para recebimento é a mesma selecionada para o pagamento (CONTAS_ORIGEM_DESTINO_IGUAIS);       &ensp;5.1.5 - Tipo de conta inválida: A conta indicada não permite operações de pagamento (CONTA_NAO_PERMITE_PAGAMENTO);       &ensp;5.1.6 - Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento. Essa validação não deverá ocorrer no caso de um pagamento agendado (SALDO_INSUFICIENTE);       &ensp;5.1.7 - Limites da transação: Valida se o valor ultrapassa o limite estabelecido [na instituição/no arranjo/outro] para permitir a realização de transações pelo cliente (VALOR_ACIMA_LIMITE);       &ensp;5.1.8 - QRCode inválido: O QRCode utilizado para a iniciação de pagamento não é válido (QRCODE_INVALIDO);       &ensp;5.1.9 - Valor inválido: O valor enviado não é válido para o QR Code informado (VALOR_INVALIDO);       &ensp;5.1.10 - Não informado: Demais validações não explicitamente informadas (ex. suspeita de fraude) e consentimentos rejeitados em versões que não existiam o campo rejectionReason na API de Pagamentos (NAO_INFORMADO)       &ensp;5.1.11 - Tempo expirado consumo: O usuário não finalizou o fluxo de pagamento e o consentimento expirou (TEMPO_EXPIRADO_CONSUMO).     5.2 **[Momentos obrigatórios de validação dos rejectionReasons de acordo com o funil de consentimentos.](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/150863940) Para casos em que um consentimento for rejeitado por mais de um motivo, seguir a ordem de prioridade da tabela.**      ```   |----------------------------------|------------------------------|---------------------|   | Etapas do funil de consentimento | rejectionReason/code         | Ordem de prioridade |   |----------------------------------|------------------------------|---------------------|   |                                  | TEMPO_EXPIRADO_AUTORIZACAO   |          1          |   | Início da autenticação           | FALHA_INFRAESTRUTURA         |          2          |   |                                  | NAO_INFORMADO                |          3          |   |----------------------------------|------------------------------|---------------------|   |                                  | TEMPO_EXPIRADO_AUTORIZACAO   |          1          |   |                                  | REJEITADO_USUARIO            |          2          |   | Conclusão da autenticação        | FALHA_INFRAESTRUTURA         |          3          |   |                                  | NAO_INFORMADO                |          4          |   |----------------------------------|------------------------------|---------------------|   |                                  | CONTA_NAO_PERMITE_PAGAMENTO  |          1          |   |                                  | CONTAS_ORIGEM_DESTINO_IGUAIS |          2          |   |                                  | VALOR_INVALIDO               |          3          |   | Autorização do cliente           | QRCODE_INVALIDO              |          4          |   |                                  | VALOR_ACIMA_LIMITE           |          5          |   |                                  | SALDO_INSUFICIENTE           |          6          |   |                                  | FALHA_INFRAESTRUTURA         |          7          |   |                                  | NAO_INFORMADO                |          8          |   |----------------------------------|------------------------------|---------------------|   |                                  | FALHA_INFRAESTRUTURA         |          1          |   | Authorisation code emitido       | NAO_INFORMADO                |          2          |   |                                  | TEMPO_EXPIRADO_CONSUMO       |          3          |   |----------------------------------|------------------------------|---------------------|   ```   Existem dois `endpoints` para cancelamento de pagamentos, um deles é o _PATCH /pix/payments/{paymentId}_ e o outro é o _PATCH /pix/payments/consents/{consentId}_.   - O _PATCH /pix/payments/{paymentId}_ deve ser utilizado para o cancelamento de um pagamento de forma unitária. Não deve ser utilizado para o cancelamento de todos os agendamentos recorrentes associados a um consentimento.   - O _PATCH /pix/payments/consents/{consentId}_ deve ser utilizado no cancelamento de todas as ocorrências de pagamentos agendados presentes em uma recorrência de pagamentos. Todos os pagamentos associados ao consentimento informado e passíveis de cancelamento (ainda não liquidados, com os status PDNG e SCHD) deverão ser cancelados.   # noqa: E501

    OpenAPI spec version: 4.0.0-beta.4
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ResponseCreatePixPaymentData(object):
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
        'rejection_reason': 'RejectionReason',
        'local_instrument': 'EnumLocalInstrument',
        'cnpj_initiator': 'str',
        'payment': 'ResponseCreatePixPaymentPayment',
        'transaction_identification': 'str',
        'remittance_information': 'str',
        'creditor_account': 'CreditorAccount',
        'debtor_account': 'DebtorAccount',
        'authorisation_flow': 'str'
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
        'creditor_account': 'creditorAccount',
        'debtor_account': 'debtorAccount',
        'authorisation_flow': 'authorisationFlow'
    }

    def __init__(self, payment_id=None, end_to_end_id=None, consent_id=None, creation_date_time=None, status_update_date_time=None, proxy=None, ibge_town_code=None, status=None, rejection_reason=None, local_instrument=None, cnpj_initiator=None, payment=None, transaction_identification=None, remittance_information=None, creditor_account=None, debtor_account=None, authorisation_flow=None):  # noqa: E501
        """ResponseCreatePixPaymentData - a model defined in Swagger"""  # noqa: E501
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
        self._debtor_account = None
        self._authorisation_flow = None
        self.discriminator = None
        self.payment_id = payment_id
        self.end_to_end_id = end_to_end_id
        if consent_id is not None:
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
        self.debtor_account = debtor_account
        if authorisation_flow is not None:
            self.authorisation_flow = authorisation_flow

    @property
    def payment_id(self):
        """Gets the payment_id of this ResponseCreatePixPaymentData.  # noqa: E501

        Código ou identificador único informado pela instituição detentora da conta para representar a iniciação de pagamento individual. O `paymentId` deve ser diferente do `endToEndId`. Este é o identificador que deverá ser utilizado na consulta ao status da iniciação de pagamento efetuada.   # noqa: E501

        :return: The payment_id of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this ResponseCreatePixPaymentData.

        Código ou identificador único informado pela instituição detentora da conta para representar a iniciação de pagamento individual. O `paymentId` deve ser diferente do `endToEndId`. Este é o identificador que deverá ser utilizado na consulta ao status da iniciação de pagamento efetuada.   # noqa: E501

        :param payment_id: The payment_id of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: str
        """
        if payment_id is None:
            raise ValueError("Invalid value for `payment_id`, must not be `None`")  # noqa: E501

        self._payment_id = payment_id

    @property
    def end_to_end_id(self):
        """Gets the end_to_end_id of this ResponseCreatePixPaymentData.  # noqa: E501


        :return: The end_to_end_id of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: EndToEndId
        """
        return self._end_to_end_id

    @end_to_end_id.setter
    def end_to_end_id(self, end_to_end_id):
        """Sets the end_to_end_id of this ResponseCreatePixPaymentData.


        :param end_to_end_id: The end_to_end_id of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: EndToEndId
        """
        if end_to_end_id is None:
            raise ValueError("Invalid value for `end_to_end_id`, must not be `None`")  # noqa: E501

        self._end_to_end_id = end_to_end_id

    @property
    def consent_id(self):
        """Gets the consent_id of this ResponseCreatePixPaymentData.  # noqa: E501

        Identificador único do consentimento criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).    [Restrição] Este campo é de preenchimento obrigatório quando o valor do campo authorisationFlow for igual a FIDO_FLOW.   # noqa: E501

        :return: The consent_id of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this ResponseCreatePixPaymentData.

        Identificador único do consentimento criado para a iniciação de pagamento solicitada. Deverá ser um URN - Uniform Resource Name. Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN seja um identificador de recurso persistente e independente da localização. Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex) - o identificador específico dentro do namespace (C1DD33123). Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).    [Restrição] Este campo é de preenchimento obrigatório quando o valor do campo authorisationFlow for igual a FIDO_FLOW.   # noqa: E501

        :param consent_id: The consent_id of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._consent_id = consent_id

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this ResponseCreatePixPaymentData.  # noqa: E501

        Data e hora em que o recurso foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :return: The creation_date_time of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this ResponseCreatePixPaymentData.

        Data e hora em que o recurso foi criado. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :param creation_date_time: The creation_date_time of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def status_update_date_time(self):
        """Gets the status_update_date_time of this ResponseCreatePixPaymentData.  # noqa: E501

        Data e hora da última atualização da iniciação de pagamento. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :return: The status_update_date_time of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: datetime
        """
        return self._status_update_date_time

    @status_update_date_time.setter
    def status_update_date_time(self, status_update_date_time):
        """Sets the status_update_date_time of this ResponseCreatePixPaymentData.

        Data e hora da última atualização da iniciação de pagamento. Uma string com data e hora conforme especificação RFC-3339, sempre com a utilização de timezone UTC(UTC time format).   # noqa: E501

        :param status_update_date_time: The status_update_date_time of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: datetime
        """
        if status_update_date_time is None:
            raise ValueError("Invalid value for `status_update_date_time`, must not be `None`")  # noqa: E501

        self._status_update_date_time = status_update_date_time

    @property
    def proxy(self):
        """Gets the proxy of this ResponseCreatePixPaymentData.  # noqa: E501

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória. No caso de telefone celular deve ser informado no padrão E.1641. Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres. No caso de CPF deverá ser informado com 11 números, sem pontos ou traços. Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços. No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223. Se informado, a detentora da conta deve validar o proxy no DICT quando localInstrument for igual a DICT, QRDN ou QRES e validar o campo creditorAccount. Esta validação é opcional caso o localInstrument for igual a INIC. [Restrição] Se localInstrument for igual a MANU, o campo proxy não deve ser preenchido. Se localInstrument for igual INIC, DICT, QRDN ou QRES, o campo proxy deve ser sempre preenchido com a chave Pix.   # noqa: E501

        :return: The proxy of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this ResponseCreatePixPaymentData.

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória. No caso de telefone celular deve ser informado no padrão E.1641. Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres. No caso de CPF deverá ser informado com 11 números, sem pontos ou traços. Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços. No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223. Se informado, a detentora da conta deve validar o proxy no DICT quando localInstrument for igual a DICT, QRDN ou QRES e validar o campo creditorAccount. Esta validação é opcional caso o localInstrument for igual a INIC. [Restrição] Se localInstrument for igual a MANU, o campo proxy não deve ser preenchido. Se localInstrument for igual INIC, DICT, QRDN ou QRES, o campo proxy deve ser sempre preenchido com a chave Pix.   # noqa: E501

        :param proxy: The proxy of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    @property
    def ibge_town_code(self):
        """Gets the ibge_town_code of this ResponseCreatePixPaymentData.  # noqa: E501

        O campo ibgetowncode no arranjo PIX, tem o mesmo comportamento que o campo codMun descrito no item 1.6.6 do manual do PIX, conforme segue:  1. Caso a informação referente ao município não seja enviada; o PSP do recebedor assumirá que não existem feriados estaduais e municipais no período em questão;   # noqa: E501

        :return: The ibge_town_code of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._ibge_town_code

    @ibge_town_code.setter
    def ibge_town_code(self, ibge_town_code):
        """Sets the ibge_town_code of this ResponseCreatePixPaymentData.

        O campo ibgetowncode no arranjo PIX, tem o mesmo comportamento que o campo codMun descrito no item 1.6.6 do manual do PIX, conforme segue:  1. Caso a informação referente ao município não seja enviada; o PSP do recebedor assumirá que não existem feriados estaduais e municipais no período em questão;   # noqa: E501

        :param ibge_town_code: The ibge_town_code of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._ibge_town_code = ibge_town_code

    @property
    def status(self):
        """Gets the status of this ResponseCreatePixPaymentData.  # noqa: E501


        :return: The status of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: EnumPaymentStatusType
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResponseCreatePixPaymentData.


        :param status: The status of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: EnumPaymentStatusType
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def rejection_reason(self):
        """Gets the rejection_reason of this ResponseCreatePixPaymentData.  # noqa: E501


        :return: The rejection_reason of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: RejectionReason
        """
        return self._rejection_reason

    @rejection_reason.setter
    def rejection_reason(self, rejection_reason):
        """Sets the rejection_reason of this ResponseCreatePixPaymentData.


        :param rejection_reason: The rejection_reason of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: RejectionReason
        """

        self._rejection_reason = rejection_reason

    @property
    def local_instrument(self):
        """Gets the local_instrument of this ResponseCreatePixPaymentData.  # noqa: E501


        :return: The local_instrument of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: EnumLocalInstrument
        """
        return self._local_instrument

    @local_instrument.setter
    def local_instrument(self, local_instrument):
        """Sets the local_instrument of this ResponseCreatePixPaymentData.


        :param local_instrument: The local_instrument of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: EnumLocalInstrument
        """
        if local_instrument is None:
            raise ValueError("Invalid value for `local_instrument`, must not be `None`")  # noqa: E501

        self._local_instrument = local_instrument

    @property
    def cnpj_initiator(self):
        """Gets the cnpj_initiator of this ResponseCreatePixPaymentData.  # noqa: E501

        CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix.  # noqa: E501

        :return: The cnpj_initiator of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._cnpj_initiator

    @cnpj_initiator.setter
    def cnpj_initiator(self, cnpj_initiator):
        """Sets the cnpj_initiator of this ResponseCreatePixPaymentData.

        CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix.  # noqa: E501

        :param cnpj_initiator: The cnpj_initiator of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: str
        """
        if cnpj_initiator is None:
            raise ValueError("Invalid value for `cnpj_initiator`, must not be `None`")  # noqa: E501

        self._cnpj_initiator = cnpj_initiator

    @property
    def payment(self):
        """Gets the payment of this ResponseCreatePixPaymentData.  # noqa: E501


        :return: The payment of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: ResponseCreatePixPaymentPayment
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this ResponseCreatePixPaymentData.


        :param payment: The payment of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: ResponseCreatePixPaymentPayment
        """
        if payment is None:
            raise ValueError("Invalid value for `payment`, must not be `None`")  # noqa: E501

        self._payment = payment

    @property
    def transaction_identification(self):
        """Gets the transaction_identification of this ResponseCreatePixPaymentData.  # noqa: E501

        Trata-se de um identificador de transação que deve ser retransmitido intacto pelo PSP do pagador ao gerar a ordem de pagamento.  [Restrição] A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora, caso ele tenha sido enviado na requisição da iniciação do pagamento.   # noqa: E501

        :return: The transaction_identification of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_identification

    @transaction_identification.setter
    def transaction_identification(self, transaction_identification):
        """Sets the transaction_identification of this ResponseCreatePixPaymentData.

        Trata-se de um identificador de transação que deve ser retransmitido intacto pelo PSP do pagador ao gerar a ordem de pagamento.  [Restrição] A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora, caso ele tenha sido enviado na requisição da iniciação do pagamento.   # noqa: E501

        :param transaction_identification: The transaction_identification of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._transaction_identification = transaction_identification

    @property
    def remittance_information(self):
        """Gets the remittance_information of this ResponseCreatePixPaymentData.  # noqa: E501

        Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.   # noqa: E501

        :return: The remittance_information of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._remittance_information

    @remittance_information.setter
    def remittance_information(self, remittance_information):
        """Sets the remittance_information of this ResponseCreatePixPaymentData.

        Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.   # noqa: E501

        :param remittance_information: The remittance_information of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._remittance_information = remittance_information

    @property
    def creditor_account(self):
        """Gets the creditor_account of this ResponseCreatePixPaymentData.  # noqa: E501


        :return: The creditor_account of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: CreditorAccount
        """
        return self._creditor_account

    @creditor_account.setter
    def creditor_account(self, creditor_account):
        """Sets the creditor_account of this ResponseCreatePixPaymentData.


        :param creditor_account: The creditor_account of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: CreditorAccount
        """
        if creditor_account is None:
            raise ValueError("Invalid value for `creditor_account`, must not be `None`")  # noqa: E501

        self._creditor_account = creditor_account

    @property
    def debtor_account(self):
        """Gets the debtor_account of this ResponseCreatePixPaymentData.  # noqa: E501


        :return: The debtor_account of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: DebtorAccount
        """
        return self._debtor_account

    @debtor_account.setter
    def debtor_account(self, debtor_account):
        """Sets the debtor_account of this ResponseCreatePixPaymentData.


        :param debtor_account: The debtor_account of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: DebtorAccount
        """
        if debtor_account is None:
            raise ValueError("Invalid value for `debtor_account`, must not be `None`")  # noqa: E501

        self._debtor_account = debtor_account

    @property
    def authorisation_flow(self):
        """Gets the authorisation_flow of this ResponseCreatePixPaymentData.  # noqa: E501

        Campo condicional utilizado para identificar o fluxo de autorização em que o pagamento foi solicitado.  [Restrição] Se CIBA ou FIDO, preenchimento obrigatório. Caso o campo não esteja presente no payload, subentende-se que o fluxo de autorização utilizado é o HYBRID_FLOW.   # noqa: E501

        :return: The authorisation_flow of this ResponseCreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_flow

    @authorisation_flow.setter
    def authorisation_flow(self, authorisation_flow):
        """Sets the authorisation_flow of this ResponseCreatePixPaymentData.

        Campo condicional utilizado para identificar o fluxo de autorização em que o pagamento foi solicitado.  [Restrição] Se CIBA ou FIDO, preenchimento obrigatório. Caso o campo não esteja presente no payload, subentende-se que o fluxo de autorização utilizado é o HYBRID_FLOW.   # noqa: E501

        :param authorisation_flow: The authorisation_flow of this ResponseCreatePixPaymentData.  # noqa: E501
        :type: str
        """
        allowed_values = ["HYBRID_FLOW", "CIBA_FLOW", "FIDO_FLOW"]  # noqa: E501
        if authorisation_flow not in allowed_values:
            raise ValueError(
                "Invalid value for `authorisation_flow` ({0}), must be one of {1}"  # noqa: E501
                .format(authorisation_flow, allowed_values)
            )

        self._authorisation_flow = authorisation_flow

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
        if issubclass(ResponseCreatePixPaymentData, dict):
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
        if not isinstance(other, ResponseCreatePixPaymentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
