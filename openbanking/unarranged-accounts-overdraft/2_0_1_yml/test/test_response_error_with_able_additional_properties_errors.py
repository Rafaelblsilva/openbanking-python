# coding: utf-8

"""
    API Unarranged-accounts-overdraft - Open Finance Brasil

    API de informações de operações de adiantamento a depositantes do Open Finance Brasil – Fase 2. API que retorna informações de operações de crédito do tipo adiantamento a depositantes mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ### Observação   - No endpoint `/contracts/{contratId}/payments` a paginação ocorrerá sob os dados contidos no campo `releases` do tipo lista.  ## Permissions necessárias para a API Unarranged-accounts-overdraft  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **UNARRANGED_ACCOUNTS_OVERDRAFT_READ** ### `/contracts/{contractId}`   - permissions: **UNARRANGED_ACCOUNTS_OVERDRAFT_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **UNARRANGED_ACCOUNTS_OVERDRAFT_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **UNARRANGED_ACCOUNTS_OVERDRAFT_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **UNARRANGED_ACCOUNTS_OVERDRAFT_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import unarranged-accounts-overdraft_2_0_1_yml
from unarranged-accounts-overdraft_2_0_1_yml.models.response_error_with_able_additional_properties_errors import ResponseErrorWithAbleAdditionalPropertiesErrors  # noqa: E501
from unarranged-accounts-overdraft_2_0_1_yml.rest import ApiException


class TestResponseErrorWithAbleAdditionalPropertiesErrors(unittest.TestCase):
    """ResponseErrorWithAbleAdditionalPropertiesErrors unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testResponseErrorWithAbleAdditionalPropertiesErrors(self):
        """Test ResponseErrorWithAbleAdditionalPropertiesErrors"""
        # FIXME: construct object with mandatory attributes with example values
        # model = unarranged-accounts-overdraft_2_0_1_yml.models.response_error_with_able_additional_properties_errors.ResponseErrorWithAbleAdditionalPropertiesErrors()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
