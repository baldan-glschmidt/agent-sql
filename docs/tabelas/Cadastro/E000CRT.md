# E000CRT

## Descrição

Tabelas - Integrações - Carteiras de cobrança

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
| CodCrt | String(002) | Não | Código interno da carteira de cobrança |

---

## Chave Primária

- SeqInt

---

## Índices

### E000CRTIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- CodCrt

---

## Relacionamentos

Nenhum relacionamento cadastrado.
