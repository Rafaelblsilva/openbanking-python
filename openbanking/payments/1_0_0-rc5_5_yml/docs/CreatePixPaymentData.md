# CreatePixPaymentData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_instrument** | [**EnumLocalInstrument**](EnumLocalInstrument.md) |  | 
**payment** | [**PaymentPix**](PaymentPix.md) |  | 
**creditor_account** | [**CreditorAccount**](CreditorAccount.md) |  | 
**remittance_information** | **str** | Deve ser preenchido sempre que o usuário pagador inserir alguma informação adicional em um pagamento, a ser enviada ao recebedor.  | [optional] 
**qr_code** | **str** | Obs: Campo reservado para uso futuro.   Sequência de caracteres que corresponde ao QR Code disponibilizado para o pagador.   É a sequência de caracteres que seria lida pelo leitor de QR Code, e deve propiciar o retorno dos dados do pagador após consulta na DICT.   Essa funcionalidade é possível tanto para QR Code estático quanto para QR Code dinâmico.   No arranjo do Pix esta é a mesma sequência gerada e/ou lida pela funcionalidade Pix Copia e Cola.   Este campo deverá ser no formato UTF-8.   [Restrição] Preenchimento obrigatório para pagamentos por QR Code, observado o tamanho máximo de 512 bytes.  | [optional] 
**proxy** | **str** | Chave cadastrada no DICT pertencente ao recebedor. Os tipos de chaves podem ser: telefone, e-mail, cpf/cnpj ou chave aleatória.   No caso de telefone celular deve ser informado no padrão E.1641.   Para e-mail deve ter o formato xxxxxxxx@xxxxxxx.xxx(.xx) e no máximo 77 caracteres.   No caso de CPF deverá ser informado com 11 números, sem pontos ou traços.   Para o caso de CNPJ deverá ser informado com 14 números, sem pontos ou traços.   No caso de chave aleatória deve ser informado o UUID gerado pelo DICT, conforme formato especificado na RFC41223.   [Restrição] Obrigatório quando o campo localInstrument for igual a DICT.  | [optional] 
**cnpj_initiator** | **str** | CNPJ do Iniciador de Pagamento devidamente habilitado para a prestação de Serviço de Iniciação no Pix. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

