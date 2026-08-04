# E120EAP

## Descrição

Vendas - Pedidos - Envio de Parcelas para Análise de Crédito Externa

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqEac | Number(004,0) | Não | Sequência de envio do pedido para análise de crédito externa |
| SeqPar | Number(003,0) | Não | Sequência da parcela |
| VctPar | Date | Sim | Data de vencimento da parcela |
| VlrPar | Number(015,2) | Sim | Valor da parcela |
| SitEac | Number(001,0) | Sim | Situação Envio |
| TipAec | Number(001,0) | Sim | Tipo do autenticador externo de crédito de clientes |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqEac
- SeqPar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120EAP_001

**Tabela:** E070FIL

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |

