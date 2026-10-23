# R080EXC

## Descrição

Exceções do Quadro de Lotação

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| DatIni | Date | Não | Data Inicial da Exceção |
| EmpChe | Number(004,0) | Sim | Código da empresa do chefe |
| TipChe | Number(001,0) | Sim | Tipo do Colaborador Chefe |
| CadChe | Number(009,0) | Sim | Código do Colaborador Chefe |
| DatFim | Date | Sim | Data Final da Exceção |

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

### IR_R080EXC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

