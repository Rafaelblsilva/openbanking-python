# coding: utf-8

"""
    API Consents - Open Finance Brasil

    API que trata da criação, consulta e revogação de consentimentos para o Open Finance Brasil Dados cadastrais e transacionais - customer-data.   Não possui segregação entre pessoa natural e pessoa jurídica.      # Orientações importantes A API Consents trata dos consentimentos exclusivamente para a Dados cadastrais e transacionais do Open Finance Brasil. - As informações da instituição receptora não trafegam na API Consents – a autenticação da receptora se dá através do [DCR](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378307/Dynamic+Client+Registration).    - Na chamada para a criação do consentimento deve-se utilizar um token gerado via `client_credentials`. - Após o `POST` de criação do consentimento, o `STATUS` devolvido na resposta deverá ser `AWAITING_AUTHORISATION`. - O `STATUS` será alterado para `AUTHORISED` somente após autenticação e confirmação por parte do usuário na instituição transmissora dos dados. - Alteração obrigatória do status `AWAITING_AUTHORISATION` para `REVOKED` após 60 minutos. - Todas as datas trafegadas nesta API seguem o padrão da [RFC3339](https://tools.ietf.org/html/rfc3339) e formato \"zulu\". - A descrição do fluxo de consentimento encontra-se disponível no [Portal do desenvolvedor](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17369300/Dados+Cadastrais+e+Transacionais#Fluxo-b%C3%A1sico-de-consentimento). - O arquivo com o mapeamento completo entre `Roles`, `scopes` e `permissions` está disponibilizado no Portal do desenvolvedor, no mesmo item acima - descrição do fluxo de consentimento. - A receptora deve enviar obrigatoriamente, no pedido de criação de consentimento, todas as permissions dos agrupamentos de dados as quais ela deseja consentimento, conforme tabela abaixo:      ```   |----------------------|-------------------------------|----------------------------------------------------------|   | CATEGORIA DE DADOS   | AGRUPAMENTO                   | PERMISSIONS                                              |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Dados Cadastrais PF           | CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Informações complementares PF | CUSTOMERS_PERSONAL_ADITTIONALINFO_READ                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Dados Cadastrais PJ           | CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Informações complementares PJ | CUSTOMERS_BUSINESS_ADITTIONALINFO_READ                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Saldos                        | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_BALANCES_READ                                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Limites                       | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_OVERDRAFT_LIMITS_READ                           |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Extratos                      | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_TRANSACTIONS_READ                               |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Limites                       | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_LIMITS_READ                        |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Transações                    | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Faturas                       | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_READ                         |   |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ            |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Operações de Crédito | Dados do Contrato             | LOANS_READ                                               |   |                      |                               | LOANS_WARRANTIES_READ                                    |   |                      |                               | LOANS_SCHEDULED_INSTALMENTS_READ                         |   |                      |                               | LOANS_PAYMENTS_READ                                      |   |                      |                               | FINANCINGS_READ                                          |   |                      |                               | FINANCINGS_WARRANTIES_READ                               |   |                      |                               | FINANCINGS_SCHEDULED_INSTALMENTS_READ                    |   |                      |                               | FINANCINGS_PAYMENTS_READ                                 |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_READ                       |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_WARRANTIES_READ            |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_SCHEDULED_INSTALMENTS_READ |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_PAYMENTS_READ              |   |                      |                               | INVOICE_FINANCINGS_READ                                  |   |                      |                               | INVOICE_FINANCINGS_WARRANTIES_READ                       |   |                      |                               | INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ            |   |                      |                               | INVOICE_FINANCINGS_PAYMENTS_READ                         |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Investimento         | Dados da Operação             | BANK_FIXED_INCOMES_READ                                  |   |                      |                               | CREDIT_FIXED_INCOMES_READ                                |   |                      |                               | FUNDS_READ                                               |   |                      |                               | VARIABLE_INCOMES_READ                                    |   |                      |                               | TREASURE_TITLES_READ                                     |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   ``` - A instituição transmissora deve validar o preenchimento correto desses agrupamentos no momento da geração do consentimento. - Caso a instiuição receptora envie permissões divergentes ao agrupamento especificado na tabela, a transmissora deve rejeitar o pedido da receptora dando retorno HTTP Status Code 400. - A transmissora deve retornar, da lista de permissions requisitadas, apenas o subconjunto de permissions por ela suportada, removendo da lista as permissions de produtos não suportados e retornando HTTP Status Code 201. Caso não restem permissões funcionais, a instituição transmissora deve retornar o erro HTTP Code \"422 Unprocessable Entity\". - O endpoint `POST /consents/{consentId}/extends` é utilizado para renovação de consentimento ativo do cliente.  Ou seja, quando a receptora recebe pedido de renovação de consentimento com status ainda ativo para a transmissora, ela deve requisitar este endpoint. - Apenas consentimentos autorizados (status AUTHORISED) podem ser renovados pelo uso do endpoint `POST /consents/{consentId}/extends`. Essa renovação é feita exclusivamente via backende resulta em:   - Alteração do `expirationDateTime` do consentimento vigente;   - Persistência de informações para listar histórico de alterações que podem ser acessadas via endpoint `GET /consents/{consentId}/extends`. - A data de expiração `2300-01-01T00:00:00Z` (`expirationDateTime= 2300-01-01T00:00:00Z`) é a representação técnica de um consentimento com prazo de expiração indeterminado.  Ou seja, sempre que o cliente escolher prazo indeterminado para expiração de consentimento, a instituição receptora deve preencher `expirationDateTime= 2300-01-01T00:00:00Z` e assim informá-la para à instituição transmissora.  De igual forma, a instituição transmissora deve entender e representar consentimento com `expirationDateTime= 2300-01-01T00:00:00Z` como um consentimento com prazo de expiração indeterminado. - Os consentimentos em estado expirado ou cancelado não podem ser renovados sem redirecionamento.  Ou seja, não é possível utilizar o endpoint `POST /consents/{consentId}/extends` para consentimentos nesses estados (status REJECTED).  A transmissora deve retornar status de erro 422 (`ESTADO_CONSENTIMENTO_INVALIDO`) para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) deve ser possível por apenas um cliente logado.  Isso implica que qualquer usuário (`loggedUser`) com permissão para o consentimento associado deve ser capaz de finalizar o fluxo de renovação sem redirecionamento.   A transmissora deve retornar status de erro 422 (DEPENDE_MULTIPLA_ALCADA) para requisições que necessitam de múltipla alçada. - Para consentimentos Pessoa Natural apenas o loggedUser criador do consentimento consegue renovar sem redirecionamento (`POST /consents/{consentId}/extends`). A transmissora deve retornar status de erro 403 para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) deve ser possível para consentimento para o qual foi emitido um refresh token opaco.  Não deve ser possível quando o consentimento está vinculado a um refresh token do tipo JWT (com prazo não prorrogável).  A transmissora deve retornar status de erro 422 (`REFRESH_TOKEN_JWT`) para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) deve ocorrer apenas até o período de 12 meses após a data de requisição (`current_datetime<= expirationDateTime<= current_datetime+12meses`), ou com prazo de expiração indeterminado (`expirationDateTime=2300-01-01T00:00:00Z`).  A transmissora deve retornar status de erro 422 (`DATA_EXPIRACAO_INVALIDA`) para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) sempre aumenta a data de expiração final do consentimento em relação à data de expiração vigente.  Ou seja, um consentimento com prazo de expiração para 6 meses no futuro não pode ter sua data de expiração alterada para apenas 3 meses no futuro.  A transmissora deve retornar status de erro 422 (`DATA_EXPIRACAO_INVALIDA`) para requisições que não seguem essa definição. - A renovação de consentimento ativo do cliente somente poderá ser aceita pela transmissora para um usuário logado na receptora, identificado por seu documento (`loggedUser`; `businessEntity` quando aplicável) e permitido a partir de token de acesso (informado no cabeçalho `Authorization`) conseguido anteriormente durante a criação e confirmação do consentimento vigente.  A transmissora deve validar documento fornecido (`loggedUser`; `businessEntity` quando aplicável) e token de acesso para executar a renovação de consentimento. Caso a transmissora detecte que trata-se de acesso inválido por questões de segurança, é esperado status de erro 401 ou 403. - Após a renovação de consentimento (`POST /consents/{consentId}/extends`) a transmissora deve garantir que a data de expiração do refresh token opaco, ao qual o consentimento está associado, seja:   - sem expiração: refresh token permanece ativo, desde que o consentimento associado permaneça ativo (status AUTHORIZED);   - com expiração: desde que, no mínimo, a nova data de expiração do refreshtoken seja igual à nova data do consentimento. - A lista do payload de resposta do endpoint de histórico de renovações feitas (`GET /consents/{consentId}/extends`) deve ser entregue em ordem decrescente pela data de requisição (`data[].requestDateTime`).  Dessa forma, o primeiro item da lista apresentará a mesma data de expiração do consentimento vigente, pois foi a última renovação feita.   # noqa: E501

    OpenAPI spec version: 2.2.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "consents-2-2-0-yml"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="API Consents - Open Finance Brasil",
    author_email="gt-interfaces@openbankingbr.org",
    url="",
    keywords=["Swagger", "API Consents - Open Finance Brasil"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    API que trata da criação, consulta e revogação de consentimentos para o Open Finance Brasil Dados cadastrais e transacionais - customer-data.   Não possui segregação entre pessoa natural e pessoa jurídica.      # Orientações importantes A API Consents trata dos consentimentos exclusivamente para a Dados cadastrais e transacionais do Open Finance Brasil. - As informações da instituição receptora não trafegam na API Consents – a autenticação da receptora se dá através do [DCR](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378307/Dynamic+Client+Registration).    - Na chamada para a criação do consentimento deve-se utilizar um token gerado via &#x60;client_credentials&#x60;. - Após o &#x60;POST&#x60; de criação do consentimento, o &#x60;STATUS&#x60; devolvido na resposta deverá ser &#x60;AWAITING_AUTHORISATION&#x60;. - O &#x60;STATUS&#x60; será alterado para &#x60;AUTHORISED&#x60; somente após autenticação e confirmação por parte do usuário na instituição transmissora dos dados. - Alteração obrigatória do status &#x60;AWAITING_AUTHORISATION&#x60; para &#x60;REVOKED&#x60; após 60 minutos. - Todas as datas trafegadas nesta API seguem o padrão da [RFC3339](https://tools.ietf.org/html/rfc3339) e formato \&quot;zulu\&quot;. - A descrição do fluxo de consentimento encontra-se disponível no [Portal do desenvolvedor](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17369300/Dados+Cadastrais+e+Transacionais#Fluxo-b%C3%A1sico-de-consentimento). - O arquivo com o mapeamento completo entre &#x60;Roles&#x60;, &#x60;scopes&#x60; e &#x60;permissions&#x60; está disponibilizado no Portal do desenvolvedor, no mesmo item acima - descrição do fluxo de consentimento. - A receptora deve enviar obrigatoriamente, no pedido de criação de consentimento, todas as permissions dos agrupamentos de dados as quais ela deseja consentimento, conforme tabela abaixo:      &#x60;&#x60;&#x60;   |----------------------|-------------------------------|----------------------------------------------------------|   | CATEGORIA DE DADOS   | AGRUPAMENTO                   | PERMISSIONS                                              |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Dados Cadastrais PF           | CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Informações complementares PF | CUSTOMERS_PERSONAL_ADITTIONALINFO_READ                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Dados Cadastrais PJ           | CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cadastro             | Informações complementares PJ | CUSTOMERS_BUSINESS_ADITTIONALINFO_READ                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Saldos                        | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_BALANCES_READ                                   |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Limites                       | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_OVERDRAFT_LIMITS_READ                           |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Contas               | Extratos                      | ACCOUNTS_READ                                            |   |                      |                               | ACCOUNTS_TRANSACTIONS_READ                               |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Limites                       | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_LIMITS_READ                        |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Transações                    | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ                  |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Cartão de Crédito    | Faturas                       | CREDIT_CARDS_ACCOUNTS_READ                               |   |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_READ                         |   |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ            |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Operações de Crédito | Dados do Contrato             | LOANS_READ                                               |   |                      |                               | LOANS_WARRANTIES_READ                                    |   |                      |                               | LOANS_SCHEDULED_INSTALMENTS_READ                         |   |                      |                               | LOANS_PAYMENTS_READ                                      |   |                      |                               | FINANCINGS_READ                                          |   |                      |                               | FINANCINGS_WARRANTIES_READ                               |   |                      |                               | FINANCINGS_SCHEDULED_INSTALMENTS_READ                    |   |                      |                               | FINANCINGS_PAYMENTS_READ                                 |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_READ                       |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_WARRANTIES_READ            |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_SCHEDULED_INSTALMENTS_READ |   |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_PAYMENTS_READ              |   |                      |                               | INVOICE_FINANCINGS_READ                                  |   |                      |                               | INVOICE_FINANCINGS_WARRANTIES_READ                       |   |                      |                               | INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ            |   |                      |                               | INVOICE_FINANCINGS_PAYMENTS_READ                         |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   | Investimento         | Dados da Operação             | BANK_FIXED_INCOMES_READ                                  |   |                      |                               | CREDIT_FIXED_INCOMES_READ                                |   |                      |                               | FUNDS_READ                                               |   |                      |                               | VARIABLE_INCOMES_READ                                    |   |                      |                               | TREASURE_TITLES_READ                                     |   |                      |                               | RESOURCES_READ                                           |   |----------------------|-------------------------------|----------------------------------------------------------|   &#x60;&#x60;&#x60; - A instituição transmissora deve validar o preenchimento correto desses agrupamentos no momento da geração do consentimento. - Caso a instiuição receptora envie permissões divergentes ao agrupamento especificado na tabela, a transmissora deve rejeitar o pedido da receptora dando retorno HTTP Status Code 400. - A transmissora deve retornar, da lista de permissions requisitadas, apenas o subconjunto de permissions por ela suportada, removendo da lista as permissions de produtos não suportados e retornando HTTP Status Code 201. Caso não restem permissões funcionais, a instituição transmissora deve retornar o erro HTTP Code \&quot;422 Unprocessable Entity\&quot;. - O endpoint &#x60;POST /consents/{consentId}/extends&#x60; é utilizado para renovação de consentimento ativo do cliente.  Ou seja, quando a receptora recebe pedido de renovação de consentimento com status ainda ativo para a transmissora, ela deve requisitar este endpoint. - Apenas consentimentos autorizados (status AUTHORISED) podem ser renovados pelo uso do endpoint &#x60;POST /consents/{consentId}/extends&#x60;. Essa renovação é feita exclusivamente via backende resulta em:   - Alteração do &#x60;expirationDateTime&#x60; do consentimento vigente;   - Persistência de informações para listar histórico de alterações que podem ser acessadas via endpoint &#x60;GET /consents/{consentId}/extends&#x60;. - A data de expiração &#x60;2300-01-01T00:00:00Z&#x60; (&#x60;expirationDateTime&#x3D; 2300-01-01T00:00:00Z&#x60;) é a representação técnica de um consentimento com prazo de expiração indeterminado.  Ou seja, sempre que o cliente escolher prazo indeterminado para expiração de consentimento, a instituição receptora deve preencher &#x60;expirationDateTime&#x3D; 2300-01-01T00:00:00Z&#x60; e assim informá-la para à instituição transmissora.  De igual forma, a instituição transmissora deve entender e representar consentimento com &#x60;expirationDateTime&#x3D; 2300-01-01T00:00:00Z&#x60; como um consentimento com prazo de expiração indeterminado. - Os consentimentos em estado expirado ou cancelado não podem ser renovados sem redirecionamento.  Ou seja, não é possível utilizar o endpoint &#x60;POST /consents/{consentId}/extends&#x60; para consentimentos nesses estados (status REJECTED).  A transmissora deve retornar status de erro 422 (&#x60;ESTADO_CONSENTIMENTO_INVALIDO&#x60;) para requisições que não seguem essa definição. - A renovação de consentimento (&#x60;POST /consents/{consentId}/extends&#x60;) deve ser possível por apenas um cliente logado.  Isso implica que qualquer usuário (&#x60;loggedUser&#x60;) com permissão para o consentimento associado deve ser capaz de finalizar o fluxo de renovação sem redirecionamento.   A transmissora deve retornar status de erro 422 (DEPENDE_MULTIPLA_ALCADA) para requisições que necessitam de múltipla alçada. - Para consentimentos Pessoa Natural apenas o loggedUser criador do consentimento consegue renovar sem redirecionamento (&#x60;POST /consents/{consentId}/extends&#x60;). A transmissora deve retornar status de erro 403 para requisições que não seguem essa definição. - A renovação de consentimento (&#x60;POST /consents/{consentId}/extends&#x60;) deve ser possível para consentimento para o qual foi emitido um refresh token opaco.  Não deve ser possível quando o consentimento está vinculado a um refresh token do tipo JWT (com prazo não prorrogável).  A transmissora deve retornar status de erro 422 (&#x60;REFRESH_TOKEN_JWT&#x60;) para requisições que não seguem essa definição. - A renovação de consentimento (&#x60;POST /consents/{consentId}/extends&#x60;) deve ocorrer apenas até o período de 12 meses após a data de requisição (&#x60;current_datetime&lt;&#x3D; expirationDateTime&lt;&#x3D; current_datetime+12meses&#x60;), ou com prazo de expiração indeterminado (&#x60;expirationDateTime&#x3D;2300-01-01T00:00:00Z&#x60;).  A transmissora deve retornar status de erro 422 (&#x60;DATA_EXPIRACAO_INVALIDA&#x60;) para requisições que não seguem essa definição. - A renovação de consentimento (&#x60;POST /consents/{consentId}/extends&#x60;) sempre aumenta a data de expiração final do consentimento em relação à data de expiração vigente.  Ou seja, um consentimento com prazo de expiração para 6 meses no futuro não pode ter sua data de expiração alterada para apenas 3 meses no futuro.  A transmissora deve retornar status de erro 422 (&#x60;DATA_EXPIRACAO_INVALIDA&#x60;) para requisições que não seguem essa definição. - A renovação de consentimento ativo do cliente somente poderá ser aceita pela transmissora para um usuário logado na receptora, identificado por seu documento (&#x60;loggedUser&#x60;; &#x60;businessEntity&#x60; quando aplicável) e permitido a partir de token de acesso (informado no cabeçalho &#x60;Authorization&#x60;) conseguido anteriormente durante a criação e confirmação do consentimento vigente.  A transmissora deve validar documento fornecido (&#x60;loggedUser&#x60;; &#x60;businessEntity&#x60; quando aplicável) e token de acesso para executar a renovação de consentimento. Caso a transmissora detecte que trata-se de acesso inválido por questões de segurança, é esperado status de erro 401 ou 403. - Após a renovação de consentimento (&#x60;POST /consents/{consentId}/extends&#x60;) a transmissora deve garantir que a data de expiração do refresh token opaco, ao qual o consentimento está associado, seja:   - sem expiração: refresh token permanece ativo, desde que o consentimento associado permaneça ativo (status AUTHORIZED);   - com expiração: desde que, no mínimo, a nova data de expiração do refreshtoken seja igual à nova data do consentimento. - A lista do payload de resposta do endpoint de histórico de renovações feitas (&#x60;GET /consents/{consentId}/extends&#x60;) deve ser entregue em ordem decrescente pela data de requisição (&#x60;data[].requestDateTime&#x60;).  Dessa forma, o primeiro item da lista apresentará a mesma data de expiração do consentimento vigente, pois foi a última renovação feita.   # noqa: E501
    """
)
