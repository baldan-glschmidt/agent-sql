# R128ACU

## Descrição

Custos por Assunto - Geral

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAss | Number(004,0) | Não | Código do Assunto |
| CodOem | Number(008,0) | Não | Código da Entidade |
| CmpCus | Date | Não | Competência do Item de Custo |
| CodFlt | Number(003,0) | Sim | Código da Regra |
| ComCus | String(200) | Sim | Comentário |

---

## Chave Primária

- CodAss
- CodOem
- CmpCus

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R128ACU_000

**Tabela:** R128ASS

| Origem | Destino |
|--------|---------|
| CodAss | CodAss |

### IR_R128ACU_001

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

