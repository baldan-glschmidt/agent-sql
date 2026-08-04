# E068VAM

## Descrição

Tabelas - Valores para aprovação multinível

---

## Resumo

- Campos: 15
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| RotNap | Number(002,0) | Não | Código da rotina para controle de níveis de aprovação |
| CodAga | String(005) | Não | Código da forma de agrupamento para aprovação multinível |
| VlrFna | Number(015,2) | Não | Valor da faixa para a rotina de controle de níveis de aprovação |
| DesFna | String(100) | Sim | Descrição da faixa para a rotina de controle de níveis de aprovação |
| NivApr | String(250) | Sim | Níveis de aprovação exigidos para a faixa até da rotina de controle de aprovação |
| SitFna | String(001) | Não | Situação da faixa até da rotina de controle de níveis de aprovação |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última atualização |
| DatAtu | Date | Sim | Data da última atualização do cadastro |
| HorAtu | Number(005,0) | Sim | Hora/minuto da última atualização do cadastro |
| AprSeq | String(001) | Sim | Indicativo se o controle de aprovação se dará de forma sequêncial |
| NumAva | Number(008,0) | Sim | Número mínimo de avalistas |

---

## Chave Primária

- CodEmp
- RotNap
- CodAga
- VlrFna

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
