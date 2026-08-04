# E069LPV

## Descrição

Cadastros - Convênios - Ligações Convênio x Produto

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCnv | Number(004,0) | Não | Código do convênio |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodPro | String(014) | Não | Código do produto do pedido |
| CodDer | String(007) | Não | Código da derivação do produto do pedido |
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
- CodEmp
- CodPro
- CodDer

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E069LPV_000

**Tabela:** E069CNV

| Origem | Destino |
|--------|---------|
| CodCnv | CodCnv |

