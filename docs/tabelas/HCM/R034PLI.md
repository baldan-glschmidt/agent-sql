# R034PLI

## Descrição

Percentuais Livres do Empregado

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CodPer | Number(002,0) | Não | Código do Percentual Livre |
| DesPer | String(030) | Sim | Descrição do Percentual Livre |
| PerLiv | Number(007,4) | Sim | Percentual Livre |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034PLI_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

