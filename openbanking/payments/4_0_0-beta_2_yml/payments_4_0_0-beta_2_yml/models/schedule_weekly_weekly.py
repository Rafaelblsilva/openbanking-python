# coding: utf-8

"""
    API Payment Initiation - Open Finance Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Finance Brasil. Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API: - `CONTA`, referente às instituições detentoras de conta participantes do Open Finance Brasil; - `PAGTO`, referente às instituições iniciadoras de pagamento participantes do Open Finance Brasil.  Os tokens utilizados para consumo nos endpoints de consentimentos devem possuir o scope `payments` e os `endpoints` de pagamentos devem possuir os `scopes`, `openid` e `payments`.  Esta API não requer a implementação de `permissions` para sua utilização. Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Regras do arranjo Pix A implementação e o uso da API de Pagamentos Pix devem seguir as regras do arranjo Pix do Banco Central, que podem ser encontradas no link abaixo:    [https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix](https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix)  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:  - Certificados exigidos para assinatura de mensagens: [[EN] Padrão de Certificados Open Finance Brasil 2.1](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/82084176/EN+Padr+o+de+Certificados+Open+Finance+Brasil+2.1%20%E2%80%8B)  - Como assinar o payload JWS: [Como Assinar o Payload](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/180061175/Como+Assinar+o+Payload+-+v3.0.0+-+Pagamentos)  ## Controle de acesso  Os endpoints de consulta e cancelamento devem suportar somente acesso a partir de access_token emitido por meio de um grant_type do tipo client_credentials.  Para a criação do consentimento deve-se utilizar client_credentials e para criação de pagamentos deve-se utilizar authorization_code.  ## Aprovações de múltipla alçada  Para o caso de Pix imediato, todas as aprovações necessárias devem ser realizadas nos canais da detentora até às 23:59 (horário de Brasília) da data de solicitação do pagamento. Já para o caso de Pix agendado, todas as aprovações devem ser realizadas até a data/hora limite suportada pela detentora.  ## Validações **Validações** (*após o processo de DCR e obtenção de token client credential*– não escopo dessa documentação)   Durante a jornada de iniciação de pagamento, diferentes validações são necessárias pela instituição detentora  de conta e devem ocorrer conforme a seguir:   1. Na criação do consentimento (*POST /consents*);  2. Na criação do pagamento - Síncrono (*POST /payments*);  3. Validações na consulta do pagamento (*GET /pix/payments/{paymentId}*); 4. Demais validações executadas durante o processamento assíncrono do pagamento pela detentora, poderão ser consultados pela iniciadora através do endpoint (*GET /pix/payments/{paymentId}*) previstos com retorno HTTP Code 200 - OK com status RJCT (Rejected) e rejectionReason; 5. Demais validações executadas durante o processamento assíncrono do consentimento pela detentora poderão ser consultados pela iniciadora através do endpoint (*GET /consents/{consentId}*) previstos com retorno HTTP Code 200 – OK com status REJECTED e rejectionReason  **Os tipos de validações dispostas abaixo não determinam a ordem em que as instituições devem implementá-las**  1. **Validações na criação do consentimento (_POST /consents_)**     1.1 **Orientações Iniciais**       &ensp;1.1.1 Não devem ser retornadas na resposta deste endpointinformações associadas ao usuário/cliente (ex.  insuficiência de saldo, conta inexistente/bloqueada).       &ensp;1.1.2 Não devem ser executadas validações no DICT (Diretório de Identificadores de Contas Transacionais do Pix), a partir dos dados compartilhados nesse *endpoint*. Tais  validações podem ocorrer somente na criação do pagamento;        &ensp;1.1.3 Não devem ser realizadas validações de informações sobre o usuário/cliente durante a criação do consentimento.   1.2 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;1.2.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;1.2.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;1.2.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;1.2.4 Validação de Claims (exceto data);         &emsp;1.2.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;1.2.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     1.3 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**        &ensp;1.3.1 **Sintáticos**         &emsp;1.3.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios são informados (PARAMETRO_NAO_INFORMADO);         &emsp;1.3.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;1.3.2 **Semânticos**         &emsp;1.3.2.1 Forma de pagamento: Valida se a forma de pagamento é suportada pela detentora (FORMA_PAGAMENTO_INVALIDA) **Obs. No detalhe do erro, a variável “modalidade” deve ser comunicada pela detentora da forma mais clara possível - ex. modalidade de pagamento não suportada (_localInstrument_ - QRES) ou tipo de arranjo pagamento não suportado (_type_ – ex. Pix / TED – previsto para inclusão futura);**         &emsp;1.3.2.2 Data de pagamento: Valida se a data de pagamento enviada é válida para a forma de pagamento selecionada (DATA_PAGAMENTO_INVALIDA);         &emsp;1.3.2.3 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;1.3.2.4 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;1.3.2.5 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA).    2. **Validações na criação do pagamento - Síncrono (_POST /payments_)**     2.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;2.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;2.1.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;2.1.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;2.1.4 Validação de Claims (exceto data);         &emsp;2.1.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;2.1.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     2.2 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**       &ensp;2.2.1 **Sintáticos**         &emsp;2.3.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios são informados (PARAMETRO_NAO_INFORMADO);         &emsp;2.3.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;2.2.2 **Semânticos**         &emsp;2.2.2.1 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);         &emsp;2.2.2.2 Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora (VALOR_ACIMA_LIMITE);         &emsp;2.2.2.3 Valor informado (QR Code): Valida se valor enviado é válido para o QR Code informado (VALOR_INVALIDO);         &emsp;2.2.2.4 Cobrança inválida: Valida expiração, vencimento e status (COBRANCA_INVALIDA);         &emsp;2.2.2.5 Status Consentimento: Valida se o consentimento encontra-se em um dos estados finais “CONSUMED” ou “REJECTED\" (CONSENTIMENTO_INVALIDO);         &emsp;2.2.2.6 Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO)         &emsp;2.2.2.7 Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa (ex. chave Pix inválida, QRCode inválido, conta bloqueada);         &emsp;2.2.2.8 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;2.2.2.9 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;2.2.2.10 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA);         &emsp;2.2.2.11 Consentimento pendente de autorização: Em `PARTIALLY_ACCEPTED` aguardando aprovação de múltiplas alçadas. Não consome nem invalida o consentimento (CONSENTIMENTO_PENDENTE_AUTORIZACAO).     2.3 **Casos de erro para validações síncronas no DICT**       &ensp;Nesse cenário, o pagamento não é criado, porém o consentimento deve ser alterado para o status CONSUMED Retorno esperado do endpoint POST/Payments: HTTP Code 422 - Unprocessable Entity:       &ensp;• Erro por dados inválidos: Conforme item **2.2.2.8**       &ensp;• Erro por suspeita de fraude: Conforme item **2.2.2.9**    3. **Validações na consulta do pagamento (_GET /pix/payments/{paymentId}_)**     3.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token)**       &ensp;3.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;3.1.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED).    4. **Demais validações executadas durante o processamento assíncrono do pagamento pela detentora, poderão ser consultados pela iniciadora através do endpoint _GET /pix/payments/{paymentId}_ previstos com retorno HTTP Code 200 - OK com status RJCT (Rejected) e rejectionReason conforme abaixo (detalhamento adicional na documentação técnica da API):**     4.1 **Demais validações durante processamento assíncrono**       &ensp;4.1.1 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento. No caso de um pagamento agendado, a validação só ocorre na tentativa de liquidação do pagamento (SALDO_INSUFICIENTE);       &ensp;4.1.2 Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora (VALOR_ACIMA_LIMITE);       &ensp;4.1.3 Valor informado (QR Code): Valida se valor enviado é válido para o QR Code informado (VALOR_INVALIDO);       &ensp;4.1.4 Cobrança inválida: Valida expiração, vencimento e status (COBRANCA_INVALIDA);       &ensp;4.1.5 Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO);       &ensp;4.1.6 Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa (ex. chave Pix inválida, QRCode inválido, conta bloqueada);       &ensp;4.1.7 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);       &ensp;4.1.8 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);       &ensp;4.1.9 Validação SPI: Externaliza validações no SPI (PAGAMENTO_RECUSADO_SPI);       &ensp;4.1.10 Falha em agendamentos: Uma ou mais incidências de pagamento não foram possíveis de ser agendadas (FALHA_AGENDAMENTO_PAGAMENTOS);     4.2 **Casos de erro para validações assíncronas no DICT**       &ensp;Neste cenário o pagamento é criado com sucesso (status RCVD) e o consentimento é consumido (status CONSUMED), porém, as validações contra o DICT só ocorrerão de forma assíncrona e em caso de negativa será percebido pela iniciadora na consulta do pagamento (GET /Payments).       &ensp;Retorno esperado do endpoint GET /Payments: HTTP Code 200 - OK.       &ensp;Status do Pagamento: RJCT (Rejected), com as seguintes opções rejectionReason:       &ensp;• Erro por dados inválidos: Conforme item **4.1.7**;       &ensp;• Erro por suspeita de fraude: Conforme item **4.1.8**.  5. **Demais validações executadas durante o processamento assíncrono do consentimento pela detentora poderão ser consultados pela iniciadora através do endpoint _GET /consents/{consentId}_ previstos com retorno HTTP Code 200 – OK com status REJECTED e rejectionReason conforme abaixo:**     5.1 **Validações durante o processamento assíncrono**       &ensp;5.1.1 - Falha de infraestrutura: Ocorreu algum erro interno na detentora durante processamento da criação do consentimento (FALHA_INFRAESTRUTURA)       &ensp;5.1.2 - Tempo de autorização expirado: O usuário não confirmou o consentimento e o mesmo expirou (TEMPO_EXPIRADO_AUTORIZACAO);       &ensp;5.1.3 - Rejeitado pelo usuário: O usuário explicitamente rejeitou a autorização do consentimento (REJEITADO_USUARIO);       &ensp;5.1.4 - Mesma conta origem/destino: A conta indicada pelo usuário para recebimento é a mesma selecionada para o pagamento (CONTAS_ORIGEM_DESTINO_IGUAIS);       &ensp;5.1.5 - Tipo de conta inválida: A conta indicada não permite operações de pagamento (CONTA_NAO_PERMITE_PAGAMENTO);       &ensp;5.1.6 - Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento. Essa validação não deverá ocorrer no caso de um pagamento agendado (SALDO_INSUFICIENTE);       &ensp;5.1.7 - Limites da transação: Valida se o valor ultrapassa o limite estabelecido [na instituição/no arranjo/outro] para permitir a realização de transações pelo cliente (VALOR_ACIMA_LIMITE);       &ensp;5.1.8 - QRCode inválido: O QRCode utilizado para a iniciação de pagamento não é válido (QRCODE_INVALIDO);       &ensp;5.1.9 - Valor inválido: O valor enviado não é válido para o QR Code informado (VALOR_INVALIDO);       &ensp;5.1.10 - Não informado: Demais validações não explicitamente informadas (ex. suspeita de fraude) e consentimentos rejeitados em versões que não existiam o campo rejectionReason na API de Pagamentos (NAO_INFORMADO)       &ensp;5.1.11 - Tempo expirado consumo: O usuário não finalizou o fluxo de pagamento e o consentimento expirou (TEMPO_EXPIRADO_CONSUMO).     5.2 **[Momentos obrigatórios de validação dos rejectionReasons de acordo com o funil de consentimentos.](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/150863940)**      ```   |----------------------------------|------------------------------|   | Etapas do funil de consentimento | rejectionReason/code         |   |----------------------------------|------------------------------|   | Início da autenticação           | FALHA_INFRAESTRUTURA         |   |                                  | TEMPO_EXPIRADO_AUTORIZACAO   |   |                                  | NAO_INFORMADO                |   |----------------------------------|------------------------------|   | Conclusão da autenticação        | FALHA_INFRAESTRUTURA         |   |                                  | TEMPO_EXPIRADO_AUTORIZACAO   |   |                                  | REJEITADO_USUARIO            |   |                                  | NAO_INFORMADO                |   |----------------------------------|------------------------------|   | Autorização do cliente           | FALHA_INFRAESTRUTURA         |   |                                  | CONTAS_ORIGEM_DESTINO_IGUAIS |   |                                  | CONTA_NAO_PERMITE_PAGAMENTO  |   |                                  | SALDO_INSUFICIENTE           |   |                                  | VALOR_ACIMA_LIMITE           |   |                                  | QRCODE_INVALIDO              |   |                                  | VALOR_INVALIDO               |   |                                  | NAO_INFORMADO                |   |----------------------------------|------------------------------|   | Authorisation code emitido       | FALHA_INFRAESTRUTURA         |   |                                  | TEMPO_EXPIRADO_CONSUMO       |   |                                  | NAO_INFORMADO                |   |----------------------------------|------------------------------|   ```   Existem dois `endpoints` para cancelamento de pagamentos, um deles é o _PATCH /pix/payments/{paymentId}_ e o outro é o _PATCH /pix/payments/consents/{consentId}_.   - O _PATCH /pix/payments/{paymentId}_ deve ser utilizado para o cancelamento de um pagamento de forma unitária. Não deve ser utilizado para o cancelamento de todos os agendamentos recorrentes associados a um consentimento.   - O _PATCH /pix/payments/consents/{consentId}_ deve ser utilizado no cancelamento de todas as ocorrências de pagamentos agendados presentes em uma recorrência de pagamentos. Todos os pagamentos associados ao consentimento informado e passíveis de cancelamento (ainda não liquidados, com os status PDNG e SCHD) deverão ser cancelados.   # noqa: E501

    OpenAPI spec version: 4.0.0-beta.2
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ScheduleWeeklyWeekly(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'day_of_week': 'str',
        'start_date': 'date',
        'quantity': 'int'
    }

    attribute_map = {
        'day_of_week': 'dayOfWeek',
        'start_date': 'startDate',
        'quantity': 'quantity'
    }

    def __init__(self, day_of_week=None, start_date=None, quantity=None):  # noqa: E501
        """ScheduleWeeklyWeekly - a model defined in Swagger"""  # noqa: E501
        self._day_of_week = None
        self._start_date = None
        self._quantity = None
        self.discriminator = None
        self.day_of_week = day_of_week
        self.start_date = start_date
        self.quantity = quantity

    @property
    def day_of_week(self):
        """Gets the day_of_week of this ScheduleWeeklyWeekly.  # noqa: E501


        :return: The day_of_week of this ScheduleWeeklyWeekly.  # noqa: E501
        :rtype: str
        """
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week):
        """Sets the day_of_week of this ScheduleWeeklyWeekly.


        :param day_of_week: The day_of_week of this ScheduleWeeklyWeekly.  # noqa: E501
        :type: str
        """
        if day_of_week is None:
            raise ValueError("Invalid value for `day_of_week`, must not be `None`")  # noqa: E501
        allowed_values = ["SEGUNDA_FEIRA", "TERCA_FEIRA", "QUARTA_FEIRA", "QUINTA_FEIRA", "SEXTA_FEIRA", "SABADO", "DOMINGO"]  # noqa: E501
        if day_of_week not in allowed_values:
            raise ValueError(
                "Invalid value for `day_of_week` ({0}), must be one of {1}"  # noqa: E501
                .format(day_of_week, allowed_values)
            )

        self._day_of_week = day_of_week

    @property
    def start_date(self):
        """Gets the start_date of this ScheduleWeeklyWeekly.  # noqa: E501


        :return: The start_date of this ScheduleWeeklyWeekly.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ScheduleWeeklyWeekly.


        :param start_date: The start_date of this ScheduleWeeklyWeekly.  # noqa: E501
        :type: date
        """
        if start_date is None:
            raise ValueError("Invalid value for `start_date`, must not be `None`")  # noqa: E501

        self._start_date = start_date

    @property
    def quantity(self):
        """Gets the quantity of this ScheduleWeeklyWeekly.  # noqa: E501


        :return: The quantity of this ScheduleWeeklyWeekly.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ScheduleWeeklyWeekly.


        :param quantity: The quantity of this ScheduleWeeklyWeekly.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ScheduleWeeklyWeekly, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScheduleWeeklyWeekly):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
