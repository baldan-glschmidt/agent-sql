# E026RAM

## Descrição

Tabelas - Ramos de Atividade

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRam | String(005) | Não | Código do ramo de atividade |
| DesRam | String(100) | Não | Descrição do ramo de atividade |
| AbrRam | String(010) | Não | Abreviatura do ramo de atividade |
| IndExp | Number(001,0) | Sim | Indicativo se o registro foi alterado para exportar para o palm |
| DatPal | Date | Sim | Data da última alteração para o Palmtop |
| HorPal | Number(005,0) | Sim | Hora/minuto da última alteração para o Palm |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela criação do ramo de atividade |
| DatGer | Date | Sim | Data da geração |
| HorGer | Number(005,0) | Sim | Hora da geração |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| USU_TipRbi | String(001) | Sim | Tipo do Ramo para o BI(Business Intelligence) |

---

## Chave Primária

- CodRam

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
