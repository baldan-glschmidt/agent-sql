# E900POP

## Descrição

O.P./O.S. - Pedidos da O.P./O.S.

---

## Resumo

- Campos: 16
- Chave Primária: 12 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da Empresa |
| CodOri | String(003) | Não | Origem do Produto/Serviço da O.P./O.S. |
| NumOrp | Number(009,0) | Não | Número da Ordem de Produção/Serviço |
| CodFil | Number(005,0) | Não | Código da Filial do Pedido |
| NumPed | Number(008,0) | Não | Número do Pedido |
| SeqIpd | Number(004,0) | Não | Item do Pedido (quando O.P./O.S. atende Pedido específico) |
| CodPvp | String(008) | Não | Código do Período |
| PvpPai | String(008) | Não | Código do Período gerador (Procedente) quando é necessário produtos intermediários |
| AgrNec | String(025) | Não | Agrupamento de necessidades |
| AgrPai | String(025) | Não | Agrupamento de necessidades pai |
| CodPro | String(014) | Não | Código do Produto/Serviço |
| CodDer | String(007) | Não | Código de Derivação do Produto |
| QtdPrv | Number(014,5) | Não | Quantidade Prevista por Derivação |
| CodFxa | String(015) | Sim | Código da faixa da grade |
| CodPgr | String(005) | Sim | Código da Proporcionalidade da Grade de Derivações |
| IdxGrd | Number(006,0) | Sim | Indexador da Grade |

---

## Chave Primária

- CodEmp
- CodOri
- NumOrp
- CodFil
- NumPed
- SeqIpd
- CodPvp
- PvpPai
- CodPro
- CodDer
- AgrNec
- AgrPai

---

## Índices

### E900POPIndice2

**Tipo:** Não unico

Campos:
- CodEmp
- CodFil
- NumPed
- SeqIpd
- CodPro
- CodDer

---

## Relacionamentos

### IR_E900POP_001

**Tabela:** E083ORI

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodOri | CodOri |

### IR_E900POP_006

**Tabela:** E016PVP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPvp | CodPvp |

### IR_E900POP_011

**Tabela:** E075DER

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodPro | CodPro |
| CodDer | CodDer |

