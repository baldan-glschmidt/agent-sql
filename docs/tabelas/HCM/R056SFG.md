# R056SFG

## Descrição

Saque do FGTS

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CmpSaq | Date | Não | Competência do Saque |
| ValSaq | Number(011,2) | Sim | Valor do Saque Efetuado |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpSaq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R056SFG_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

