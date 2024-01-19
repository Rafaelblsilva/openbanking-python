# coding: utf-8

"""
    API Variable Incomes - Open Finance Brasil

    API de informações de operações de Renda Variável Open Finance Brasil – Fase 4.  API que retorna informações de operações de investimento do tipo Renda Variável mantidas nas instituições transmissoras por seus clientes, incluindo dados como informações do produto, quantidade, saldos em posição do cliente, movimentações financeiras e detalhes da nota de negociação.  Não possui segregação entre pessoa natural e pessoa jurídica. Requer consentimento do cliente para todos os endpoints.  A granularidade de exposição de operações de renda variável se dá por cada ativo (ticker) da carteira do cliente.  Compartilhamento considera lote padrão e fracionário, entretanto, no Open Finance Brasil, as informações são consolidadas via ticker do lote padrão.  A defasagem em relação ao canal eletrônico da instituição deve ser o fechamento (pregão) do dia anterior (d-1).   Em relação ao aluguel de ações: neste momento não faz parte do escopo de compartilhamento a carteira/posição de aluguel do cliente (ativos alugados e movimentações relacionadas a esses ativos).  Apenas deve ser compartilhado as transações de pagamento ou recebimento de juros oriundos dos contratos de ações alugadas (ou doadas) pelos clientes.  Para o identificador do investimento (investmentId) deve ser adotado o seguinte comportamento:  - Após 12 meses sem movimentações e com quantidade de ativos zerada, o resourceId correspondente ao investmentId em questão deve passar ao status UNAVAILABLE (considerando consentimento válido);  - Nas situações em que o cliente compre novamente o ativo após um período de 12 meses sem movimentação e com quantidade de ativos zerada, o mesmo identificador (investmentId) deve ser utilizado. Especificamente para tais produtos, o status do recurso na resources deve passar de UNAVAILABLE para AVAILABLE.  Segue abaixo tabela com o escopo de produtos a ser considerado para compartilhamento:  ```    |----------------------|-------------------------------|----------------------|-----------------------------------|    | CLASSE DE ATIVOS     | PRODUTO                       | SUBPRODUTO           | DENOMINAÇÃO                       |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       |     -                | FIAGRO                            |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | Subscrição           | Bonus / Direito / Recibo          |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de Investimentos       | Fundo imobiliario    | FII                               |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Ações                         | À vista              | ON / PN / UNIT                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF de Renda Variável             |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF                  | ETF Internacional                 |    |----------------------|-------------------------------|----------------------|-----------------------------------|    | Renda Variável       | Fundos de índices             | ETF Renda Fixa       | ETF Renda Fixa                    |    |----------------------|-------------------------------|----------------------|-----------------------------------|    ```   # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from variable-incomes_1_1_0_yml.api_client import ApiClient


class BrokerNoteDetailsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def variable_incomes_get_investments_investment_id_broker_notes_broker_note_id(self, broker_note_id, authorization, x_fapi_interaction_id, **kwargs):  # noqa: E501
        """Obtém as informações da nota de negociação identificado nas movimentações de compra e venda de ativos em bolsa. O brokerNoteId é enviado nos movimentos de compra ou venda de ativos e deve ser passada como parâmetro de entrada no endpoint “Nota de Negociação”.Como conteúdo do campo brokerNoteId é esperado que a transmissora gere um identificar único, imutável, para cada número (natural) de nota de negociação.   # noqa: E501

        Obtém as informações da nota de negociação identificado nas movimentações de compra e venda de ativos em bolsa. O brokerNoteId é enviado nos movimentos de compra ou venda de ativos e deve ser passada como parâmetro de entrada no endpoint “Nota de Negociação”.Como conteúdo do campo brokerNoteId é esperado que a transmissora gere um identificar único, imutável, para cada número (natural) de nota de negociação.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.variable_incomes_get_investments_investment_id_broker_notes_broker_note_id(broker_note_id, authorization, x_fapi_interaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str broker_note_id: Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \"espelhado\" pela transmissora (server) no cabeçalho de resposta. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC.
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponseVariableIncomesBroker
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.variable_incomes_get_investments_investment_id_broker_notes_broker_note_id_with_http_info(broker_note_id, authorization, x_fapi_interaction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.variable_incomes_get_investments_investment_id_broker_notes_broker_note_id_with_http_info(broker_note_id, authorization, x_fapi_interaction_id, **kwargs)  # noqa: E501
            return data

    def variable_incomes_get_investments_investment_id_broker_notes_broker_note_id_with_http_info(self, broker_note_id, authorization, x_fapi_interaction_id, **kwargs):  # noqa: E501
        """Obtém as informações da nota de negociação identificado nas movimentações de compra e venda de ativos em bolsa. O brokerNoteId é enviado nos movimentos de compra ou venda de ativos e deve ser passada como parâmetro de entrada no endpoint “Nota de Negociação”.Como conteúdo do campo brokerNoteId é esperado que a transmissora gere um identificar único, imutável, para cada número (natural) de nota de negociação.   # noqa: E501

        Obtém as informações da nota de negociação identificado nas movimentações de compra e venda de ativos em bolsa. O brokerNoteId é enviado nos movimentos de compra ou venda de ativos e deve ser passada como parâmetro de entrada no endpoint “Nota de Negociação”.Como conteúdo do campo brokerNoteId é esperado que a transmissora gere um identificar único, imutável, para cada número (natural) de nota de negociação.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.variable_incomes_get_investments_investment_id_broker_notes_broker_note_id_with_http_info(broker_note_id, authorization, x_fapi_interaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str broker_note_id: Identifica de forma única  o relacionamento do cliente com o produto, mantendo as regras de imutabilidade dentro da instituição transmissora. (required)
        :param str authorization: Cabeçalho HTTP padrão. Permite que as credenciais sejam fornecidas dependendo do tipo de recurso solicitado (required)
        :param str x_fapi_interaction_id: Um UUID RFC4122 usado como um ID de correlação entre request e response. Campo de geração e envio obrigatório pela receptora (client) e o seu valor deve ser \"espelhado\" pela transmissora (server) no cabeçalho de resposta. (required)
        :param str x_fapi_auth_date: Data em que o usuário logou pela última vez com o receptor. Representada de acordo com a RFC7231. Exemplo: Sun, 10 Sep 2017 19:43:31 UTC.
        :param str x_fapi_customer_ip_address: O endereço IP do usuário se estiver atualmente logado com o receptor.
        :param str x_customer_user_agent: Indica o user-agent que o usuário utiliza.
        :return: ResponseVariableIncomesBroker
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['broker_note_id', 'authorization', 'x_fapi_interaction_id', 'x_fapi_auth_date', 'x_fapi_customer_ip_address', 'x_customer_user_agent']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method variable_incomes_get_investments_investment_id_broker_notes_broker_note_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'broker_note_id' is set
        if ('broker_note_id' not in params or
                params['broker_note_id'] is None):
            raise ValueError("Missing the required parameter `broker_note_id` when calling `variable_incomes_get_investments_investment_id_broker_notes_broker_note_id`")  # noqa: E501
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `variable_incomes_get_investments_investment_id_broker_notes_broker_note_id`")  # noqa: E501
        # verify the required parameter 'x_fapi_interaction_id' is set
        if ('x_fapi_interaction_id' not in params or
                params['x_fapi_interaction_id'] is None):
            raise ValueError("Missing the required parameter `x_fapi_interaction_id` when calling `variable_incomes_get_investments_investment_id_broker_notes_broker_note_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'broker_note_id' in params:
            path_params['brokerNoteId'] = params['broker_note_id']  # noqa: E501

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
        auth_settings = ['OAuth2AuthorizationCode']  # noqa: E501

        return self.api_client.call_api(
            '/broker-notes/{brokerNoteId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResponseVariableIncomesBroker',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
