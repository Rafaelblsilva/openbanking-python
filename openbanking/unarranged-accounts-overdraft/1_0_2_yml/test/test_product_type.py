# coding: utf-8

"""
    API Unarranged-accounts-overdraft - Open Banking Brasil

    API de informações de operações de adiantamento a depositantes do Open Banking Brasil – Fase 2. API que retorna informações de operações de crédito do tipo adiantamento a depositantes mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos, amortizações, garantias, encargos e taxas de juros remuneratórios.\\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Unarranged-accounts-overdraft  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **UNARRANGED_ACCOUNTS_OVERDRAFT_READ** ### `/contracts/{contractId}`   - permissions: **UNARRANGED_ACCOUNTS_OVERDRAFT_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **UNARRANGED_ACCOUNTS_OVERDRAFT_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **UNARRANGED_ACCOUNTS_OVERDRAFT_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **UNARRANGED_ACCOUNTS_OVERDRAFT_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import unarranged-accounts-overdraft_1_0_2_yml
from unarranged-accounts-overdraft_1_0_2_yml.models.product_type import ProductType  # noqa: E501
from unarranged-accounts-overdraft_1_0_2_yml.rest import ApiException


class TestProductType(unittest.TestCase):
    """ProductType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductType(self):
        """Test ProductType"""
        # FIXME: construct object with mandatory attributes with example values
        # model = unarranged-accounts-overdraft_1_0_2_yml.models.product_type.ProductType()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
