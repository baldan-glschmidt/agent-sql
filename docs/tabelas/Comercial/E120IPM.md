# E120IPM

## Descrição

Vendas - Pedidos - Itens abertos para MRP

---

## Resumo

- Campos: 20
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
| SeqIpd | Number(004,0) | Não | Sequência de item do pedido |
| SeqIpm | Number(004,0) | Não | Sequência de item do pedido aberto para MRP |
| QtdPoc | Number(014,5) | Sim | Quantidade do produto do pedido a ser produzida ou comprada |
| QtdXpl | Number(014,5) | Sim | Quantidade Explodida no Cálculo de Necessidades (Já feito a Explosão de Nec.) |
| DatEnt | Date | Não | Data de previsão de entrega para o produto do pedido |
| USU_UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| USU_DatGer | Date | Sim | Data da geração do registro |
| USU_HorGer | Number(005,0) | Sim | Hora da geração do registro |
| USU_UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| USU_DatAlt | Date | Sim | Data da última alteração do registro |
| USU_HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |
| USU_DatPrg | Date | Sim | Data Programação Sequenciamento do Mancal |
| USU_CODCEL | Number(004,0) | Sim | Código da Célula |
| USU_SEQPRG | Number(004,0) | Sim | Sequencia Programação do Dia |
| USU_RELPRD | String(015) | Sim | Nome Relatório |
| USU_SITIPM | String(001) | Sim | Situação do Item de pedido da tabela MRP |
| USU_IndGer | String(001) | Sim | Indicativo gerado componente |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqIpd
- SeqIpm

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
