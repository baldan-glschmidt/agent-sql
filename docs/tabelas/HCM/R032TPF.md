# R032TPF

## Descrição

Pagtos Terceiros - Rateio - Contas Financeiras

---

## Resumo

- Campos: 9
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPte | Date | Não | Competência de Pagto Terceiro |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Terceiro |
| SeqPte | Number(003,0) | Não | Sequência |
| CodRat | Number(009,0) | Não | Código do Rateio |
| ConFin | Number(007,0) | Não | Conta Financeira |
| PerFin | Number(005,2) | Sim | % Conta Financeira |

---

## Chave Primária

- NumEmp
- CodFil
- CmpPte
- TipCol
- NumCad
- SeqPte
- CodRat
- ConFin

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032TPF_006

**Tabela:** R032TPR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CmpPte | CmpPte |
| TipCol | TipCol |
| NumCad | NumCad |
| SeqPte | SeqPte |
| CodRat | CodRat |

