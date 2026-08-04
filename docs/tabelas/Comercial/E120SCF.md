# E120SCF

## Descrição

Vendas - Pedidos - Controle da simulação de frete

---

## Resumo

- Campos: 11
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
| SeqSml | Number(009,0) | Não | Sequência da simulação de frete |
| SitSml | Number(001,0) | Sim | Situação da simulação de frete |
| MsgErr | String(250) | Sim | Mensagem de erro da simulação de frete |
| MotCan | String(100) | Sim | Motivo de cancelamento da simulação de frete |
| XmlExp | Image | Sim | XML exportado na simulação de frete |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqSml

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
