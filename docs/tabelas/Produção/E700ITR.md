# E700ITR

## Descrição

Ficha - Modelo - Tabela de relacionamento entre derivações - Itens

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodTar | String(016) | Não | Código da tabela de relacionamento, utilizado p/ geração automatica ao combinar componentes do modelo |
| CodRlc | String(006) | Não | Código do relacionamento entre duas máscaras de derivações |
| CodDe1 | String(007) | Não | Código da primeira derivação associada ao relacionamento |
| CodDe2 | String(007) | Sim | Código da segunda derivação associada ao relacionamento |
| DatGer | Date | Sim | Data de geração/alteração do registro |
| HorGer | Number(005,0) | Sim | Hora de geração/alteração do registro |
| UsuGer | Number(010,0) | Sim | Código do usuário responsável pela geração/alteração do registro |

---

## Chave Primária

- CodEmp
- CodTar
- CodRlc
- CodDe1

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E700ITR_002

**Tabela:** E700TAR

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodTar | CodTar |
| CodRlc | CodRlc |

