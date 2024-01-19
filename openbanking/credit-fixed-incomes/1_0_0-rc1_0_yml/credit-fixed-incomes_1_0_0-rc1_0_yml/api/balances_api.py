# coding: utf-8

"""
    API Credit Fixed Incomes - Open Finance Brasil

    API de informações de operações de Renda Fixa Crédito do Open Finance Brasil – Fase 4. API que retorna informações de operações de investimento do tipo Renda Fixa Crédito (Debêntures, CRI/CRA) mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação do produto, rentabilidade, quantidade, prazos, saldos em posição do cliente e movimentações financeiras. Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints. A exposição se dará por cada operação de renda fixa contratada pelo cliente.   # noqa: E501

    OpenAPI spec version: 1.0.0-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from credit-fixed-incomes_1_0_0-rc1_0_yml.api_client import ApiClient


class BalancesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def credit_fixed_incomes_get_investments_investment_id_balances(self, investment_id, authorization, x_fapi_interaction_id, **kwargs):  # noqa: E501
        """Obtém a posição da operação de Renda Fixa Crédito identificada por investmentId.  # noqa: E501

        Obtém a posição da operação de Renda Fixa Crédito identificada por investmentId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credit_fixed_incomes_get_investments_investment_id_balances(investment_id, authorization, x_fapi_interaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str investment_id: Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \"espelhado\" pela transmissora (server) no cabeçalho de resposta. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC.
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponseCreditFixedIncomesBalances
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.credit_fixed_incomes_get_investments_investment_id_balances_with_http_info(investment_id, authorization, x_fapi_interaction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.credit_fixed_incomes_get_investments_investment_id_balances_with_http_info(investment_id, authorization, x_fapi_interaction_id, **kwargs)  # noqa: E501
            return data

    def credit_fixed_incomes_get_investments_investment_id_balances_with_http_info(self, investment_id, authorization, x_fapi_interaction_id, **kwargs):  # noqa: E501
        """Obtém a posição da operação de Renda Fixa Crédito identificada por investmentId.  # noqa: E501

        Obtém a posição da operação de Renda Fixa Crédito identificada por investmentId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.credit_fixed_incomes_get_investments_investment_id_balances_with_http_info(investment_id, authorization, x_fapi_interaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str investment_id: Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \"espelhado\" pela transmissora (server) no cabeçalho de resposta. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC.
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponseCreditFixedIncomesBalances
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['investment_id', 'authorization', 'x_fapi_interaction_id', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_customer_user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method credit_fixed_incomes_get_investments_investment_id_balances" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'investment_id' is set
        if ('investment_id' not in params or
                params['investment_id'] is None):
            raise ValueError("Missing the required parameter `investment_id` when calling `credit_fixed_incomes_get_investments_investment_id_balances`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `credit_fixed_incomes_get_investments_investment_id_balances`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `credit_fixed_incomes_get_investments_investment_id_balances`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'investment_id' in params:
            path_params['investmentId'] = params['investment_id']  # noqa: E501

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
            ['application/json', 'application/json; charset=utf-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2Security', 'OpenId']  # noqa: E501

        return self.api_client.call_api(
            '/investments/{investmentId}/balances', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseCreditFixedIncomesBalances',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
