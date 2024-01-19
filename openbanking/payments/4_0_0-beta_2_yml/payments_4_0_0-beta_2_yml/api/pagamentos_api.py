# coding: utf-8

"""
    API Payment Initiation - Open Finance Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Finance Brasil. Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API: - `CONTA`, referente às instituições detentoras de conta participantes do Open Finance Brasil; - `PAGTO`, referente às instituições iniciadoras de pagamento participantes do Open Finance Brasil.  Os tokens utilizados para consumo nos endpoints de consentimentos devem possuir o scope `payments` e os `endpoints` de pagamentos devem possuir os `scopes`, `openid` e `payments`.  Esta API não requer a implementação de `permissions` para sua utilização. Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Regras do arranjo Pix A implementação e o uso da API de Pagamentos Pix devem seguir as regras do arranjo Pix do Banco Central, que podem ser encontradas no link abaixo:    [https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix](https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix)  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:  - Certificados exigidos para assinatura de mensagens: [[EN] Padrão de Certificados Open Finance Brasil 2.1](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/82084176/EN+Padr+o+de+Certificados+Open+Finance+Brasil+2.1%20%E2%80%8B)  - Como assinar o payload JWS: [Como Assinar o Payload](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/180061175/Como+Assinar+o+Payload+-+v3.0.0+-+Pagamentos)  ## Controle de acesso  Os endpoints de consulta e cancelamento devem suportar somente acesso a partir de access_token emitido por meio de um grant_type do tipo client_credentials.  Para a criação do consentimento deve-se utilizar client_credentials e para criação de pagamentos deve-se utilizar authorization_code.  ## Aprovações de múltipla alçada  Para o caso de Pix imediato, todas as aprovações necessárias devem ser realizadas nos canais da detentora até às 23:59 (horário de Brasília) da data de solicitação do pagamento. Já para o caso de Pix agendado, todas as aprovações devem ser realizadas até a data/hora limite suportada pela detentora.  ## Validações **Validações** (*após o processo de DCR e obtenção de token client credential*– não escopo dessa documentação)   Durante a jornada de iniciação de pagamento, diferentes validações são necessárias pela instituição detentora  de conta e devem ocorrer conforme a seguir:   1. Na criação do consentimento (*POST /consents*);  2. Na criação do pagamento - Síncrono (*POST /payments*);  3. Validações na consulta do pagamento (*GET /pix/payments/{paymentId}*); 4. Demais validações executadas durante o processamento assíncrono do pagamento pela detentora, poderão ser consultados pela iniciadora através do endpoint (*GET /pix/payments/{paymentId}*) previstos com retorno HTTP Code 200 - OK com status RJCT (Rejected) e rejectionReason; 5. Demais validações executadas durante o processamento assíncrono do consentimento pela detentora poderão ser consultados pela iniciadora através do endpoint (*GET /consents/{consentId}*) previstos com retorno HTTP Code 200 – OK com status REJECTED e rejectionReason  **Os tipos de validações dispostas abaixo não determinam a ordem em que as instituições devem implementá-las**  1. **Validações na criação do consentimento (_POST /consents_)**     1.1 **Orientações Iniciais**       &ensp;1.1.1 Não devem ser retornadas na resposta deste endpointinformações associadas ao usuário/cliente (ex.  insuficiência de saldo, conta inexistente/bloqueada).       &ensp;1.1.2 Não devem ser executadas validações no DICT (Diretório de Identificadores de Contas Transacionais do Pix), a partir dos dados compartilhados nesse *endpoint*. Tais  validações podem ocorrer somente na criação do pagamento;        &ensp;1.1.3 Não devem ser realizadas validações de informações sobre o usuário/cliente durante a criação do consentimento.   1.2 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;1.2.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;1.2.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;1.2.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;1.2.4 Validação de Claims (exceto data);         &emsp;1.2.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;1.2.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     1.3 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**        &ensp;1.3.1 **Sintáticos**         &emsp;1.3.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios são informados (PARAMETRO_NAO_INFORMADO);         &emsp;1.3.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;1.3.2 **Semânticos**         &emsp;1.3.2.1 Forma de pagamento: Valida se a forma de pagamento é suportada pela detentora (FORMA_PAGAMENTO_INVALIDA) **Obs. No detalhe do erro, a variável “modalidade” deve ser comunicada pela detentora da forma mais clara possível - ex. modalidade de pagamento não suportada (_localInstrument_ - QRES) ou tipo de arranjo pagamento não suportado (_type_ – ex. Pix / TED – previsto para inclusão futura);**         &emsp;1.3.2.2 Data de pagamento: Valida se a data de pagamento enviada é válida para a forma de pagamento selecionada (DATA_PAGAMENTO_INVALIDA);         &emsp;1.3.2.3 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;1.3.2.4 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;1.3.2.5 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA).    2. **Validações na criação do pagamento - Síncrono (_POST /payments_)**     2.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;2.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;2.1.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;2.1.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;2.1.4 Validação de Claims (exceto data);         &emsp;2.1.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;2.1.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     2.2 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**       &ensp;2.2.1 **Sintáticos**         &emsp;2.3.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios são informados (PARAMETRO_NAO_INFORMADO);         &emsp;2.3.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;2.2.2 **Semânticos**         &emsp;2.2.2.1 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);         &emsp;2.2.2.2 Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora (VALOR_ACIMA_LIMITE);         &emsp;2.2.2.3 Valor informado (QR Code): Valida se valor enviado é válido para o QR Code informado (VALOR_INVALIDO);         &emsp;2.2.2.4 Cobrança inválida: Valida expiração, vencimento e status (COBRANCA_INVALIDA);         &emsp;2.2.2.5 Status Consentimento: Valida se o consentimento encontra-se em um dos estados finais “CONSUMED” ou “REJECTED\" (CONSENTIMENTO_INVALIDO);         &emsp;2.2.2.6 Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO)         &emsp;2.2.2.7 Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa (ex. chave Pix inválida, QRCode inválido, conta bloqueada);         &emsp;2.2.2.8 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;2.2.2.9 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;2.2.2.10 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA);         &emsp;2.2.2.11 Consentimento pendente de autorização: Em `PARTIALLY_ACCEPTED` aguardando aprovação de múltiplas alçadas. Não consome nem invalida o consentimento (CONSENTIMENTO_PENDENTE_AUTORIZACAO).     2.3 **Casos de erro para validações síncronas no DICT**       &ensp;Nesse cenário, o pagamento não é criado, porém o consentimento deve ser alterado para o status CONSUMED Retorno esperado do endpoint POST/Payments: HTTP Code 422 - Unprocessable Entity:       &ensp;• Erro por dados inválidos: Conforme item **2.2.2.8**       &ensp;• Erro por suspeita de fraude: Conforme item **2.2.2.9**    3. **Validações na consulta do pagamento (_GET /pix/payments/{paymentId}_)**     3.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token)**       &ensp;3.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;3.1.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED).    4. **Demais validações executadas durante o processamento assíncrono do pagamento pela detentora, poderão ser consultados pela iniciadora através do endpoint _GET /pix/payments/{paymentId}_ previstos com retorno HTTP Code 200 - OK com status RJCT (Rejected) e rejectionReason conforme abaixo (detalhamento adicional na documentação técnica da API):**     4.1 **Demais validações durante processamento assíncrono**       &ensp;4.1.1 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento. No caso de um pagamento agendado, a validação só ocorre na tentativa de liquidação do pagamento (SALDO_INSUFICIENTE);       &ensp;4.1.2 Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora (VALOR_ACIMA_LIMITE);       &ensp;4.1.3 Valor informado (QR Code): Valida se valor enviado é válido para o QR Code informado (VALOR_INVALIDO);       &ensp;4.1.4 Cobrança inválida: Valida expiração, vencimento e status (COBRANCA_INVALIDA);       &ensp;4.1.5 Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO);       &ensp;4.1.6 Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa (ex. chave Pix inválida, QRCode inválido, conta bloqueada);       &ensp;4.1.7 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);       &ensp;4.1.8 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);       &ensp;4.1.9 Validação SPI: Externaliza validações no SPI (PAGAMENTO_RECUSADO_SPI);       &ensp;4.1.10 Falha em agendamentos: Uma ou mais incidências de pagamento não foram possíveis de ser agendadas (FALHA_AGENDAMENTO_PAGAMENTOS);     4.2 **Casos de erro para validações assíncronas no DICT**       &ensp;Neste cenário o pagamento é criado com sucesso (status RCVD) e o consentimento é consumido (status CONSUMED), porém, as validações contra o DICT só ocorrerão de forma assíncrona e em caso de negativa será percebido pela iniciadora na consulta do pagamento (GET /Payments).       &ensp;Retorno esperado do endpoint GET /Payments: HTTP Code 200 - OK.       &ensp;Status do Pagamento: RJCT (Rejected), com as seguintes opções rejectionReason:       &ensp;• Erro por dados inválidos: Conforme item **4.1.7**;       &ensp;• Erro por suspeita de fraude: Conforme item **4.1.8**.  5. **Demais validações executadas durante o processamento assíncrono do consentimento pela detentora poderão ser consultados pela iniciadora através do endpoint _GET /consents/{consentId}_ previstos com retorno HTTP Code 200 – OK com status REJECTED e rejectionReason conforme abaixo:**     5.1 **Validações durante o processamento assíncrono**       &ensp;5.1.1 - Falha de infraestrutura: Ocorreu algum erro interno na detentora durante processamento da criação do consentimento (FALHA_INFRAESTRUTURA)       &ensp;5.1.2 - Tempo de autorização expirado: O usuário não confirmou o consentimento e o mesmo expirou (TEMPO_EXPIRADO_AUTORIZACAO);       &ensp;5.1.3 - Rejeitado pelo usuário: O usuário explicitamente rejeitou a autorização do consentimento (REJEITADO_USUARIO);       &ensp;5.1.4 - Mesma conta origem/destino: A conta indicada pelo usuário para recebimento é a mesma selecionada para o pagamento (CONTAS_ORIGEM_DESTINO_IGUAIS);       &ensp;5.1.5 - Tipo de conta inválida: A conta indicada não permite operações de pagamento (CONTA_NAO_PERMITE_PAGAMENTO);       &ensp;5.1.6 - Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento. Essa validação não deverá ocorrer no caso de um pagamento agendado (SALDO_INSUFICIENTE);       &ensp;5.1.7 - Limites da transação: Valida se o valor ultrapassa o limite estabelecido [na instituição/no arranjo/outro] para permitir a realização de transações pelo cliente (VALOR_ACIMA_LIMITE);       &ensp;5.1.8 - QRCode inválido: O QRCode utilizado para a iniciação de pagamento não é válido (QRCODE_INVALIDO);       &ensp;5.1.9 - Valor inválido: O valor enviado não é válido para o QR Code informado (VALOR_INVALIDO);       &ensp;5.1.10 - Não informado: Demais validações não explicitamente informadas (ex. suspeita de fraude) e consentimentos rejeitados em versões que não existiam o campo rejectionReason na API de Pagamentos (NAO_INFORMADO)       &ensp;5.1.11 - Tempo expirado consumo: O usuário não finalizou o fluxo de pagamento e o consentimento expirou (TEMPO_EXPIRADO_CONSUMO).     5.2 **[Momentos obrigatórios de validação dos rejectionReasons de acordo com o funil de consentimentos.](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/150863940)**      ```   |----------------------------------|------------------------------|   | Etapas do funil de consentimento | rejectionReason/code         |   |----------------------------------|------------------------------|   | Início da autenticação           | FALHA_INFRAESTRUTURA         |   |                                  | TEMPO_EXPIRADO_AUTORIZACAO   |   |                                  | NAO_INFORMADO                |   |----------------------------------|------------------------------|   | Conclusão da autenticação        | FALHA_INFRAESTRUTURA         |   |                                  | TEMPO_EXPIRADO_AUTORIZACAO   |   |                                  | REJEITADO_USUARIO            |   |                                  | NAO_INFORMADO                |   |----------------------------------|------------------------------|   | Autorização do cliente           | FALHA_INFRAESTRUTURA         |   |                                  | CONTAS_ORIGEM_DESTINO_IGUAIS |   |                                  | CONTA_NAO_PERMITE_PAGAMENTO  |   |                                  | SALDO_INSUFICIENTE           |   |                                  | VALOR_ACIMA_LIMITE           |   |                                  | QRCODE_INVALIDO              |   |                                  | VALOR_INVALIDO               |   |                                  | NAO_INFORMADO                |   |----------------------------------|------------------------------|   | Authorisation code emitido       | FALHA_INFRAESTRUTURA         |   |                                  | TEMPO_EXPIRADO_CONSUMO       |   |                                  | NAO_INFORMADO                |   |----------------------------------|------------------------------|   ```   Existem dois `endpoints` para cancelamento de pagamentos, um deles é o _PATCH /pix/payments/{paymentId}_ e o outro é o _PATCH /pix/payments/consents/{consentId}_.   - O _PATCH /pix/payments/{paymentId}_ deve ser utilizado para o cancelamento de um pagamento de forma unitária. Não deve ser utilizado para o cancelamento de todos os agendamentos recorrentes associados a um consentimento.   - O _PATCH /pix/payments/consents/{consentId}_ deve ser utilizado no cancelamento de todas as ocorrências de pagamentos agendados presentes em uma recorrência de pagamentos. Todos os pagamentos associados ao consentimento informado e passíveis de cancelamento (ainda não liquidados, com os status PDNG e SCHD) deverão ser cancelados.   # noqa: E501

    OpenAPI spec version: 4.0.0-beta.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from payments_4_0_0-beta_2_yml.api_client import ApiClient


class PagamentosApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def payments_get_consents_consent_id(self, consent_id, authorization, x_fapi_interaction_id, **kwargs):  # noqa: E501
        """Consultar consentimento para iniciação de pagamento.  # noqa: E501

        Método para consulta do consentimento para a iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_get_consents_consent_id(consent_id, authorization, x_fapi_interaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str consent_id: O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePaymentConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payments_get_consents_consent_id_with_http_info(consent_id, authorization, x_fapi_interaction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.payments_get_consents_consent_id_with_http_info(consent_id, authorization, x_fapi_interaction_id, **kwargs)  # noqa: E501
            return data

    def payments_get_consents_consent_id_with_http_info(self, consent_id, authorization, x_fapi_interaction_id, **kwargs):  # noqa: E501
        """Consultar consentimento para iniciação de pagamento.  # noqa: E501

        Método para consulta do consentimento para a iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_get_consents_consent_id_with_http_info(consent_id, authorization, x_fapi_interaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str consent_id: O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePaymentConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent_id', 'authorization', 'x_fapi_interaction_id', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_customer_user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method payments_get_consents_consent_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'consent_id' is set
        if ('consent_id' not in params or
                params['consent_id'] is None):
            raise ValueError("Missing the required parameter `consent_id` when calling `payments_get_consents_consent_id`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `payments_get_consents_consent_id`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `payments_get_consents_consent_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'consent_id' in params:
            path_params['consentId'] = params['consent_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501
        if 'x_customer_user_agent' in params:
            header_params['x-customer-user-agent'] = params['x_customer_user_agent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/jwt', 'application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/consents/{consentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsePaymentConsent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def payments_get_pix_payments_payment_id(self, payment_id, authorization, x_fapi_interaction_id, **kwargs):  # noqa: E501
        """Consultar iniciação de pagamento.  # noqa: E501

        Método para consultar uma iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_get_pix_payments_payment_id(payment_id, authorization, x_fapi_interaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payment_id: Identificador da operação de pagamento. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePixPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payments_get_pix_payments_payment_id_with_http_info(payment_id, authorization, x_fapi_interaction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.payments_get_pix_payments_payment_id_with_http_info(payment_id, authorization, x_fapi_interaction_id, **kwargs)  # noqa: E501
            return data

    def payments_get_pix_payments_payment_id_with_http_info(self, payment_id, authorization, x_fapi_interaction_id, **kwargs):  # noqa: E501
        """Consultar iniciação de pagamento.  # noqa: E501

        Método para consultar uma iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_get_pix_payments_payment_id_with_http_info(payment_id, authorization, x_fapi_interaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payment_id: Identificador da operação de pagamento. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePixPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_id', 'authorization', 'x_fapi_interaction_id', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_customer_user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method payments_get_pix_payments_payment_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in params or
                params['payment_id'] is None):
            raise ValueError("Missing the required parameter `payment_id` when calling `payments_get_pix_payments_payment_id`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `payments_get_pix_payments_payment_id`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `payments_get_pix_payments_payment_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_id' in params:
            path_params['paymentId'] = params['payment_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501
        if 'x_customer_user_agent' in params:
            header_params['x-customer-user-agent'] = params['x_customer_user_agent']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/jwt', 'application/json; charset=utf-8', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2ClientCredentials']  # noqa: E501

        return self.api_client.call_api(
            '/pix/payments/{paymentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsePixPayment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def payments_patch_pix_payments_consent_id(self, body, authorization, x_fapi_interaction_id, x_idempotency_key, consent_id, **kwargs):  # noqa: E501
        """Cancelar todos os pagamentos referentes ao mesmo Consentimento.  # noqa: E501

        Esse endpoint deve ser usado para cancelar, a pedido do cliente pagador, as transações que estejam em uma das seguintes situações: Agendada com sucesso (SCHD) ou retida para análise (PDNG). O cancelamento de pagamentos agendados (SCHD) podem ser enviados até 23:59 (Horário de Brasília) do dia anterior à data de efetivação do pagamento. Todos os pagamentos vinculados a esse consentimento e previstos para ocorrer a partir do dia seguinte serão cancelados. Os pagamentos já liquidados não são passíveis de cancelamento. - Se não restar nenhum pagamento (ocorrência) que poderá ser cancelado, a requisição PATCH retorna HTTP Status 422 com o code PAGAMENTO_NAO_PERMITE_CANCELAMENTO. - Caso receba um 422, a iniciadora deve fazer uma requisição GET no pagamento para verificar a situação atual dele, bem como detalhes associados. - Caso o consentimento enviado pelo iniciador no path de requisição não exista na detentora de conta, a detentora deverá retornar código 404.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_patch_pix_payments_consent_id(body, authorization, x_fapi_interaction_id, x_idempotency_key, consent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PatchPixPayment body: Payload para cancelamento do pagamento. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str consent_id: O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePatchPixConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payments_patch_pix_payments_consent_id_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, consent_id, **kwargs)  # noqa: E501
        else:
            (data) = self.payments_patch_pix_payments_consent_id_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, consent_id, **kwargs)  # noqa: E501
            return data

    def payments_patch_pix_payments_consent_id_with_http_info(self, body, authorization, x_fapi_interaction_id, x_idempotency_key, consent_id, **kwargs):  # noqa: E501
        """Cancelar todos os pagamentos referentes ao mesmo Consentimento.  # noqa: E501

        Esse endpoint deve ser usado para cancelar, a pedido do cliente pagador, as transações que estejam em uma das seguintes situações: Agendada com sucesso (SCHD) ou retida para análise (PDNG). O cancelamento de pagamentos agendados (SCHD) podem ser enviados até 23:59 (Horário de Brasília) do dia anterior à data de efetivação do pagamento. Todos os pagamentos vinculados a esse consentimento e previstos para ocorrer a partir do dia seguinte serão cancelados. Os pagamentos já liquidados não são passíveis de cancelamento. - Se não restar nenhum pagamento (ocorrência) que poderá ser cancelado, a requisição PATCH retorna HTTP Status 422 com o code PAGAMENTO_NAO_PERMITE_CANCELAMENTO. - Caso receba um 422, a iniciadora deve fazer uma requisição GET no pagamento para verificar a situação atual dele, bem como detalhes associados. - Caso o consentimento enviado pelo iniciador no path de requisição não exista na detentora de conta, a detentora deverá retornar código 404.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_patch_pix_payments_consent_id_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, consent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PatchPixPayment body: Payload para cancelamento do pagamento. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str consent_id: O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePatchPixConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'x_fapi_interaction_id', 'x_idempotency_key', 'consent_id', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_customer_user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method payments_patch_pix_payments_consent_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `payments_patch_pix_payments_consent_id`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `payments_patch_pix_payments_consent_id`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `payments_patch_pix_payments_consent_id`")  # noqa: E501
        # verify the required parameter 'x_idempotency_key' is set
        if ('x_idempotency_key' not in params or
                params['x_idempotency_key'] is None):
            raise ValueError("Missing the required parameter `x_idempotency_key` when calling `payments_patch_pix_payments_consent_id`")  # noqa: E501
        # verify the required parameter 'consent_id' is set
        if ('consent_id' not in params or
                params['consent_id'] is None):
            raise ValueError("Missing the required parameter `consent_id` when calling `payments_patch_pix_payments_consent_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'consent_id' in params:
            path_params['consentId'] = params['consent_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501
        if 'x_customer_user_agent' in params:
            header_params['x-customer-user-agent'] = params['x_customer_user_agent']  # noqa: E501
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
            '/pix/payments/consents/{consentId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsePatchPixConsent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def payments_patch_pix_payments_payment_id(self, body, authorization, x_fapi_interaction_id, payment_id, **kwargs):  # noqa: E501
        """Cancelar iniciação de pagamento.  # noqa: E501

        Esse endpoint deve ser usado para cancelar, a pedido do cliente pagador, as transações que estejam em uma das seguintes situações: Agendada com sucesso (SCHD) ou retida para análise (PDNG).  - Caso a requisição seja bem sucedida, a transação vai para a situação CANC.  - Caso o status do pagamento seja diferente de SCHD/PDNG ou alguma outra regra de negócio impeça o cancelamento, a requisição PATCH retorna HTTP Status 422 com o code PAGAMENTO_NAO_PERMITE_CANCELAMENTO.  - Caso receba um 422, a iniciadora deve fazer uma requisição GET no pagamento para verificar a situação atual dele, bem como detalhes associados.  O cancelamento de pagamento agendado (SCHD) pode ser enviado até 23:59 (Horário de Brasília) do dia anterior à data de efetivação do pagamento.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_patch_pix_payments_payment_id(body, authorization, x_fapi_interaction_id, payment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PatchPixPayment body: Payload para cancelamento do pagamento. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str payment_id: Identificador da operação de pagamento. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePatchPixPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payments_patch_pix_payments_payment_id_with_http_info(body, authorization, x_fapi_interaction_id, payment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.payments_patch_pix_payments_payment_id_with_http_info(body, authorization, x_fapi_interaction_id, payment_id, **kwargs)  # noqa: E501
            return data

    def payments_patch_pix_payments_payment_id_with_http_info(self, body, authorization, x_fapi_interaction_id, payment_id, **kwargs):  # noqa: E501
        """Cancelar iniciação de pagamento.  # noqa: E501

        Esse endpoint deve ser usado para cancelar, a pedido do cliente pagador, as transações que estejam em uma das seguintes situações: Agendada com sucesso (SCHD) ou retida para análise (PDNG).  - Caso a requisição seja bem sucedida, a transação vai para a situação CANC.  - Caso o status do pagamento seja diferente de SCHD/PDNG ou alguma outra regra de negócio impeça o cancelamento, a requisição PATCH retorna HTTP Status 422 com o code PAGAMENTO_NAO_PERMITE_CANCELAMENTO.  - Caso receba um 422, a iniciadora deve fazer uma requisição GET no pagamento para verificar a situação atual dele, bem como detalhes associados.  O cancelamento de pagamento agendado (SCHD) pode ser enviado até 23:59 (Horário de Brasília) do dia anterior à data de efetivação do pagamento.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_patch_pix_payments_payment_id_with_http_info(body, authorization, x_fapi_interaction_id, payment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PatchPixPayment body: Payload para cancelamento do pagamento. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str payment_id: Identificador da operação de pagamento. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePatchPixPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'x_fapi_interaction_id', 'payment_id', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_customer_user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method payments_patch_pix_payments_payment_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `payments_patch_pix_payments_payment_id`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `payments_patch_pix_payments_payment_id`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `payments_patch_pix_payments_payment_id`")  # noqa: E501
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in params or
                params['payment_id'] is None):
            raise ValueError("Missing the required parameter `payment_id` when calling `payments_patch_pix_payments_payment_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_id' in params:
            path_params['paymentId'] = params['payment_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501
        if 'x_customer_user_agent' in params:
            header_params['x-customer-user-agent'] = params['x_customer_user_agent']  # noqa: E501

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
            '/pix/payments/{paymentId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsePatchPixPayment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def payments_post_consents(self, body, authorization, x_fapi_interaction_id, x_idempotency_key, **kwargs):  # noqa: E501
        """Criar consentimento para a iniciação de pagamento.  # noqa: E501

        Método de criação do consentimento para a iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_post_consents(body, authorization, x_fapi_interaction_id, x_idempotency_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePaymentConsent body: Payload para criação do consentimento para iniciação do pagamento. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponseCreatePaymentConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payments_post_consents_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, **kwargs)  # noqa: E501
        else:
            (data) = self.payments_post_consents_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, **kwargs)  # noqa: E501
            return data

    def payments_post_consents_with_http_info(self, body, authorization, x_fapi_interaction_id, x_idempotency_key, **kwargs):  # noqa: E501
        """Criar consentimento para a iniciação de pagamento.  # noqa: E501

        Método de criação do consentimento para a iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_post_consents_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePaymentConsent body: Payload para criação do consentimento para iniciação do pagamento. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponseCreatePaymentConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'x_fapi_interaction_id', 'x_idempotency_key', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_customer_user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method payments_post_consents" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `payments_post_consents`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `payments_post_consents`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `payments_post_consents`")  # noqa: E501
        # verify the required parameter 'x_idempotency_key' is set
        if ('x_idempotency_key' not in params or
                params['x_idempotency_key'] is None):
            raise ValueError("Missing the required parameter `x_idempotency_key` when calling `payments_post_consents`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501
        if 'x_customer_user_agent' in params:
            header_params['x-customer-user-agent'] = params['x_customer_user_agent']  # noqa: E501
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
            '/consents', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseCreatePaymentConsent',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def payments_post_pix_payments(self, body, authorization, x_fapi_interaction_id, x_idempotency_key, **kwargs):  # noqa: E501
        """Criar iniciação de pagamento.  # noqa: E501

        Método para criar uma iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_post_pix_payments(body, authorization, x_fapi_interaction_id, x_idempotency_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePixPayment body: Payload para criação da iniciação do pagamento Pix. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponseCreatePixPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payments_post_pix_payments_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, **kwargs)  # noqa: E501
        else:
            (data) = self.payments_post_pix_payments_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, **kwargs)  # noqa: E501
            return data

    def payments_post_pix_payments_with_http_info(self, body, authorization, x_fapi_interaction_id, x_idempotency_key, **kwargs):  # noqa: E501
        """Criar iniciação de pagamento.  # noqa: E501

        Método para criar uma iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_post_pix_payments_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePixPayment body: Payload para criação da iniciação do pagamento Pix. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponseCreatePixPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'x_fapi_interaction_id', 'x_idempotency_key', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_customer_user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method payments_post_pix_payments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `payments_post_pix_payments`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `payments_post_pix_payments`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `payments_post_pix_payments`")  # noqa: E501
        # verify the required parameter 'x_idempotency_key' is set
        if ('x_idempotency_key' not in params or
                params['x_idempotency_key'] is None):
            raise ValueError("Missing the required parameter `x_idempotency_key` when calling `payments_post_pix_payments`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_fapi_auth_date' in params:
            header_params['x-fapi-auth-date'] = params['x_fapi_auth_date']  # noqa: E501
        if 'x_fapi_customer_ip_address' in params:
            header_params['x-fapi-customer-ip-address'] = params['x_fapi_customer_ip_address']  # noqa: E501
        if 'x_fapi_interaction_id' in params:
            header_params['x-fapi-interaction-id'] = params['x_fapi_interaction_id']  # noqa: E501
        if 'x_customer_user_agent' in params:
            header_params['x-customer-user-agent'] = params['x_customer_user_agent']  # noqa: E501
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
            '/pix/payments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseCreatePixPayment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
