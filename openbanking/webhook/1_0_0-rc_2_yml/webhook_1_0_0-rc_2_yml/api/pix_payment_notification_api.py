# coding: utf-8

"""
    API Webhook - Open Finance Brasil

    API de Webhook é responsável por notificar eventos definidos em cada uma das APIs que possuem a funcionalidade no Open Finance Brasil.    Informações sobre endpoints suportados e funcionamento podem ser encontrados na página <a href=\"https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/105021661/Conven+o+de+Webhook\">Convenção de Webhook</a>, disponível no portal do desenvolvedor do Open Finance Brasil.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from webhook_1_0_0-rc_2_yml.api_client import ApiClient


class PixPaymentNotificationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def pix_payment_notification(self, body, x_webhook_interaction_id, payment_id, version_api, **kwargs):  # noqa: E501
        """Notificações de mudanças de estados do pagamento: Arranjo Pix da API de Iniciação de Pagamentos.  # noqa: E501

        Notificações de mudanças de estados do pagamento: Arranjo Pix da API de Iniciação de Pagamentos.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pix_payment_notification(body, x_webhook_interaction_id, payment_id, version_api, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestBodyWebhook body: Payload enviado para notificar a alteração no estado do pagamento. (required)
        :param str x_webhook_interaction_id: Identificador único para cada tentativa de notificação realizada. O identificador deverá seguir o padrão UID [RFC4122](https://tools.ietf.org/html/rfc4122). (required)
        :param str payment_id: Identificador da operação de pagamento. (required)
        :param str version_api: Identifica a versão da API que deverá ser utilizada para recebimento da notificação via webhook (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.pix_payment_notification_with_http_info(body, x_webhook_interaction_id, payment_id, version_api, **kwargs)  # noqa: E501
        else:
            (data) = self.pix_payment_notification_with_http_info(body, x_webhook_interaction_id, payment_id, version_api, **kwargs)  # noqa: E501
            return data

    def pix_payment_notification_with_http_info(self, body, x_webhook_interaction_id, payment_id, version_api, **kwargs):  # noqa: E501
        """Notificações de mudanças de estados do pagamento: Arranjo Pix da API de Iniciação de Pagamentos.  # noqa: E501

        Notificações de mudanças de estados do pagamento: Arranjo Pix da API de Iniciação de Pagamentos.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.pix_payment_notification_with_http_info(body, x_webhook_interaction_id, payment_id, version_api, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RequestBodyWebhook body: Payload enviado para notificar a alteração no estado do pagamento. (required)
        :param str x_webhook_interaction_id: Identificador único para cada tentativa de notificação realizada. O identificador deverá seguir o padrão UID [RFC4122](https://tools.ietf.org/html/rfc4122). (required)
        :param str payment_id: Identificador da operação de pagamento. (required)
        :param str version_api: Identifica a versão da API que deverá ser utilizada para recebimento da notificação via webhook (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_webhook_interaction_id', 'payment_id', 'version_api']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method pix_payment_notification" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `pix_payment_notification`")  # noqa: E501
        # verify the required parameter 'x_webhook_interaction_id' is set
        if ('x_webhook_interaction_id' not in params or
                params['x_webhook_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_webhook_interaction_id` when calling `pix_payment_notification`")  # noqa: E501
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in params or
                params['payment_id'] is None):
            raise ValueError("Missing the required parameter `payment_id` when calling `pix_payment_notification`")  # noqa: E501
        # verify the required parameter 'version_api' is set
        if ('version_api' not in params or
                params['version_api'] is None):
            raise ValueError("Missing the required parameter `version_api` when calling `pix_payment_notification`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_id' in params:
            path_params['paymentId'] = params['payment_id']  # noqa: E501
        if 'version_api' in params:
            path_params['versionApi'] = params['version_api']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_webhook_interaction_id' in params:
            header_params['x-webhook-interaction-id'] = params['x_webhook_interaction_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/payments/{versionApi}/pix/payments/{paymentId}', 'POST',
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
