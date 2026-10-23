# R950CTD

## Descrição

Mobile - Configuração detalhes

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTkn | String(120) | Não | Código token - tabela detalhe |
| CodPar | String(120) | Não | Código do parâmetro |
| ValPar | String(255) | Sim | Valor do parâmetro |

---

## Chave Primária

- CodTkn
- CodPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R950CTD_000

**Tabela:** R950CTM

| Origem | Destino |
|--------|---------|
| CodTkn | CodTkn |

