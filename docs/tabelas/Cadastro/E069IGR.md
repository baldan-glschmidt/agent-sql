# E069IGR

## Descrição

Tabelas - Convênios - Itens de Grupo de Produto/Serviço

---

## Resumo

- Campos: 16
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodGps | String(015) | Não | Código do Grupo de Produto/Serviço |
| SeqIgr | Number(005,0) | Não | Sequencia do Item de Grupo de Produto/Serviço |
| TipIgr | String(001) | Sim | Produto/Serviço |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodOri | String(003) | Sim | Código de Origem do Produto |
| CodFam | String(006) | Sim | Código da Família do Produto |
| CodAgc | String(005) | Sim | Código de agrupamento de materiais/produtos para compras ou vendas |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação do Produto (tamanho, cor, etc.) |
| CodSer | String(014) | Sim | Código do serviço |
| CodMar | String(010) | Sim | Código da Marca/Etiqueta vinculada a um produto ou a um pedido |
| CodClc | String(010) | Sim | Código da coleção |
| CodCor | Number(004,0) | Sim | Código da Cor |
| DatAlt | Date | Não | Data de Alteração |
| HorAlt | Number(005,0) | Não | Hora de Alteração |
| UsuAlt | Number(010,0) | Não | Usuário responsável pela última alteração |

---

## Chave Primária

- CodGps
- SeqIgr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
