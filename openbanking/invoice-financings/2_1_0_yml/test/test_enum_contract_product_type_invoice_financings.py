# coding: utf-8

"""
    API Invoice-financings - Open Finance Brasil

    API de informações de operações de antecipação de recebíveis do Open Finance Brasil - Fase 2.  API que retorna informações de operações de crédito do tipo antecipação de recebíveis, mantidas nas instituições transmissoras por seus clientes, incluindo dados como denominação, modalidade, número do contrato, tarifas, prazo, prestações, pagamentos (ao menos para os últimos 12 meses), amortizações, garantias, encargos e taxas de juros remuneratórios. \\ Não possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ### Observação:   - No endpoint `/contracts/{contratId}/payments` a paginação ocorrerá sob os dados contidos no campo `releases` do tipo lista.     ## Permissions necessárias para a API Invoice-financings  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/contracts`   - permissions:     - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}`   - permissions:     - GET: **INVOICE_FINANCINGS_READ** ### `/contracts/{contractId}/warranties`   - permissions:     - GET: **INVOICE_FINANCINGS_WARRANTIES_READ** ### `/contracts/{contractId}/scheduled-instalments`   - permissions:     - GET: **INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ** ### `/contracts/{contractId}/payments`   - permissions:     - GET: **INVOICE_FINANCINGS_PAYMENTS_READ**   # noqa: E501

    OpenAPI spec version: 2.1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import invoice-financings_2_1_0_yml
from invoice-financings_2_1_0_yml.models.enum_contract_product_type_invoice_financings import EnumContractProductTypeInvoiceFinancings  # noqa: E501
from invoice-financings_2_1_0_yml.rest import ApiException


class TestEnumContractProductTypeInvoiceFinancings(unittest.TestCase):
    """EnumContractProductTypeInvoiceFinancings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnumContractProductTypeInvoiceFinancings(self):
        """Test EnumContractProductTypeInvoiceFinancings"""
        # FIXME: construct object with mandatory attributes with example values
        # model = invoice-financings_2_1_0_yml.models.enum_contract_product_type_invoice_financings.EnumContractProductTypeInvoiceFinancings()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
