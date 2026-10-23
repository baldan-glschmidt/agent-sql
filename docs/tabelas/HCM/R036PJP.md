# R036PJP

## Descrição

Pensão Judicial - Pagamentos

---

## Resumo

- Campos: 16
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodDep | Number(002,0) | Não | Código do dependente |
| SeqPag | Number(003,0) | Não | Sequência do Pagamento da Pensão |
| OriPen | String(001) | Sim | Origem (C,F,R,P) |
| TipPen | String(001) | Sim | Tipo pensão (N,F,D,P) |
| DatRf1 | Date | Sim | Data referência 1 origem |
| DatRf2 | Date | Sim | Data referência 2 origem |
| CodCal | Number(005,0) | Sim | Código cálculo origem |
| BasPen | Number(011,2) | Sim | Base de cálculo |
| ValPen | Number(011,2) | Sim | Valor calculado |
| CodFil | Number(006,0) | Sim | Código Filial |
| SeqPte | Number(003,0) | Sim | Sequência |
| CalSis | Number(001,0) | Sim | Cálculo do Sistema |
| DatRf3 | Date | Sim | Data referência 3 origem |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep
- SeqPag

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R036PJP_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

