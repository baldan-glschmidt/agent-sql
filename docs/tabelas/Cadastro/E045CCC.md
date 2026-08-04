# E045CCC

## Descrição

Tabelas - Relacionamento entre Centro Custo/Conta Auxiliar X Conta Contábil X Critério

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CtaAux | Number(009,0) | Não | Número reduzido da conta auxiliar |
| CodCcu | String(009) | Não | Código do centro de custos |
| CtaRed | Number(007,0) | Não | Número reduzido da conta contábil |
| CodCri | Number(006,0) | Não | Código do critério |
| CtaDeb | Number(007,0) | Sim | Número reduzido da conta de débito |
| CtaCre | Number(007,0) | Sim | Número reduzido da conta de crédito |

---

## Chave Primária

- CodEmp
- CodFil
- CtaAux
- CodCcu
- CtaRed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E045CCC_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

