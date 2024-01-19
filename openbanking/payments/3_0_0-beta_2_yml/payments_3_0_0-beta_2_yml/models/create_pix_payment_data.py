# coding: utf-8

"""
    API Payment Initiation - Open Finance Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Finance Brasil. Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API: - `CONTA`, referente às instituições detentoras de conta participantes do Open Finance Brasil; - `PAGTO`, referente às instituições iniciadoras de pagamento participantes do Open Finance Brasil.  Os tokens utilizados para consumo nos endpoints de consentimentos devem possuir o scope `payments` e os `endpoints` de pagamentos devem possuir os `scopes`, `openid` e `payments`.  Esta API não requer a implementação de `permissions` para sua utilização. Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Regras do arranjo Pix A implementação e o uso da API de Pagamentos Pix devem seguir as regras do arranjo Pix do Banco Central, que podem ser encontradas no link abaixo:    [https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix](https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix)  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:  - Certificados exigidos para assinatura de mensagens: [Padrões de certificados digitais Open Finance Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Como assinar o payload JWS: [https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/18055279/Como+Assinar+o+Payload+-+v2.0.0-rc1.0+-+Pagamentos](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/18055279/Como+Assinar+o+Payload+-+v2.0.0-rc1.0+-+Pagamentos)  ## Controle de acesso  O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).  Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.  Para o caso de QR Code estático e dinâmico a detentora deverá obrigatoriamente realizar validações sobre o conteúdo dos campos recebidos. Entretanto, a escolha do momento desta validação na criação do consentimento ou no pagamento, fica a cargo da detentora.  ## Aprovações de múltipla alçada  Para o caso de Pix imediato, todas as aprovações necessárias devem ser realizadas nos canais da detentora até às 23:59 (horário de Brasília) da data de solicitação do pagamento. Já para o caso de Pix agendado, todas as aprovações devem ser realizadas até a data/hora limite suportada pela detentora.  ## Validações **Validações** (*após o processo de DCR e obtenção de token client credential*– não escopo dessa documentação)   Durante a jornada de iniciação de pagamento, diferentes validações são necessárias pela instituição detentora  de conta e devem ocorrer conforme a seguir:   1. Na criação do consentimento (*POST /consents*);  2. Na criação do pagamento - Síncrono (*POST /payments*);  3. Validações na consulta do pagamento (*GET /pix/payments/{paymentId}*); 4. Demais validações executadas durante o processamento assíncrono do pagamento pela detentora, poderão ser consultados pela iniciadora através do endpoint (*GET /pix/payments/{paymentId}*) previstos com retorno HTTP Code 200 - OK com status RJCT (Rejected) e rejectionReason; 5. Demais validações executadas durante o processamento assíncrono do consentimento pela detentora poderão ser consultados pela iniciadora através do endpoint (*GET /consents/{consentId}*) previstos com retorno HTTP Code 200 – OK com status REJECTED e rejectionReason  **Os tipos de validações dispostas abaixo não determinam a ordem em que as instituições devem implementá-las**  1. **Validações na criação do consentimento (_POST /consents_)**     1.1 **Orientações Iniciais**       &ensp;1.1.1 Não devem ser retornadas informações associadas ao usuário/cliente (ex. insuficiência de saldo, conta inexistente/bloqueada), uma vez que o cliente ainda não autorizou o consentimento / consumo de seus dados para o pagamento.       &ensp;1.1.2 Não devem ser executadas validações no DICT (Diretório de Identificadores de Contas Transacionais do Pix), a partir dos dados compartilhados nesse *endpoint*. Tais  validações podem ocorrer somente na criação do pagamento;     1.2 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;1.2.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;1.2.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;1.2.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;1.2.4 Validação de Claims (exceto data);         &emsp;1.2.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;1.2.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     1.3 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**        &ensp;1.3.1 **Sintáticos**         &emsp;1.3.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios são informados (PARAMETRO_NAO_INFORMADO);         &emsp;1.3.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;1.3.2 **Semânticos**         &emsp;1.3.2.1 Forma de pagamento: Valida se a forma de pagamento é suportada pela detentora (FORMA_PAGAMENTO_INVALIDA) **Obs. No detalhe do erro, a variável “modalidade” deve ser comunicada pela detentora da forma mais clara possível - ex. modalidade de pagamento não suportada (_localInstrument_ - QRES) ou tipo de arranjo pagamento não suportado (_type_ – ex. Pix / TED – previsto para inclusão futura);**         &emsp;1.3.2.2 Data de pagamento: Valida se a data de pagamento enviada é válida para a forma de pagamento selecionada (DATA_PAGAMENTO_INVALIDA);         &emsp;1.3.2.3 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;1.3.2.4 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;1.3.2.5 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA).    2. **Validações na criação do pagamento - Síncrono (_POST /payments_)**     2.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;2.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;2.1.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;2.1.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;2.1.4 Validação de Claims (exceto data);         &emsp;2.1.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;2.1.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     2.2 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**       &ensp;2.2.1 **Sintáticos**         &emsp;2.3.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios são informados (PARAMETRO_NAO_INFORMADO);         &emsp;2.3.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;2.2.2 **Semânticos**         &emsp;2.2.2.1 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);         &emsp;2.2.2.2 Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora (VALOR_ACIMA_LIMITE);         &emsp;2.2.2.3 Valor informado (QR Code): Valida se valor enviado é válido para o QR Code informado (VALOR_INVALIDO);         &emsp;2.2.2.4 Cobrança inválida: Valida expiração, vencimento e status (COBRANCA_INVALIDA);         &emsp;2.2.2.5 Status Consentimento: Valida se status de consentimento é diferente de “AUTHORISED” (CONSENTIMENTO_INVALIDO);         &emsp;2.2.2.6 Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO)         &emsp;2.2.2.7 Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa (ex. chave Pix inválida, QRCode inválido, conta bloqueada);         &emsp;2.2.2.8 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;2.2.2.9 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;2.2.2.10 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA).     2.3 **Casos de erro para validações síncronas no DICT**       &ensp;Nesse cenário, o pagamento não é criado, porém o consentimento deve ser alterado para o status CONSUMED Retorno esperado do endpoint POST/Payments: HTTP Code 422 - Unprocessable Entity:       &ensp;• Erro por dados inválidos: Conforme item **2.2.2.8**       &ensp;• Erro por suspeita de fraude: Conforme item **2.2.2.9**    3. **Validações na consulta do pagamento (_GET /pix/payments/{paymentId}_)**     3.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token)**       &ensp;3.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;3.1.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED).    4. **Demais validações executadas durante o processamento assíncrono do pagamento pela detentora, poderão ser consultados pela iniciadora através do endpoint _GET /pix/payments/{paymentId}_ previstos com retorno HTTP Code 200 - OK com status RJCT (Rejected) e rejectionReason conforme abaixo (detalhamento adicional na documentação técnica da API):**     4.1 **Demais validações durante processamento assíncrono**       &ensp;4.1.1 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);       &ensp;4.1.2 Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora (VALOR_ACIMA_LIMITE);       &ensp;4.1.3 Valor informado (QR Code): Valida se valor enviado é válido para o QR Code informado (VALOR_INVALIDO);       &ensp;4.1.4 Cobrança inválida: Valida expiração, vencimento e status (COBRANCA_INVALIDA);       &ensp;4.1.5 Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO);       &ensp;4.1.6 Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa (ex. chave Pix inválida, QRCode inválido, conta bloqueada);       &ensp;4.1.7 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);       &ensp;4.1.8 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);       &ensp;4.1.9 Validação SPI: Externaliza validações no SPI (PAGAMENTO_RECUSADO_SPI);     4.2 **Casos de erro para validações assíncronas no DICT**       &ensp;Neste cenário o pagamento é criado com sucesso (status RCVD) e o consentimento é consumido (status CONSUMED), porém, as validações contra o DICT só ocorrerão de forma assíncrona e em caso de negativa será percebido pela iniciadora na consulta do pagamento (GET /Payments).       &ensp;Retorno esperado do endpoint GET /Payments: HTTP Code 200 - OK.       &ensp;Status do Pagamento: RJCT (Rejected), com as seguintes opções rejectionReason:       &ensp;• Erro por dados inválidos: Conforme item **4.1.7**;       &ensp;• Erro por suspeita de fraude: Conforme item **4.1.8**.  5. **Demais validações executadas durante o processamento assíncrono do consentimento pela detentora poderão ser consultados pela iniciadora através do endpoint _GET /consents/{consentId}_ previstos com retorno HTTP Code 200 – OK com status REJECTED e rejectionReason conforme abaixo:**     5.1 **Validações durante o processamento assíncrono**       &ensp;5.1.1 - Falha de infraestrutura: Ocorreu algum erro interno na detentora durante processamento da criação do consentimento (FALHA_INFRAESTRUTURA)       &ensp;5.1.2 - Tempo de autorização expirado: O usuário não confirmou o consentimento e o mesmo expirou (TEMPO_EXPIRADO_AUTORIZACAO);       &ensp;5.1.3 - Rejeitado pelo usuário: O usuário explicitamente rejeitou a autorização do consentimento (REJEITADO_USUARIO);       &ensp;5.1.4 - Mesma conta origem/destino: A conta indicada pelo usuário para recebimento é a mesma selecionada para o pagamento (CONTAS_ORIGEM_DESTINO_IGUAIS);       &ensp;5.1.5 - Tipo de conta inválida: A conta indicada não permite operações de pagamento (CONTA_NAO_PERMITE_PAGAMENTO);       &ensp;5.1.6 - Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);       &ensp;5.1.7 - Limites da transação: Valida se o valor ultrapassa o limite estabelecido [na instituição/no arranjo/outro] para permitir a realização de transações pelo cliente (VALOR_ACIMA_LIMITE);       &ensp;5.1.8 - QRCode inválido: O QRCode utilizado para a iniciação de pagamento não é válido (QRCODE_INVALIDO);       &ensp;5.1.9 - VALOR_INVALIDO: O valor enviado não é válido para o QR Code informado (VALOR_INVALIDO);       &ensp;5.1.10 - NAO_INFORMADO: Demais validações não explicitamente informadas (ex. suspeita de fraude) (NAO_INFORMADO);       &ensp;5.1.11 - TEMPO_EXPIRADO_CONSUMO: O usuário não finalizou o fluxo de pagamento e o consentimento expirou (TEMPO_EXPIRADO_CONSUMO).     5.2 **Momentos de validação dos rejectionReasons de acordo com o funil de consentimentos.**   ```   |----------------------------------|------------------------------|   | Etapas do funil de consentimento | rejectionReason/code         |   |----------------------------------|------------------------------|   | Início da autenticação           | FALHA_INFRAESTRUTURA         |   |                                  | TEMPO_EXPIRADO_AUTORIZACAO   |   |                                  | NAO_INFORMADO                |   |----------------------------------|------------------------------|   | Conclusão da autenticação        | FALHA_INFRAESTRUTURA         |   |                                  | TEMPO_EXPIRADO_AUTORIZACAO   |   |                                  | REJEITADO_USUARIO            |   |                                  | NAO_INFORMADO                |   |----------------------------------|------------------------------|   | Autorização do cliente           | FALHA_INFRAESTRUTURA         |   |                                  | CONTAS_ORIGEM_DESTINO_IGUAIS |   |                                  | CONTA_NAO_PERMITE_PAGAMENTO  |   |                                  | SALDO_INSUFICIENTE           |   |                                  | VALOR_ACIMA_LIMITE           |   |                                  | QRCODE_INVALIDO              |   |                                  | VALOR_INVALIDO               |   |                                  | NAO_INFORMADO                |   |----------------------------------|------------------------------|   | Authorisation code emitido       | FALHA_INFRAESTRUTURA         |   |                                  | TEMPO_EXPIRADO_CONSUMO       |   |                                  | NAO_INFORMADO                |   |----------------------------------|------------------------------|   ```   # noqa: E501

    OpenAPI spec version: 3.0.0-beta.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreatePixPaymentData(object):
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
        'end_to_end_id': 'EndToEndIdWithoutRestriction',
        'local_instrument': 'EnumLocalInstrument',
        'payment': 'PaymentPix',
        'creditor_account': 'CreditorAccount',
        'remittance_information': 'str',
        'qr_code': 'str',
        'proxy': 'str',
        'cnpj_initiator': 'str',
        'transaction_identification': 'str',
        'ibge_town_code': 'str',
        'authorisation_flow': 'str'
    }

    attribute_map = {
        'end_to_end_id': 'endToEndId',
        'local_instrument': 'localInstrument',
        'payment': 'payment',
        'creditor_account': 'creditorAccount',
        'remittance_information': 'remittanceInformation',
        'qr_code': 'qrCode',
        'proxy': 'proxy',
        'cnpj_initiator': 'cnpjInitiator',
        'transaction_identification': 'transactionIdentification',
        'ibge_town_code': 'ibgeTownCode',
        'authorisation_flow': 'authorisationFlow'
    }

    def __init__(self, end_to_end_id=None, local_instrument=None, payment=None, creditor_account=None, remittance_information=None, qr_code=None, proxy=None, cnpj_initiator=None, transaction_identification=None, ibge_town_code=None, authorisation_flow=None):  # noqa: E501
        """CreatePixPaymentData - a model defined in Swagger"""  # noqa: E501
        self._end_to_end_id = None
        self._local_instrument = None
        self._payment = None
        self._creditor_account = None
        self._remittance_information = None
        self._qr_code = None
        self._proxy = None
        self._cnpj_initiator = None
        self._transaction_identification = None
        self._ibge_town_code = None
        self._authorisation_flow = None
        self.discriminator = None
        self.end_to_end_id = end_to_end_id
        self.local_instrument = local_instrument
        self.payment = payment
        self.creditor_account = creditor_account
        if remittance_information is not None:
            self.remittance_information = remittance_information
        if qr_code is not None:
            self.qr_code = qr_code
        if proxy is not None:
            self.proxy = proxy
        self.cnpj_initiator = cnpj_initiator
        if transaction_identification is not None:
            self.transaction_identification = transaction_identification
        if ibge_town_code is not None:
            self.ibge_town_code = ibge_town_code
        if authorisation_flow is not None:
            self.authorisation_flow = authorisation_flow

    @property
    def end_to_end_id(self):
        """Gets the end_to_end_id of this CreatePixPaymentData.  # noqa: E501


        :return: The end_to_end_id of this CreatePixPaymentData.  # noqa: E501
        :rtype: EndToEndIdWithoutRestriction
        """
        return self._end_to_end_id

    @end_to_end_id.setter
    def end_to_end_id(self, end_to_end_id):
        """Sets the end_to_end_id of this CreatePixPaymentData.


        :param end_to_end_id: The end_to_end_id of this CreatePixPaymentData.  # noqa: E501
        :type: EndToEndIdWithoutRestriction
        """
        if end_to_end_id is None:
            raise ValueError("Invalid value for `end_to_end_id`, must not be `None`")  # noqa: E501

        self._end_to_end_id = end_to_end_id

    @property
    def local_instrument(self):
        """Gets the local_instrument of this CreatePixPaymentData.  # noqa: E501


        :return: The local_instrument of this CreatePixPaymentData.  # noqa: E501
        :rtype: EnumLocalInstrument
        """
        return self._local_instrument

    @local_instrument.setter
    def local_instrument(self, local_instrument):
        """Sets the local_instrument of this CreatePixPaymentData.


        :param local_instrument: The local_instrument of this CreatePixPaymentData.  # noqa: E501
        :type: EnumLocalInstrument
        """
        if local_instrument is None:
            raise ValueError("Invalid value for `local_instrument`, must not be `None`")  # noqa: E501

        self._local_instrument = local_instrument

    @property
    def payment(self):
        """Gets the payment of this CreatePixPaymentData.  # noqa: E501


        :return: The payment of this CreatePixPaymentData.  # noqa: E501
        :rtype: PaymentPix
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this CreatePixPaymentData.


        :param payment: The payment of this CreatePixPaymentData.  # noqa: E501
        :type: PaymentPix
        """
        if payment is None:
            raise ValueError("Invalid value for `payment`, must not be `None`")  # noqa: E501

        self._payment = payment

    @property
    def creditor_account(self):
        """Gets the creditor_account of this CreatePixPaymentData.  # noqa: E501


        :return: The creditor_account of this CreatePixPaymentData.  # noqa: E501
        :rtype: CreditorAccount
        """
        return self._creditor_account

    @creditor_account.setter
    def creditor_account(self, creditor_account):
        """Sets the creditor_account of this CreatePixPaymentData.


        :param creditor_account: The creditor_account of this CreatePixPaymentData.  # noqa: E501
        :type: CreditorAccount
        """
        if creditor_account is None:
            raise ValueError("Invalid value for `creditor_account`, must not be `None`")  # noqa: E501

        self._creditor_account = creditor_account

    @property
    def remittance_information(self):
        """Gets the remittance_information of this CreatePixPaymentData.  # noqa: E501

        Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.   # noqa: E501

        :return: The remittance_information of this CreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._remittance_information

    @remittance_information.setter
    def remittance_information(self, remittance_information):
        """Sets the remittance_information of this CreatePixPaymentData.

        Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.   # noqa: E501

        :param remittance_information: The remittance_information of this CreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._remittance_information = remittance_information

    @property
    def qr_code(self):
        """Gets the qr_code of this CreatePixPaymentData.  # noqa: E501

        Sequência de caracteres que corresponde ao QR Code disponibilizado para o pagador. É a sequência de caracteres que seria lida pelo leitor de QR Code, e deve propiciar o retorno dos dados do pagador após consulta na DICT. Essa funcionalidade é possível tanto para QR Code estático quanto para QR Code dinâmico. No arranjo do Pix esta é a mesma sequência gerada e/ou lida pela funcionalidade Pix Copia e Cola. Este campo deverá ser no formato UTF-8. [Restrição] Preenchimento obrigatório para pagamentos por QR Code, observado o tamanho máximo de 512 bytes.   # noqa: E501

        :return: The qr_code of this CreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._qr_code

    @qr_code.setter
    def qr_code(self, qr_code):
        """Sets the qr_code of this CreatePixPaymentData.

        Sequência de caracteres que corresponde ao QR Code disponibilizado para o pagador. É a sequência de caracteres que seria lida pelo leitor de QR Code, e deve propiciar o retorno dos dados do pagador após consulta na DICT. Essa funcionalidade é possível tanto para QR Code estático quanto para QR Code dinâmico. No arranjo do Pix esta é a mesma sequência gerada e/ou lida pela funcionalidade Pix Copia e Cola. Este campo deverá ser no formato UTF-8. [Restrição] Preenchimento obrigatório para pagamentos por QR Code, observado o tamanho máximo de 512 bytes.   # noqa: E501

        :param qr_code: The qr_code of this CreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._qr_code = qr_code

    @property
    def proxy(self):
        """Gets the proxy of this CreatePixPaymentData.  # noqa: E501

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória. No caso de telefone celular deve ser informado no padrão E.1641. Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres. No caso de CPF deverá ser informado com 11 números, sem pontos ou traços. Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços. No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223. Se informado, a detentora da conta deve validar o proxy no DICT quando localInstrument for igual a DICT, QRDN ou QRES e validar o campo creditorAccount. Esta validação é opcional caso o localInstrument for igual a INIC. [Restrição] Se localInstrument for igual a MANU, o campo proxy não deve ser preenchido. Se localInstrument for igual INIC, DICT, QRDN ou QRES, o campo proxy deve ser sempre preenchido com a chave Pix.   # noqa: E501

        :return: The proxy of this CreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CreatePixPaymentData.

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória. No caso de telefone celular deve ser informado no padrão E.1641. Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres. No caso de CPF deverá ser informado com 11 números, sem pontos ou traços. Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços. No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223. Se informado, a detentora da conta deve validar o proxy no DICT quando localInstrument for igual a DICT, QRDN ou QRES e validar o campo creditorAccount. Esta validação é opcional caso o localInstrument for igual a INIC. [Restrição] Se localInstrument for igual a MANU, o campo proxy não deve ser preenchido. Se localInstrument for igual INIC, DICT, QRDN ou QRES, o campo proxy deve ser sempre preenchido com a chave Pix.   # noqa: E501

        :param proxy: The proxy of this CreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    @property
    def cnpj_initiator(self):
        """Gets the cnpj_initiator of this CreatePixPaymentData.  # noqa: E501

        CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix.  # noqa: E501

        :return: The cnpj_initiator of this CreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._cnpj_initiator

    @cnpj_initiator.setter
    def cnpj_initiator(self, cnpj_initiator):
        """Sets the cnpj_initiator of this CreatePixPaymentData.

        CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix.  # noqa: E501

        :param cnpj_initiator: The cnpj_initiator of this CreatePixPaymentData.  # noqa: E501
        :type: str
        """
        if cnpj_initiator is None:
            raise ValueError("Invalid value for `cnpj_initiator`, must not be `None`")  # noqa: E501

        self._cnpj_initiator = cnpj_initiator

    @property
    def transaction_identification(self):
        """Gets the transaction_identification of this CreatePixPaymentData.  # noqa: E501

        Trata-se de um identificador de transação que deve ser retransmitido intacto pelo PSP do pagador ao gerar a ordem de pagamento. Essa informação permitirá ao recebedor identificar e correlacionar a transferência, quando recebida, com a apresentação das instruções ao pagador. Os caracteres permitidos no contexto do Pix para o campo txid (EMV 62-05) são: - Letras minúsculas, de ‘a’ a ‘z’ - Letras maiúsculas, de ‘A’ a ‘z’ - Dígitos decimais, de ‘0’ a ‘9’  [Restrição] Preenchimento condicional de acordo com o conteúdo do campo localInstument:  – MANU - O campo transactionIdentification não deve ser preenchido.   – DICT - O campo transactionIdentification não deve ser preenchido.   – INIC - O campo transactionIdentification deve ser preenchido obrigatoriamente e deve conter até 25 caracteres alfanuméricos ([a-z|A-Z|0-9]).   – QRES - Caso o QR Code estático possua o dado <i><<i/>TxId<i>><i/> preenchido, o campo transactionIdentification deverá ser preenchido com este valor, caso o QR Code não possua o <i><<i/>TxId<i>><i/> o campo transactionIdentification não deverá ser preenchido. O <i><<i/>TxId<i>><i/> deve conter até 25 caracteres alfanuméricos ([a-z|A-Z|0-9]).   – QRDN - Será obrigatório seu preenchimento com o <i><<i/>TxId<i>><i/> do payload JSON do QR Code dinâmico. O <i><<i/>TxId<i>><i/> deve conter entre 26 e 35 caracteres alfanuméricos ([a-z|A-Z|0-9]).  A detentora de conta deve validar se a condicionalidade e o formato do campo foram atendidas pela iniciadora de pagamento.     # noqa: E501

        :return: The transaction_identification of this CreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_identification

    @transaction_identification.setter
    def transaction_identification(self, transaction_identification):
        """Sets the transaction_identification of this CreatePixPaymentData.

        Trata-se de um identificador de transação que deve ser retransmitido intacto pelo PSP do pagador ao gerar a ordem de pagamento. Essa informação permitirá ao recebedor identificar e correlacionar a transferência, quando recebida, com a apresentação das instruções ao pagador. Os caracteres permitidos no contexto do Pix para o campo txid (EMV 62-05) são: - Letras minúsculas, de ‘a’ a ‘z’ - Letras maiúsculas, de ‘A’ a ‘z’ - Dígitos decimais, de ‘0’ a ‘9’  [Restrição] Preenchimento condicional de acordo com o conteúdo do campo localInstument:  – MANU - O campo transactionIdentification não deve ser preenchido.   – DICT - O campo transactionIdentification não deve ser preenchido.   – INIC - O campo transactionIdentification deve ser preenchido obrigatoriamente e deve conter até 25 caracteres alfanuméricos ([a-z|A-Z|0-9]).   – QRES - Caso o QR Code estático possua o dado <i><<i/>TxId<i>><i/> preenchido, o campo transactionIdentification deverá ser preenchido com este valor, caso o QR Code não possua o <i><<i/>TxId<i>><i/> o campo transactionIdentification não deverá ser preenchido. O <i><<i/>TxId<i>><i/> deve conter até 25 caracteres alfanuméricos ([a-z|A-Z|0-9]).   – QRDN - Será obrigatório seu preenchimento com o <i><<i/>TxId<i>><i/> do payload JSON do QR Code dinâmico. O <i><<i/>TxId<i>><i/> deve conter entre 26 e 35 caracteres alfanuméricos ([a-z|A-Z|0-9]).  A detentora de conta deve validar se a condicionalidade e o formato do campo foram atendidas pela iniciadora de pagamento.     # noqa: E501

        :param transaction_identification: The transaction_identification of this CreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._transaction_identification = transaction_identification

    @property
    def ibge_town_code(self):
        """Gets the ibge_town_code of this CreatePixPaymentData.  # noqa: E501

        O campo ibgetowncode no arranjo PIX, tem o mesmo comportamento que o campo codMun descrito no item 1.6.6 do manual do PIX, conforme segue:  1. Caso a informação referente ao município não seja enviada; o PSP do recebedor assumirá que não existem feriados estaduais e municipais no período em questão;   # noqa: E501

        :return: The ibge_town_code of this CreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._ibge_town_code

    @ibge_town_code.setter
    def ibge_town_code(self, ibge_town_code):
        """Sets the ibge_town_code of this CreatePixPaymentData.

        O campo ibgetowncode no arranjo PIX, tem o mesmo comportamento que o campo codMun descrito no item 1.6.6 do manual do PIX, conforme segue:  1. Caso a informação referente ao município não seja enviada; o PSP do recebedor assumirá que não existem feriados estaduais e municipais no período em questão;   # noqa: E501

        :param ibge_town_code: The ibge_town_code of this CreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._ibge_town_code = ibge_town_code

    @property
    def authorisation_flow(self):
        """Gets the authorisation_flow of this CreatePixPaymentData.  # noqa: E501

        Campo condicional utilizado para identificar o fluxo de autorização em que o pagamento foi solicitado.  [Restrição] Se CIBA ou FIDO, preenchimento obrigatório. Caso o campo não esteja presente no payload, subentende-se que o fluxo de autorização utilizado é o HYBRID_FLOW.   # noqa: E501

        :return: The authorisation_flow of this CreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._authorisation_flow

    @authorisation_flow.setter
    def authorisation_flow(self, authorisation_flow):
        """Sets the authorisation_flow of this CreatePixPaymentData.

        Campo condicional utilizado para identificar o fluxo de autorização em que o pagamento foi solicitado.  [Restrição] Se CIBA ou FIDO, preenchimento obrigatório. Caso o campo não esteja presente no payload, subentende-se que o fluxo de autorização utilizado é o HYBRID_FLOW.   # noqa: E501

        :param authorisation_flow: The authorisation_flow of this CreatePixPaymentData.  # noqa: E501
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
        if issubclass(CreatePixPaymentData, dict):
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
        if not isinstance(other, CreatePixPaymentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
