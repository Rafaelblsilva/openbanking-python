# coding: utf-8

"""
    API Automatic Payments - Open Finance Brasil

    API de Iniciação de Pagamentos automáticos, responsável por viabilizar as operações de iniciação de pagamentos automáticos (Pix automático e Sweeping Accounts) para o Open Finance Brasil.  Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos endpoints dedicados ao consentimento nesta API.  # Orientações - `CONTA`, referente às instituições detentoras de conta participantes do Open Finance Brasil; - `PAGTO`, referente às instituições iniciadoras de pagamento participantes do Open Finance Brasil.  Os tokens utilizados para consumo nos endpoints de consentimentos devem possuir o scope payments e os endpoints de pagamentos recorrentes devem possuir os scopes openid e payments.  Esta API não requer a implementação de permissions para sua utilização.  Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão Assinaturas do guia de segurança.  ## Orientações gerais sobre os consentimentos de pagamentos automáticos - Duração e reutilização do consentimento: A utilização das credenciais geradas a partir de uma autorização de um consentimento recorrente deve durar até que o consentimento recorrente atinja o fim do seu ciclo de vida, conforme detalhado na sua [máquina de estados](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/198410647).  - Credenciais: As credenciais (authorization_code) geradas na autorização do consentimento devem ser utilizadas para criação dos pagamentos subsequentes utilizando o mecanismo de refresh, caso necessário. Maiores informações através do link [[PT] Open Finance Brasil Financial-grade API Security Profile 1.0 Implementers Draft 3 - Área do Desenvolvedor -Open Finance Brasil - Área do Desenvolvedor (atlassian.net)](https://openfinancebrasil.atlassian.net/wiki/spaces/OF/pages/82051180/PT+Open+Finance+Brasil+Financial-grade+API+Security+Profile+1.0+Implementers+Draft+3#7.2.2.-Servidor-de-autorização)  ## Regras do arranjo Pix A implementação e o uso da API de Pagamentos Automáticos (Pix) devem seguir as regras do arranjo Pix do Banco Central, que podem ser encontradas no link abaixo:   [Banco Central do Brasil](https://www.bcb.gov.br/estabilidadefinanceira/pix?modalAberto=regulamentacao_pix)  ## Assinatura de payloads No contexto da API de Pagamentos Automáticos, os payloads de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora de conta devem estar assinados.  Para o processo de assinatura destes payloads, as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor.  ## Controle de acesso - Os endpoints de consulta de pagamentos GET /pix/recurring-payments/{recurringPaymentId} e GET /pix/recurring-payments devem suportar acesso a partir de access_token emitido por meio de um grant_type do tipo client credentials, como opção do uso do token vinculado ao consentimento (hybrid flow). - Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.  ## Aprovações de múltipla alçada  Todas as aprovações devem ser realizadas até a data/hora limite suportada pela detentora e em tempo hábil para realizar o primeiro pagamento.  ## Validações da edição do consentimento recorrente para o produto Pix Automático  Para permitir a edição dos campos de um consentimento na iniciadora sem que se faça necessário o redirecionamento para o  ambiente da detentora de conta, é necessário o envio de indicadores de risco.  Esta medida visa proporcionar à detentora de conta as informações necessárias para decidir sobre os ajustes no consentimento de forma segura  ## Validações  Durante a jornada de iniciação de pagamento, diferentes validações são necessárias pela instituição detentora de conta e devem ocorrer conforme a seguir:  1. **Validações na criação do consentimento de longa duração (_POST /recurring-consents_)**     1.1 **Orientações Iniciais**       &ensp;1.1.1 Não devem ser retornadas na resposta deste endpoint informações associadas ao usuário/cliente (ex. insuficiência de saldo, conta inexistente/bloqueada).       &ensp;1.1.2 Não devem ser realizadas validações de informações sobre o usuário/cliente durante a criação do consentimento.     1.2 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;1.2.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;1.2.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;1.2.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;1.2.4 Validação de Claims (exceto data);         &emsp;1.2.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;1.2.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     1.3 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**        &ensp;1.3.1 **Sintáticos**         &emsp;1.3.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios foram informados (PARAMETRO_NAO_INFORMADO);         &emsp;1.3.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;1.3.2 **Semânticos**         &emsp;1.3.2.1 Data de pagamento: Valida se a data de pagamento enviada é válida para a forma de pagamento selecionada (DATA_PAGAMENTO_INVALIDA);         &emsp;1.3.2.2 Detalhes do pagamento: Valida se determinado parâmetro informado obedece às regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;1.3.2.3 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;1.3.2.4 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA);         &emsp;1.3.2.5 Funcionalidade não habilitada: A detentora de conta não oferece o serviço nessa modalidade (FUNCIONALIDADE_NAO_HABILITADA).    2. **Demais validações executadas durante o processamento assíncrono do consentimento pela detentora poderão ser consultados pela iniciadora através do endpoint GET /recurring-consents/{recurringConsentId} previstos com retorno HTTP Code 200 – OK com status REJECTED e rejectionReason conforme abaixo:**     2.1 **Validações durante o processamento assíncrono do consentimento**       &ensp;2.1.1 Falha de infraestrutura: Ocorreu algum erro interno na detentora durante processamento da criação do consentimento (FALHA_INFRAESTRUTURA);       &ensp;2.1.2 Tempo de autorização expirado: O usuário não confirmou o consentimento e o mesmo expirou (TEMPO_EXPIRADO_AUTORIZACAO);       &ensp;2.1.3 Rejeitado pelo usuário: O usuário explicitamente rejeitou a autorização do consentimento (REJEITADO_USUARIO);       &ensp;2.1.4 Mesma conta origem/destino: A conta indicada pelo usuário para recebimento é a mesma selecionada para o pagamento (CONTAS_ORIGEM_DESTINO_IGUAIS);       &ensp;2.1.5 Tipo de conta inválida: A conta indicada não permite operações de pagamento (CONTA_NAO_PERMITE_PAGAMENTO);       &ensp;2.1.6 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);       &ensp;2.1.7 Limites da transação: Valida se o valor ultrapassa o limite estabelecido [na instituição/no arranjo/outro] para permitir a realização de transações pelo cliente (VALOR_ACIMA_LIMITE);    3. **Demais validações executadas durante o processamento assíncrono do consentimento pela detentora, poderão ser consultados pela iniciadora através dos endpoints GET /recurring-consents/{recurringConsentId} previstos com retorno HTTP Code 200 - OK com status REVOKED e revocationReason conforme abaixo (detalhamento adicional na documentação técnica da API).**     3.1 **Demais validações durante o processamento assíncrono:**       &ensp;3.1.1 Nao informado: Validações não explicitamente informadas (ex. suspeita de fraude) (NAO_INFORMADO);       &ensp;3.1.2 Revogado pelo recebedor: O usuário recebedor solicitou explicitamente ao iniciador a revogação do consentimento (ex: término de contrato) (REVOGADO_RECEBEDOR);       &ensp;3.1.3 Revogado pelo pagador: O usuário pagador solicitou explicitamente a revogação do consentimento (REVOGADO_USUARIO).    4. **Validações na criação do pagamento - Síncrono (_POST /pix/recurring-payments_)**     4.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token, jwt, assinatura)**       &ensp;4.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;4.1.2 Validação de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED);       &ensp;4.1.3 Validação de assinatura da mensagem: Valida se assinatura das mensagens enviadas está correta – HTTP Code 400 (BAD_SIGNATURE);       &ensp;4.1.4 Validação de Claims (exceto data);         &emsp;4.1.4.1 Valida se dados (aud, iss, iat e jti) são válidos - HTTP status code 403 – (INVALID_CLIENT);         &emsp;4.1.4.2 Valida reuso de jti - HTTP Code 403 (INVALID_CLIENT).     4.2 **Casos de erro sintáticos e semânticos, previstos com retorno HTTP Code 422 - Unprocessable Entity (detalhamento adicional na documentação técnica da API):**       &ensp;4.2.1 Sintáticos         &emsp;4.2.1.1 Envio de campos obrigatórios: Valida se todos os campos obrigatórios são informados (PARAMETRO_NAO_INFORMADO);         &emsp;4.2.1.2 Formatação de parâmetros: Valida se parâmetros informados obedecem a formatação especificada (PARAMETRO_INVALIDO).       &ensp;4.2.2 Semânticos         &emsp;4.2.2.1 Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);         &emsp;4.2.2.2 Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora na conta do cliente pagador (VALOR_ACIMA_LIMITE);         &emsp;4.2.2.3 Valor informado: Valida se valor enviado é válido para o consentimento associado ao pagamento (VALOR_INVALIDO);         &emsp;4.2.2.4 Status Consentimento: Valida se status de consentimento é diferente de “AUTHORISED” (CONSENTIMENTO_INVALIDO);         &emsp;4.2.2.5 Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);         &emsp;4.2.2.6 Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO)         &emsp;4.2.2.7 Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa;         &emsp;4.2.2.8 Detalhes do pagamento: Valida se determinado parâmetro informado obedece as regras de negócio (DETALHE_PAGAMENTO_INVALIDO);         &emsp;4.2.2.9 Pagamento recusado no Sistema de Pagamentos Instantâneos (SPI) (PAGAMENTO_RECUSADO_SPI);         &emsp;4.2.2.10 Idempotência: Valida se há divergência entre chave de idempotência e informações enviadas (ERRO_IDEMPOTENCIA);         &emsp;4.2.2.11 Limite valor excedido por período: Foi atingido o valor limite permitido pelo usuário por um determinado período de tempo no consentimento do pagamento (LIMITE_PERIODO_VALOR_EXCEDIDO);         &emsp;4.2.2.12 Limite quantidade excedida por período: A quantidade de cobranças atingiu o limite determinado pelo usuário na criação do consentimento (LIMITE_PERIODO_QUANTIDADE_EXCEDIDO).    5. **Validações na consulta do pagamento (_GET /pix/recurring-payments/{recurringPaymentId}_ e _GET /pix/recurring-payments_)**     5.1 **Casos de erro relacionados às permissões de segurança para acesso à API (ex. certificado, access_token)**       &ensp;5.1.1 Validação de Certificado: Valida utilização de certificado correto durante processo de DCR - HTTP Code 401 (INVALID_CLIENT);       &ensp;5.1.2 Validações de Access_Token: Verifica se Access_Token utilizado está correto - HTTP Code 401 (UNAUTHORIZED).  6. **Demais validações executadas durante o processamento assíncrono do pagamento pela detentora, poderão ser consultados pela iniciadora através dos endpoints _GET /pix/recurring-payments/{recurringPaymentId}_ e _GET /pix/recurring-payments_ previstos com retorno HTTP Code 200 - OK com status RJCT (Rejected) e rejectionReason conforme abaixo (detalhamento adicional na documentação técnica da API):**     6.1 **Demais validações durante o processamento assíncrono:**       &ensp;6.1.1 - Saldo do usuário: Valida se a conta selecionada possui saldo suficiente para realizar o pagamento (SALDO_INSUFICIENTE);       &ensp;6.1.2 - Limites da transação: Valida se valor (ou quantidade de transações) ultrapassa faixa de limite parametrizada na detentora (VALOR_ACIMA_LIMITE);       &ensp;6.1.3 - Valor informado: Valida se valor enviado é válido para o consentimento do pagamento (VALOR_INVALIDO);       &ensp;6.1.4 - Demais validações não explicitamente informadas (ex. suspeita de fraude): (NAO_INFORMADO);       &ensp;6.1.5 - Divergência entre pagamento e consentimento: Valida se dados do pagamento são diferentes dos dados do consentimento (PAGAMENTO_DIVERGENTE_CONSENTIMENTO);       &ensp;6.1.6 - Recusado pela detentora: Valida se pagamento foi recusado pela detentora (PAGAMENTO_RECUSADO_DETENTORA), com a descrição do motivo de recusa;       &ensp;6.1.7 - Pagamento recusado no Sistema de Pagamentos Instantâneos (SPI) (PAGAMENTO_RECUSADO_SPI);       &ensp;6.1.8 - Erro de infraestrutura na consulta ao SPI: Ocorreu uma falha de infraestrutura durante a consulta ao SPI(FALHA_INFRAESTRUTURA_SPI);       &ensp;6.1.9 - Erro de infraestrutura na consulta ao ICP: Ocorreu uma falha de infraestrutura durante a consulta ao ICP (FALHA_INFRAESTRUTURA_ICP);       &ensp;6.1.10 - Erro de infraestrutura na comunicação com o PSP do recebedor: Ocorreu uma falha de infraestrutura durante a comunicação com o PSP do recebedor (FALHA_INFRAESTRUTURA_PSP_RECEBEDOR);       &ensp;6.1.11 - Erro de infraestrutura interno na detentora: Ocorreu uma falha de infraestrutura interna na detentora durante o processamento do pagamento (FALHA_INFRAESTRUTURA_DETENTORA);       &ensp;6.1.12 - Status Consentimento: Valida se status de consentimento é diferente de “AUTHORISED” (CONSENTIMENTO_INVALIDO);    ## Validações antifraude do Sweeping accounts  - Afim de garantir a mesma titularidade e aumentar a segurança das transações do produto Sweeping Accounts, as validações abaixo poderão ser realizadas pela detetora de conta e pela iniciadora, quando localinstrument for igual a DICT ou INIC. A detentora PODE usar a API Consultar Vinculo (DICT API) do arranjo Pix e validar no momento de transação ao menos os atributos abaixo mencionados:   - se o valor dos atributos de fraude abaixo são iguais a 0, de modo a evitar que contas criadas especificamente para uso indevido do Sweeping accounts impactem o ecossistema      - OwnerStatistics.Spi.FraudMarkers.ApplicationFrauds.d90     - OwnerStatistics.Spi.FraudMarkers.MuleAccounts.d90     - OwnerStatistics.Spi.FraudMarkers.ScammerAccounts.d90     - OwnerStatistics.Spi.FraudMarkers.OtherFrauds.d90     - OwnerStatistics.Spi.FraudMarkers.UnknownFrauds.d90   # noqa: E501

    OpenAPI spec version: 1.0.0-beta.4
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RiskSignalsConsents(object):
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
        'device_id': 'str',
        'is_rooted_device': 'bool',
        'screen_brightness': 'float',
        'elapsed_time_since_boot': 'int',
        'os_version': 'str',
        'user_time_zone_offset': 'str',
        'language': 'str',
        'screen_dimensions': 'RiskSignalsPaymentsManualScreenDimensions',
        'account_tenure': 'date',
        'geolocation': 'RiskSignalsPaymentsManualGeolocation',
        'is_call_in_progress': 'bool',
        'is_dev_mode_enabled': 'bool',
        'is_mock_gps': 'bool',
        'is_emulated': 'bool',
        'is_monkey_runner': 'bool',
        'is_charging': 'bool',
        'antenna_information': 'str',
        'is_usb_connected': 'bool',
        'integrity': 'RiskSignalsPaymentsManualIntegrity'
    }

    attribute_map = {
        'device_id': 'deviceId',
        'is_rooted_device': 'isRootedDevice',
        'screen_brightness': 'screenBrightness',
        'elapsed_time_since_boot': 'elapsedTimeSinceBoot',
        'os_version': 'osVersion',
        'user_time_zone_offset': 'userTimeZoneOffset',
        'language': 'language',
        'screen_dimensions': 'screenDimensions',
        'account_tenure': 'accountTenure',
        'geolocation': 'geolocation',
        'is_call_in_progress': 'isCallInProgress',
        'is_dev_mode_enabled': 'isDevModeEnabled',
        'is_mock_gps': 'isMockGPS',
        'is_emulated': 'isEmulated',
        'is_monkey_runner': 'isMonkeyRunner',
        'is_charging': 'isCharging',
        'antenna_information': 'antennaInformation',
        'is_usb_connected': 'isUsbConnected',
        'integrity': 'integrity'
    }

    def __init__(self, device_id=None, is_rooted_device=None, screen_brightness=None, elapsed_time_since_boot=None, os_version=None, user_time_zone_offset=None, language=None, screen_dimensions=None, account_tenure=None, geolocation=None, is_call_in_progress=None, is_dev_mode_enabled=None, is_mock_gps=None, is_emulated=None, is_monkey_runner=None, is_charging=None, antenna_information=None, is_usb_connected=None, integrity=None):  # noqa: E501
        """RiskSignalsConsents - a model defined in Swagger"""  # noqa: E501
        self._device_id = None
        self._is_rooted_device = None
        self._screen_brightness = None
        self._elapsed_time_since_boot = None
        self._os_version = None
        self._user_time_zone_offset = None
        self._language = None
        self._screen_dimensions = None
        self._account_tenure = None
        self._geolocation = None
        self._is_call_in_progress = None
        self._is_dev_mode_enabled = None
        self._is_mock_gps = None
        self._is_emulated = None
        self._is_monkey_runner = None
        self._is_charging = None
        self._antenna_information = None
        self._is_usb_connected = None
        self._integrity = None
        self.discriminator = None
        self.device_id = device_id
        self.is_rooted_device = is_rooted_device
        self.screen_brightness = screen_brightness
        self.elapsed_time_since_boot = elapsed_time_since_boot
        self.os_version = os_version
        self.user_time_zone_offset = user_time_zone_offset
        self.language = language
        self.screen_dimensions = screen_dimensions
        self.account_tenure = account_tenure
        if geolocation is not None:
            self.geolocation = geolocation
        if is_call_in_progress is not None:
            self.is_call_in_progress = is_call_in_progress
        if is_dev_mode_enabled is not None:
            self.is_dev_mode_enabled = is_dev_mode_enabled
        if is_mock_gps is not None:
            self.is_mock_gps = is_mock_gps
        if is_emulated is not None:
            self.is_emulated = is_emulated
        if is_monkey_runner is not None:
            self.is_monkey_runner = is_monkey_runner
        if is_charging is not None:
            self.is_charging = is_charging
        if antenna_information is not None:
            self.antenna_information = antenna_information
        if is_usb_connected is not None:
            self.is_usb_connected = is_usb_connected
        if integrity is not None:
            self.integrity = integrity

    @property
    def device_id(self):
        """Gets the device_id of this RiskSignalsConsents.  # noqa: E501

        ID único do dispositivo gerado pela plataforma.  # noqa: E501

        :return: The device_id of this RiskSignalsConsents.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this RiskSignalsConsents.

        ID único do dispositivo gerado pela plataforma.  # noqa: E501

        :param device_id: The device_id of this RiskSignalsConsents.  # noqa: E501
        :type: str
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def is_rooted_device(self):
        """Gets the is_rooted_device of this RiskSignalsConsents.  # noqa: E501

        Indica se o dispositivo atualmente está com permissão de “root”.  # noqa: E501

        :return: The is_rooted_device of this RiskSignalsConsents.  # noqa: E501
        :rtype: bool
        """
        return self._is_rooted_device

    @is_rooted_device.setter
    def is_rooted_device(self, is_rooted_device):
        """Sets the is_rooted_device of this RiskSignalsConsents.

        Indica se o dispositivo atualmente está com permissão de “root”.  # noqa: E501

        :param is_rooted_device: The is_rooted_device of this RiskSignalsConsents.  # noqa: E501
        :type: bool
        """
        if is_rooted_device is None:
            raise ValueError("Invalid value for `is_rooted_device`, must not be `None`")  # noqa: E501

        self._is_rooted_device = is_rooted_device

    @property
    def screen_brightness(self):
        """Gets the screen_brightness of this RiskSignalsConsents.  # noqa: E501

        Indica o nível de brilho da tela do dispositivo.   Em dispositivos Android o valor é um inteiro, entre 0 e 255, inclusive;   Em dispositivos iOS o valor é um ponto flutuante entre 0.0 e 1.0.   # noqa: E501

        :return: The screen_brightness of this RiskSignalsConsents.  # noqa: E501
        :rtype: float
        """
        return self._screen_brightness

    @screen_brightness.setter
    def screen_brightness(self, screen_brightness):
        """Sets the screen_brightness of this RiskSignalsConsents.

        Indica o nível de brilho da tela do dispositivo.   Em dispositivos Android o valor é um inteiro, entre 0 e 255, inclusive;   Em dispositivos iOS o valor é um ponto flutuante entre 0.0 e 1.0.   # noqa: E501

        :param screen_brightness: The screen_brightness of this RiskSignalsConsents.  # noqa: E501
        :type: float
        """
        if screen_brightness is None:
            raise ValueError("Invalid value for `screen_brightness`, must not be `None`")  # noqa: E501

        self._screen_brightness = screen_brightness

    @property
    def elapsed_time_since_boot(self):
        """Gets the elapsed_time_since_boot of this RiskSignalsConsents.  # noqa: E501

        Indica por quanto tempo (em milissegundos) o dispositivo está ligado.  # noqa: E501

        :return: The elapsed_time_since_boot of this RiskSignalsConsents.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time_since_boot

    @elapsed_time_since_boot.setter
    def elapsed_time_since_boot(self, elapsed_time_since_boot):
        """Sets the elapsed_time_since_boot of this RiskSignalsConsents.

        Indica por quanto tempo (em milissegundos) o dispositivo está ligado.  # noqa: E501

        :param elapsed_time_since_boot: The elapsed_time_since_boot of this RiskSignalsConsents.  # noqa: E501
        :type: int
        """
        if elapsed_time_since_boot is None:
            raise ValueError("Invalid value for `elapsed_time_since_boot`, must not be `None`")  # noqa: E501

        self._elapsed_time_since_boot = elapsed_time_since_boot

    @property
    def os_version(self):
        """Gets the os_version of this RiskSignalsConsents.  # noqa: E501

        Versão do sistema operacional.  # noqa: E501

        :return: The os_version of this RiskSignalsConsents.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this RiskSignalsConsents.

        Versão do sistema operacional.  # noqa: E501

        :param os_version: The os_version of this RiskSignalsConsents.  # noqa: E501
        :type: str
        """
        if os_version is None:
            raise ValueError("Invalid value for `os_version`, must not be `None`")  # noqa: E501

        self._os_version = os_version

    @property
    def user_time_zone_offset(self):
        """Gets the user_time_zone_offset of this RiskSignalsConsents.  # noqa: E501

        Indica a configuração de fuso horário do dispositivo do usuário, com o formato UTC offset: ±hh[:mm]   # noqa: E501

        :return: The user_time_zone_offset of this RiskSignalsConsents.  # noqa: E501
        :rtype: str
        """
        return self._user_time_zone_offset

    @user_time_zone_offset.setter
    def user_time_zone_offset(self, user_time_zone_offset):
        """Sets the user_time_zone_offset of this RiskSignalsConsents.

        Indica a configuração de fuso horário do dispositivo do usuário, com o formato UTC offset: ±hh[:mm]   # noqa: E501

        :param user_time_zone_offset: The user_time_zone_offset of this RiskSignalsConsents.  # noqa: E501
        :type: str
        """
        if user_time_zone_offset is None:
            raise ValueError("Invalid value for `user_time_zone_offset`, must not be `None`")  # noqa: E501

        self._user_time_zone_offset = user_time_zone_offset

    @property
    def language(self):
        """Gets the language of this RiskSignalsConsents.  # noqa: E501

        Indica o idioma do dispositivo no formato ISO 639-1.  # noqa: E501

        :return: The language of this RiskSignalsConsents.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this RiskSignalsConsents.

        Indica o idioma do dispositivo no formato ISO 639-1.  # noqa: E501

        :param language: The language of this RiskSignalsConsents.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def screen_dimensions(self):
        """Gets the screen_dimensions of this RiskSignalsConsents.  # noqa: E501


        :return: The screen_dimensions of this RiskSignalsConsents.  # noqa: E501
        :rtype: RiskSignalsPaymentsManualScreenDimensions
        """
        return self._screen_dimensions

    @screen_dimensions.setter
    def screen_dimensions(self, screen_dimensions):
        """Sets the screen_dimensions of this RiskSignalsConsents.


        :param screen_dimensions: The screen_dimensions of this RiskSignalsConsents.  # noqa: E501
        :type: RiskSignalsPaymentsManualScreenDimensions
        """
        if screen_dimensions is None:
            raise ValueError("Invalid value for `screen_dimensions`, must not be `None`")  # noqa: E501

        self._screen_dimensions = screen_dimensions

    @property
    def account_tenure(self):
        """Gets the account_tenure of this RiskSignalsConsents.  # noqa: E501

        Data de cadastro do cliente na iniciadora.  # noqa: E501

        :return: The account_tenure of this RiskSignalsConsents.  # noqa: E501
        :rtype: date
        """
        return self._account_tenure

    @account_tenure.setter
    def account_tenure(self, account_tenure):
        """Sets the account_tenure of this RiskSignalsConsents.

        Data de cadastro do cliente na iniciadora.  # noqa: E501

        :param account_tenure: The account_tenure of this RiskSignalsConsents.  # noqa: E501
        :type: date
        """
        if account_tenure is None:
            raise ValueError("Invalid value for `account_tenure`, must not be `None`")  # noqa: E501

        self._account_tenure = account_tenure

    @property
    def geolocation(self):
        """Gets the geolocation of this RiskSignalsConsents.  # noqa: E501


        :return: The geolocation of this RiskSignalsConsents.  # noqa: E501
        :rtype: RiskSignalsPaymentsManualGeolocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation):
        """Sets the geolocation of this RiskSignalsConsents.


        :param geolocation: The geolocation of this RiskSignalsConsents.  # noqa: E501
        :type: RiskSignalsPaymentsManualGeolocation
        """

        self._geolocation = geolocation

    @property
    def is_call_in_progress(self):
        """Gets the is_call_in_progress of this RiskSignalsConsents.  # noqa: E501

        Indica chamada ativa no momento do vínculo.  [Restrição] Caso o sinal de risco esteja disponível (cliente permitiu que fosse coletado), o mesmo deverá ser enviado   # noqa: E501

        :return: The is_call_in_progress of this RiskSignalsConsents.  # noqa: E501
        :rtype: bool
        """
        return self._is_call_in_progress

    @is_call_in_progress.setter
    def is_call_in_progress(self, is_call_in_progress):
        """Sets the is_call_in_progress of this RiskSignalsConsents.

        Indica chamada ativa no momento do vínculo.  [Restrição] Caso o sinal de risco esteja disponível (cliente permitiu que fosse coletado), o mesmo deverá ser enviado   # noqa: E501

        :param is_call_in_progress: The is_call_in_progress of this RiskSignalsConsents.  # noqa: E501
        :type: bool
        """

        self._is_call_in_progress = is_call_in_progress

    @property
    def is_dev_mode_enabled(self):
        """Gets the is_dev_mode_enabled of this RiskSignalsConsents.  # noqa: E501

        Indica se o dispositivo está em modo de desenvolvedor.  # noqa: E501

        :return: The is_dev_mode_enabled of this RiskSignalsConsents.  # noqa: E501
        :rtype: bool
        """
        return self._is_dev_mode_enabled

    @is_dev_mode_enabled.setter
    def is_dev_mode_enabled(self, is_dev_mode_enabled):
        """Sets the is_dev_mode_enabled of this RiskSignalsConsents.

        Indica se o dispositivo está em modo de desenvolvedor.  # noqa: E501

        :param is_dev_mode_enabled: The is_dev_mode_enabled of this RiskSignalsConsents.  # noqa: E501
        :type: bool
        """

        self._is_dev_mode_enabled = is_dev_mode_enabled

    @property
    def is_mock_gps(self):
        """Gets the is_mock_gps of this RiskSignalsConsents.  # noqa: E501

        Indica se o dispositivo está usando um GPS falso.  # noqa: E501

        :return: The is_mock_gps of this RiskSignalsConsents.  # noqa: E501
        :rtype: bool
        """
        return self._is_mock_gps

    @is_mock_gps.setter
    def is_mock_gps(self, is_mock_gps):
        """Sets the is_mock_gps of this RiskSignalsConsents.

        Indica se o dispositivo está usando um GPS falso.  # noqa: E501

        :param is_mock_gps: The is_mock_gps of this RiskSignalsConsents.  # noqa: E501
        :type: bool
        """

        self._is_mock_gps = is_mock_gps

    @property
    def is_emulated(self):
        """Gets the is_emulated of this RiskSignalsConsents.  # noqa: E501

        Indica se o dispositivo é emulado ou real.  # noqa: E501

        :return: The is_emulated of this RiskSignalsConsents.  # noqa: E501
        :rtype: bool
        """
        return self._is_emulated

    @is_emulated.setter
    def is_emulated(self, is_emulated):
        """Sets the is_emulated of this RiskSignalsConsents.

        Indica se o dispositivo é emulado ou real.  # noqa: E501

        :param is_emulated: The is_emulated of this RiskSignalsConsents.  # noqa: E501
        :type: bool
        """

        self._is_emulated = is_emulated

    @property
    def is_monkey_runner(self):
        """Gets the is_monkey_runner of this RiskSignalsConsents.  # noqa: E501

        Indica o uso do MonkeyRunner.  # noqa: E501

        :return: The is_monkey_runner of this RiskSignalsConsents.  # noqa: E501
        :rtype: bool
        """
        return self._is_monkey_runner

    @is_monkey_runner.setter
    def is_monkey_runner(self, is_monkey_runner):
        """Sets the is_monkey_runner of this RiskSignalsConsents.

        Indica o uso do MonkeyRunner.  # noqa: E501

        :param is_monkey_runner: The is_monkey_runner of this RiskSignalsConsents.  # noqa: E501
        :type: bool
        """

        self._is_monkey_runner = is_monkey_runner

    @property
    def is_charging(self):
        """Gets the is_charging of this RiskSignalsConsents.  # noqa: E501

        Indica se a bateria do dispositivo está sendo carregada.  # noqa: E501

        :return: The is_charging of this RiskSignalsConsents.  # noqa: E501
        :rtype: bool
        """
        return self._is_charging

    @is_charging.setter
    def is_charging(self, is_charging):
        """Sets the is_charging of this RiskSignalsConsents.

        Indica se a bateria do dispositivo está sendo carregada.  # noqa: E501

        :param is_charging: The is_charging of this RiskSignalsConsents.  # noqa: E501
        :type: bool
        """

        self._is_charging = is_charging

    @property
    def antenna_information(self):
        """Gets the antenna_information of this RiskSignalsConsents.  # noqa: E501

        Indica em qual antena o dispositivo está conectado.  # noqa: E501

        :return: The antenna_information of this RiskSignalsConsents.  # noqa: E501
        :rtype: str
        """
        return self._antenna_information

    @antenna_information.setter
    def antenna_information(self, antenna_information):
        """Sets the antenna_information of this RiskSignalsConsents.

        Indica em qual antena o dispositivo está conectado.  # noqa: E501

        :param antenna_information: The antenna_information of this RiskSignalsConsents.  # noqa: E501
        :type: str
        """

        self._antenna_information = antenna_information

    @property
    def is_usb_connected(self):
        """Gets the is_usb_connected of this RiskSignalsConsents.  # noqa: E501

        Indica se o dispositivo está conectado a outro dispositivo via USB.  # noqa: E501

        :return: The is_usb_connected of this RiskSignalsConsents.  # noqa: E501
        :rtype: bool
        """
        return self._is_usb_connected

    @is_usb_connected.setter
    def is_usb_connected(self, is_usb_connected):
        """Sets the is_usb_connected of this RiskSignalsConsents.

        Indica se o dispositivo está conectado a outro dispositivo via USB.  # noqa: E501

        :param is_usb_connected: The is_usb_connected of this RiskSignalsConsents.  # noqa: E501
        :type: bool
        """

        self._is_usb_connected = is_usb_connected

    @property
    def integrity(self):
        """Gets the integrity of this RiskSignalsConsents.  # noqa: E501


        :return: The integrity of this RiskSignalsConsents.  # noqa: E501
        :rtype: RiskSignalsPaymentsManualIntegrity
        """
        return self._integrity

    @integrity.setter
    def integrity(self, integrity):
        """Sets the integrity of this RiskSignalsConsents.


        :param integrity: The integrity of this RiskSignalsConsents.  # noqa: E501
        :type: RiskSignalsPaymentsManualIntegrity
        """

        self._integrity = integrity

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
        if issubclass(RiskSignalsConsents, dict):
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
        if not isinstance(other, RiskSignalsConsents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
