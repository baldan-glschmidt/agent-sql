# R350SSA

## Descrição

S-2399 - eSocial - Trabalhador Sem Vínculo de Emprego/Estatutário - Término - Plano Saúde

---

## Resumo

- Campos: 13
- Chave Primária: 8 campo(s)
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
| SeqRsv | Number(009,0) | Não | Sequência |
| SeqPsv | Number(009,0) | Não | Sequência |
| SeqSvl | Number(009,0) | Não | Sequência |
| SeqSau | Number(009,0) | Não | Sequência |
| CnpjOP | Number(015,0) | Sim | CNPJ da Operadora do Plano de Saúde |
| CfjIns | String(014) | Sim | CNPJ da Operadora do Plano de Saúde |
| RegAns | Number(006,0) | Sim | Registro da operadora na ANS |
| ValTit | Number(014,2) | Sim | Valor pago pelo titular |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqRsv
- SeqPsv
- SeqSvl
- SeqSau

---

## Índices

### R350SSAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
