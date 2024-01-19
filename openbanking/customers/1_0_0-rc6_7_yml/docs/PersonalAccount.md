# PersonalAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compe_code** | **str** | Código identificador atribuído pelo Banco Central do Brasil às instituições participantes do STR (Sistema de Transferência de reservas).O Compe (Sistema de Compensação de Cheques e Outros Papéis) é um sistema que identifica e processa as compensações bancárias. Ele é representado por um código de três dígitos que serve como identificador de bancos, sendo assim, cada instituição bancária possui um número exclusivo | 
**branch_code** | **str** | Código da Agência detentora da conta. (Agência é a dependência destinada ao atendimento aos clientes, ao público em geral e aos associados de cooperativas de crédito, no exercício de atividades da instituição, não podendo ser móvel ou transitória)  | 
**number** | **str** | Número da conta  | 
**check_digit** | **str** | Dígito da conta  | 
**type** | [**BusinessAccountpropertiestype**](BusinessAccountpropertiestype.md) |  | 
**subtype** | **str** | Subtipo de conta (vide Enum):  Conta individual - possui um único titular Conta conjunta simples - onde as movimentações financeiras só podem serem realizadas mediante autorização de TODOS os correntistas da conta. Conta conjunta solidária - é a modalidade cujos titulares podem realizar movimentações de forma isolada, isto é, sem que seja necessária a autorização dos demais titulares. SEM_SUB_TIPO_CONTA - para reporte nos dados de identificação quando o cliente não possuir conta na instituição transmissora.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

