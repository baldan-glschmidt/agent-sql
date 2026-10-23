# R038HOC

## Descrição

Histórico de outros contratos

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatIni | Date | Não | Data início do outro contrato |
| DatTer | Date | Sim | Data término do outro contrato |
| OutCon | String(001) | Sim | Outro Contrato de Trabalho |
| OutTet | String(001) | Sim | Teto INSS no Outro Contrato |
| OutEmp | Number(004,0) | Sim | Código da Empresa no Outro Contrato |
| OutTip | Number(001,0) | Sim | Tipo do Colaborador no Outro Contrato |
| OutCad | Number(009,0) | Sim | Código do Cadastro no Outro Contrato |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
