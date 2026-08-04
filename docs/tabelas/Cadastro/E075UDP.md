# E075UDP

## Descrição

Cadastros - Produtos - Unidades de Despacho do Produto

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto |
| CodDer | String(007) | Não | Código da derivação do Produto (tamanho, cor, etc.) |
| CodBar | Number(014,0) | Não | Código de barras da Unidade de Despacho |
| QtdUni | Number(011,2) | Não | Quantidade de unidades do produto para este código |
| ObsUdp | String(250) | Sim | Texto da observação |

---

## Chave Primária

- CodEmp
- CodPro
- CodDer
- CodBar

---

## Índices

### E075UDPIndice2

**Tipo:** Não unico

Campos:
- CodBar

---

## Relacionamentos

Nenhum relacionamento cadastrado.
