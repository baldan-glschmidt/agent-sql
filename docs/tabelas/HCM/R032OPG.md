# R032OPG

## Descrição

Pagtos Outras Empresas

---

## Resumo

- Campos: 74
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPoe | Date | Não | Competência do Pagto O.Empresa |
| CodOem | Number(008,0) | Não | Código da Outra Empresa |
| SeqPoe | Number(003,0) | Não | Sequência do pagamento |
| NroDoc | String(015) | Sim | Número da nota fiscal/fatura |
| CodRet | Number(004,0) | Sim | Código de Receita do IRRF |
| DatPag | Date | Sim | Data Pagto Rendimentos |
| PerIrf | Number(005,2) | Sim | Percentual Imposto Renda |
| RenBru | Number(011,2) | Sim | Valor bruto da(s) nota(s) fiscal(is) |
| BasIrf | Number(011,2) | Sim | Base IRRF |
| OutDes | Number(011,2) | Sim | Outros descontos |
| IrfRet | Number(011,2) | Sim | Valor do IRRF |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| CodCcu | String(018) | Sim | Código do C.Custo |
| NatDes | Number(003,0) | Sim | Natureza de Despesa |
| DatCtb | Date | Sim | Data da Contabilização |
| AssIrf | String(001) | Sim | Assinala Pagamento IRF (S,N) |
| DatRec | Date | Sim | Data Recolhimento IRF |
| RetGrp | String(001) | Sim | Origem do serviço tomado |
| ValGrp | Number(011,2) | Sim | Valor/Base GPS |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| CtaFin | Number(007,0) | Sim | Conta Financeira |
| CodNtg | Number(004,0) | Sim | Natureza de gastos |
| Bas15a | Number(011,2) | Sim | Base SAT 15 Anos |
| Bas20a | Number(011,2) | Sim | Base SAT 20 Anos |
| Bas25a | Number(011,2) | Sim | Base SAT 25 Anos |
| PerCsr | Number(005,2) | Sim | Percentual de Receita do CSRF |
| RetCsr | Number(004,0) | Sim | Código da Receita do CSRF |
| BasCsr | Number(011,2) | Sim | Base do CSRF |
| ValCsr | Number(011,2) | Sim | Valor do CSRF |
| PerCsl | Number(005,2) | Sim | Percentual de Recolhimento Individual do CSLL |
| RetCsl | Number(004,0) | Sim | Código da Receita do CSLL |
| BasCsl | Number(011,2) | Sim | Base do CSLL |
| ValCsl | Number(011,2) | Sim | Valor do CSLL |
| PerCof | Number(005,2) | Sim | Percentual de Recolhimento Individual do COFINS |
| RetCof | Number(004,0) | Sim | Código de Receita do COFINS |
| BasCof | Number(011,2) | Sim | Base do COFINS |
| ValCof | Number(011,2) | Sim | Valor do COFINS |
| PerPis | Number(005,2) | Sim | Percentual de Recolhimento Individual do PIS |
| RetPis | Number(004,0) | Sim | Código de Receita do PIS |
| BasPis | Number(011,2) | Sim | Base do PIS |
| ValPis | Number(011,2) | Sim | Valor do PIS |
| PerIss | Number(005,2) | Sim | Percentual  de Recolhimento do ISS |
| AtiIss | Number(004,0) | Sim | Código da Atividade do Serviço ISS |
| BasIss | Number(011,2) | Sim | Base de ISS |
| ValIss | Number(011,2) | Sim | Valor do ISS |
| GruCon | String(003) | Sim | Código do grupo de contas a receber ou pagar |
| CodSnf | String(003) | Sim | Série da Nota Fiscal no ERP |
| CodTns | String(005) | Sim | Código da Transação no ERP |
| CodEdc | String(003) | Sim | Código do Modelo de Documento para fins fiscais |
| DatEmi | Date | Sim | Data de emissão da Nota Fiscal |
| SerFis | String(005) | Sim | Número de série da nota fiscal/fatura |
| SerObr | Number(001,0) | Sim | Prestação de serviços em obra de construção civil |
| NumCNO | Number(012,0) | Sim | Número de inscrição no Cadastro Nacional de Obra |
| ValSer | Number(014,2) | Sim | Valor dos serviços na nota fiscal/fatura, deduzidos os material/equipamento |
| ValDed | Number(014,2) | Sim | Valor das deduções legais de auxílio-alimentação e vale transporte, em contrato |
| ValMat | Number(014,2) | Sim | Valor dos materiais e equipamentos fornecidos, desde que previstos em contrato |
| TipPro | Number(001,0) | Sim | Tipo de Inscrição do proprietário do CNO |
| InsPro | Number(015,0) | Sim | Número de inscrição (CNPJ/CPF) do proprietário do CNO |
| CfjPro | String(014) | Sim | Número de inscrição (CNPJ/CPF) do proprietário do CNO |
| CodPro | Number(009,0) | Sim | Número do processo judicial/benefício |
| ValNRe | Number(014,2) | Sim | Valor não retido pelo contratante ou depositada em juízo devido a decisão judic. |
| ValREm | Number(014,2) | Sim | Valor da retenção destacada na nota fiscal relativo aos serviços subempreitados |
| BasRet | Number(014,2) | Sim | Base de cálculo da retenção |
| ValRet | Number(014,2) | Sim | Soma do valor da retenção das notas fiscais de serviço |
| BasCon | Number(014,2) | Sim | Valor da base de cálculo dos aos serviços prestados em atividades concomitantes |
| Bas15c | Number(014,2) | Sim | Valor dos Serviços, que permitirá aposentadoria após 15 anos de contribuição |
| Bas20c | Number(014,2) | Sim | Valor dos Serviços, que permitirá aposentadoria após 20 anos de contribuição |
| Bas25c | Number(014,2) | Sim | Valor dos Serviços, que permitirá aposentadoria após 25 anos de contribuição |
| OriReg | Number(001,0) | Sim | Origem do registro |
| TipRen | Number(003,0) | Sim | Tipo de Rendimento |
| ForTri | Number(002,0) | Sim | Forma de Tributação |

---

## Chave Primária

- NumEmp
- CodFil
- CmpPoe
- CodOem
- SeqPoe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032OPG_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

### IR_R032OPG_003

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

