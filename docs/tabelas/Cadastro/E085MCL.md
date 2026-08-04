# E085MCL

## Descrição

Cadastros - Clientes - Ligação Cliente X Marca

---

## Resumo

- Campos: 15
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCli | Number(009,0) | Não | Código do Cliente |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodMar | String(010) | Não | Código da Marca/Etiqueta |
| CodRep | Number(009,0) | Sim | Código do representante padrão para o cliente |
| CodTpr | String(004) | Sim | Código da tabela de preço padrão para o cliente |
| CodCpg | String(006) | Sim | Código da condição de pagamento padrão para o cliente |
| CodFpg | Number(002,0) | Sim | Código da forma de pagamento |
| CodTra | Number(009,0) | Sim | Código da transportadora padrão para o cliente |
| CodRed | Number(009,0) | Sim | Código da transportadora de redespacho padrão para o cliente |
| CodLip | String(005) | Sim | Código da lista de preço padrão para o cliente |
| BloPed | String(001) | Sim | Indicativo se o cliente está bloqueado para a entrada de novos pedidos |
| BloFat | String(001) | Sim | Indicativo se o cliente está bloqueado para faturamento |
| BloPrd | String(001) | Sim | Indicativo se o cliente está bloqueado para produção de novos pedidos |
| ObsCom | String(250) | Sim | Observação comercial |
| ObsPrd | String(250) | Sim | Observação Produção |

---

## Chave Primária

- CodCli
- CodEmp
- CodMar

---

## Índices

### E085MCLIndice1

**Tipo:** Não unico

Campos:
- CodMar

---

## Relacionamentos

### IR_E085MCL_000

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

### IR_E085MCL_002

**Tabela:** E076MAR

| Origem | Destino |
|--------|---------|
| CodMar | CodMar |

