# R032TPG

## Descrição

Pagtos Terceiros

---

## Resumo

- Campos: 62
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPte | Date | Não | Competência Pagto Terceiro |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Terceiro |
| SeqPte | Number(003,0) | Não | Sequência |
| SrvTer | String(249) | Sim | Descrição do Serviço Prestado Pelo Terceiro |
| NroRpa | Number(009,0) | Sim | Número do RPCI |
| PerGrp | Number(004,2) | Sim | Percentual  Grps |
| DepIrf | Number(002,0) | Sim | Dependentes do IRF |
| CodRet | Number(004,0) | Sim | Código de Retenção do IRF |
| DatPag | Date | Sim | Data de Pagto dos Rendimentos |
| RenBru | Number(011,2) | Sim | Rendimentos Bruto |
| OutPrv | Number(011,2) | Sim | Outros Proventos |
| OutDes | Number(011,2) | Sim | Outros Descontos |
| BasIns | Number(011,2) | Sim | Base de Cálculo INSS |
| OutIns | Number(011,2) | Sim | Base de Cálculo INSS (Outros Pagamentos e Contratos) |
| DedIns | Number(011,2) | Sim | Deduções do Inss |
| InsTrp | Number(011,2) | Sim | INSS Transporte |
| BasIrf | Number(011,2) | Sim | Base de Cálculo do IRF |
| PenJud | Number(011,2) | Sim | Pensão Judicial |
| IrfRet | Number(011,2) | Sim | Valor do IR Retido Fonte |
| ValIss | Number(011,2) | Sim | Valor do ISS |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| CodCcu | String(018) | Sim | Código do C.Custo |
| NatDes | Number(003,0) | Sim | Natureza de Despesa |
| DatCtb | Date | Sim | Data da Contabilização |
| ConPag | String(001) | Sim | Controle Pagamento |
| AssIrf | String(001) | Sim | Assinala Pagamento IRF |
| DatRec | Date | Sim | Data Recolhimento IRF |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| CtaFin | Number(007,0) | Sim | Conta Financeira |
| CodNtg | Number(004,0) | Sim | Nat. Gasto |
| PerIss | Number(004,2) | Sim | Percentual de ISS |
| ConIns | Number(011,2) | Sim | Contribuição INSS |
| GruCon | String(003) | Sim | Código do grupo de contas a receber ou pagar |
| CodLim | Number(004,0) | Sim | Código Limite de Isenção ISS Terceiro |
| CodCid | Number(007,0) | Sim | Código da Cidade |
| CodSer | Number(003,0) | Sim | Código do Serviço |
| ValLiq | Number(011,2) | Sim | Valor Líquido |
| CodIse | Number(002,0) | Sim | Código do Motivo Isento |
| ValIse | Number(011,2) | Sim | Valor da Base IR Isenta |
| CnpjOp | Number(015,0) | Sim | CNPJ de Operadora do Plano de Saúde |
| CfjOpe | String(014) | Sim | CNPJ de Operadora do Plano de Saúde |
| NomOpe | String(060) | Sim | Nome da operadora de Plano de Saúde |
| VlrPla | Number(014,2) | Sim | Valor pago pelo Plano de Saúde |
| OriReg | Number(001,0) | Sim | Origem do registro |
| CodOpe | Number(008,0) | Sim | Código da Operadora |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| ProIns | Number(009,0) | Sim | Processo Judicial Contribuição Previdenciária |
| SusIns | Number(014,0) | Sim | Código Suspensão Contribuição Previdenciária |
| ProIRR | Number(009,0) | Sim | Processo Judicial Imposto de Renda |
| SusIRR | Number(014,0) | Sim | Código Suspensão Imposto de Renda |
| QtdDia | Number(002,0) | Sim | Quantidade de dias trabalhados pelo Segurado Especial |
| RegAns | Number(007,0) | Sim | Registro na Agência Nacional de Saúde |
| DedSim | Number(011,2) | Sim | Dedução IR Simplificado |
| USU_VlrAdi | Number(011,2) | Sim | Valor do Adiantamento |
| USU_DatEmi | Date | Sim | Data de Emiss?o do RPA |
| USU_NroChe | String(020) | Sim | Numero do Cheque |
| USU_CadObs | String(150) | Sim | Observação |
| USU_NumCfr | String(020) | Sim | Numero da Carta Frete |

---

## Chave Primária

- NumEmp
- CodFil
- CmpPte
- TipCol
- NumCad
- SeqPte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032TPG_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R032TPG_004

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

