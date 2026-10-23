# R350DES

## Descrição

S-2299 - eSocial - Desligamento

---

## Resumo

- Campos: 55
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqDes | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| IndGui | Number(001,0) | Sim | Indicativo do tipo de Guia |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| IndSeg | Number(001,0) | Sim | Indicador segmento e-social |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| MatTra | String(030) | Sim | Matrícula atribuída ao trabalhador pela empresa |
| MotDes | Number(002,0) | Sim | Código do Motivo do Desligamento |
| DatDes | Date | Sim | Data de Desligamento do Trabalhador |
| InPgAv | String(001) | Sim | Indicativo de Pagamento do Aviso Prévio Indenizado |
| AviFim | Date | Sim | Data final do Aviso Prévio Indenizado |
| PenAli | Number(001,0) | Sim | Indicativo de pensão alimentícia |
| PerAli | Number(005,2) | Sim | Percentual destinado ao alimentando |
| VlrAli | Number(014,2) | Sim | Valor destinado ao alimentando |
| AteObi | String(032) | Sim | Número que Identifica o Registro do Atestado de Óbito |
| NumPro | String(021) | Sim | Número do Processo Trabalhista Quando o Desligamento se Der Por Este Motivo |
| AviPre | Number(001,0) | Sim | Indicador de Cumprimento Parcial de Aviso Prévio |
| ObsDes | String(255) | Sim | Anotação Relevante Sobre o Desligamento do Trabalhador |
| TipSuc | Number(001,0) | Sim | Tipo de inscrição da empresa sucessora |
| CnpSuc | Number(014,0) | Sim | CNPJ/CPF da empresa sucessora |
| CfjSuc | String(014) | Sim | CNPJ/CPF da empresa sucessora |
| FimQua | Date | Sim | Data fim da quarentena |
| IndRem | Number(001,0) | Sim | Indicativo de situação de remuneração após o desligamento |
| DatRem | Date | Sim | Data fim remuneração após o desligamento |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| DatTer | Date | Sim | Data projetada para o término do aviso prévio indenizado |
| TipDem | Number(001,0) | Sim | Origem da demissão |
| DatPag | Date | Sim | Data de Pagamento |
| CodCat | Number(004,0) | Sim | Código da categoria |
| TemRcs | String(001) | Sim | Rescisão |
| EnvVal | String(001) | Sim | Envio Válido |
| EmpCon | String(001) | Sim | Empréstimo Consignado Garantia FGTS |
| MatCon | String(005) | Sim | Matrícula Instituição Consignatária |
| NroCon | Number(015,0) | Sim | Número Contrato Empréstimo Consignado |
| RegPre | Number(002,0) | Sim | Tipo de regime previdenciário |
| DiaInt | Number(002,0) | Sim | Qtde de dias trabalhados no mês pelo empregado com contrato de intermitente |
| EnvExc | String(001) | Sim | Envio Excluído |
| ProcCs | String(021) | Sim | Número Processo Contribuição Social |
| NovCPF | Number(011,0) | Sim | CPF do trabalhador |
| RegTra | Number(001,0) | Sim | Tipo de regime trabalhista |
| DatAvi | Date | Sim | Data do Aviso Prévio |
| IndPdv | String(001) | Sim | Programa de Demissão Voluntária (PDV) |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqDes

---

## Índices

### R350DESIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
