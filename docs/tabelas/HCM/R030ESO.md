# R030ESO

## Descrição

Filial - Empregador eSocial

---

## Resumo

- Campos: 20
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatAlt | Date | Não | Data Alteração |
| ClaTri | Number(002,0) | Sim | Código correspondente à classificação tributária do contribuinte |
| IndCoo | Number(001,0) | Sim | Indicativo de Cooperativa |
| IndObr | Number(001,0) | Sim | Indicativo de Construtora |
| AcoInt | Number(002,0) | Sim | Acordo Internacional Isenção de Multa |
| SocOst | String(001) | Sim | Indica se o declarante é sócio ostensivo em sociedade em conta de participação |
| SitEst | Number(002,0) | Sim | Indicativo de Situação Pessoa Jurídica |
| SitPFi | Number(002,0) | Sim | Indicativo de Situação Pessoa Física |
| RegEle | Number(001,0) | Sim | Registro Eletrônico |
| NatEst | Number(004,0) | Sim | Natureza Jurídica RAIS |
| RepSoc | String(001) | Sim | Repasse Sócio |
| FinLuc | String(001) | Sim | Indicativo de entidade educativa/prática desportiva que tenha por objetivo a assistência ao adolescente e à educação profissional (art. 430, inciso II, CLT). |
| TraTem | String(001) | Sim | Indicativo de Empresa de Trabalho Temporário (Lei n 6.019/1974), com registro no Ministério do Trabalho. |
| RegTem | String(030) | Sim | Número do registro da Empresa de Trabalho Temporário no Ministério do Trabalho. |
| BasDes | Number(001,0) | Sim | Informar se o empregador deve ser enviado ao eSocial por esta Empresa |
| OpcPRu | Number(002,0) | Sim | Opção pelo produtor rural de tributação da contribuição previdenciária |
| TraSoc | String(001) | Sim | Indica se houve transformação de Sociedade Sem Fins Lucrativos, para Socidade de Fins Lucrativos |
| PerIrr | String(001) | Sim | Indicador de pertencimento do IRRF, IN RFB 2239/2024 |

---

## Chave Primária

- NumEmp
- CodFil
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030ESO_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

