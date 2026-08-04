# E000MPV

## Descrição

Tabelas - Integrações - Marcas de Produtos

---

## Resumo

- Campos: 4
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
| CodMar | String(010) | Não | Código da Marca/Etiqueta vinculada a um produto ou a um pedido |

---

## Chave Primária

- SeqInt

---

## Índices

### E000MPVIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodMar

---

## Relacionamentos

Nenhum relacionamento cadastrado.
