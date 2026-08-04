# E000LPV

## Descrição

Tabelas - Integrações - Convênio X Produto

---

## Resumo

- Campos: 6
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
| CodCnv | Number(004,0) | Não | Código do convênio |
| CodPro | String(014) | Não | Código do produto do pedido |
| CodDer | String(007) | Não | Código da derivação do produto do pedido |

---

## Chave Primária

- SeqInt

---

## Índices

### E000LPVIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodCnv
- CodPro
- CodDer

---

## Relacionamentos

Nenhum relacionamento cadastrado.
