# R161LEV

## Descrição

Bs - Levantamento S.E. Despesas

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| DatIni | Date | Não | Data Inicial do Atendimento |
| HorIni | Number(005,0) | Não | Hora Inicial do Atendimento |
| CodDes | Number(003,0) | Não | Código Despesa |
| CmpDes | Date | Não | Competência da Despesa |
| VlrDes | Number(011,2) | Sim | Valor Despesa |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni
- CodDes
- CmpDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R161LEV_004

**Tabela:** R161ATE

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| DatIni | DatIni |
| HorIni | HorIni |

### IR_R161LEV_005

**Tabela:** R161DES

| Origem | Destino |
|--------|---------|
| CodDes | CodDes |

