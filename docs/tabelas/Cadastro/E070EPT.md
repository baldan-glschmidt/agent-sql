# E070EPT

## Descrição

Cadastros - Empresas - Parâmetros Patrimônio

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| PerFan | Date | Sim | Período bloqueado anterior da gestão de patrimônio na empresa |
| PerFec | Date | Sim | Período bloqueado da gestão de patrimônio na empresa |
| DatFec | Date | Sim | Data do processamento do bloqueio da gestão de patrimônio |
| HorFec | Number(005,0) | Sim | Hora do processamento do bloqueio da gestão de patrimônio |
| UsuFec | Number(010,0) | Sim | Usuário do bloqueio da gestão de patrimônio na empresa |
| BemUni | String(001) | Não | Indicativo que a empresa permite cadastrar bens com quantidade igual a 1(um). |
| VreBem | String(001) | Não | Indicativo se o bem(produto) deve herdar valor de entrada na NF de remessa |
| BloMov | String(001) | Não | Bloquear movimentação para bens que utilizam CIAP |

---

## Chave Primária

- CodEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
