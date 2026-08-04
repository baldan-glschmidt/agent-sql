# E000PDX

## Descrição

Gerais - Integração de pedidos com seniorX

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqItx | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| IdeUni | String(050) | Sim | Identificador único do pedido na integração com seniorX |
| SitGcp | Number(002,0) | Sim | Situação do pedido da última integração com GCP seniorX |
| DatGcp | Date | Sim | Data da última integração com GCP seniorX |
| HorGcp | Number(005,0) | Sim | Hora da última integração com GCP seniorX |
| DatGer | Date | Não | Data da geração do registro |
| HorGer | Number(005,0) | Não | Hora da geração do registro |

---

## Chave Primária

- SeqItx

---

## Índices

### E000PDXIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- NumPed

---

## Relacionamentos

Nenhum relacionamento cadastrado.
