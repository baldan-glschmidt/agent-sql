# E700CBN

## Descrição

Ficha - Modelo - Combinações de Componentes

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodMod | String(014) | Não | Código do Modelo associado ao Produto |
| CodCbn | Number(006,0) | Não | Código da combinação, gerado automaticamente ao combinar componentes do modelo |
| CodAgm | String(005) | Sim | Código de agrupamento de preço para geração da tabela de preço |
| CodClf | String(003) | Sim | Código interno da classificação fiscal do produto |
| CodUsu | Number(010,0) | Não | Código do Usuário que alterou |
| DatGer | Date | Não | Data Geração ou Alteração da ligação |
| HorGer | Number(005,0) | Não | Hora da geração/última alteração do registro |
| CodReg | Number(004,0) | Sim | Código da regra |
| SitCbn | String(001) | Não | Situação da Combinação (Ativo ou Inativo) |

---

## Chave Primária

- CodEmp
- CodMod
- CodCbn

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E700CBN_001

**Tabela:** E700MOD

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodMod | CodMod |

