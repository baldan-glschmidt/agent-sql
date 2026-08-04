# E120RAT

## Descrição

Vendas - Pedidos - Rateios

---

## Resumo

- Campos: 24
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumPed | Number(008,0) | Não | Número do pedido |
| SeqRat | Number(004,0) | Não | Sequência do rateio do pedido |
| TnsPro | String(005) | Sim | Transação de produto |
| TnsSer | String(005) | Sim | Transação de serviço |
| SeqIpd | Number(004,0) | Sim | Sequência do item de produto |
| SeqIsp | Number(003,0) | Sim | Sequência do item de serviço |
| CriRat | Number(001,0) | Não | Critério utilizado para rateio |
| SomSub | Number(001,0) | Não | Somar ou subtrair o valor no plano financeiro/centro de custos |
| NumPrj | Number(008,0) | Sim | Número do projeto |
| CodFpj | Number(004,0) | Sim | Código da fase do projeto |
| CtaFin | Number(007,0) | Sim | Conta financeira reduzida |
| CtaRed | Number(007,0) | Sim | Conta contábil reduzida |
| PerCta | Number(007,4) | Sim | Percentual rateado para a conta |
| VlrCta | Number(015,2) | Sim | Valor rateado para a conta |
| CodCcu | String(009) | Sim | Código do centro de custos |
| PerRat | Number(007,4) | Sim | Percentual rateado para o centro de custos |
| VlrRat | Number(015,2) | Sim | Valor rateado para o centro de custos |
| ObsRat | String(120) | Sim | Observação do rateio |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| TipOri | String(001) | Sim | Origem do Rateio |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqRat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120RAT_002

**Tabela:** E120PED

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |

