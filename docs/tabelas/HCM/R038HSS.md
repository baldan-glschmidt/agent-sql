# R038HSS

## Descrição

Histórico de Administradora

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodOem | Number(008,0) | Não | Código da Outra Empresa |
| DatIni | Date | Não | Data de Início do Histórico de Administradora |
| CodCct | Number(009,0) | Sim | Código do Centro de Trabalho |
| DatFim | Date | Sim | Data Final do Histórico de Administradora |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodOem
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038HSS_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R038HSS_003

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

