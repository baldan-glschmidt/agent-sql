# R026VLR

## Descrição

Valores Gerais

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ComVlr | Date | Não | Competência Valores Gerais |
| CodVlr | Number(003,0) | Não | Código do Valor Geral |
| DesVlr | String(040) | Sim | Nome do Valor Geral |
| ValVlr | Number(011,2) | Sim | Valor Geral |

---

## Chave Primária

- ComVlr
- CodVlr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R026VLR_000

**Tabela:** R026VLG

| Origem | Destino |
|--------|---------|
| ComVlr | ComVlr |

