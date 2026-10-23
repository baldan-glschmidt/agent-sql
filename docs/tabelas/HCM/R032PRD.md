# R032PRD

## Descrição

Produção

---

## Resumo

- Campos: 49
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipRot | Number(001,0) | Não | Tipo de Rotina |
| CodFil | Number(006,0) | Não | Código da Filial |
| CmpPrd | Date | Não | Competência |
| SeqPrd | Number(005,0) | Não | Sequência |
| TipPrd | String(001) | Sim | Tipo da Produção |
| RecBru | Number(014,2) | Sim | Valor da Receita Bruta |
| OriPEv | String(001) | Sim | Origem Patrocínio/Ev. Desportivos |
| TabOrg | Number(004,0) | Sim | Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| CodCcu | String(018) | Sim | Código do Centro de Custo |
| NatDes | Number(003,0) | Sim | Natureza de Despesa |
| RecSer | Number(014,2) | Sim | Valor da Receita de Serviços/Outras Atividades |
| ValImp | Number(014,2) | Sim | Valor impostos e contribuições |
| CnpjDe | Number(015,0) | Sim | CNPJ Ass. Desportiva |
| CfjDes | String(014) | Sim | CNPJ Ass. Desportiva |
| NomCnp | String(080) | Sim | Nome Empresa |
| TipRep | Number(001,0) | Sim | Tipo de Repasse |
| DatRep | Date | Sim | Data de Repasse |
| CnpjRe | Number(015,0) | Sim | CNPJ Empresa que repassou recurso |
| CfjRep | String(014) | Sim | CNPJ Empresa que repassou recurso |
| NumIns | Number(015,0) | Sim | Número Inscrição |
| CfjIns | String(014) | Sim | Número Inscrição |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição |
| IndCom | Number(001,0) | Sim | Indicativo de comercialização |
| ValRet | Number(014,2) | Sim | Valor retido pelo adquirente |
| IndAqu | Number(001,0) | Sim | Indicativo de aquisição |
| ValPre | Number(014,2) | Sim | Contribuição Previdenciária |
| ValFin | Number(014,2) | Sim | Valor % RAT |
| ValSEN | Number(014,2) | Sim | Contribuição SENAR |
| DatEmi | Date | Sim | Data de Emissão |
| NumNot | String(020) | Sim | Número Nota Fiscal |
| SerNot | String(005) | Sim | Número de Série |
| CodPro | Number(009,0) | Sim | Número Processo Judicial |
| CodSus | Number(014,0) | Sim | Código Suspensão |
| ProBk1 | Number(009,0) | Sim | Número Processo Judicial |
| SusBk1 | Number(014,0) | Sim | Código Suspensão |
| ProBk2 | Number(009,0) | Sim | Número Processo Judicial |
| SusBk2 | Number(014,0) | Sim | Código Suspensão |
| ProBk3 | Number(009,0) | Sim | Número Processo Judicial |
| SusBk3 | Number(014,0) | Sim | Código Suspensão |
| OriReg | Number(001,0) | Sim | Origem do registro |
| VPrePr | Number(014,2) | Sim | Valor de contribuição previdenciária não retido |
| VFinPr | Number(014,2) | Sim | Valor do percentual RAT não retido |
| VSenPr | Number(014,2) | Sim | Valor de contribuição SENAR não retido |
| VPreEx | Number(014,2) | Sim | Valor da Contribuição Previdenciária com exigibilidade suspensa |
| VGilEx | Number(014,2) | Sim | Valor para Gilrat com exigibilidade suspensa |
| VSenEx | Number(014,2) | Sim | Valor para Senar com exigibilidade suspensa |
| OpcPRu | Number(002,0) | Sim | Opção pelo produtor rural de tributação da contribuição previdenciária |

---

## Chave Primária

- NumEmp
- CodFil
- TipRot
- CmpPrd
- SeqPrd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032PRD_002

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

