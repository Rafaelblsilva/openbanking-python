# coding: utf-8

"""
    API Customers - Open Banking Brasil

    API de dados cadastrais de clientes do Open Banking Brasil – Fase 2. API que retorna os dados cadastrais de clientes e de seus representantes, incluindo dados de identificação, de qualificação financeira, informações sobre representantes cadastrados e sobre o relacionamento financeiro do cliente com a instituição transmissora dos dados.\\ Possui segregação entre pessoa natural e pessoa jurídica.\\ Requer consentimento do cliente para todos os `endpoints`.  # Orientações A `Role`  do diretório de participantes relacionada à presente API é a `DADOS`.\\ Para todos os `endpoints` desta API é previsto o envio de um `token` através do header `Authorization`.\\ Este token deverá estar relacionado ao consentimento (`consentId`) mantido na instituição transmissora dos dados, o qual permitirá a pesquisa e retorno, na API em questão, dos  dados relacionados ao `consentId` específico relacionado.\\ Os dados serão devolvidos na consulta desde que o `consentId` relacionado corresponda a um consentimento válido e com o status `AUTHORISED`.\\ É também necessário que o recurso em questão (conta, contrato, etc) esteja disponível na instituição transmissora (ou seja, sem boqueios de qualquer natureza e com todas as autorizações/consentimentos já autorizados).\\ Além disso as `permissions` necessárias deverão ter sido solicitadas quando da criação do consentimento relacionado (`consentId`).\\ Relacionamos a seguir as `permissions` necessárias para a consulta de dados em cada `endpoint` da presente API.  ## Permissions necessárias para a API Customers  Para cada um dos paths desta API, além dos escopos (`scopes`) indicados existem `permissions` que deverão ser observadas:  ### `/personal/identifications`   - permissions:     - GET: **CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ** ### `/personal/qualifications`   - permissions: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/personal/financial-relations`   - permissions:     - GET: **CUSTOMERS_PERSONAL_ADITTIONALINFO_READ** ### `/business/identifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ** ### `/business/qualifications`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ** ### `/business/financial-relations`   - permissions:     - GET: **CUSTOMERS_BUSINESS_ADITTIONALINFO_READ**   # noqa: E501

    OpenAPI spec version: 1.0.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import customers_1_0_1_yml
from customers_1_0_1_yml.api.customers_api import CustomersApi  # noqa: E501
from customers_1_0_1_yml.rest import ApiException


class TestCustomersApi(unittest.TestCase):
    """CustomersApi unit test stubs"""

    def setUp(self):
        self.api = CustomersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_customers_get_business_financial_relations(self):
        """Test case for customers_get_business_financial_relations

        Obtém os registros de relacionamentos com a instituição financeira e de representantes da pessoa jurídica.  # noqa: E501
        """
        pass

    def test_customers_get_business_identifications(self):
        """Test case for customers_get_business_identifications

        Obtém os registros de identificação da pessoa jurídica.  # noqa: E501
        """
        pass

    def test_customers_get_business_qualifications(self):
        """Test case for customers_get_business_qualifications

        Obtém os registros de qualificação da pessoa jurídica.  # noqa: E501
        """
        pass

    def test_customers_get_personal_financial_relations(self):
        """Test case for customers_get_personal_financial_relations

        Obtém os registros de relacionamentos com a instituição financeira e de representantes da pessoa natural.  # noqa: E501
        """
        pass

    def test_customers_get_personal_identifications(self):
        """Test case for customers_get_personal_identifications

        Obtém os registros de identificação da pessoa natural.  # noqa: E501
        """
        pass

    def test_customers_get_personal_qualifications(self):
        """Test case for customers_get_personal_qualifications

        Obtém os registros de qualificação da pessoa natural.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
