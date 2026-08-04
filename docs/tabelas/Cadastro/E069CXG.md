# E069CXG

## Descrição

Tabelas - Convênios X Grupos

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCnv | Number(004,0) | Não | Código do convênio |
| CodGps | String(015) | Não | Código do Grupo de Produto/Serviço |
| PerLpv | Number(005,2) | Sim | Percentual de participação |
| VlrLpv | Number(011,2) | Sim | Valor de participação |
| SitLpv | String(001) | Não | Situação da ligação (Ativo ou Inativo) |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAtu | Date | Sim | Data da última alteração do registro |
| HorAtu | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodCnv
- CodGps

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
