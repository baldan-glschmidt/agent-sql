# E097PEN

## Descrição

Cadastro - Pendências para a Carga

---

## Resumo

- Campos: 47
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Código da empresa |
| DatGer | Date | Não | Data da geração da pendência |
| SeqPen | Number(004,0) | Não | Sequência da Pendência |
| TipPen | Number(001,0) | Não | Tipo de ação para a pendência |
| FilTit | Number(005,0) | Sim | Código da filial do título |
| NumTit | String(015) | Sim | Número do título a receber |
| CodTpt | String(003) | Sim | Código do tipo de título a receber |
| CodCli | Number(009,0) | Não | Código do cliente |
| CodPro | String(014) | Sim | Código do produto |
| CodDer | String(007) | Sim | Código da derivação do produto |
| UniMed | String(003) | Sim | Unidade de medida do produto |
| QtdPen | Number(014,5) | Sim | Quantidade |
| VlrPen | Number(015,2) | Sim | Valor da pendência |
| VlrJrs | Number(015,2) | Sim | Valor dos juros de mora |
| VlrMul | Number(015,2) | Sim | Valor da multa cobrada |
| SitPen | Number(001,0) | Sim | Situação da pendência |
| HorGer | Number(005,0) | Sim | Hora da geração da pendência |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração da pendência |
| ObsPen | String(250) | Sim | Texto da observação |
| CheBan | String(003) | Sim | Número do banco na FEBRABAN do cheque |
| CheAge | String(007) | Sim | Número da agência do banco do cheque |
| CheCta | String(014) | Sim | Número da conta no banco do cheque |
| CheNum | String(010) | Sim | Número do cheque no banco |
| CheDat | Date | Sim | Data do vencimento do cheque |
| SitChe | Number(001,0) | Sim | Situação Cheque |
| EmiChe | String(050) | Sim | Emitente do cheque |
| EmpNfv | Number(004,0) | Sim | Código da empresa da nota fiscal de saída |
| FilNfv | Number(005,0) | Sim | Código da filial da nota fiscal de saída |
| CodSnf | String(003) | Sim | Código da série da nota fiscal de saída |
| NumNfv | Number(009,0) | Sim | Número da nota fiscal de saída |
| SeqIpv | Number(003,0) | Sim | Sequência do item na nota fiscal de saída |
| NumCfi | Number(009,0) | Sim | Número do cupom fiscal de referência da redução Z |
| EmpPed | Number(004,0) | Sim | Código da empresa do pedido |
| FilPed | Number(005,0) | Sim | Código da filial do pedido |
| NumPed | Number(008,0) | Sim | Número do pedido |
| SeqIpd | Number(004,0) | Sim | Sequência de item do pedido |
| UsuAtd | Number(010,0) | Sim | Usuário atendente da pendência |
| DatAtd | Date | Sim | Data do atendimento da pendência |
| HorAtd | Number(005,0) | Sim | Hora do atendimento da pendência |
| CodRep | Number(009,0) | Sim | Código do representante do pedido |
| CodRoe | String(003) | Sim | Código da Rota ou Localidade do Cliente |
| CodSro | String(003) | Sim | Código da Sub Rota |
| IdeEnt | Number(009,0) | Sim | Número da Entrega |
| EmpOat | Number(004,0) | Não | Código da empresa da ocorrência de assistência técnica |
| FilOat | Number(005,0) | Não | Código da filial da ocorrência de assistência técnica |
| NumOcr | Number(009,0) | Não | Número da Ocorrência (Protocolo) |
| SeqIoc | Number(004,0) | Não | Sequência do item da ocorrência |

---

## Chave Primária

- CodEmp
- DatGer
- SeqPen

---

## Índices

### E097PENIndice1

**Tipo:** Não unico

Campos:
- CodCli

---

## Relacionamentos

### IR_E097PEN_000

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E097PEN_007

**Tabela:** E085CLI

| Origem | Destino |
|--------|---------|
| CodCli | CodCli |

