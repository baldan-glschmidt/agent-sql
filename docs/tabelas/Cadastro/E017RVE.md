# E017RVE

## Descrição

Tabelas - Regiões de Venda

---

## Resumo

- Campos: 13
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodRve | String(003) | Não | Código da região de venda |
| NomRve | String(030) | Não | Nome da região de venda |
| AbrRve | String(010) | Não | Abreviatura da região de venda |
| SupRve | String(003) | Sim | Código da região superior |
| VenVmn | Number(015,2) | Sim | Valor mínimo permitido para as notas fiscais |
| RecVmt | Number(015,2) | Sim | Valor mínimo permitido para títulos do contas a receber |
| UsuGer | Number(010,0) | Sim | Usuário responsável pelo cadastro da região de venda |
| DatGer | Date | Sim | Data da geração |
| HorGer | Number(005,0) | Sim | Hora da geração |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodRve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
