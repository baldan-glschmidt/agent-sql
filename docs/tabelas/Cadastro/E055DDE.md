# E055DDE

## Descrição

Combinações dos Detalhamentos das Receitas/Deduções e Exclusões PIS/COFINS

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodDet | String(060) | Não | Código de detalhamento |
| DatCpt | Date | Não | Competência |
| SeqCon | Number(009,0) | Não | Sequência |
| CodTns | String(005) | Não | Código da transação |
| CodPro | String(014) | Não | Código do produto |
| CodSer | String(014) | Não | Código do serviço |
| CodCst | String(002) | Não | Código da situação tributária |
| AliPis | Number(015,4) | Não | Alíquota de PIS |
| AliCof | Number(015,4) | Não | Alíquota de COFINS |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |

---

## Chave Primária

- IdeUni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E055DDE_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E055DDE_002

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

### IR_E055DDE_005

**Tabela:** E055RDE

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| CodDet | CodDet |
| DatCpt | DatCpt |
| SeqCon | SeqCon |

