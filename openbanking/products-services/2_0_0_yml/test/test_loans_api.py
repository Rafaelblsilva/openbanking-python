# coding: utf-8

"""
    API's OpenData do Open Banking Brasil

    As API's descritas neste documento são referentes as API's da fase OpenData do Open Banking Brasil.  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import products-services_2_0_0_yml
from products-services_2_0_0_yml.api.loans_api import LoansApi  # noqa: E501
from products-services_2_0_0_yml.rest import ApiException


class TestLoansApi(unittest.TestCase):
    """LoansApi unit test stubs"""

    def setUp(self):
        self.api = LoansApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_business_loans(self):
        """Test case for get_business_loans

        Obtém dados sobre empréstimos pessoa jurídica  # noqa: E501
        """
        pass

    def test_get_personal_loans(self):
        """Test case for get_personal_loans

        Obtém dados sobre empréstimos pessoa natural  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
