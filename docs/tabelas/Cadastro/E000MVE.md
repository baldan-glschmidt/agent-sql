# E000MVE

## Descrição

Tabelas - Integrações - Movimentos de Estoque

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqInt | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| CodPro | String(014) | Não | Código do produto movimentado |
| CodDer | String(007) | Não | Código da derivação do produto movimentado |
| CodDep | String(010) | Não | Código do depósito movimentado |
| DatMov | Date | Não | Data da movimentação do estoque |
| SeqMov | Number(006,0) | Não | Sequência de movimento na data de movimentação |
| CodLot | String(050) | Sim | Código do lote de fabricação do produto |
| NumSep | String(050) | Sim | Número de série do produto |

---

## Chave Primária

- SeqInt

---

## Índices

### E000MVEIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodPro
- CodDer
- CodDep
- DatMov
- SeqMov
- CodLot
- NumSep

---

## Relacionamentos

Nenhum relacionamento cadastrado.
