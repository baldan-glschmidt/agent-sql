# R032OPF

## Descrição

Pagtos Outras Empresas - Rateio - Contas Financeiras

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
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPoe | Date | Não | Competência de Pagto O.Empresa |
| CodOem | Number(008,0) | Não | Código da Outra Empresa |
| SeqPoe | Number(003,0) | Não | Sequência |
| CodRat | Number(009,0) | Não | Código do Rateio |
| ConFin | Number(007,0) | Não | Conta Financeira |
| PerFin | Number(005,2) | Sim | % Conta Financeira |

---

## Chave Primária

- NumEmp
- CodFil
- CmpPoe
- CodOem
- SeqPoe
- CodRat
- ConFin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032OPF_005

**Tabela:** R032OPR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CmpPoe | CmpPoe |
| CodOem | CodOem |
| SeqPoe | SeqPoe |
| CodRat | CodRat |

