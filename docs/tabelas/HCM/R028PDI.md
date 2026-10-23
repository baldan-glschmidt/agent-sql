# R028PDI

## Descrição

Passes do Vale Transporte

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Código do Cadastro do Empregado |
| DatFal | Date | Não | Data da Falta |
| CodLin | Number(005,0) | Não | Código da Linha |
| ValPas | Number(008,2) | Sim | Valor dos Passes |
| QtdPas | Number(004,0) | Sim | Qtde de Passes Linha |
| ValMul | Number(008,2) | Sim | Valor dos Múltiplos |
| OriPvt | String(001) | Sim | Origem Faltas |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatFal
- CodLin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R028PDI_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R028PDI_004

**Tabela:** R028LVT

| Origem | Destino |
|--------|---------|
| CodLin | CodLin |

