# coding: utf-8

"""
    API Payment Initiation - Open Banking Brasil

    API de Iniciação de Pagamentos, responsável por viabilizar as operações de iniciação de pagamentos para o Open Banking Brasil.   Para cada uma das formas de pagamento previstas é necessário obter prévio consentimento do cliente através dos `endpoints` dedicados ao consentimento nesta API.  # Orientações No diretório de participantes duas `Roles` estão relacionadas à presente API:  - `CONTA`, referente às instituições detentoras de conta participantes do Open Banking Brasil; - `PAGTO`, referente às instituições iniciadoras de transação de pagamento de conta participantes do Open Banking Brasil.    Os tokens utilizados para consumo dos `endpoints` desta API devem possuir os `scopes` `openid` e `payments`.   Esta API não requer a implementação de `permissions` para sua utilização.   Todas as requisições e respostas devem ser assinadas seguindo o protocolo estabelecido na sessão <a href=\"https://openbanking-brasil.github.io/areadesenvolvedor/#assinaturas\" target=\"_blank\">Assinaturas</a> do guia de segurança.  ## Assinatura de payloads  No contexto da API Payment Initiation, os `payloads` de mensagem que trafegam tanto por parte da instituição iniciadora de transação de pagamento quanto por parte da instituição detentora  de conta devem estar assinados. Para o processo de assinatura destes `payloads` as instituições devem seguir as especificações de segurança publicadas no Portal do desenvolvedor:   - Certificados exigidos para assinatura de mensagens:   [Padrões de certificados digitais Open Banking Brasil](https://github.com/OpenBanking-Brasil/specs-seguranca/blob/main/open-banking-brasil-certificate-standards-1_ID1.md#certificado-de-assinatura-certificadoassinatura)  - Como assinar o payload JWS: [https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload](https://openbanking-brasil.github.io/areadesenvolvedor/#como-assinar-o-payload)  ## Controle de acesso    O endpoint de consulta de pagamento GET /pix/payments/{​​​paymentId}​​​ deve suportar acesso a partir de access_token emitido por meio de um grant_type do tipo `client credentials`, como opção do uso do token vinculado ao consentimento (hybrid flow).    Para evitar vazamento de informação, a detentora deve validar que o pagamento consultado pertence ao ClientId que o criou e, caso haja divergências, retorne um erro HTTP 400.       # noqa: E501

    OpenAPI spec version: 1.0.1-rc1.0
    Contact: gt-interfaces@openbankingbr.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Details(object):
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
        'qr_code': 'str',
        'proxy': 'str',
        'creditor_account': 'CreditorAccount'
    }

    attribute_map = {
        'local_instrument': 'localInstrument',
        'qr_code': 'qrCode',
        'proxy': 'proxy',
        'creditor_account': 'creditorAccount'
    }

    def __init__(self, local_instrument=None, qr_code=None, proxy=None, creditor_account=None):  # noqa: E501
        """Details - a model defined in Swagger"""  # noqa: E501
        self._local_instrument = None
        self._qr_code = None
        self._proxy = None
        self._creditor_account = None
        self.discriminator = None
        self.local_instrument = local_instrument
        if qr_code is not None:
            self.qr_code = qr_code
        if proxy is not None:
            self.proxy = proxy
        self.creditor_account = creditor_account

    @property
    def local_instrument(self):
        """Gets the local_instrument of this Details.  # noqa: E501


        :return: The local_instrument of this Details.  # noqa: E501
        :rtype: EnumLocalInstrument
        """
        return self._local_instrument

    @local_instrument.setter
    def local_instrument(self, local_instrument):
        """Sets the local_instrument of this Details.


        :param local_instrument: The local_instrument of this Details.  # noqa: E501
        :type: EnumLocalInstrument
        """
        if local_instrument is None:
            raise ValueError("Invalid value for `local_instrument`, must not be `None`")  # noqa: E501

        self._local_instrument = local_instrument

    @property
    def qr_code(self):
        """Gets the qr_code of this Details.  # noqa: E501

        Obs: Campo reservado para uso futuro.   Sequência de caracteres que corresponde ao QR Code disponibilizado para o pagador.   É a sequência de caracteres que seria lida pelo leitor de QR Code, e deve propiciar o retorno dos dados do pagador após consulta na DICT.   Essa funcionalidade é possível tanto para QR Code estático quanto para QR Code dinâmico.   No arranjo do Pix esta é a mesma sequência gerada e/ou lida pela funcionalidade Pix Copia e Cola.   Este campo deverá ser no formato UTF-8.   [Restrição] Preenchimento obrigatório para pagamentos por QR Code, observado o tamanho máximo de 512 bytes.   # noqa: E501

        :return: The qr_code of this Details.  # noqa: E501
        :rtype: str
        """
        return self._qr_code

    @qr_code.setter
    def qr_code(self, qr_code):
        """Sets the qr_code of this Details.

        Obs: Campo reservado para uso futuro.   Sequência de caracteres que corresponde ao QR Code disponibilizado para o pagador.   É a sequência de caracteres que seria lida pelo leitor de QR Code, e deve propiciar o retorno dos dados do pagador após consulta na DICT.   Essa funcionalidade é possível tanto para QR Code estático quanto para QR Code dinâmico.   No arranjo do Pix esta é a mesma sequência gerada e/ou lida pela funcionalidade Pix Copia e Cola.   Este campo deverá ser no formato UTF-8.   [Restrição] Preenchimento obrigatório para pagamentos por QR Code, observado o tamanho máximo de 512 bytes.   # noqa: E501

        :param qr_code: The qr_code of this Details.  # noqa: E501
        :type: str
        """

        self._qr_code = qr_code

    @property
    def proxy(self):
        """Gets the proxy of this Details.  # noqa: E501

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória.   No caso de telefone celular deve ser informado no padrão E.1641.   Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres.   No caso de CPF deverá ser informado com 11 números, sem pontos ou traços.   Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços.   No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223.   Se informado, a detentora da conta deve validar o proxy no DICT quando localInstrument for igual a DICT, QRDN (uso futuro) ou QRES (uso futuro) e validar o campo creditorAccount. Esta validação é opcional caso o localInstrument for igual a INIC.   [Restrição]   Se localInstrument for igual a MANU, o campo proxy não deve ser preenchido.   Se localInstrument for igual INIC, DICT, QRDN (uso futuro) ou QRES (uso futuro), o campo proxy deve ser sempre preenchido com a chave Pix.   # noqa: E501

        :return: The proxy of this Details.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this Details.

        Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória.   No caso de telefone celular deve ser informado no padrão E.1641.   Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres.   No caso de CPF deverá ser informado com 11 números, sem pontos ou traços.   Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços.   No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223.   Se informado, a detentora da conta deve validar o proxy no DICT quando localInstrument for igual a DICT, QRDN (uso futuro) ou QRES (uso futuro) e validar o campo creditorAccount. Esta validação é opcional caso o localInstrument for igual a INIC.   [Restrição]   Se localInstrument for igual a MANU, o campo proxy não deve ser preenchido.   Se localInstrument for igual INIC, DICT, QRDN (uso futuro) ou QRES (uso futuro), o campo proxy deve ser sempre preenchido com a chave Pix.   # noqa: E501

        :param proxy: The proxy of this Details.  # noqa: E501
        :type: str
        """

        self._proxy = proxy

    @property
    def creditor_account(self):
        """Gets the creditor_account of this Details.  # noqa: E501


        :return: The creditor_account of this Details.  # noqa: E501
        :rtype: CreditorAccount
        """
        return self._creditor_account

    @creditor_account.setter
    def creditor_account(self, creditor_account):
        """Sets the creditor_account of this Details.


        :param creditor_account: The creditor_account of this Details.  # noqa: E501
        :type: CreditorAccount
        """
        if creditor_account is None:
            raise ValueError("Invalid value for `creditor_account`, must not be `None`")  # noqa: E501

        self._creditor_account = creditor_account

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
        if issubclass(Details, dict):
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
        if not isinstance(other, Details):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
