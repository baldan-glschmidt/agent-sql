# E120TMS

## Descrição

Tabelas - Integrações - Calculo de frete com o TMS

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TmsPed | Number(009,0) | Não | Sequência TMS |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| PedOri | String(015) | Sim | Código do pedido origem no TMS |
| NumPed | Number(008,0) | Sim | Número do pedido |
| CodSnf | String(003) | Sim | Código da série da nota fiscal |
| NumNfv | Number(009,0) | Sim | Número da nota fiscal de saída |
| PedCan | String(001) | Sim | Indica se o pedido foi cancelado no ERP |

---

## Chave Primária

- TmsPed

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
