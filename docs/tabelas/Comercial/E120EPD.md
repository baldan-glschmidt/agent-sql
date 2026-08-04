# E120EPD

## Descrição

Vendas - Pedidos - Conteúdo das Embalagens

---

## Resumo

- Campos: 15
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
| SeqEmb | Number(006,0) | Não | Sequência de embalagem |
| SeqEpd | Number(004,0) | Não | Sequência do Conteúdo das Embalagens |
| SeqIpd | Number(004,0) | Sim | Sequência de item de produto do pedido |
| SeqEbi | Number(006,0) | Sim | Sequência da Embalagem Intermediária |
| SeqDls | Number(006,0) | Sim | Sequência de movimento de item |
| NumEmb | String(030) | Sim | Número da embalagem de Estocagem |
| QtdPro | Number(014,5) | Sim | Quantidade do produto na embalagem |
| VolIpd | Number(009,3) | Sim | Volume calculado do item |
| PesBru | Number(014,5) | Sim | Peso bruto do produto |
| PesLiq | Number(014,5) | Sim | Peso líquido do produto |
| ObsPro | String(250) | Sim | Texto da observação do produto na embalagem |
| SitEmb | Number(001,0) | Sim | Situação da Embalagem |

---

## Chave Primária

- CodEmp
- CodFil
- NumPed
- SeqEmb
- SeqEpd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E120EPD_003

**Tabela:** E120EMB

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFil | CodFil |
| NumPed | NumPed |
| SeqEmb | SeqEmb |

