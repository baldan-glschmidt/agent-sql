# R083EXC

## Descrição

PPRA - Exceção das Atividades

---

## Resumo

- Campos: 11
- Chave Primária: 10 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpPpa | Date | Não | Competência do PPRA |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodGru | Number(007,0) | Não | Grupo de Atividades |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data de início da exceção do colaborador na atividade |
| DatTer | Date | Sim | Data de término da exceção do colaborador na atividade |

---

## Chave Primária

- NumEmp
- CmpPpa
- TabOrg
- NumLoc
- CodGru
- EstCar
- CodCar
- TipCol
- NumCad
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R083EXC_003

**Tabela:** R083ARI

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CmpPpa | CmpPpa |
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R083EXC_004

**Tabela:** R083ATV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodGru | CodAtv |

### IR_R083EXC_008

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

