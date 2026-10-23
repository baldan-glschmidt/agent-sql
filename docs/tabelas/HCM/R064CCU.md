# R064CCU

## Descrição

Troca de Centro de Custo

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data Inicial da Troca de C.Custo |
| HorIni | Number(005,0) | Sim | Hora Inicial da Troca de C.Custo |
| DatFim | Date | Sim | Data Final da Troca de C.Custo |
| HorFim | Number(005,0) | Sim | Hora Final da Troca de C.Custo |
| CodCcu | String(018) | Sim | Código do Novo Centro de Custo |

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

### IR_R064CCU_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R064CCU_007

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

