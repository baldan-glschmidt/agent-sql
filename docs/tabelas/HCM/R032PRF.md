# R032PRF

## Descrição

Produção - Rateio - Contas Financeiras

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipRot | Number(001,0) | Não | Tipo de Rotina |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPrd | Date | Não | Competência |
| SeqPrd | Number(005,0) | Não | Sequência |
| CodRat | Number(009,0) | Não | Código do Rateio |
| ConFin | Number(007,0) | Não | Conta Financeira |
| PerFin | Number(005,2) | Sim | % Conta Financeira |

---

## Chave Primária

- NumEmp
- CodFil
- TipRot
- CmpPrd
- SeqPrd
- CodRat
- ConFin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032PRF_005

**Tabela:** R032PRR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| TipRot | TipRot |
| CmpPrd | CmpPrd |
| SeqPrd | SeqPrd |
| CodRat | CodRat |

