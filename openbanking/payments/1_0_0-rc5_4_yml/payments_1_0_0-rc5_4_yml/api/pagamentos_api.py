# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora  de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:   - Certificados exigidos para assinatura de mensagens:   [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Algoritmos usados para assinatura de mensagens `JWS`:   [Perfil de segurança FAPI - Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-financial-api-1_ID1.md#algorithm-considerations)  - Mensagens assinadas, `JWS` e `JWKS`:   [Guia de usuário (Receptoras e iniciadoras de pagamento)](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/tpp-user-guide.md#143-what-is-a-jwt-jwe-jws-and-jwk)    ## Controle de acesso    O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).    Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.       # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.4
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from payments_1_0_0-rc5_4_yml.api_client import ApiClient


class PagamentosApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def payments_get_consents_consent_id(self, consent_id, authorization, **kwargs):  # noqa: E501
        """Consultar consentimento para iniciação de pagamento.  # noqa: E501

        Método para consulta do consentimento para a iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_get_consents_consent_id(consent_id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str consent_id: O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePaymentConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payments_get_consents_consent_id_with_http_info(consent_id, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.payments_get_consents_consent_id_with_http_info(consent_id, authorization, **kwargs)  # noqa: E501
            return data

    def payments_get_consents_consent_id_with_http_info(self, consent_id, authorization, **kwargs):  # noqa: E501
        """Consultar consentimento para iniciação de pagamento.  # noqa: E501

        Método para consulta do consentimento para a iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_get_consents_consent_id_with_http_info(consent_id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str consent_id: O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição transnmissora (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePaymentConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['consent_id', 'authorization', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_fapi_interaction_id', 'x_customer_user_agent']  # noqa: E501
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

    def payments_get_pix_payments_payment_id(self, payment_id, authorization, **kwargs):  # noqa: E501
        """Consultar iniciação de pagamento.  # noqa: E501

        Método para consultar uma iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_get_pix_payments_payment_id(payment_id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payment_id: Identificador da operação de pagamento. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePixPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payments_get_pix_payments_payment_id_with_http_info(payment_id, authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.payments_get_pix_payments_payment_id_with_http_info(payment_id, authorization, **kwargs)  # noqa: E501
            return data

    def payments_get_pix_payments_payment_id_with_http_info(self, payment_id, authorization, **kwargs):  # noqa: E501
        """Consultar iniciação de pagamento.  # noqa: E501

        Método para consultar uma iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_get_pix_payments_payment_id_with_http_info(payment_id, authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str payment_id: Identificador da operação de pagamento. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePixPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_id', 'authorization', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_fapi_interaction_id', 'x_customer_user_agent']  # noqa: E501
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
        auth_settings = ['OAuth2AuthorizationCode', 'OAuth2ClientCredentials']  # noqa: E501

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

    def payments_post_consents(self, body, authorization, x_idempotency_key, **kwargs):  # noqa: E501
        """Criar consentimento para a iniciação de pagamento.  # noqa: E501

        Método de criação do consentimento para a iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_post_consents(body, authorization, x_idempotency_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePaymentConsent body: Payload para criação do consentimento para iniciação do pagamento. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePaymentConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payments_post_consents_with_http_info(body, authorization, x_idempotency_key, **kwargs)  # noqa: E501
        else:
            (data) = self.payments_post_consents_with_http_info(body, authorization, x_idempotency_key, **kwargs)  # noqa: E501
            return data

    def payments_post_consents_with_http_info(self, body, authorization, x_idempotency_key, **kwargs):  # noqa: E501
        """Criar consentimento para a iniciação de pagamento.  # noqa: E501

        Método de criação do consentimento para a iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_post_consents_with_http_info(body, authorization, x_idempotency_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePaymentConsent body: Payload para criação do consentimento para iniciação do pagamento. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePaymentConsent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'x_idempotency_key', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_fapi_interaction_id', 'x_customer_user_agent']  # noqa: E501
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
        auth_settings = ['OAuth2ClientCredentials', 'OpenId']  # noqa: E501

        return self.api_client.call_api(
            '/consents', 'POST',
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

    def payments_post_pix_payments(self, body, authorization, x_idempotency_key, **kwargs):  # noqa: E501
        """Criar iniciação de pagamento.  # noqa: E501

        Método para criar uma iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_post_pix_payments(body, authorization, x_idempotency_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePixPayment body: Payload para criação da iniciação do pagamento Pix. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePixPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.payments_post_pix_payments_with_http_info(body, authorization, x_idempotency_key, **kwargs)  # noqa: E501
        else:
            (data) = self.payments_post_pix_payments_with_http_info(body, authorization, x_idempotency_key, **kwargs)  # noqa: E501
            return data

    def payments_post_pix_payments_with_http_info(self, body, authorization, x_idempotency_key, **kwargs):  # noqa: E501
        """Criar iniciação de pagamento.  # noqa: E501

        Método para criar uma iniciação de pagamento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payments_post_pix_payments_with_http_info(body, authorization, x_idempotency_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreatePixPayment body: Payload para criação da iniciação do pagamento Pix. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponsePixPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'authorization', 'x_idempotency_key', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_fapi_interaction_id', 'x_customer_user_agent']  # noqa: E501
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
        auth_settings = ['OAuth2AuthorizationCode']  # noqa: E501

        return self.api_client.call_api(
            '/pix/payments', 'POST',
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
