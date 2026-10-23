# R910PMT

## Descrição

Permissões de tabelas (só para consultas)

---

## Resumo

- Campos: 9
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NomTbl | String(032) | Não | Nome da tabela |
| CodEnt | Number(010,0) | Não | Código da entidade. |
| PerCon | String(001) | Não | Permite consultar |
| PerIns | String(001) | Não | Permite Inserir |
| PerAlt | String(001) | Não | Permite Inserir |
| PerExc | String(001) | Não | Permite Excluir |
| PerCcp | String(001) | Não | Permite customizar campos |
| PerCIx | String(001) | Não | Permite customizar índices |
| AltPer | String(001) | Não | Alterar permissões |

---

## Chave Primária

- NomTbl
- CodEnt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
