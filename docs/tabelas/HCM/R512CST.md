# R512CST

## Descrição

Consulta Web - Customização

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
| CodPer | Number(004,0) | Não | Perfil de Consulta Web |
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

### IR_R512CST_000

**Tabela:** R512PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

