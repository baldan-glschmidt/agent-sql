# E705SVA

## Descrição

Ficha - Modelo - Variações Consumo - Seqüências

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodMdp | String(008) | Não | Código da máscara de derivação |
| CodVac | String(005) | Não | Código da variação p/ utilização no consumo do modelo |
| CodDer | String(007) | Não | Código da derivação p/ atribuir variação de consumo |
| SeqCmd | Number(007,0) | Não | Ordenação seqüencial da derivação (na máscara de derivação) |
| VlrVar | Number(009,6) | Sim | Valor da variação de consumo atribuída à derivação de produto na máscara |

---

## Chave Primária

- CodEmp
- CodMdp
- CodVac
- CodDer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
