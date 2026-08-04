# E000CCA

## Descrição

Tabelas - Integrações - Categorias de Crédito

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
| CodCca | String(003) | Não | Código da categoria do cliente para a análise de crédito |

---

## Chave Primária

- SeqInt

---

## Índices

### E000CCAIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodCca

---

## Relacionamentos

Nenhum relacionamento cadastrado.
