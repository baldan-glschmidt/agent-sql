# R050AIF

## Descrição

DARF

---

## Resumo

- Campos: 27
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRec | Number(004,0) | Não | Código da Receita |
| DatApu | Date | Não | Data Apuração |
| NumPar | Number(002,0) | Não | Número da Parcela |
| DatCor | Date | Sim | Data de Início Correção |
| DatVen | Date | Sim | Data de Vencimento Receita |
| ComPag | Date | Sim | Competência do Pagto |
| IniApu | Date | Sim | Data Apuração Inicial |
| FimApu | Date | Sim | Data Apuração Final |
| ConPag | String(001) | Sim | Controle de Pagamento (S,N) |
| OriAif | String(001) | Sim | Controle Origem (E,D) |
| ComDar | String(041) | Sim | Comentário DARF |
| TpcBas | Number(002,0) | Sim | Tipo Período Bases |
| ValRec | Number(011,2) | Sim | Valor da Receita |
| ValCmp | Number(011,2) | Sim | Valor da Compensação |
| ValLiq | Number(011,2) | Sim | Valor Líquido |
| PerMul | Number(005,2) | Sim | % Multa |
| ValOri | Number(011,2) | Sim | Valor Original |
| BasCal | Number(011,2) | Sim | Base de Cálculo |
| ValTot | Number(011,2) | Sim | Valor Total |
| ValCor | Number(011,2) | Sim | Valor da Correção |
| ValMul | Number(011,2) | Sim | Valor da Multa |
| ValJur | Number(011,2) | Sim | Valor dos Juros |
| ValAcu | Number(011,2) | Sim | Valor Acumulador |
| FatAcu | Number(011,2) | Sim | Faturamento Acumulado |
| PerSim | Number(005,2) | Sim | Percentual de Enquadramento no Simples |

---

## Chave Primária

- NumEmp
- CodFil
- CodRec
- DatApu
- NumPar

---

## Índices

### R050AIFIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- DatApu
- CodFil
- CodRec
- NumPar

---

## Relacionamentos

### IR_R050AIF_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R050AIF_002

**Tabela:** R050REC

| Origem | Destino |
|--------|---------|
| CodRec | CodRec |

