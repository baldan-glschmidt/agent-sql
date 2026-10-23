# R511CST

## Descrição

Avaliação - Formulário de avaliação - customização

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
| CodPfa | Number(004,0) | Não | Perfil do formulário de avaliação |
| SeqCss | Number(002,0) | Não | Sequencia do arquivo de customização |
| UrlCss | String(201) | Sim | URL do arquivo CSS usado para a customização do layout |

---

## Chave Primária

- CodPfa
- SeqCss

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R511CST_000

**Tabela:** R511FAP

| Origem | Destino |
|--------|---------|
| CodPfa | CodPfa |

