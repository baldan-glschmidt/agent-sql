# R350BEI

## Descrição

S-2410 - Cadastro de Benefício - Entes Públicos - Início

---

## Resumo

- Campos: 49
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
| SeqBei | Number(009,0) | Não | Sequência |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfBen | Number(011,0) | Sim | Número do CPF do beneficiário |
| NroBen | String(020) | Não | Número do Benefício |
| DatIni | Date | Não | Data Referência |
| CadIni | String(001) | Sim | Indicar se a data de início do benefício é anterior à obrigatoriedade dos eventos não periódicos para o ente público no eSocial |
| SitBen | Number(001,0) | Não | Indicar a situação do benefício no órgão declarante |
| DatPub | Date | Sim | Data de publicação da concessão do benefício |
| TipBen | Number(004,0) | Não | Tipo Benefício |
| PanSeg | Number(002,0) | Não | Tipo de plano de segregação da massa |
| MatEso | String(030) | Sim | Matrícula do servidor/militar no Sistema de RH do órgão cujo vínculo deu ensejo ao benefício |
| CNPJOr | Number(014,0) | Sim | CNPJ do órgão público responsável pela matrícula |
| CfjOri | String(014) | Sim | CNPJ do órgão público responsável pela matrícula |
| DscBen | String(255) | Sim | Descrição do instrumento ou situação que originou o pagamento do benefício |
| DetJud | String(001) | Sim | Benefício foi concedido por determinação judicial |
| PenMor | Number(001,0) | Sim | Tipo de pensão por morte |
| CpfIns | Number(011,0) | Sim | CPF do instituidor da pensão por morte |
| DatIns | Date | Sim | Data de óbito do instituidor da pensão por morte |
| CNPJAn | Number(014,0) | Sim | CNPJ do órgão público anterior |
| CfjAnt | String(014) | Sim | CNPJ do órgão público anterior |
| BenAnt | String(020) | Sim | Número do Benefício Anterior |
| DatSuc | Date | Sim | Data da transferência do benefício para o órgão público declarante |
| DscSuc | String(255) | Sim | Observação Sucessão |
| CPFAnt | Number(011,0) | Sim | CPF do trabalhador |
| BenCPF | String(020) | Sim | Benefício Anterior |
| DatCPF | Date | Sim | Data de Alteração do CPF |
| ObsCPF | String(255) | Sim | Observação da Alteração de CPF |
| DatTer | Date | Sim | Data de término do benefício. |
| MtvTer | Number(002,0) | Sim | Motivo da cessação do benefício |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvExc | String(001) | Sim | Exclusão realizada |
| EnvVal | String(001) | Sim | Determina se envio é válido |
| SitHom | Number(002,0) | Sim | Situação da Homologação |
| DatHom | Date | Sim | Data da Homologação do Benefício pelo Tribunal de Contas Competente |
| TipDep | Number(002,0) | Sim | Tipo de Dependente do Instituidor da Pensão por Morte |
| DesDep | String(100) | Sim | Descrição da Dependência do Instituidor da Pensão por Morte |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqBei

---

## Índices

### R350BEIIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
