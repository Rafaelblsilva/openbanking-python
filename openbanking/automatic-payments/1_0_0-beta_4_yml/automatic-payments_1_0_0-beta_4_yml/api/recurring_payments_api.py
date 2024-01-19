# coding: utf-8

"""
    API Automatic Payments - Open Finance Brasil

    API de Iniciação de Pagamentos automáticos, responsável por viabilizar as operações de iniciação de pagamentos automáticos (Pix automático e Sweeping Accounts) para o Open Finance Brasil.  Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos endpoints dedicados ao consentimento nesta API.  # Orientações - `CONTA`, referente às instituições detentoras de conta participantes do Open Finance Brasil; - `PAGTO`, referente às instituições iniciadoras de pagamento participantes do Open Finance Brasil.  Os tokens utilizados para consumo nos endpoints de consentimentos devem possuir o scope payments e os endpoints de pagamentos recorrentes devem possuir os scopes openid e payments.  Esta API não requer a implementação de permissions para sua utilização.  Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão Assinaturas do guia de segurança.  ## Orientações gerais sobre os consentimentos de pagamentos automáticos - Duração e reutilização do consentimento: A utilização das credenciais geradas a partir de uma autorização de um consentimento recorrente deve durar até que o consentimento recorrente atinja o fim do seu ciclo de vida, conforme detalhado na sua [máquina de estados](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/198410647).  - Credenciais: As credenciais (authorization_code) geradas na autorização do consentimento devem ser utilizadas para criação dos pagamentos subsequentes utilizando o mecanismo de refresh, caso necessário. Maiores informações através do link [[PT] Open Finance Brasil Financial-grade API Security Profile 1.0 Implementers Draft 3 - Área do Desenvolvedor -Open Finance Brasil - Área do Desenvolvedor (atlassian.net)](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/82051180/PT+Open+Finance+Brasil+Financial-grade+API+Security+Profile+1.0+Implementers+Draft+3#7.2.2.-Servidor-de-autorização)  ## Regras do arranjo Pix A implementação e o uso da API de Pagamentos Automáticos (Pix) devem seguir as regras do arranjo Pix do Banco Central, que podem ser encontradas no link abaixo:   [Banco Central do Brasil](https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix)  ## Assinatura de payloads No contexto da API de Pagamentos Automáticos, os payloads de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora de conta devem estar assinados.  Para o processo de assinatura destes payloads, as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor.  ## Controle de acesso - Os endpoints de consulta de pagamentos GET /pix/recurring-payments/{recurringPaymentId} e GET /pix/recurring-payments devem suportar acesso a partir de access_token emitido por meio de um grant_type do tipo client credentials, como opção do uso do token vinculado ao consentimento (hybrid flow). - Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.  ## Aprovações de múltipla alçada  Todas as aprovações devem ser realizadas até a data/hora limite suportada pela detentora e em tempo hábil para realizar o primeiro pagamento.  ## Validações da edição do consentimento recorrente para o produto Pix Automático  Para permitir a edição dos campos de um consentimento na iniciadora sem que se faça necessário o redirecionamento para o  ambiente da detentora de conta, é necessário o envio de indicadores de risco.  Esta medida visa proporcionar à detentora de conta as informações necessárias para decidir sobre os ajustes no consentimento de forma segura  ## Validações  Durante a jornada de iniciação de pagamento, diferentes validações são necessárias pela instituição detentora de conta e devem ocorrer conforme a seguir:  1. **Validações na criação do consentimento de longa duração (_POST /recurring-consents_)**     1.1 **Orientações Iniciais**       &ensp;1.1.1 Não devem ser retornadas na resposta deste endpoint informações associadas ao usuário/cliente (ex. insuficiência de saldo, conta inexistente/bloqueada).       &ensp;1.1.2 Não devem ser realizadas validações de informações sobre o usuário/cliente durante a criação do consentimento.     1.2 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;1.2.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;1.2.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;1.2.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;1.2.4 Validação de Claims (exceto data);         &emsp;1.2.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;1.2.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     1.3 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**        &ensp;1.3.1 **Sintáticos**         &emsp;1.3.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios foram informados (PARAMETRO_NAO_INFORMADO);         &emsp;1.3.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;1.3.2 **Semânticos**         &emsp;1.3.2.1 Data de pagamento: Valida se a data de pagamento enviada é válida para a forma de pagamento selecionada (DATA_PAGAMENTO_INVALIDA);         &emsp;1.3.2.2 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;1.3.2.3 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;1.3.2.4 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA);         &emsp;1.3.2.5 Funcionalidade não habilitada: A detentora de conta não oferece o serviço nessa modalidade (FUNCIONALIDADE_NAO_HABILITADA).    2. **Demais validações executadas durante o processamento assíncrono do consentimento pela detentora poderão ser consultados pela iniciadora através do endpoint GET /recurring-consents/{recurringConsentId} previstos com retorno HTTP Code 200 – OK com status REJECTED e rejectionReason conforme abaixo:**     2.1 **Validações durante o processamento assíncrono do consentimento**       &ensp;2.1.1 Falha de infraestrutura: Ocorreu algum erro interno na detentora durante processamento da criação do consentimento (FALHA_INFRAESTRUTURA);       &ensp;2.1.2 Tempo de autorização expirado: O usuário não confirmou o consentimento e o mesmo expirou (TEMPO_EXPIRADO_AUTORIZACAO);       &ensp;2.1.3 Rejeitado pelo usuário: O usuário explicitamente rejeitou a autorização do consentimento (REJEITADO_USUARIO);       &ensp;2.1.4 Mesma conta origem/destino: A conta indicada pelo usuário para recebimento é a mesma selecionada para o pagamento (CONTAS_ORIGEM_DESTINO_IGUAIS);       &ensp;2.1.5 Tipo de conta inválida: A conta indicada não permite operações de pagamento (CONTA_NAO_PERMITE_PAGAMENTO);       &ensp;2.1.6 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);       &ensp;2.1.7 Limites da transação: Valida se o valor ultrapassa o limite estabelecido [na instituição/no arranjo/outro] para permitir a realização de transações pelo cliente (VALOR_ACIMA_LIMITE);    3. **Demais validações executadas durante o processamento assíncrono do consentimento pela detentora, poderão ser consultados pela iniciadora através dos endpoints GET /recurring-consents/{recurringConsentId} previstos com retorno HTTP Code 200 - OK com status REVOKED e revocationReason conforme abaixo (detalhamento adicional na documentação técnica da API).**     3.1 **Demais validações durante o processamento assíncrono:**       &ensp;3.1.1 Nao informado: Validações não explicitamente informadas (ex. suspeita de fraude) (NAO_INFORMADO);       &ensp;3.1.2 Revogado pelo recebedor: O usuário recebedor solicitou explicitamente ao iniciador a revogação do consentimento (ex: término de contrato) (REVOGADO_RECEBEDOR);       &ensp;3.1.3 Revogado pelo pagador: O usuário pagador solicitou explicitamente a revogação do consentimento (REVOGADO_USUARIO).    4. **Validações na criação do pagamento - Síncrono (_POST /pix/recurring-payments_)**     4.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;4.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;4.1.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;4.1.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;4.1.4 Validação de Claims (exceto data);         &emsp;4.1.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;4.1.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     4.2 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**       &ensp;4.2.1 Sintáticos         &emsp;4.2.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios são informados (PARAMETRO_NAO_INFORMADO);         &emsp;4.2.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;4.2.2 Semânticos         &emsp;4.2.2.1 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);         &emsp;4.2.2.2 Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora na conta do cliente pagador (VALOR_ACIMA_LIMITE);         &emsp;4.2.2.3 Valor informado: Valida se valor enviado é válido para o consentimento associado ao pagamento (VALOR_INVALIDO);         &emsp;4.2.2.4 Status Consentimento: Valida se status de consentimento é diferente de “AUTHORISED” (CONSENTIMENTO_INVALIDO);         &emsp;4.2.2.5 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;4.2.2.6 Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO)         &emsp;4.2.2.7 Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa;         &emsp;4.2.2.8 Detalhes do pagamento: Valida se determinado parâmetro informado obedece as regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;4.2.2.9 Pagamento recusado no Sistema de Pagamentos Instantâneos (SPI) (PAGAMENTO_RECUSADO_SPI);         &emsp;4.2.2.10 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA);         &emsp;4.2.2.11 Limite valor excedido por período: Foi atingido o valor limite permitido pelo usuário por um determinado período de tempo no consentimento do pagamento (LIMITE_PERIODO_VALOR_EXCEDIDO);         &emsp;4.2.2.12 Limite quantidade excedida por período: A quantidade de cobranças atingiu o limite determinado pelo usuário na criação do consentimento (LIMITE_PERIODO_QUANTIDADE_EXCEDIDO).    5. **Validações na consulta do pagamento (_GET /pix/recurring-payments/{recurringPaymentId}_ e _GET /pix/recurring-payments_)**     5.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token)**       &ensp;5.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;5.1.2 Validações de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED).  6. **Demais validações executadas durante o processamento assíncrono do pagamento pela detentora, poderão ser consultados pela iniciadora através dos endpoints _GET /pix/recurring-payments/{recurringPaymentId}_ e _GET /pix/recurring-payments_ previstos com retorno HTTP Code 200 - OK com status RJCT (Rejected) e rejectionReason conforme abaixo (detalhamento adicional na documentação técnica da API):**     6.1 **Demais validações durante o processamento assíncrono:**       &ensp;6.1.1 - Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);       &ensp;6.1.2 - Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora (VALOR_ACIMA_LIMITE);       &ensp;6.1.3 - Valor informado: Valida se valor enviado é válido para o consentimento do pagamento (VALOR_INVALIDO);       &ensp;6.1.4 - Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);       &ensp;6.1.5 - Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO);       &ensp;6.1.6 - Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa;       &ensp;6.1.7 - Pagamento recusado no Sistema de Pagamentos Instantâneos (SPI) (PAGAMENTO_RECUSADO_SPI);       &ensp;6.1.8 - Erro de infraestrutura na consulta ao SPI: Ocorreu uma falha de infraestrutura durante a consulta ao SPI(FALHA_INFRAESTRUTURA_SPI);       &ensp;6.1.9 - Erro de infraestrutura na consulta ao ICP: Ocorreu uma falha de infraestrutura durante a consulta ao ICP (FALHA_INFRAESTRUTURA_ICP);       &ensp;6.1.10 - Erro de infraestrutura na comunicação com o PSP do recebedor: Ocorreu uma falha de infraestrutura durante a comunicação com o PSP do recebedor (FALHA_INFRAESTRUTURA_PSP_RECEBEDOR);       &ensp;6.1.11 - Erro de infraestrutura interno na detentora: Ocorreu uma falha de infraestrutura interna na detentora durante o processamento do pagamento (FALHA_INFRAESTRUTURA_DETENTORA);       &ensp;6.1.12 - Status Consentimento: Valida se status de consentimento é diferente de “AUTHORISED” (CONSENTIMENTO_INVALIDO);    ## Validações antifraude do Sweeping accounts  - Afim de garantir a mesma titularidade e aumentar a segurança das transações do produto Sweeping Accounts, as validações abaixo poderão ser realizadas pela detetora de conta e pela iniciadora, quando localinstrument for igual a DICT ou INIC. A detentora PODE usar a API Consultar Vinculo (DICT API) do arranjo Pix e validar no momento de transação ao menos os atributos abaixo mencionados:   - se o valor dos atributos de fraude abaixo são iguais a 0, de modo a evitar que contas criadas especificamente para uso indevido do Sweeping accounts impactem o ecossistema      - OwnerStatistics.Spi.FraudMarkers.ApplicationFrauds.d90     - OwnerStatistics.Spi.FraudMarkers.MuleAccounts.d90     - OwnerStatistics.Spi.FraudMarkers.ScammerAccounts.d90     - OwnerStatistics.Spi.FraudMarkers.OtherFrauds.d90     - OwnerStatistics.Spi.FraudMarkers.UnknownFrauds.d90   # noqa: E501

    OpenAPI spec version: 1.0.0-beta.4
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from automatic-payments_1_0_0-beta_4_yml.api_client import ApiClient


class RecurringPaymentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def automatic_payments_get_pix_recurring_payments(self, authorization, x_fapi_interaction_id, recurring_consent_id, **kwargs):  # noqa: E501
        """Busca informações de transações de pagamentos associadas a um consentimento.  # noqa: E501

        Método para buscar informações sobre um conjunto de pagamentos associados ao mesmo recurringConsentId.  Também é possível enviar uma data de início (startDate) e final (endDate), caso a busca seja por transações em uma determinada janela de tempo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.automatic_payments_get_pix_recurring_payments(authorization, x_fapi_interaction_id, recurring_consent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str recurring_consent_id: O `recurringConsentId` é o identificador único do consentimento de longa duração e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independe da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para `recurringConsentId` temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora (bancoex). - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  (required)
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o iniciador.
        :param str start_date: Data inicial de corte da ocorrência do pagamento ligada ao consentimento de longa duração.
        :param str end_date: Data final de corte para recuperação da ocorrência do pagamento ligada ao consentimento de longa duração.
        :return: ResponseRecurringPixPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.automatic_payments_get_pix_recurring_payments_with_http_info(authorization, x_fapi_interaction_id, recurring_consent_id, **kwargs)  # noqa: E501
        else:
            (data) = self.automatic_payments_get_pix_recurring_payments_with_http_info(authorization, x_fapi_interaction_id, recurring_consent_id, **kwargs)  # noqa: E501
            return data

    def automatic_payments_get_pix_recurring_payments_with_http_info(self, authorization, x_fapi_interaction_id, recurring_consent_id, **kwargs):  # noqa: E501
        """Busca informações de transações de pagamentos associadas a um consentimento.  # noqa: E501

        Método para buscar informações sobre um conjunto de pagamentos associados ao mesmo recurringConsentId.  Também é possível enviar uma data de início (startDate) e final (endDate), caso a busca seja por transações em uma determinada janela de tempo.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.automatic_payments_get_pix_recurring_payments_with_http_info(authorization, x_fapi_interaction_id, recurring_consent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str recurring_consent_id: O `recurringConsentId` é o identificador único do consentimento de longa duração e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independe da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para `recurringConsentId` temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora (bancoex). - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  (required)
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o iniciador.
        :param str start_date: Data inicial de corte da ocorrência do pagamento ligada ao consentimento de longa duração.
        :param str end_date: Data final de corte para recuperação da ocorrência do pagamento ligada ao consentimento de longa duração.
        :return: ResponseRecurringPixPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_fapi_interaction_id', 'recurring_consent_id', 'x_customer_user_agent', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'start_date', 'end_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method automatic_payments_get_pix_recurring_payments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `automatic_payments_get_pix_recurring_payments`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `automatic_payments_get_pix_recurring_payments`")  # noqa: E501
        # verify the required parameter 'recurring_consent_id' is set
        if ('recurring_consent_id' not in params or
                params['recurring_consent_id'] is None):
            raise ValueError("Missing the required parameter `recurring_consent_id` when calling `automatic_payments_get_pix_recurring_payments`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'recurring_consent_id' in params:
            query_params.append(('recurringConsentId', params['recurring_consent_id']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_customer_user_agent' in params:
            header_params['x-customer-user-agent'] = params['x_customer_user_agent']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/jwt', 'application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/pix/recurring-payments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseRecurringPixPayment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def automatic_payments_get_pix_recurring_payments_payment_id(self, authorization, x_fapi_interaction_id, recurring_payment_id, **kwargs):  # noqa: E501
        """Busca informações de uma transação de pagamento.  # noqa: E501

        Método para buscar informações sobre um pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.automatic_payments_get_pix_recurring_payments_payment_id(authorization, x_fapi_interaction_id, recurring_payment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str recurring_payment_id: Identificador da operação de pagamento. (required)
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o iniciador.
        :return: ResponseRecurringPaymentsIdRead
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.automatic_payments_get_pix_recurring_payments_payment_id_with_http_info(authorization, x_fapi_interaction_id, recurring_payment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.automatic_payments_get_pix_recurring_payments_payment_id_with_http_info(authorization, x_fapi_interaction_id, recurring_payment_id, **kwargs)  # noqa: E501
            return data

    def automatic_payments_get_pix_recurring_payments_payment_id_with_http_info(self, authorization, x_fapi_interaction_id, recurring_payment_id, **kwargs):  # noqa: E501
        """Busca informações de uma transação de pagamento.  # noqa: E501

        Método para buscar informações sobre um pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.automatic_payments_get_pix_recurring_payments_payment_id_with_http_info(authorization, x_fapi_interaction_id, recurring_payment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str recurring_payment_id: Identificador da operação de pagamento. (required)
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o iniciador.
        :return: ResponseRecurringPaymentsIdRead
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_fapi_interaction_id', 'recurring_payment_id', 'x_customer_user_agent', 'x_fapi_auth_date', 'x_fapi_customer_ip_address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method automatic_payments_get_pix_recurring_payments_payment_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `automatic_payments_get_pix_recurring_payments_payment_id`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `automatic_payments_get_pix_recurring_payments_payment_id`")  # noqa: E501
        # verify the required parameter 'recurring_payment_id' is set
        if ('recurring_payment_id' not in params or
                params['recurring_payment_id'] is None):
            raise ValueError("Missing the required parameter `recurring_payment_id` when calling `automatic_payments_get_pix_recurring_payments_payment_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'recurring_payment_id' in params:
            path_params['recurringPaymentId'] = params['recurring_payment_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_customer_user_agent' in params:
            header_params['x-customer-user-agent'] = params['x_customer_user_agent']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/jwt', 'application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/pix/recurring-payments/{recurringPaymentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseRecurringPaymentsIdRead',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def automatic_payments_patch_pix_recurring_payments_payment_id(self, body, authorization, x_fapi_interaction_id, x_idempotency_key, recurring_payment_id, **kwargs):  # noqa: E501
        """Cancelamento de solicitação de pagamento automático.  # noqa: E501

        Esse endpoint deve ser usado para cancelar as transações que estejam em uma das seguintes situações:  Agendada com sucesso (SCHD), retida para análise (PDNG). Caso a requisição seja bem sucedida, a transação vai para a situação CANC.   Caso o status do pagamento seja diferente de SCHD/PDNG ou alguma outra regra de negócio impeça o cancelamento, a requisição PATCH retorna  HTTP Status 422 com o code PAGAMENTO_NAO_PERMITE_CANCELAMENTO.   Caso receba um 422, a iniciadora deve fazer uma requisição GET no pagamento para verificar a situação atual dele, bem como detalhes associados.   [Restrição] Para o Pix Automático (“recurringConfiguration” igual a “automatic”) tanto o recebedor quanto o pagador poderão realizar o  cancelamento, sendo permitido ao recebedor a solicitação de cancelamento até as 22:00 (Horário de Brasília) e ao pagador até as 23:59  (Horário de Brasília) do dia anterior à data de efetivação do pagamento.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.automatic_payments_patch_pix_recurring_payments_payment_id(body, authorization, x_fapi_interaction_id, x_idempotency_key, recurring_payment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PatchPixPayment body: Atualização do Pagamento Recorrente. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str recurring_payment_id: Identificador da operação de pagamento. (required)
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o iniciador.
        :return: ResponseRecurringPaymentsIdRead
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.automatic_payments_patch_pix_recurring_payments_payment_id_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, recurring_payment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.automatic_payments_patch_pix_recurring_payments_payment_id_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, recurring_payment_id, **kwargs)  # noqa: E501
            return data

    def automatic_payments_patch_pix_recurring_payments_payment_id_with_http_info(self, body, authorization, x_fapi_interaction_id, x_idempotency_key, recurring_payment_id, **kwargs):  # noqa: E501
        """Cancelamento de solicitação de pagamento automático.  # noqa: E501

        Esse endpoint deve ser usado para cancelar as transações que estejam em uma das seguintes situações:  Agendada com sucesso (SCHD), retida para análise (PDNG). Caso a requisição seja bem sucedida, a transação vai para a situação CANC.   Caso o status do pagamento seja diferente de SCHD/PDNG ou alguma outra regra de negócio impeça o cancelamento, a requisição PATCH retorna  HTTP Status 422 com o code PAGAMENTO_NAO_PERMITE_CANCELAMENTO.   Caso receba um 422, a iniciadora deve fazer uma requisição GET no pagamento para verificar a situação atual dele, bem como detalhes associados.   [Restrição] Para o Pix Automático (“recurringConfiguration” igual a “automatic”) tanto o recebedor quanto o pagador poderão realizar o  cancelamento, sendo permitido ao recebedor a solicitação de cancelamento até as 22:00 (Horário de Brasília) e ao pagador até as 23:59  (Horário de Brasília) do dia anterior à data de efetivação do pagamento.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.automatic_payments_patch_pix_recurring_payments_payment_id_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, recurring_payment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PatchPixPayment body: Atualização do Pagamento Recorrente. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str recurring_payment_id: Identificador da operação de pagamento. (required)
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o iniciador.
        :return: ResponseRecurringPaymentsIdRead
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'x_fapi_interaction_id', 'x_idempotency_key', 'recurring_payment_id', 'x_customer_user_agent', 'x_fapi_auth_date', 'x_fapi_customer_ip_address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method automatic_payments_patch_pix_recurring_payments_payment_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `automatic_payments_patch_pix_recurring_payments_payment_id`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `automatic_payments_patch_pix_recurring_payments_payment_id`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `automatic_payments_patch_pix_recurring_payments_payment_id`")  # noqa: E501
        # verify the required parameter 'x_idempotency_key' is set
        if ('x_idempotency_key' not in params or
                params['x_idempotency_key'] is None):
            raise ValueError("Missing the required parameter `x_idempotency_key` when calling `automatic_payments_patch_pix_recurring_payments_payment_id`")  # noqa: E501
        # verify the required parameter 'recurring_payment_id' is set
        if ('recurring_payment_id' not in params or
                params['recurring_payment_id'] is None):
            raise ValueError("Missing the required parameter `recurring_payment_id` when calling `automatic_payments_patch_pix_recurring_payments_payment_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'recurring_payment_id' in params:
            path_params['recurringPaymentId'] = params['recurring_payment_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_customer_user_agent' in params:
            header_params['x-customer-user-agent'] = params['x_customer_user_agent']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501
        if 'x_idempotency_key' in params:
            header_params['x-idempotency-key'] = params['x_idempotency_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/jwt', 'application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/jwt'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/pix/recurring-payments/{recurringPaymentId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseRecurringPaymentsIdRead',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def automatic_payments_post_pix_recurring_payments(self, body, authorization, x_fapi_interaction_id, x_idempotency_key, **kwargs):  # noqa: E501
        """Cria uma transação de pagamento.  # noqa: E501

        Método para criação de uma transação de pagamento. Retorna um recurringPaymentId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.automatic_payments_post_pix_recurring_payments(body, authorization, x_fapi_interaction_id, x_idempotency_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRecurringPixPayment body: Payload para criação da iniciação do pagamento Pix. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o iniciador.
        :return: ResponseRecurringPaymentsIdPost
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.automatic_payments_post_pix_recurring_payments_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, **kwargs)  # noqa: E501
        else:
            (data) = self.automatic_payments_post_pix_recurring_payments_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, **kwargs)  # noqa: E501
            return data

    def automatic_payments_post_pix_recurring_payments_with_http_info(self, body, authorization, x_fapi_interaction_id, x_idempotency_key, **kwargs):  # noqa: E501
        """Cria uma transação de pagamento.  # noqa: E501

        Método para criação de uma transação de pagamento. Retorna um recurringPaymentId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.automatic_payments_post_pix_recurring_payments_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateRecurringPixPayment body: Payload para criação da iniciação do pagamento Pix. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o iniciador. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o iniciador.
        :return: ResponseRecurringPaymentsIdPost
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'x_fapi_interaction_id', 'x_idempotency_key', 'x_customer_user_agent', 'x_fapi_auth_date', 'x_fapi_customer_ip_address']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method automatic_payments_post_pix_recurring_payments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `automatic_payments_post_pix_recurring_payments`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `automatic_payments_post_pix_recurring_payments`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `automatic_payments_post_pix_recurring_payments`")  # noqa: E501
        # verify the required parameter 'x_idempotency_key' is set
        if ('x_idempotency_key' not in params or
                params['x_idempotency_key'] is None):
            raise ValueError("Missing the required parameter `x_idempotency_key` when calling `automatic_payments_post_pix_recurring_payments`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_customer_user_agent' in params:
            header_params['x-customer-user-agent'] = params['x_customer_user_agent']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501
        if 'x_idempotency_key' in params:
            header_params['x-idempotency-key'] = params['x_idempotency_key']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/jwt', 'application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/jwt'])  # noqa: E501

        # Authentication setting
        auth_settings = ['NonRedirectAuthorizationCode', 'OAuth2AuthorizationCode']  # noqa: E501

        return self.api_client.call_api(
            '/pix/recurring-payments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseRecurringPaymentsIdPost',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
