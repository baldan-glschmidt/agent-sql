# E000FEC

## Descrição

Tabelas - Gerais - Controle de Fechamento de Período

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(005,0) | Não | Código da Filial |
| ModFec | String(003) | Não | Área ou gestão ao qual pertence o fechamento |
| SeqFec | Number(010,0) | Não | Sequência de geração do histórico do fechamento do período |
| DatFin | Date | Não | Data final do período fechado |
| DatIni | Date | Sim | Data inicial do período fechado |
| DatGer | Date | Não | Data de geração do registro de Fechamento de um período |
| HorGer | Number(005,0) | Não | Hora de geração do registro de fechamento |
| UsuGer | Number(010,0) | Não | Usuário que gerou o registro de fechamento do período |
| FecCan | String(001) | Não | Fechamento cancelado (Indica quando um período já fechado foi reaberto) |

---

## Chave Primária

- CodEmp
- CodFil
- ModFec
- SeqFec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
