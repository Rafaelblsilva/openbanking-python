# coding: utf-8

# flake8: noqa
"""
    API Consents - Open Finance Brasil

    API que trata da criação, consulta e revogação de consentimentos para o Open Finance Brasil Dados cadastrais e transacionais - customer-data.   Não possui segregação entre pessoa natural e pessoa jurídica.      # Orientações importantes A API Consents trata dos consentimentos exclusivamente para a Dados cadastrais e transacionais do Open Finance Brasil. - A API consents é composta de endpoints que permitem:   - Pedido de criação do consentimento pela receptora: `POST /consents`   - Devolução do pedido de criação pela transmissora: `GET /consents/{consentId}`   - Pedido de renovação de consentimento do cliente pela receptora: `POST /consents/{consentId}/extends`   - Devolução de lista com histórico de renovações efetuadas: `GET /consents/{consentId}/extensions`   - Pedido de revogação do consentimento: `DELETE /consents/{consentId}` - Recomenda-se fortemente a leitura da seção “Orientações – Consentimento” para maiores detalhes, regras e restrições referente aos endpoints da API Consents - As informações da instituição receptora não trafegam na API Consents – a autenticação da receptora se dá através do [DCR](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17378307/Dynamic+Client+Registration). - Na chamada para a criação, consulta e revogação do consentimento deve-se utilizar um token gerado via `client_credentials`. Na chamada para renovação do consentimento deve-se utilizar um token gerado via `authorization_code`. - Na chamada para a criação do consentimento deve-se utilizar um token gerado via `client_credentials`. - Após o `POST` de criação do consentimento, o `STATUS` devolvido na resposta deverá ser `AWAITING_AUTHORISATION`. - O `STATUS` será alterado para `AUTHORISED` somente após autenticação e confirmação por parte do usuário na instituição transmissora dos dados. - Alteração obrigatória do status `AWAITING_AUTHORISATION` para `REJECTED` após 60 minutos. - Todas as datas trafegadas nesta API seguem o padrão da [RFC3339](https://tools.ietf.org/html/rfc3339) e formato \"zulu\". - A descrição do fluxo de consentimento encontra-se disponível no [Portal do desenvolvedor](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/17369300/Dados+Cadastrais+e+Transacionais#Fluxo-b%C3%A1sico-de-consentimento). - O arquivo com o mapeamento completo entre `Roles`, `scopes` e `permissions` está disponibilizado no Portal do desenvolvedor, no mesmo item acima - descrição do fluxo de consentimento. - Pedidos de renovação de consentimento somente podem alterar a data de validade (conforme as regras definidas em Orientações – Consentimento) e a finalidade do consentimento, e aplica-se somente a consentimentos ativos ( status AUTHORIZED) - No caso de criação ou renovação de consentimentos com prazo indeterminado, a receptora não deve enviar o atributo expirationDateTime. Para prazos determinados o campo deve ser enviado. - A receptora deve enviar obrigatoriamente, no pedido de criação de consentimento, todas as permissions dos agrupamentos de dados as quais ela deseja consentimento, conforme tabela abaixo:    ```   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   | ROLE  | CATEGORIA DE DADOS   | AGRUPAMENTO                   | PERMISSIONS                                              | SCOPE OAUTH 2.0               |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CUSTOMERS_PERSONAL_IDENTIFICATIONS_READ                  | customers                     |   |       | Cadastro             | Dados Cadastrais PF           |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           | resources                     |   |       |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CUSTOMERS_PERSONAL_ADITTIONALINFO_READ                   | customers                     |   |       | Cadastro             | Informações complementares PF |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           | resources                     |   | DADOS |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CUSTOMERS_BUSINESS_IDENTIFICATIONS_READ                  | customers                     |   |       | Cadastro             | Dados Cadastrais PJ           |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           | resources                     |   |       |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CUSTOMERS_BUSINESS_ADITTIONALINFO_READ                   | customers                     |   |       | Cadastro             | Informações complementares PJ |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           | resources                     |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | ACCOUNTS_READ                                            |                               |   |       |                      |                               |----------------------------------------------------------| accounts                      |   |       | Contas               | Saldos                        | ACCOUNTS_BALANCES_READ                                   |                               |   |       |                      |                               |----------------------------------------------------------| resources                     |   |       |                      |                               | RESOURCES_READ                                           |                               |   |       |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | ACCOUNTS_READ                                            |                               |   |       |                      |                               |----------------------------------------------------------| accounts                      |   | DADOS | Contas               | Limites                       | ACCOUNTS_OVERDRAFT_LIMITS_READ                           |                               |   |       |                      |                               |----------------------------------------------------------| resources                     |   |       |                      |                               | RESOURCES_READ                                           |                               |   |       |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | ACCOUNTS_READ                                            |                               |   |       |                      |                               |----------------------------------------------------------| accounts                      |   |       | Contas               | Extratos                      | ACCOUNTS_TRANSACTIONS_READ                               |                               |   |       |                      |                               |----------------------------------------------------------| resources                     |   |       |                      |                               | RESOURCES_READ                                           |                               |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CREDIT_CARDS_ACCOUNTS_READ                               |                               |   |       |                      |                               |----------------------------------------------------------| credit-cards-accounts         |   |       | Cartão de Crédito    | Limites                       | CREDIT_CARDS_ACCOUNTS_LIMITS_READ                        |                               |   |       |                      |                               |----------------------------------------------------------| resources                     |   |       |                      |                               | RESOURCES_READ                                           |                               |   |       |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CREDIT_CARDS_ACCOUNTS_READ                               |                               |   |       |                      |                               |----------------------------------------------------------| credit-cards-accounts         |   |       | Cartão de Crédito    | Transações                    | CREDIT_CARDS_ACCOUNTS_TRANSACTIONS_READ                  |                               |   | DADOS |                      |                               |----------------------------------------------------------| resources                     |   |       |                      |                               | RESOURCES_READ                                           |                               |   |       |----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | CREDIT_CARDS_ACCOUNTS_READ                               |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_READ                         | credit-cards-accounts         |   |       | Cartão de Crédito    | Faturas                       |----------------------------------------------------------|                               |   |       |                      |                               | CREDIT_CARDS_ACCOUNTS_BILLS_TRANSACTIONS_READ            | resources                     |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           |                               |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | LOANS_READ                                               |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | LOANS_WARRANTIES_READ                                    |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | LOANS_SCHEDULED_INSTALMENTS_READ                         |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | LOANS_PAYMENTS_READ                                      |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | FINANCINGS_READ                                          |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | FINANCINGS_WARRANTIES_READ                               |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | FINANCINGS_SCHEDULED_INSTALMENTS_READ                    | loans                         |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | FINANCINGS_PAYMENTS_READ                                 | financings                    |   |       |                      |                               |----------------------------------------------------------|                               |   | DADOS | Operações de Crédito | Dados do Contrato             | UNARRANGED_ACCOUNTS_OVERDRAFT_READ                       | unarranged-accounts-overdraft |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_WARRANTIES_READ            | invoice-financings            |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_SCHEDULED_INSTALMENTS_READ | resources                     |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | UNARRANGED_ACCOUNTS_OVERDRAFT_PAYMENTS_READ              |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | INVOICE_FINANCINGS_READ                                  |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | INVOICE_FINANCINGS_WARRANTIES_READ                       |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | INVOICE_FINANCINGS_SCHEDULED_INSTALMENTS_READ            |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | INVOICE_FINANCINGS_PAYMENTS_READ                         |                               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           |                               |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | BANK_FIXED_INCOMES_READ                                  | bank-fixed-incomes            |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | CREDIT_FIXED_INCOMES_READ                                | credit-fixed-incomes          |   |       |                      |                               |----------------------------------------------------------|                               |   | DADOS | Investimento         | Dados da Operação             | FUNDS_READ                                               | variable-incomes              |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | VARIABLE_INCOMES_READ                                    | treasure-titles               |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | TREASURE_TITLES_READ                                     | funds                         |   |       |                      |                               |----------------------------------------------------------|                               |   |       |                      |                               | RESOURCES_READ                                           | resources                     |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|   |       |                      |                               | EXCHANGES_READ                                           |                               |   | DADOS | Câmbio               | Dados da Operação             |----------------------------------------------------------| exchanges                     |   |       |                      |                               | RESOURCES_READ                                           |                               |   |-------|----------------------|-------------------------------|----------------------------------------------------------|-------------------------------|      ``` - A instituição transmissora deve validar o preenchimento correto desses agrupamentos no momento da geração do consentimento. - Caso a instiuição receptora envie permissões divergentes ao agrupamento especificado na tabela, a transmissora deve rejeitar o pedido da receptora dando retorno HTTP Status Code 400. - A transmissora deve retornar, da lista de permissions requisitadas, apenas o subconjunto de permissions por ela suportada, removendo da lista as permissions de produtos não suportados e retornando HTTP Status Code 201. A única exceção a este comportamento são os casos de produtos agrupados, como Operações de crédito e Investimentos, para os quais todas as permissões do agrupamento devem ser mantidas. Caso não restem permissões funcionais, a instituição transmissora deve retornar o erro HTTP Code \"422 Unprocessable Entity\". - A renovação de consentimento não pode ser efetuada em situações determinadas.  É esperado status 401 ou 403 para situações em que o erro for tratado na camada de segurança.  Para erros tratados em camada de negócio, a transmissora deve retornar 422 com as mensagens especificadas na documentação caso haja pedido de renovação de consentimentos nas situações abaixo:   - Não deve ser possível quando o consentimento foi criado demandando aprovações por múltiplas alçadas   - Consentimentos em estado expirado ou cancelado não podem ser renovados sem redirecionamento   - Não será permitida uma nova data de expiração de consentimento superior a 12 meses da data de requisição, exceto quando a alteração for para prazo indeterminado - Caso o método DELETE seja chamado para um consentimento que já se encontra no STATUS `REJECTED` deve se retornar o STATUS CODE 422. - O endpoint `POST /consents/{consentId}/extends` é utilizado para renovação de consentimento ativo do cliente.  Ou seja, quando a receptora recebe pedido de renovação de consentimento com status ainda ativo para a transmissora, ela deve requisitar este endpoint. - Apenas consentimentos autorizados (status AUTHORISED) podem ser renovados pelo uso do endpoint `POST /consents/{consentId}/extends`. Essa renovação é feita exclusivamente via backende resulta em:   - Alteração do `expirationDateTime` do consentimento vigente;   - Persistência de informações para listar histórico de alterações que podem ser acessadas via endpoint `GET /consents/{consentId}/extensions`. - A data de expiração `2300-01-01T00:00:00Z` (`expirationDateTime= 2300-01-01T00:00:00Z`) é a representação técnica de um consentimento com prazo de expiração indeterminado.  Ou seja, sempre que o cliente escolher prazo indeterminado para expiração de consentimento, a instituição receptora deve preencher `expirationDateTime= 2300-01-01T00:00:00Z` e assim informá-la para à instituição transmissora.  De igual forma, a instituição transmissora deve entender e representar consentimento com `expirationDateTime= 2300-01-01T00:00:00Z` como um consentimento com prazo de expiração indeterminado. - Os consentimentos em estado expirado ou cancelado não podem ser renovados sem redirecionamento.  Ou seja, não é possível utilizar o endpoint `POST /consents/{consentId}/extends` para consentimentos nesses estados (status REJECTED).  A transmissora deve retornar status de erro 422 (`ESTADO_CONSENTIMENTO_INVALIDO`) para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) deve ser possível por apenas um cliente logado.  Isso implica que qualquer usuário (`loggedUser`) com permissão para o consentimento associado deve ser capaz de finalizar o fluxo de renovação sem redirecionamento.   A transmissora deve retornar status de erro 422 (DEPENDE_MULTIPLA_ALCADA) para requisições que necessitam de múltipla alçada. - Para consentimentos Pessoa Natural apenas o loggedUser criador do consentimento consegue renovar sem redirecionamento (`POST /consents/{consentId}/extends`). A transmissora deve retornar status de erro 403 para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) deve ocorrer apenas até o período de 12 meses após a data de requisição (`current_datetime<= expirationDateTime<= current_datetime+12meses`), ou com prazo de expiração indeterminado (`expirationDateTime=2300-01-01T00:00:00Z`).  A transmissora deve retornar status de erro 422 (`DATA_EXPIRACAO_INVALIDA`) para requisições que não seguem essa definição. - A renovação de consentimento (`POST /consents/{consentId}/extends`) sempre aumenta a data de expiração final do consentimento em relação à data de expiração vigente.  Ou seja, um consentimento com prazo de expiração para 6 meses no futuro não pode ter sua data de expiração alterada para apenas 3 meses no futuro.  A transmissora deve retornar status de erro 422 (`DATA_EXPIRACAO_INVALIDA`) para requisições que não seguem essa definição. - A renovação de consentimento ativo do cliente somente poderá ser aceita pela transmissora para um usuário logado na receptora, identificado por seu documento (`loggedUser`; `businessEntity` quando aplicável) e permitido a partir de token de acesso (informado no cabeçalho `Authorization`) conseguido anteriormente durante a criação e confirmação do consentimento vigente.  A transmissora deve validar documento fornecido (`loggedUser`; `businessEntity` quando aplicável) e token de acesso para executar a renovação de consentimento. Caso a transmissora detecte que trata-se de acesso inválido por questões de segurança, é esperado status de erro 401 ou 403. - Após a renovação de consentimento (`POST /consents/{consentId}/extends`) a transmissora deve garantir que a data de expiração do refresh token opaco, ao qual o consentimento está associado, seja:   - sem expiração: refresh token permanece ativo, desde que o consentimento associado permaneça ativo (status AUTHORIZED);   - com expiração: desde que, no mínimo, a nova data de expiração do refreshtoken seja igual à nova data do consentimento. - A lista do payload de resposta do endpoint de histórico de renovações feitas (`GET /consents/{consentId}/extensions`) deve ser entregue em ordem decrescente pela data de requisição (`data[].requestDateTime`).  Dessa forma, o primeiro item da lista apresentará a mesma data de expiração do consentimento vigente, pois foi a última renovação feita.   # noqa: E501

    OpenAPI spec version: 3.0.0-beta.1
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from consents_3_0_0-beta_1_yml.models.business_entity import BusinessEntity
from consents_3_0_0-beta_1_yml.models.business_entity_document import BusinessEntityDocument
from consents_3_0_0-beta_1_yml.models.business_entity_document_extensions import BusinessEntityDocumentExtensions
from consents_3_0_0-beta_1_yml.models.business_entity_extensions import BusinessEntityExtensions
from consents_3_0_0-beta_1_yml.models.create_consent import CreateConsent
from consents_3_0_0-beta_1_yml.models.create_consent_data import CreateConsentData
from consents_3_0_0-beta_1_yml.models.create_consent_extensions import CreateConsentExtensions
from consents_3_0_0-beta_1_yml.models.create_consent_extensions_data import CreateConsentExtensionsData
from consents_3_0_0-beta_1_yml.models.enum_reason_code import EnumReasonCode
from consents_3_0_0-beta_1_yml.models.enum_rejected_by import EnumRejectedBy
from consents_3_0_0-beta_1_yml.models.inline_response529 import InlineResponse529
from consents_3_0_0-beta_1_yml.models.inline_response529_errors import InlineResponse529Errors
from consents_3_0_0-beta_1_yml.models.inline_response529_meta import InlineResponse529Meta
from consents_3_0_0-beta_1_yml.models.links import Links
from consents_3_0_0-beta_1_yml.models.logged_user import LoggedUser
from consents_3_0_0-beta_1_yml.models.logged_user_document import LoggedUserDocument
from consents_3_0_0-beta_1_yml.models.logged_user_document_extensions import LoggedUserDocumentExtensions
from consents_3_0_0-beta_1_yml.models.logged_user_extensions import LoggedUserExtensions
from consents_3_0_0-beta_1_yml.models.meta import Meta
from consents_3_0_0-beta_1_yml.models.meta_error import MetaError
from consents_3_0_0-beta_1_yml.models.model422_response_error_create_consent import Model422ResponseErrorCreateConsent
from consents_3_0_0-beta_1_yml.models.model422_response_error_create_consent_errors import Model422ResponseErrorCreateConsentErrors
from consents_3_0_0-beta_1_yml.models.rejected_reason import RejectedReason
from consents_3_0_0-beta_1_yml.models.response_consent import ResponseConsent
from consents_3_0_0-beta_1_yml.models.response_consent_data import ResponseConsentData
from consents_3_0_0-beta_1_yml.models.response_consent_extensions import ResponseConsentExtensions
from consents_3_0_0-beta_1_yml.models.response_consent_extensions_data import ResponseConsentExtensionsData
from consents_3_0_0-beta_1_yml.models.response_consent_read import ResponseConsentRead
from consents_3_0_0-beta_1_yml.models.response_consent_read_data import ResponseConsentReadData
from consents_3_0_0-beta_1_yml.models.response_consent_read_data_rejection import ResponseConsentReadDataRejection
from consents_3_0_0-beta_1_yml.models.response_consent_read_extensions import ResponseConsentReadExtensions
from consents_3_0_0-beta_1_yml.models.response_consent_read_extensions_data import ResponseConsentReadExtensionsData
from consents_3_0_0-beta_1_yml.models.response_error import ResponseError
from consents_3_0_0-beta_1_yml.models.response_error_errors import ResponseErrorErrors
