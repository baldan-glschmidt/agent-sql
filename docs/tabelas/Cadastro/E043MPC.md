# E043MPC

## Descrição

Tabelas - Modelos de Planos

---

## Resumo

- Campos: 16
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodMpc | Number(004,0) | Não | Código do modelo de plano |
| DesMpc | String(040) | Não | Descrição do modelo de plano |
| TipPla | Number(001,0) | Não | Tipo do modelo de plano |
| IncCta | Number(004,0) | Sim | Valor de incremento para criação do código da conta |
| ModCtb | Number(004,0) | Sim | Código do modelo de plano contábil associado ao plano financeiro |
| MpcRef | String(001) | Sim | Indicativo que o modelo de plano é referencial |
| CodRef | String(010) | Sim | Código da instituição responsável pelo modelo de plano referencial |
| ObsMpc | String(250) | Sim | Observação do modelo de plano |
| SitMpc | String(001) | Não | Situação do modelo de plano |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela alteração |
| DatAlt | Date | Sim | Data da alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da alteração do registro |
| IntPos | String(001) | Sim | Indicativo se o registro integra no Gestão Safra |

---

## Chave Primária

- CodMpc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
