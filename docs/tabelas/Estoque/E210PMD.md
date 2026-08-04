# E210PMD

## Descrição

Estoques - Preço Médio Depósito

---

## Resumo

- Campos: 17
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificação do mov. preço médio depósito |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodDep | String(010) | Não | Código do depósito |
| CodFam | String(006) | Não | Código da família de produto |
| PrmAnt | Number(021,10) | Sim | Preço Médio Anterior do estoque por depósito. |
| QtdAnt | Number(014,5) | Sim | Quantidade em estoque total antes do fechamento |
| VlrAnt | Number(015,2) | Sim | Valor em estoque total antes do fechamento |
| PrmEst | Number(021,10) | Sim | Preço Médio do estoque por depósito. |
| QtdEst | Number(014,5) | Sim | Quantidade em estoque total após o fechamento |
| VlrEst | Number(015,2) | Sim | Valor em estoque total após o fechamento |
| DatFec | Date | Sim | Data base para o fechamento do estoque |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela atualização do registro |
| DatAtu | Date | Sim | Data da atualização do registro |
| HorAtu | Number(005,0) | Sim | Hora da atualização do registro |

---

## Chave Primária

- IdeUni

---

## Índices

### E210PMDindice1

**Tipo:** Unico

Campos:
- CodEmp
- CodDep
- CodFam

---

## Relacionamentos

Nenhum relacionamento cadastrado.
