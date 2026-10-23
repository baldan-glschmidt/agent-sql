# R032TPO

## Descrição

Pagtos Terceiros - Outros Valores

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

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
| CodOut | Number(004,0) | Não | Código do Outro Valor |
| ValOut | Number(011,2) | Sim | Valor |

---

## Chave Primária

- NumEmp
- CodFil
- CmpPte
- TipCol
- NumCad
- SeqPte
- CodOut

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032TPO_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R032TPO_005

**Tabela:** R032TPG

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CmpPte | CmpPte |
| TipCol | TipCol |
| NumCad | NumCad |
| SeqPte | SeqPte |

### IR_R032TPO_006

**Tabela:** R010TOV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodOut | CodOut |

