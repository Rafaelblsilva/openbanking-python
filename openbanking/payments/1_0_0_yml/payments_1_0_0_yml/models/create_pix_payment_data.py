# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora  de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:   - Certificados exigidos para assinatura de mensagens:   [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Algoritmos usados para assinatura de mensagens `JWS`:   [Perfil de segurança FAPI - Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-financial-api-1_ID1.md#algorithm-considerations)  - Mensagens assinadas, `JWS` e `JWKS`:   [Guia de usuário (Receptoras e iniciadoras de pagamento)](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/tpp-user-guide.md#143-what-is-a-jwt-jwe-jws-and-jwk)    ## Controle de acesso    O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).    Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.       # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CreatePixPaymentData(object):
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
        'local_instrument': 'EnumLocalInstrument',
        'payment': 'PaymentPix',
        'creditor_account': 'CreditorAccount',
        'remittance_information': 'str',
        'qr_code': 'str',
        'proxy': 'str',
        'cnpj_initiator': 'str'
    }

    attribute_map = {
        'local_instrument': 'localInstrument',
        'payment': 'payment',
        'creditor_account': 'creditorAccount',
        'remittance_information': 'remittanceInformation',
        'qr_code': 'qrCode',
        'proxy': 'proxy',
        'cnpj_initiator': 'cnpjInitiator'
    }

    def __init__(self, local_instrument=None, payment=None, creditor_account=None, remittance_information=None, qr_code=None, proxy=None, cnpj_initiator=None):  # noqa: E501
        """CreatePixPaymentData - a model defined in Swagger"""  # noqa: E501
        self._local_instrument = None
        self._payment = None
        self._creditor_account = None
        self._remittance_information = None
        self._qr_code = None
        self._proxy = None
        self._cnpj_initiator = None
        self.discriminator = None
        self.local_instrument = local_instrument
        self.payment = payment
        self.creditor_account = creditor_account
        if remittance_information is not None:
            self.remittance_information = remittance_information
        if qr_code is not None:
            self.qr_code = qr_code
        if proxy is not None:
            self.proxy = proxy
        self.cnpj_initiator = cnpj_initiator

    @property
    def local_instrument(self):
        """Gets the local_instrument of this CreatePixPaymentData.  # noqa: E501


        :return: The local_instrument of this CreatePixPaymentData.  # noqa: E501
        :rtype: EnumLocalInstrument
        """
        return self._local_instrument

    @local_instrument.setter
    def local_instrument(self, local_instrument):
        """Sets the local_instrument of this CreatePixPaymentData.


        :param local_instrument: The local_instrument of this CreatePixPaymentData.  # noqa: E501
        :type: EnumLocalInstrument
        """
        if local_instrument is None:
            raise ValueError("Invalid value for `local_instrument`, must not be `None`")  # noqa: E501

        self._local_instrument = local_instrument

    @property
    def payment(self):
        """Gets the payment of this CreatePixPaymentData.  # noqa: E501


        :return: The payment of this CreatePixPaymentData.  # noqa: E501
        :rtype: PaymentPix
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """Sets the payment of this CreatePixPaymentData.


        :param payment: The payment of this CreatePixPaymentData.  # noqa: E501
        :type: PaymentPix
        """
        if payment is None:
            raise ValueError("Invalid value for `payment`, must not be `None`")  # noqa: E501

        self._payment = payment

    @property
    def creditor_account(self):
        """Gets the creditor_account of this CreatePixPaymentData.  # noqa: E501


        :return: The creditor_account of this CreatePixPaymentData.  # noqa: E501
        :rtype: CreditorAccount
        """
        return self._creditor_account

    @creditor_account.setter
    def creditor_account(self, creditor_account):
        """Sets the creditor_account of this CreatePixPaymentData.


        :param creditor_account: The creditor_account of this CreatePixPaymentData.  # noqa: E501
        :type: CreditorAccount
        """
        if creditor_account is None:
            raise ValueError("Invalid value for `creditor_account`, must not be `None`")  # noqa: E501

        self._creditor_account = creditor_account

    @property
    def remittance_information(self):
        """Gets the remittance_information of this CreatePixPaymentData.  # noqa: E501

        Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.   # noqa: E501

        :return: The remittance_information of this CreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._remittance_information

    @remittance_information.setter
    def remittance_information(self, remittance_information):
        """Sets the remittance_information of this CreatePixPaymentData.

        Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.   # noqa: E501

        :param remittance_information: The remittance_information of this CreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._remittance_information = remittance_information

    @property
    def qr_code(self):
        """Gets the qr_code of this CreatePixPaymentData.  # noqa: E501

        Obs: Campo reservado para uso futuro.   Sequência de caracteres que corresponde ao QR Code disponibilizado para o pagador.   É a sequência de caracteres que seria lida pelo leitor de QR Code, e deve propiciar o retorno dos dados do pagador após consulta na DICT.   Essa funcionalidade é possível tanto para QR Code estático quanto para QR Code dinâmico.   No arranjo do Pix esta é a mesma sequência gerada e/ou lida pela funcionalidade Pix Copia e Cola.   Este campo deverá ser no formato UTF-8.   [Restrição] Preenchimento obrigatório para pagamentos por QR Code, observado o tamanho máximo de 512 bytes.   # noqa: E501

        :return: The qr_code of this CreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._qr_code

    @qr_code.setter
    def qr_code(self, qr_code):
        """Sets the qr_code of this CreatePixPaymentData.

        Obs: Campo reservado para uso futuro.   Sequência de caracteres que corresponde ao QR Code disponibilizado para o pagador.   É a sequência de caracteres que seria lida pelo leitor de QR Code, e deve propiciar o retorno dos dados do pagador após consulta na DICT.   Essa funcionalidade é possível tanto para QR Code estático quanto para QR Code dinâmico.   No arranjo do Pix esta é a mesma sequência gerada e/ou lida pela funcionalidade Pix Copia e Cola.   Este campo deverá ser no formato UTF-8.   [Restrição] Preenchimento obrigatório para pagamentos por QR Code, observado o tamanho máximo de 512 bytes.   # noqa: E501

        :param qr_code: The qr_code of this CreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._qr_code = qr_code

    @property
    def proxy(self):
        """Gets the proxy of this CreatePixPaymentData.  # noqa: E501

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória.   No caso de telefone celular deve ser informado no padrão E.1641.   Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres.   No caso de CPF deverá ser informado com 11 números, sem pontos ou traços.   Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços.   No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223.   [Restrição] Obrigatório quando o campo localInstrument for igual a DICT.   # noqa: E501

        :return: The proxy of this CreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this CreatePixPaymentData.

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória.   No caso de telefone celular deve ser informado no padrão E.1641.   Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres.   No caso de CPF deverá ser informado com 11 números, sem pontos ou traços.   Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços.   No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223.   [Restrição] Obrigatório quando o campo localInstrument for igual a DICT.   # noqa: E501

        :param proxy: The proxy of this CreatePixPaymentData.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    @property
    def cnpj_initiator(self):
        """Gets the cnpj_initiator of this CreatePixPaymentData.  # noqa: E501

        CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix.  # noqa: E501

        :return: The cnpj_initiator of this CreatePixPaymentData.  # noqa: E501
        :rtype: str
        """
        return self._cnpj_initiator

    @cnpj_initiator.setter
    def cnpj_initiator(self, cnpj_initiator):
        """Sets the cnpj_initiator of this CreatePixPaymentData.

        CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix.  # noqa: E501

        :param cnpj_initiator: The cnpj_initiator of this CreatePixPaymentData.  # noqa: E501
        :type: str
        """
        if cnpj_initiator is None:
            raise ValueError("Invalid value for `cnpj_initiator`, must not be `None`")  # noqa: E501

        self._cnpj_initiator = cnpj_initiator

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
        if issubclass(CreatePixPaymentData, dict):
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
        if not isinstance(other, CreatePixPaymentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
