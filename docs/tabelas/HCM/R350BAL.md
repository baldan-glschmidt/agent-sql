# R350BAL

## Descrição

S-2405 - Cadastro de Beneficiário - Entes Públicos - Alteração

---

## Resumo

- Campos: 36
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
| SeqBal | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código que identifica a versão de leiaute utilizado para geração do arquivo |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfBen | Number(011,0) | Sim | Número do CPF do beneficiário |
| DatAlt | Date | Sim | Data Alteração das Informações |
| NomBen | String(070) | Sim | Nome do beneficiário |
| SexBen | String(001) | Sim | Sexo do beneficiário |
| RacCor | Number(001,0) | Sim | Raça e cor do beneficiário |
| EstCiv | Number(001,0) | Sim | Estado civil do beneficiário |
| DoeInc | String(001) | Sim | Beneficiário possuí doença incapacitante |
| TipLog | String(004) | Sim | Tipo de Logradouro |
| DesLog | String(100) | Sim | Descrição do logradouro |
| NumLog | String(010) | Sim | Número do logradouro |
| CplLog | String(030) | Sim | Complemento do logradouro |
| BaiLog | String(090) | Sim | Nome do bairro/distrito |
| CEPLog | Number(008,0) | Sim | Código de Endereçamento Postal |
| MunLog | Number(007,0) | Sim | Código do município |
| EstLog | String(002) | Sim | Sigla da Unidade da Federação |
| PaiLog | Number(003,0) | Sim | Código do país |
| CidLog | String(050) | Sim | Nome da Cidade |
| PosLog | String(012) | Sim | Código de Endereçamento Postal - estrangeiro |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvExc | String(001) | Sim | Exclusão realizada |
| EnvVal | String(001) | Sim | Determina se envio é válido |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqBal

---

## Índices

### R350BALIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
