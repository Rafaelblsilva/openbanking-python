# coding: utf-8

"""
    API Resources - Open Finance Brasil

    API que trata da consulta do status de recursos para o Open Finance Brasil - Fase 2.\\ Não possui segregação entre pessoa natural e pessoa jurídica.  # Orientações importantes - A API resources lista os recursos vinculados ao consentimento específico, identificado por `consentId` e vinculado ao token enviado no header `Authorization`. - Os `STATUS` dos recursos listados DEVEM considerar não apenas o consentimento vinculado mas também a disponibilidade do recurso na instituição transmissora dos dados. - A `permission` específica desta API  - `RESOURCES_READ` - DEVE ser solicitada pela instituição receptora na ocasião do pedido de criação do consentimento. - A consulta à API Resources não é obrigatória por parte das instituições receptoras - esta API foi criada para dar visibilidade da existência de ocorrências que possam impedir o compartilhamento de determinados recursos por parte da instituição transmissora dos dados. - O identificador do recurso devolvido na API Resources - `resourceId` - quando apresentado corresponde ao mesmo identificador designado para o recurso em sua API específica, o seja: o `resourceId` corresponde ao `accountId` da API accounts, ao `creditCardAccountId` da API de conta pós-paga e assim sucessivamente.  ## Status previstos para os recursos listados na API Resources - AVAILABLE: indica que o recurso encontra-se disponível e o(s) consentimento(s) associado(s) possui(em) status `AUTHORISED`. - UNAVAILABLE: indica que o recurso não está mais disponível, por exemplo, em caso de uma conta encerrada. - TEMPORARILY_UNAVAILABLE: indica que o recurso encontra-se temporariamente indisponível, embora o(s) consentimento(s) associado(s) possua(m) status `AUTHORISED`.   Caso de exemplo: conta temporariamente bloqueada por suspeita de fraude. - PENDING_AUTHORISATION: indica a existência de pendências para o compartilhamento do recurso, por exemplo, em caso de alçada dupla, quando é necessário o consentimento de mais de um titular.  ## Permissions necessárias para a API Resources ### `/resources`   - permissions:     - GET: **RESOURCES_READ**   # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from resources_2_0_1_yml.api_client import ApiClient


class ResourcesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def resources_get_resources(self, authorization, **kwargs):  # noqa: E501
        """Obtém a lista de recursos consentidos pelo cliente.  # noqa: E501

        Método para obter a lista de recursos mantidos pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_get_resources(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseResourceList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resources_get_resources_with_http_info(authorization, **kwargs)  # noqa: E501
        else:
            (data) = self.resources_get_resources_with_http_info(authorization, **kwargs)  # noqa: E501
            return data

    def resources_get_resources_with_http_info(self, authorization, **kwargs):  # noqa: E501
        """Obtém a lista de recursos consentidos pelo cliente.  # noqa: E501

        Método para obter a lista de recursos mantidos pelo cliente na instituição transmissora e para as quais ele tenha fornecido consentimento.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resources_get_resources_with_http_info(authorization, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a [RFC7231](https://tools.ietf.org/html/rfc7231).Exemplo: Sun, 10 Sep 2017 19:43:31 UTC
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_fapi_interaction_id: Um UID [RFC4122](https://tools.ietf.org/html/rfc4122) usado como um ID de correlação. Se fornecido, o transmissor deve \"reproduzir\" esse valor no cabeçalho de resposta.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseResourceList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_fapi_interaction_id', 'x_customer_user_agent', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resources_get_resources" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `resources_get_resources`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page-size', params['page_size']))  # noqa: E501

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
            ['application/json', 'application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2Security', 'OpenId']  # noqa: E501

        return self.api_client.call_api(
            '/resources', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseResourceList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
