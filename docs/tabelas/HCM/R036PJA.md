# R036PJA

## Descrição

Pensão Judicial - Ajuste de Pagamentos

---

## Resumo

- Campos: 12
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
| OriPen | String(001) | Sim | Origem (C,F,R,P,M) |
| TipPen | String(001) | Sim | Tipo pensão (N,F,D,P) |
| CodCal | Number(005,0) | Sim | Código cálculo origem |
| DatRf1 | Date | Sim | Data referência 1 origem |
| DatRf2 | Date | Sim | Data referência 2 origem |
| OpeAju | String(001) | Sim | Operação |
| ValAju | Number(011,2) | Sim | Valor do Ajuste |

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

### IR_R036PJA_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

