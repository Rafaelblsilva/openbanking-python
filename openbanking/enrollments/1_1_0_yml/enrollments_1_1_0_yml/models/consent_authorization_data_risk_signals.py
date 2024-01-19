# coding: utf-8

"""
    API Enrollments for Payment Initiation - Open Finance Brasil

    Família de API para permitir o pagamento sem redirecionamento via Open Finance Brasil.   Permite tanto o gerenciamento dos dispositivos vinculados as contas quanto a autorização de consentimentos criados via fluxo sem redirecionamento.   # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: squad-jornada@openfinancebrasil.org.br
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ConsentAuthorizationDataRiskSignals(object):
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
        'screen_dimensions': 'RiskSignalsDataScreenDimensions',
        'account_tenure': 'date',
        'geolocation': 'RiskSignalsDataGeolocation',
        'is_call_in_progress': 'bool',
        'is_dev_mode_enabled': 'bool',
        'is_mock_gps': 'bool',
        'is_emulated': 'bool',
        'is_monkey_runner': 'bool',
        'is_charging': 'bool',
        'antenna_information': 'str',
        'is_usb_connected': 'bool',
        'integrity': 'RiskSignalsDataIntegrity'
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
        """ConsentAuthorizationDataRiskSignals - a model defined in Swagger"""  # noqa: E501
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
        """Gets the device_id of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        ID único do dispositivo gerado pela plataforma.  # noqa: E501

        :return: The device_id of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this ConsentAuthorizationDataRiskSignals.

        ID único do dispositivo gerado pela plataforma.  # noqa: E501

        :param device_id: The device_id of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: str
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id

    @property
    def is_rooted_device(self):
        """Gets the is_rooted_device of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica se o dispositivo atualmente está com permissão de “root”.  # noqa: E501

        :return: The is_rooted_device of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: bool
        """
        return self._is_rooted_device

    @is_rooted_device.setter
    def is_rooted_device(self, is_rooted_device):
        """Sets the is_rooted_device of this ConsentAuthorizationDataRiskSignals.

        Indica se o dispositivo atualmente está com permissão de “root”.  # noqa: E501

        :param is_rooted_device: The is_rooted_device of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: bool
        """
        if is_rooted_device is None:
            raise ValueError("Invalid value for `is_rooted_device`, must not be `None`")  # noqa: E501

        self._is_rooted_device = is_rooted_device

    @property
    def screen_brightness(self):
        """Gets the screen_brightness of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica o nível de brilho da tela do dispositivo.   Em dispositivos Android o valor é um inteiro, entre 0 e 255, inclusive;   Em dispositivos iOS o valor é um ponto flutuante entre 0.0 e 1.0.   # noqa: E501

        :return: The screen_brightness of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: float
        """
        return self._screen_brightness

    @screen_brightness.setter
    def screen_brightness(self, screen_brightness):
        """Sets the screen_brightness of this ConsentAuthorizationDataRiskSignals.

        Indica o nível de brilho da tela do dispositivo.   Em dispositivos Android o valor é um inteiro, entre 0 e 255, inclusive;   Em dispositivos iOS o valor é um ponto flutuante entre 0.0 e 1.0.   # noqa: E501

        :param screen_brightness: The screen_brightness of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: float
        """
        if screen_brightness is None:
            raise ValueError("Invalid value for `screen_brightness`, must not be `None`")  # noqa: E501

        self._screen_brightness = screen_brightness

    @property
    def elapsed_time_since_boot(self):
        """Gets the elapsed_time_since_boot of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica por quanto tempo (em milissegundos) o dispositivo está ligado.  # noqa: E501

        :return: The elapsed_time_since_boot of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time_since_boot

    @elapsed_time_since_boot.setter
    def elapsed_time_since_boot(self, elapsed_time_since_boot):
        """Sets the elapsed_time_since_boot of this ConsentAuthorizationDataRiskSignals.

        Indica por quanto tempo (em milissegundos) o dispositivo está ligado.  # noqa: E501

        :param elapsed_time_since_boot: The elapsed_time_since_boot of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: int
        """
        if elapsed_time_since_boot is None:
            raise ValueError("Invalid value for `elapsed_time_since_boot`, must not be `None`")  # noqa: E501

        self._elapsed_time_since_boot = elapsed_time_since_boot

    @property
    def os_version(self):
        """Gets the os_version of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Versão do sistema operacional.  # noqa: E501

        :return: The os_version of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this ConsentAuthorizationDataRiskSignals.

        Versão do sistema operacional.  # noqa: E501

        :param os_version: The os_version of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: str
        """
        if os_version is None:
            raise ValueError("Invalid value for `os_version`, must not be `None`")  # noqa: E501

        self._os_version = os_version

    @property
    def user_time_zone_offset(self):
        """Gets the user_time_zone_offset of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica a configuração de fuso horário do dispositivo do usuário, com o formato UTC offset: ±hh[:mm]   # noqa: E501

        :return: The user_time_zone_offset of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: str
        """
        return self._user_time_zone_offset

    @user_time_zone_offset.setter
    def user_time_zone_offset(self, user_time_zone_offset):
        """Sets the user_time_zone_offset of this ConsentAuthorizationDataRiskSignals.

        Indica a configuração de fuso horário do dispositivo do usuário, com o formato UTC offset: ±hh[:mm]   # noqa: E501

        :param user_time_zone_offset: The user_time_zone_offset of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: str
        """
        if user_time_zone_offset is None:
            raise ValueError("Invalid value for `user_time_zone_offset`, must not be `None`")  # noqa: E501

        self._user_time_zone_offset = user_time_zone_offset

    @property
    def language(self):
        """Gets the language of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica o idioma do dispositivo no formato ISO 639-1.  # noqa: E501

        :return: The language of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ConsentAuthorizationDataRiskSignals.

        Indica o idioma do dispositivo no formato ISO 639-1.  # noqa: E501

        :param language: The language of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def screen_dimensions(self):
        """Gets the screen_dimensions of this ConsentAuthorizationDataRiskSignals.  # noqa: E501


        :return: The screen_dimensions of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: RiskSignalsDataScreenDimensions
        """
        return self._screen_dimensions

    @screen_dimensions.setter
    def screen_dimensions(self, screen_dimensions):
        """Sets the screen_dimensions of this ConsentAuthorizationDataRiskSignals.


        :param screen_dimensions: The screen_dimensions of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: RiskSignalsDataScreenDimensions
        """
        if screen_dimensions is None:
            raise ValueError("Invalid value for `screen_dimensions`, must not be `None`")  # noqa: E501

        self._screen_dimensions = screen_dimensions

    @property
    def account_tenure(self):
        """Gets the account_tenure of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Data de cadastro do cliente na iniciadora.  # noqa: E501

        :return: The account_tenure of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: date
        """
        return self._account_tenure

    @account_tenure.setter
    def account_tenure(self, account_tenure):
        """Sets the account_tenure of this ConsentAuthorizationDataRiskSignals.

        Data de cadastro do cliente na iniciadora.  # noqa: E501

        :param account_tenure: The account_tenure of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: date
        """
        if account_tenure is None:
            raise ValueError("Invalid value for `account_tenure`, must not be `None`")  # noqa: E501

        self._account_tenure = account_tenure

    @property
    def geolocation(self):
        """Gets the geolocation of this ConsentAuthorizationDataRiskSignals.  # noqa: E501


        :return: The geolocation of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: RiskSignalsDataGeolocation
        """
        return self._geolocation

    @geolocation.setter
    def geolocation(self, geolocation):
        """Sets the geolocation of this ConsentAuthorizationDataRiskSignals.


        :param geolocation: The geolocation of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: RiskSignalsDataGeolocation
        """

        self._geolocation = geolocation

    @property
    def is_call_in_progress(self):
        """Gets the is_call_in_progress of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica chamada ativa no momento do vínculo.  [Restrição] Caso o sinal de risco esteja disponível (cliente permitiu que fosse coletado), o mesmo deverá ser enviado   # noqa: E501

        :return: The is_call_in_progress of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: bool
        """
        return self._is_call_in_progress

    @is_call_in_progress.setter
    def is_call_in_progress(self, is_call_in_progress):
        """Sets the is_call_in_progress of this ConsentAuthorizationDataRiskSignals.

        Indica chamada ativa no momento do vínculo.  [Restrição] Caso o sinal de risco esteja disponível (cliente permitiu que fosse coletado), o mesmo deverá ser enviado   # noqa: E501

        :param is_call_in_progress: The is_call_in_progress of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: bool
        """

        self._is_call_in_progress = is_call_in_progress

    @property
    def is_dev_mode_enabled(self):
        """Gets the is_dev_mode_enabled of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica se o dispositivo está em modo de desenvolvedor.  # noqa: E501

        :return: The is_dev_mode_enabled of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: bool
        """
        return self._is_dev_mode_enabled

    @is_dev_mode_enabled.setter
    def is_dev_mode_enabled(self, is_dev_mode_enabled):
        """Sets the is_dev_mode_enabled of this ConsentAuthorizationDataRiskSignals.

        Indica se o dispositivo está em modo de desenvolvedor.  # noqa: E501

        :param is_dev_mode_enabled: The is_dev_mode_enabled of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: bool
        """

        self._is_dev_mode_enabled = is_dev_mode_enabled

    @property
    def is_mock_gps(self):
        """Gets the is_mock_gps of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica se o dispositivo está usando um GPS falso.  # noqa: E501

        :return: The is_mock_gps of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: bool
        """
        return self._is_mock_gps

    @is_mock_gps.setter
    def is_mock_gps(self, is_mock_gps):
        """Sets the is_mock_gps of this ConsentAuthorizationDataRiskSignals.

        Indica se o dispositivo está usando um GPS falso.  # noqa: E501

        :param is_mock_gps: The is_mock_gps of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: bool
        """

        self._is_mock_gps = is_mock_gps

    @property
    def is_emulated(self):
        """Gets the is_emulated of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica se o dispositivo é emulado ou real.  # noqa: E501

        :return: The is_emulated of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: bool
        """
        return self._is_emulated

    @is_emulated.setter
    def is_emulated(self, is_emulated):
        """Sets the is_emulated of this ConsentAuthorizationDataRiskSignals.

        Indica se o dispositivo é emulado ou real.  # noqa: E501

        :param is_emulated: The is_emulated of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: bool
        """

        self._is_emulated = is_emulated

    @property
    def is_monkey_runner(self):
        """Gets the is_monkey_runner of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica o uso do MonkeyRunner.  # noqa: E501

        :return: The is_monkey_runner of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: bool
        """
        return self._is_monkey_runner

    @is_monkey_runner.setter
    def is_monkey_runner(self, is_monkey_runner):
        """Sets the is_monkey_runner of this ConsentAuthorizationDataRiskSignals.

        Indica o uso do MonkeyRunner.  # noqa: E501

        :param is_monkey_runner: The is_monkey_runner of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: bool
        """

        self._is_monkey_runner = is_monkey_runner

    @property
    def is_charging(self):
        """Gets the is_charging of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica se a bateria do dispositivo está sendo carregada.  # noqa: E501

        :return: The is_charging of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: bool
        """
        return self._is_charging

    @is_charging.setter
    def is_charging(self, is_charging):
        """Sets the is_charging of this ConsentAuthorizationDataRiskSignals.

        Indica se a bateria do dispositivo está sendo carregada.  # noqa: E501

        :param is_charging: The is_charging of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: bool
        """

        self._is_charging = is_charging

    @property
    def antenna_information(self):
        """Gets the antenna_information of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica em qual antena o dispositivo está conectado.  # noqa: E501

        :return: The antenna_information of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: str
        """
        return self._antenna_information

    @antenna_information.setter
    def antenna_information(self, antenna_information):
        """Sets the antenna_information of this ConsentAuthorizationDataRiskSignals.

        Indica em qual antena o dispositivo está conectado.  # noqa: E501

        :param antenna_information: The antenna_information of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: str
        """

        self._antenna_information = antenna_information

    @property
    def is_usb_connected(self):
        """Gets the is_usb_connected of this ConsentAuthorizationDataRiskSignals.  # noqa: E501

        Indica se o dispositivo está conectado a outro dispositivo via USB.  # noqa: E501

        :return: The is_usb_connected of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: bool
        """
        return self._is_usb_connected

    @is_usb_connected.setter
    def is_usb_connected(self, is_usb_connected):
        """Sets the is_usb_connected of this ConsentAuthorizationDataRiskSignals.

        Indica se o dispositivo está conectado a outro dispositivo via USB.  # noqa: E501

        :param is_usb_connected: The is_usb_connected of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: bool
        """

        self._is_usb_connected = is_usb_connected

    @property
    def integrity(self):
        """Gets the integrity of this ConsentAuthorizationDataRiskSignals.  # noqa: E501


        :return: The integrity of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :rtype: RiskSignalsDataIntegrity
        """
        return self._integrity

    @integrity.setter
    def integrity(self, integrity):
        """Sets the integrity of this ConsentAuthorizationDataRiskSignals.


        :param integrity: The integrity of this ConsentAuthorizationDataRiskSignals.  # noqa: E501
        :type: RiskSignalsDataIntegrity
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
        if issubclass(ConsentAuthorizationDataRiskSignals, dict):
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
        if not isinstance(other, ConsentAuthorizationDataRiskSignals):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
