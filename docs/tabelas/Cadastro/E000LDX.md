# E000LDX

## Descrição

Tabelas - Gerais - Log dos documentos enviadaos para integração com seniorX

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| TipIsx | Number(002,0) | Não | Tipo de integração com seniorX |
| TipCti | Number(009,0) | Não | Tipo de documento na integração com seniorX |
| SitIsx | String(001) | Sim | Situação da integração com seniorX |
| SeqItx | Number(009,0) | Não | Número sequencial dos registros de integração |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |
| IdeLlx | String(050) | Sim | Identificador do log de lote |

---

## Chave Primária

- IdeUni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
