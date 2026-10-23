# R032RCB

## Descrição

Recebimentos

---

## Resumo

- Campos: 36
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| CmpRcb | Date | Não | Competência Recebimento |
| SeqRcb | Number(003,0) | Não | Sequência do Recebimento |
| DatRcb | Date | Sim | Data de Emissão |
| NotFis | String(010) | Sim | Número da Nota Fiscal |
| ValRcb | Number(011,2) | Sim | Base Retenção |
| Ret11p | Number(011,2) | Sim | Valor Retenção |
| OriCmp | String(001) | Sim | Origem da Compensação (N, D, F) |
| Cmp13s | Number(011,2) | Sim | Valor Compensado na GPS de 13° Salário |
| CmpMes | Number(011,2) | Sim | Valor Compensado na GPS da Folha Normal |
| SerPre | Number(001,0) | Sim | Serviço Prestado |
| SerFis | String(005) | Sim | Número de Série |
| DatPag | Date | Sim | Data de Pagamento |
| SerObr | Number(001,0) | Sim | Prestação Serviço em Obra |
| NumCNO | Number(012,0) | Sim | Número Inscrição CNO |
| ValBru | Number(014,2) | Sim | Valor Bruto |
| ValSer | Number(014,2) | Sim | Valor Serviço |
| ValDed | Number(014,2) | Sim | Valor Deduções |
| ValMat | Number(014,2) | Sim | Valor Mat. e Equipamento |
| Bas15a | Number(014,2) | Sim | Base SAT 15 Anos |
| Val15a | Number(014,2) | Sim | Valor SAT 15 Anos |
| Bas20a | Number(014,2) | Sim | Base SAT 20 Anos |
| Val20a | Number(014,2) | Sim | Valor SAT 20 Anos |
| Bas25a | Number(014,2) | Sim | Base SAT 25 Anos |
| Val25a | Number(014,2) | Sim | Valor SAT 25 Anos |
| RetSub | Number(014,2) | Sim | Valor Ret. Subempreitada |
| CnpjSu | Number(015,0) | Sim | CNPJ do Subempreiteiro |
| CfjSub | String(014) | Sim | CNPJ do Subempreiteiro |
| TipPro | Number(001,0) | Sim | Tipo Inscrição Proprietário CNO |
| InsPro | Number(015,0) | Sim | Número Inscrição |
| CfjPro | String(014) | Sim | Número Inscrição |
| ValNRe | Number(014,2) | Sim | Valor Não Retido |
| NumPro | Number(009,0) | Sim | Número do Processo Judicial |
| OriReg | Number(001,0) | Sim | Origem do registro |

---

## Chave Primária

- NumEmp
- CodFil
- CodRat
- CmpRcb
- SeqRcb

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032RCB_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

