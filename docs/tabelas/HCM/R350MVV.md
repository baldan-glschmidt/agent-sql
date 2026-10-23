# R350MVV

## Descrição

S-2299 - eSocial - Desligamento - Informação de múltiplos vínculos

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
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
| SeqMvv | Number(009,0) | Não | Sequência |
| SeqOcs | String(010) | Sim | Seq. Outros Contratos |
| IndMvi | Number(001,0) | Sim | Indicador de Desconto da Contribuição Previdenciária do Trabalhador |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqDes
- SeqMvv

---

## Índices

### R350MVVIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
