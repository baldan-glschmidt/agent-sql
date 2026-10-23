# R030GRP

## Descrição

Filiais da Empresa - Grps

---

## Resumo

- Campos: 29
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| TipGrp | Number(001,0) | Não | Tipo da Gps da Filial |
| DatGrp | Date | Não | Data de Alteração dos Dados da Gps |
| FilEmp | Number(006,0) | Sim | Filial Empregadora |
| CodFpa | Number(003,0) | Sim | Código Fpas |
| AciTra | Number(007,0) | Sim | Código Acidente Trabalho |
| PerSat | Number(005,2) | Sim | Percentual RAT - Devido |
| RatNae | Number(005,2) | Sim | RAT do CNAE |
| PerSli | Number(005,2) | Sim | Percentual RAT - Liminar |
| PerCon | Number(007,4) | Sim | % Parte Convênios Gps |
| PerIse | Number(005,2) | Sim | % Isenção Filantrópica |
| CgcCab | String(001) | Sim | Cabeçalho Gps - Campos 9 e 10 (CNPJ ou CEI) |
| Ob1Grp | String(060) | Sim | Observação p/ GPS |
| Ob2Grp | String(060) | Sim | Campo 8 Gps - Linha 2 |
| Ob3Grp | String(060) | Sim | Campo 8 Gps - Linha 3 |
| Ob4Grp | String(060) | Sim | Campo 8 Gps - Linha 4 |
| FatFap | Number(007,4) | Sim | Fator FAP |
| AplFap | String(001) | Sim | Aplica Fator FAP |
| PerRed | Number(005,2) | Sim | % Redutor TI Exportação |
| DesFol | Number(001,0) | Sim | Desoneração da Folha de Pagamento |
| PerDes | Number(005,2) | Sim | % Receita Bruta |
| ProRAT | Number(009,0) | Sim | Número do processo administrativo/judicial do RAT |
| ProFAP | Number(009,0) | Sim | Número do processo administrativo/judicial do FAP |
| CodTer | Number(004,0) | Sim | Código de Terceiros eSocial |
| TerSus | Number(004,0) | Sim | Código de Terceiros Suspensos eSocial |
| SusRat | Number(014,0) | Sim | Código Suspensão RAT |
| SusFap | Number(014,0) | Sim | Código Suspensão FAP |
| PerSen | Number(005,2) | Sim | Percentual Adicional do Senai |

---

## Chave Primária

- NumEmp
- CodFil
- TipGrp
- DatGrp

---

## Índices

### R030GRPIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- FilEmp

### R030GRPIndice3

**Tipo:** Não unico

Campos:
- CodFpa

---

## Relacionamentos

### IR_R030GRP_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R030GRP_004

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| FilEmp | CodFil |

### IR_R030GRP_005

**Tabela:** R026FPA

| Origem | Destino |
|--------|---------|
| CodFpa | CodFpa |

