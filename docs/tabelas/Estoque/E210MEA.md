# E210MEA

## Descrição

Estoques - Movimento de estoque agrupado

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqMea | Number(009,0) | Não | Identificador de registro |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Sim | Código da derivação |
| CodDep | String(010) | Sim | Código do depósito |
| DatMov | Date | Sim | Data da movimentação do estoque |
| SeqMov | Number(006,0) | Sim | Sequência de movimento na data de movimentação |

---

## Chave Primária

- SeqMea

---

## Índices

### E210MEAIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer
- CodDep

### E210MEAIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodPro
- CodDer
- CodDep
- DatMov
- SeqMov

---

## Relacionamentos

Nenhum relacionamento cadastrado.
