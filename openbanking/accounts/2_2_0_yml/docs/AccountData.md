# AccountData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand_name** | **str** | Nome da Marca reportada pelo participante no Open Finance. Recomenda-se utilizar, sempre que possível, o mesmo nome de marca atribuído no campo do diretório Customer Friendly Server Name (Authorisation Server). | 
**company_cnpj** | **str** | Número completo do CNPJ da instituição responsável pelo Cadastro - o CNPJ corresponde ao número de inscrição no Cadastro de Pessoa Jurídica. Deve-se ter apenas os números do CNPJ, sem máscara | 
**type** | [**EnumAccountType**](EnumAccountType.md) |  | 
**compe_code** | **str** | Código identificador atribuído pelo Banco Central do Brasil às instituições participantes do STR (Sistema de Transferência de reservas).O Compe (Sistema de Compensação de Cheques e Outros Papéis) é um sistema que identifica e processa as compensações bancárias. Ele é representado por um código de três dígitos que serve como identificador de bancos, sendo assim, cada instituição bancária possui um número exclusivo | 
**branch_code** | **str** | Código da Agência detentora da conta. (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória)  [Restrição] Obrigatoriamente deve ser preenchido quando o campo \&quot;type\&quot; for diferente de CONTA_PAGAMENTO_PRE_PAGA.  | [optional] 
**number** | **str** | Número da conta | 
**check_digit** | **str** | Dígito da conta | 
**account_id** | **str** | Identifica de forma única  a conta do cliente, mantendo as regras de imutabilidade dentro da instituição transmissora. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

