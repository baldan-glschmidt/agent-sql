# R056SEF

## Descrição

Informações Enviadas Para o SEFIP

---

## Resumo

- Campos: 35
- Chave Primária: 11 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colabolador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodRat | Number(009,0) | Não | Código do Rateio |
| CodOem | Number(008,0) | Não | Tomador de Serviço/Obra Construção Civil |
| CdrFgt | Number(003,0) | Não | Código de Recolhimento do FGTS |
| CmpSef | Date | Não | Competência de Geração do SEFIP |
| NumPro | Number(011,0) | Não | Número do Processo |
| TipSef | Number(001,0) | Não | Tipo Sefip |
| SeqReg | Number(002,0) | Não | Sequência do Registro |
| BasFgt | Number(011,2) | Sim | Base de FGTS |
| RecFgt | Number(011,2) | Sim | Base de FGTS Recolhido |
| Bas13s | Number(011,2) | Sim | Base de FGTS de 13° Salário |
| Rec13s | Number(011,2) | Sim | Base de FGTS de 13° Salário Recolhido |
| BasIns | Number(011,2) | Sim | Base de INSS |
| BasI13 | Number(011,2) | Sim | Base de INSS de 13° Salário |
| ValIns | Number(011,2) | Sim | Valor de INSS |
| ModFgt | Number(001,0) | Sim | Modalidade do Trabalhador no Arquivo |
| DatGer | Date | Sim | Data da Geração do SEFIP |
| AnoPro | Number(004,0) | Sim | Ano do Processo |
| NumVar | Number(005,0) | Sim | Número da Vara/JCJ |
| PerIni | Date | Sim | Período de Início |
| PerFim | Date | Sim | Período de Fim |
| NumPis | Number(011,0) | Sim | PIS/PASEP/CI do Trabalhador |
| DatAdm | Date | Sim | Data de Admissão |
| DatNas | Date | Sim | Data de Nascimento |
| CodCbo | String(006) | Sim | Código Brasileiro de Ocupação |
| CodOco | Number(002,0) | Sim | Código da Ocorrência |
| CatSef | Number(002,0) | Sim | Categoria do Trabalhador |
| CodFpa | Number(003,0) | Sim | Código Fpas |
| OriReg | String(001) | Sim | Origem do Registro |
| DatFgt | Date | Sim | Data de Recolhimento FGTS |
| IndRec | Number(001,0) | Sim | Indicador de Recolhimento FGTS |
| InsFgt | String(001) | Sim | Enviada Base INSS como Base FGTS |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodFil
- CodRat
- CodOem
- CdrFgt
- CmpSef
- NumPro
- TipSef
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R056SEF_003

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

