# R350ATC

## Descrição

S-2240 - eSocial - Condições Ambientais do Trabalho - Ambientes

---

## Resumo

- Campos: 14
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
| SeqAtc | Number(009,0) | Não | Sequência Ambiente |
| CodAmb | String(030) | Sim | Código do ambiente no qual o trabalhador está desempenhando as atividades (Obsoleto) |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| LocAmb | Number(001,0) | Sim | Tipo de estabelecimento do ambiente de trabalho |
| DscSet | String(100) | Sim | Descrição do lugar administrativo onde o trabalhador exerce suas atividades |
| TpInAm | Number(001,0) | Sim | Código correspondente ao tipo de inscrição do ambiente |
| NrInAm | Number(015,0) | Sim | Número de inscrição onde está localizado o ambiente - Obsoleto |
| CfjAmb | String(014) | Sim | Número de inscrição onde está localizado o ambiente |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- DatIni
- SeqCon
- SeqAtc

---

## Índices

### R350ATCIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
