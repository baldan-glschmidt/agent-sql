# R034ESR

## Descrição

Escala de Serviço

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatAlt | Date | Não | Data de Alteração da Escala |
| CodSeq | Number(003,0) | Não | Sequência (0 até 999) |
| DiaFol | String(001) | Sim | Dia de Folga |
| CodSrv | Number(004,0) | Sim | Código do Serviço |
| CodTSe | Number(002,0) | Sim | Turno de Serviço |
| TipFol | Number(002,0) | Sim | Tipo de Folga |
| SemIni | Number(002,0) | Sim | Semana Inicial |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt
- CodSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
