# E700TAR

## Descrição

Ficha - Modelo - Tabela de relacionamento entre derivações

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodTar | String(016) | Não | Código da tabela de relacionamento, utilizado p/ geração automatica ao combinar componentes do modelo |
| CodRlc | String(006) | Não | Código do relacionamento entre duas máscaras de derivações |
| DesRlc | String(040) | Não | Descrição do código do relacionamento |
| CodFam | String(006) | Sim | Código da Família de produto ao qual a tabela pertence |
| CodMd1 | String(008) | Não | Código da primeira máscara de derivação permitida p/ relacionamento |
| CodMd2 | String(008) | Não | Código da segunda máscara de derivação permitida p/ relacionamento |
| DatGer | Date | Sim | Data de geração/alteração do registro |
| HorGer | Number(005,0) | Sim | Hora de geração/alteração do registro |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pela geração/alteração do registro |
| SitRlc | String(001) | Sim | Situação da tabela de relacionamento |

---

## Chave Primária

- CodEmp
- CodTar
- CodRlc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
