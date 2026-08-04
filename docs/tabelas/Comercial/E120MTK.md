# E120MTK

## Descrição

Vendas - Pedidos - Movimentações Tracking

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| CodTrk | String(050) | Não | Código do tracking |
| SeqMtk | Number(004,0) | Não | Sequência da movimentação tracking |
| CodFas | Number(006,0) | Sim | Código da fase |
| CanFas | String(001) | Sim | Indicativo se cancelou a fase |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- CodTrk
- SeqMtk

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
