# R036PJT

## Descrição

Pensão Judicial - Terceiros

---

## Resumo

- Campos: 6
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
| CodDep | Number(002,0) | Não | Código do Dependente |
| SinBas | String(001) | Sim | Indica se o valor será somado ou diminuído para formar a base |
| BasPjt | Number(001,0) | Não | Valores que compõem a base de pensão do terceiro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep
- BasPjt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R036PJT_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

