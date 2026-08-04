# E097MON

## Descrição

Cadastro - Pendências de Montagem

---

## Resumo

- Campos: 46
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFil | Number(005,0) | Não | Código da filial |
| NumMon | Number(008,0) | Não | Número de controle de montagem |
| SeqMon | Number(004,0) | Não | Sequência do documento de montagem |
| CodFor | Number(009,0) | Sim | Código do fornecedor que realizará a montagem |
| CodCli | Number(009,0) | Sim | Código do cliente |
| DatGer | Date | Sim | Data da geração da pendência |
| HorGer | Number(005,0) | Sim | Hora da geração da pendência |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração da pendência |
| SitMon | Number(001,0) | Sim | Situação da montagem |
| ProMon | Number(002,0) | Sim | Procedência do documento de montagem |
| CodFam | String(006) | Sim | Código da família do produto |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação do produto |
| QtdMon | Number(014,5) | Sim | Quantidade |
| VlrPmo | Number(015,2) | Sim | Valor padrão da montagem |
| ObsMon | String(250) | Sim | Texto da observação da montagem |
| FilNfv | Number(005,0) | Sim | Código da filial da nota fiscal de saída |
| CodSnf | String(003) | Sim | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Sim | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Sim | Seqüência do item na nota fiscal de saída |
| DatPrv | Date | Sim | Data de previsão de entrega do produto ou serviço |
| HorPrv | Number(005,0) | Sim | Hora do atendimento do movimento de estoque |
| FilPed | Number(005,0) | Sim | Código da Filial do Pedido de Venda |
| NumPed | Number(008,0) | Sim | Número do Pedido de Venda |
| SeqIpd | Number(004,0) | Sim | Item do Pedido |
| CodMot | Number(006,0) | Sim | Código do motivo do cancelamento total/parcial da montagem |
| ObsMot | String(250) | Sim | Observação do motivo do cancelamento total/parcial da montagem |
| DatCan | Date | Sim | Data do último cancelamento de determinada quantidade |
| HorCan | Number(005,0) | Sim | Hora do último cancelamento de determinada quantidade |
| VlrFmo | Number(015,2) | Sim | Valor final da montagem |
| EmpTcp | Number(004,0) | Sim | Código da empresa |
| FilTcp | Number(005,0) | Sim | Código da filial |
| NumTit | String(015) | Sim | Número do título a pagar |
| CodTpt | String(003) | Sim | Código do tipo do título a pagar |
| DatMon | Date | Sim | Data agendada para montagem |
| HorMon | Number(005,0) | Sim | Hora agendada para a montagem |
| EmpOcp | Number(004,0) | Sim | Código da empresa da ordem de compra |
| FilOcp | Number(005,0) | Sim | Código da filial da ordem de compra |
| NumOcp | Number(008,0) | Sim | Número da ordem de compra |
| SeqIso | Number(004,0) | Sim | Sequência do item de serviço na ordem de compra |
| TipEnd | Number(001,0) | Sim | Tipo do endereço onde se realizará a montagem |
| SeqEnd | Number(005,0) | Sim | Sequência do endereço onde se realizará a montagem |
| PrdMon | String(001) | Sim | Período de montagem |
| DatRea | Date | Sim | Data em que a montagem foi realizada |
| HorRea | Number(005,0) | Sim | Hora em que a montagem foi realizada |

---

## Chave Primária

- CodEmp
- CodFil
- NumMon
- SeqMon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_E097MON_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

