# E120FPP

## Descrição

Vendas - Pedidos - Fila paralela para geracao de notas/pré-faturas

---

## Resumo

- Campos: 13
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | String(050) | Não | Identificador único alfanumérico |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| MsgGer | String(999) | Sim | Mensagem da geração do registro |
| QtdTtv | Number(004,0) | Sim | Quantidade total de tentativas de movimentação já efetuadas |
| QtdTat | Number(004,0) | Sim | Quantidade de tentativas desde que foi zerado o contador |
| PrcDes | Number(001,0) | Sim | Processo destino |
| DatAlt | Date | Sim | Data da última tentativa |
| HorAlt | Number(005,0) | Sim | hora da última tentativa |
| CodPra | Number(004,0) | Sim | Código do processo que executou |

---

## Chave Primária

- IdeUni

---

## Índices

### E120FPPIndice1

**Tipo:** Unico

Campos:
- CodEmp
- CodFil
- NumPed

---

## Relacionamentos

Nenhum relacionamento cadastrado.
