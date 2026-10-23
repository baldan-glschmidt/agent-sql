# R128GCU

## Descrição

Custos Geral - Geral

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
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| CodFlt | Number(003,0) | Sim | Código da Regra |
| ComCus | String(200) | Sim | Comentário |

---

## Chave Primária

- CodOem
- CmpCus

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128GCU_000

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

