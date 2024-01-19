# coding: utf-8

"""
    APIs Admin do Open Finance Brasil

    As API's administrativas são recursos que podem ser consumidos apenas pelo diretório para avaliação e controle da qualidade dos serviços fornecidos pelas instituições financeiras  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from admin_2_0_0_yml.api_client import ApiClient


class MetricsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_metrics(self, **kwargs):  # noqa: E501
        """Obtém as métricas de disponibilidade das APIs  # noqa: E501

        Obtém as métricas de disponibilidade das APIs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :param str period: Período a ser consultado   * `CURRENT` - Métricas do dia atual.   * `ALL` - Métricas de todo o período disponível (últimos 7 dias). 
        :return: ResponseMetricsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_metrics_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_metrics_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_metrics_with_http_info(self, **kwargs):  # noqa: E501
        """Obtém as métricas de disponibilidade das APIs  # noqa: E501

        Obtém as métricas de disponibilidade das APIs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metrics_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :param str period: Período a ser consultado   * `CURRENT` - Métricas do dia atual.   * `ALL` - Métricas de todo o período disponível (últimos 7 dias). 
        :return: ResponseMetricsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size', 'period']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metrics" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page-size', params['page_size']))  # noqa: E501
        if 'period' in params:
            query_params.append(('period', params['period']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/metrics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseMetricsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
