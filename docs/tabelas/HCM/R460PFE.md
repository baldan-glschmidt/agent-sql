# R460PFE

## Descrição

Portal Web - Períodos de Férias - Programação

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
| IniPer | Date | Não | Início do Período Aquisitivo |
| PrgDat | Date | Não | Início Férias |
| PrgDfe | Number(004,2) | Sim | Dias de Férias |
| PrgDab | Number(004,2) | Sim | Dias de Abono Pecuniário |
| Prg13s | String(001) | Sim | Pagar Adiantamento 13° Salário |
| IndAut | String(001) | Sim | Indica se Está Autorizado |
| MsgCol | String(075) | Sim | Mensagem ao Colaborador |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniPer
- PrgDat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
