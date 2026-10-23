# R350REI

## Descrição

S-2298 - eSocial - Reintegração/Outros Provimentos

---

## Resumo

- Campos: 26
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqRei | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfTra | Number(011,0) | Sim | Número do CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| MatTra | String(030) | Sim | Matrícula atribuída ao trabalhador pela empresa |
| TipRei | Number(001,0) | Sim | Tipo da reintegração |
| NumPro | String(021) | Sim | Número do processo, em caso de reintegração por determinação judicial |
| NumLei | String(013) | Sim | Número e Ano de publicação da Lei de Anistia |
| DatRet | Date | Sim | Data do efetivo retorno ao trabalho |
| DatRei | Date | Sim | Data a partir da qual o trabalhador deverá ser considerado como reintegrado |
| PagJui | String(001) | Sim | Pagamento Juízo |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Determina se envio é válido |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqRei

---

## Índices

### R350REIIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
