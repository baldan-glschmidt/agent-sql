# R054GRP

## Descrição

GPS

---

## Resumo

- Campos: 41
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| ComGrp | Date | Não | Competência GRPS |
| OriSal | Number(002,0) | Não | Código de Origem |
| CodOem | Number(008,0) | Não | Código da Outra Empresa |
| SeqReg | Number(002,0) | Não | Sequência do Registro da GPS |
| ComPag | Date | Sim | Competência de Pagto |
| AciTra | Number(007,0) | Sim | Código de Acidente de Trabalho |
| CodTer | Number(004,0) | Sim | Código Recolhimento de Terceiros |
| NroEmp | Number(006,0) | Sim | N. de Empregados Empresa |
| PerMul | Number(005,2) | Sim | Percentual da Multa |
| DesPr1 | String(010) | Sim | Descrição Produto 1 - Campo19 |
| OriGrp | String(001) | Sim | Tipo Origem (E,D) |
| DesPr2 | String(010) | Sim | Descrição Produto 2 - Campo20 |
| ConPag | String(001) | Sim | Controle Pagto (E,S,N) |
| ValSeg | Number(011,2) | Sim | Valor Parte Empregados |
| ValEmp | Number(011,2) | Sim | Valor Parte Empresa |
| ValTer | Number(011,2) | Sim | Valor Parte Terceiros |
| ValPr1 | Number(011,2) | Sim | Valor Produto 1 - Campo19 |
| ValPr2 | Number(011,2) | Sim | Valor Produto 2 - Campo20 |
| ValDed | Number(011,2) | Sim | Valor de Deduções do FPAS |
| BasEmp | Number(011,2) | Sim | Base Contribuição Empregado |
| BasOu1 | Number(011,2) | Sim | Base Contr.Emp/Autônomos  1 |
| PerOu1 | Number(004,2) | Sim | % Base Contr. Emp/Autônomos 1 |
| BasOu2 | Number(011,2) | Sim | Base Contr.Emp/Autônomos  2 |
| PerOu2 | Number(004,2) | Sim | % Base Contr. Emp/Autônomos 2 |
| Cmp11p | Number(011,2) | Sim | % Compensação N.F. |
| ValCmp | Number(011,2) | Sim | Valor da Compensação |
| CodPr1 | Number(004,0) | Sim | Código Produto 1 - Campo19 |
| CodPr2 | Number(004,0) | Sim | Código Produto 2 - Campo20 |
| Obser1 | String(060) | Sim | Observacão Linha 1 |
| Obser2 | String(060) | Sim | Observacão Linha 2 |
| Obser3 | String(060) | Sim | Observacão Linha 3 |
| Obser4 | String(060) | Sim | Observacão Linha 4 |
| DedVlr | Number(011,2) | Sim | Valor das Deduções |
| AcoPre | String(001) | Sim | Acordo em Comissão Conciliação Prévia |
| CodCom | Number(004,0) | Sim | Código da vara |
| NumPro | Number(011,0) | Sim | Número do processo para recolhimento do SEFIP |
| AnoPro | Number(004,0) | Sim | Ano do Processo |
| CodCal | Number(005,0) | Sim | Código de Cálculo |

---

## Chave Primária

- NumEmp
- CodFil
- CodRat
- ComGrp
- OriSal
- CodOem
- SeqReg

---

## Índices

### R054GRPIndice2

**Tipo:** Unico

Campos:
- NumEmp
- OriSal
- CodFil
- CodRat
- ComGrp
- CodOem
- SeqReg

---

## Relacionamentos

### IR_R054GRP_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

