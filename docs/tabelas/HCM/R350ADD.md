# R350ADD

## Descrição

S-2299 - eSocial - Identificação dos advogados

---

## Resumo

- Campos: 12
- Chave Primária: 7 campo(s)
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
| SeqDes | Number(009,0) | Não | Sequência |
| SeqRec | Number(009,0) | Não | Sequência |
| SeqAdd | Number(009,0) | Não | Sequência |
| TipIns | Number(001,0) | Sim | Tipo de inscrição do Advogado |
| NumIns | Number(014,0) | Sim | Número de inscrição do Advogado |
| CfjIns | String(014) | Sim | Número de inscrição do Advogado |
| ValAdv | Number(014,2) | Sim | Valor da despesa com advogados |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqDes
- SeqRec
- SeqAdd

---

## Índices

### R350ADDIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
