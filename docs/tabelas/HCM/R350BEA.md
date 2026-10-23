# R350BEA

## Descrição

S-2416 - Cadastro de Benefício - Entes Públicos - Alteração

---

## Resumo

- Campos: 30
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
| SeqBea | Number(009,0) | Não | Sequência |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfBen | Number(011,0) | Sim | Número do CPF do beneficiário |
| NroBen | String(020) | Não | Número do Benefício |
| DatAlt | Date | Não | Data Alteração do Benefício |
| TipBen | Number(004,0) | Não | Tipo Benefício |
| PanSeg | Number(001,0) | Não | Tipo de plano de segregação da massa |
| DscBen | String(255) | Sim | Descrição do instrumento ou situação que originou o pagamento do benefício |
| PenMor | Number(001,0) | Sim | Tipo de pensão por morte |
| IndSus | String(001) | Sim | Indicativo de suspensão do benefício |
| MtvSus | Number(002,0) | Sim | Motivo da suspensão do benefício |
| DscSus | String(255) | Sim | Descrição do motivo da suspensão do benefício |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvExc | String(001) | Sim | Exclusão realizada |
| EnvVal | String(001) | Sim | Determina se envio é válido |
| TipDep | Number(002,0) | Sim | Tipo de Dependente do Instituidor da Pensão por Morte |
| DesDep | String(100) | Sim | Descrição da Dependência do Instituidor da Pensão por Morte |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqBea

---

## Índices

### R350BEAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
