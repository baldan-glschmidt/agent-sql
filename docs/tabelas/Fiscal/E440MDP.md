# E440MDP

## Descrição

Compras - Notas Fiscais de Entrada - Manifesto Documento Fiscal - Parcelas

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodSma | String(003) | Não | Código da série do manifesto |
| NumMan | Number(009,0) | Não | Número do manifesto |
| NumPar | Number(003,0) | Não | Número da parcela do Manifesto |
| VctPar | Date | Sim | Data de vencimento da parcela do Manifesto |
| VlrPar | Number(015,2) | Sim | Valor da parcela do Manifesto |

---

## Chave Primária

- CodEmp
- CodFil
- CodSma
- NumMan
- NumPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E440MDP_003

**Tabela:** E440MDF

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodSma | CodSma |
| NumMan | NumMan |

