# R046ATC

## Descrição

Conversão Acidente de Trabalho

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
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatCnv | Date | Não | Data Conversão |
| CmpEso | Date | Não | Competência Periódicos eSocial |
| DscCnv | String(255) | Sim | Descrição |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatCnv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R046ATC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

