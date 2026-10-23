# R011PAS

## Descrição

Programação das Compensações do Banco de Horas

---

## Resumo

- Campos: 10
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodBHr | Number(005,0) | Não | Código do Banco de Horas |
| IniCre | Date | Não | Início do Período de Crédito |
| FimCre | Date | Sim | Fim do Período de Crédito |
| SitCre | Number(003,0) | Não | Situação de Crédito |
| IniDeb | Date | Não | Início do Período de Débito |
| FimDeb | Date | Sim | Fim do Período de Débito |
| SitDeb | Number(003,0) | Não | Situação de Débito |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodBHr
- IniCre
- SitCre
- IniDeb
- SitDeb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R011PAS_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R011PAS_003

**Tabela:** R011BHR

| Origem | Destino |
|--------|---------|
| CodBHr | CodBHr |

