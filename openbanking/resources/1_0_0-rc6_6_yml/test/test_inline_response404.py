# coding: utf-8

"""
    API Resources - Open Banking Brasil

    API que trata da consulta do status de recursos para o Open Banking Brasil - Fase 2.\\ Não possui segregação entre pessoa natural e pessoa jurídica.  # Orientações importantes - A API resources lista os recursos vinculados ao consentimento específico, identificado por `consentId` e vinculado ao token enviado no header `Authorization`. - Os `STATUS` dos recursos listados DEVEM considerar não apenas o consentimento vinculado mas também a disponibilidade do recurso na instituição transmissora dos dados. - Na lista de recursos devolvida na API resources somente constará informação no atributo `resourceId` para recursos com o `STATUS` `AVAILABLE`. - Para os demais `STATUS` não é devolvido o identificador do recurso - `resourceId`. - A `permission` específica desta API  - `RESOURCES_READ` - DEVE ser solicitada pela instituição receptora na ocasião do pedido de criação do consentimento. - A consulta à API Resources não é obrigatória por parte das instituições receptoras - esta API foi criada para dar visibilidade da existência de ocorrências que possam impedir o compartilhamento de determinados recursos por parte da instituição transmissora dos dados. - O identificador do recurso devolvido na API Resources - `resourceId` - quando apresentado corresponde ao mesmo identificador designado para o recurso em sua API específica, o seja: o `resourceId` corresponde ao `accountId` da API accounts, ao `creditCardAccountId` da API de conta pós-paga e assim sucessivamente.  ## Status previstos para os recursos listados na API Resources - AVAILABLE: indica que o recurso encontra-se disponível e o(s) consentimento(s) associado(s) possui(em) status `AUTHORISED`. - UNAVAILABLE: indica que o recurso não está mais disponível, por exemplo, em caso de uma conta encerrada. - TEMPORARILY_UNAVAILABLE: indica que o recurso encontra-se temporariamente indisponível, embora o(s) consentimento(s) associado(s) possua(m) status `AUTHORISED`.   Caso de exemplo: conta temporariamente bloqueada por suspeita de fraude. - PENDING_AUTHORISATION: indica a existência de pendências para o compartilhamento do recurso, por exemplo, em caso de alçada dupla, quando é necessário o consentimento de mais de um titular.  ## Permissions necessárias para a API Resources ### `/resources`   - permissions:     - GET: **RESOURCES_READ**   # noqa: E501

    OpenAPI spec version: 1.0.0-rc6.6
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import resources_1_0_0-rc6_6_yml
from resources_1_0_0-rc6_6_yml.models.inline_response404 import InlineResponse404  # noqa: E501
from resources_1_0_0-rc6_6_yml.rest import ApiException


class TestInlineResponse404(unittest.TestCase):
    """InlineResponse404 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponse404(self):
        """Test InlineResponse404"""
        # FIXME: construct object with mandatory attributes with example values
        # model = resources_1_0_0-rc6_6_yml.models.inline_response404.InlineResponse404()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
