# R107CST

## Descrição

Perfil PDI - Customização

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
| CodPer | Number(004,0) | Não | Perfil de PDI Web |
| SeqCss | Number(002,0) | Não | Sequência do arquivo de customização |
| UrlCss | String(201) | Sim | URL do arquivo CSS usado para a customização do layout |

---

## Chave Primária

- CodPer
- SeqCss

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R107CST_000

**Tabela:** R107PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

