# E120TRK

## Descrição

Vendas - Pedidos - Tracking

---

## Resumo

- Campos: 16
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
| CodTrk | String(050) | Não | Código do tracking |
| LinTrk | String(500) | Sim | Link do tracking |
| TipDoc | String(030) | Sim | Tipo de documento |
| SerDoc | String(020) | Sim | Série do documento |
| DocExt | String(030) | Sim | Número do documento externo |
| CodPla | Number(006,0) | Sim | Código do plano |
| CanTrk | String(001) | Sim | Indicativo se cancelou o tracking |
| TrfTrk | String(001) | Sim | Indicativo se transferiu o tracking |
| NumAne | Number(012,0) | Não | Número da análise de embarque |
| NumPfa | Number(009,0) | Não | Número da pré-fatura |
| UsuGer | Number(010,0) | Não | Usuário responsável pela geração do registro |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- CodTrk

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
