# E140ADQ

## Descrição

Tabelas - Notas Fiscais de Saída - Adquirentes

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSnf | String(003) | Não | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Não | Número da nota fiscal de saída |
| SeqAdq | Number(003,0) | Não | Sequência do Adquirente |
| CodCli | Number(009,0) | Não | Código do Cliente |
| IndDec | String(001) | Não | Indicador de declarante |
| PerAdq | Number(007,4) | Sim | Proporção adquirida individual |
| CreIbs | Number(015,2) | Sim | Valor Crédito IBS |
| CreCbs | Number(015,2) | Sim | Valor Crédito CBS |

---

## Chave Primária

- CodEmp
- CodFil
- CodSnf
- NumNfv
- SeqAdq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E140ADQ_002

**Tabela:** E020SNF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |

### IR_E140ADQ_003

**Tabela:** E140NFV

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSnf | CodSnf |
| NumNfv | NumNfv |

### IR_E140ADQ_005

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

