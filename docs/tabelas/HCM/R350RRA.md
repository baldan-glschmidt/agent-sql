# R350RRA

## Descrição

S-2240 - eSocial - Condições Ambientais do Trabalho - Responsáveis

---

## Resumo

- Campos: 15
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data em que o trabalhador iniciou as atividades no ambiente de trabalho |
| SeqCon | Number(009,0) | Não | Sequência |
| SeqRra | Number(009,0) | Não | Sequência Responsável |
| CpfRsp | Number(011,0) | Sim | CPF do responsável pelos registros ambientais |
| NisRsp | Number(011,0) | Sim | NIS do responsável pelos registros ambientais (Obsoleto) |
| NomRsp | String(070) | Sim | Nome do responsável pelos registros ambientais (Obsoleto) |
| IdeCon | Number(001,0) | Sim | Órgão de classe ao qual o responsável pelos registros ambientais está vinculado |
| SigCon | String(020) | Sim | Sigla do órgão de classe ao qual o responsável pelos registros ambientais está vinculado |
| NumCon | String(014) | Sim | Número de inscrição do responsável pelos registros ambientais no órgão de classe |
| EstCon | String(002) | Sim | UF de expedição do órgão de classe do responsável pelos registros ambientais |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- DatIni
- SeqCon
- SeqRra

---

## Índices

### R350RRAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
