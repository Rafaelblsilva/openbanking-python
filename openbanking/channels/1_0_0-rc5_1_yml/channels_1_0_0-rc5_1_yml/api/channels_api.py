# coding: utf-8

"""
    APIs OpenData do Open Banking Brasil

    As APIs descritas neste documento são referentes as APIs da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 1.0.0-rc5.1
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from channels_1_0_0-rc5_1_yml.api_client import ApiClient


class ChannelsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_banking_agents(self, **kwargs):  # noqa: E501
        """Obtém a lista de correspondentes bancários da instituição financeira.  # noqa: E501

        Método para obter a lista de correspondentes bancários da instituição financeira.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_banking_agents(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseBankingAgentsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_banking_agents_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_banking_agents_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_banking_agents_with_http_info(self, **kwargs):  # noqa: E501
        """Obtém a lista de correspondentes bancários da instituição financeira.  # noqa: E501

        Método para obter a lista de correspondentes bancários da instituição financeira.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_banking_agents_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseBankingAgentsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_banking_agents" % key
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

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/banking-agents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseBankingAgentsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_branches(self, **kwargs):  # noqa: E501
        """Obtém a lista de dependências próprias da instituição financeira.  # noqa: E501

        Método para obter a lista de dependências próprias da instituição financeira.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_branches(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseBranchesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_branches_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_branches_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_branches_with_http_info(self, **kwargs):  # noqa: E501
        """Obtém a lista de dependências próprias da instituição financeira.  # noqa: E501

        Método para obter a lista de dependências próprias da instituição financeira.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_branches_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseBranchesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_branches" % key
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

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/branches', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseBranchesList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_electronic_channels(self, **kwargs):  # noqa: E501
        """Obtém a lista de canais eletrônicos de atendimento da instituição financeira.  # noqa: E501

        Método para obter a lista de canais eletrônicos de atendimento da instituição financeira.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_electronic_channels(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseElectronicChannelsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_electronic_channels_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_electronic_channels_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_electronic_channels_with_http_info(self, **kwargs):  # noqa: E501
        """Obtém a lista de canais eletrônicos de atendimento da instituição financeira.  # noqa: E501

        Método para obter a lista de canais eletrônicos de atendimento da instituição financeira.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_electronic_channels_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseElectronicChannelsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_electronic_channels" % key
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

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/electronic-channels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseElectronicChannelsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_phone_channels(self, **kwargs):  # noqa: E501
        """Obtém a lista de canais telefônicos de atendimento da instituição financeira.  # noqa: E501

        Método para obter a lista de canais telefônicos de atendimento da instituição financeira.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_phone_channels(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponsePhoneChannelsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_phone_channels_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_phone_channels_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_phone_channels_with_http_info(self, **kwargs):  # noqa: E501
        """Obtém a lista de canais telefônicos de atendimento da instituição financeira.  # noqa: E501

        Método para obter a lista de canais telefônicos de atendimento da instituição financeira.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_phone_channels_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponsePhoneChannelsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_phone_channels" % key
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

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/phone-channels', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponsePhoneChannelsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_shared_automated_teller_machines(self, **kwargs):  # noqa: E501
        """Obtém a lista de terminais compartilhados de autoatendimento.  # noqa: E501

        Método para obter a lista de terminais compartilhados de autoatendimento da instituição financeira.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shared_automated_teller_machines(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseSharedAutomatedTellerMachinesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_shared_automated_teller_machines_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_shared_automated_teller_machines_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_shared_automated_teller_machines_with_http_info(self, **kwargs):  # noqa: E501
        """Obtém a lista de terminais compartilhados de autoatendimento.  # noqa: E501

        Método para obter a lista de terminais compartilhados de autoatendimento da instituição financeira.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shared_automated_teller_machines_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Número da página que está sendo requisitada (o valor da primeira página é 1).
        :param int page_size: Quantidade total de registros por páginas.
        :return: ResponseSharedAutomatedTellerMachinesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shared_automated_teller_machines" % key
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

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/shared-automated-teller-machines', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseSharedAutomatedTellerMachinesList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
