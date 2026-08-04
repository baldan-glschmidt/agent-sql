# E120SPA

## Descrição

Vendas - Pedidos - Situação Pedido na Análise de Crédito

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqSpa | Number(004,0) | Não | Sequência do situação do pedido na análise de crédito |
| DesSpa | String(999) | Sim | Descrição da situação do pedido na análise de crédito |
| SitPac | Number(002,0) | Não | Situação do pedido na análise de crédito |
| UsuGer | Number(010,0) | Sim | Código do usuário que gerou o registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SeqEnv | Number(004,0) | Sim | Sequência do envio do pedido para todos os autenticadores |
| MotSit | String(255) | Sim | Motivo da situação da análise de crédito do pedido |
| ParAna | String(255) | Sim | Parecer do analista de crédito |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqSpa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
