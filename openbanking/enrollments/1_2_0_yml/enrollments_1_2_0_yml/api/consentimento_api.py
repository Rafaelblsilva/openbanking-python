# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    Família de API para permitir o pagamento sem redirecionamento via Open Finance Brasil.   Permite tanto o gerenciamento dos dispositivos vinculados as contas quanto a autorização de consentimentos criados via fluxo sem redirecionamento.   # noqa: E501

    OpenAPI spec version: 1.2.0
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from enrollments_1_2_0_yml.api_client import ApiClient


class ConsentimentoApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def authorize_consent(self, body, authorization, x_fapi_interaction_id, x_idempotency_key, consent_id, **kwargs):  # noqa: E501
        """Autorização de um consentimento de pagamentos na jornada sem redirecionamento  # noqa: E501

        Autorização de um consentimento de pagamentos em status `AWAITING_AUTHORISATION` a partir do access_token emitido pela jornada sem redirecionamento e envio de sinais de risco.   O consentimento de pagamento deve transitar ao status `AUTHORISED` na execução com sucesso desse método.   Em caso de falha, o status do consentimento do pagamento precisa transitar para o status `REJECTED`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authorize_consent(body, authorization, x_fapi_interaction_id, x_idempotency_key, consent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConsentAuthorization body: Payload para criação de vínculo de conta. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str consent_id: O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com a iniciadora.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.authorize_consent_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, consent_id, **kwargs)  # noqa: E501
        else:
            (data) = self.authorize_consent_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, consent_id, **kwargs)  # noqa: E501
            return data

    def authorize_consent_with_http_info(self, body, authorization, x_fapi_interaction_id, x_idempotency_key, consent_id, **kwargs):  # noqa: E501
        """Autorização de um consentimento de pagamentos na jornada sem redirecionamento  # noqa: E501

        Autorização de um consentimento de pagamentos em status `AWAITING_AUTHORISATION` a partir do access_token emitido pela jornada sem redirecionamento e envio de sinais de risco.   O consentimento de pagamento deve transitar ao status `AUTHORISED` na execução com sucesso desse método.   Em caso de falha, o status do consentimento do pagamento precisa transitar para o status `REJECTED`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.authorize_consent_with_http_info(body, authorization, x_fapi_interaction_id, x_idempotency_key, consent_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConsentAuthorization body: Payload para criação de vínculo de conta. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UUID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. A detentora deve obrigatoriamente retornar o campo com o mesmo valor recebido da iniciadora. (required)
        :param str x_idempotency_key: Cabeçalho HTTP personalizado. Identificador de solicitação exclusivo para suportar a idempotência. (required)
        :param str consent_id: O consentId é o identificador único do consentimento e deverá ser um URN - Uniform Resource Name.   Um URN, conforme definido na [RFC8141](https://tools.ietf.org/html/rfc8141) é um Uniform Resource  Identifier - URI - que é atribuído sob o URI scheme \"urn\" e um namespace URN específico, com a intenção de que o URN  seja um identificador de recurso persistente e independente da localização.   Considerando a string urn:bancoex:C1DD33123 como exemplo para consentId temos: - o namespace(urn) - o identificador associado ao namespace da instituição detentora de conta (bancoex)  - o identificador específico dentro do namespace (C1DD33123).   Informações mais detalhadas sobre a construção de namespaces devem ser consultadas na [RFC8141](https://tools.ietf.org/html/rfc8141).  (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com a iniciadora. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com a iniciadora.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: None
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
                    " to method authorize_consent" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `authorize_consent`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `authorize_consent`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `authorize_consent`")  # noqa: E501
        # verify the required parameter 'x_idempotency_key' is set
        if ('x_idempotency_key' not in params or
                params['x_idempotency_key'] is None):
            raise ValueError("Missing the required parameter `x_idempotency_key` when calling `authorize_consent`")  # noqa: E501
        # verify the required parameter 'consent_id' is set
        if ('consent_id' not in params or
                params['consent_id'] is None):
            raise ValueError("Missing the required parameter `consent_id` when calling `authorize_consent`")  # noqa: E501

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
            ['application/json; charset=utf-8', 'application/jwt', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/jwt'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2AuthorizationCode']  # noqa: E501

        return self.api_client.call_api(
            '/consents/{consentId}/authorise', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)