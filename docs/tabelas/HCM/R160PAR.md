# R160PAR

## Descrição

BS - Parcelas dos Empréstimos

---

## Resumo

- Campos: 9
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CmpEpt | Date | Não | Competência do Empréstimo |
| SeqEpt | Number(002,0) | Não | Sequência do Empréstimo |
| NumPar | Number(003,0) | Não | Número da Parcela |
| CodCal | Number(005,0) | Sim | Código de Cálculo |
| VlrPar | Number(011,2) | Sim | Valor da Parcela |
| VlrJur | Number(011,2) | Sim | Valor dos Juros |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpEpt
- SeqEpt
- NumPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R160PAR_004

**Tabela:** R160EPT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CmpEpt | CmpEpt |
| SeqEpt | SeqEpt |

