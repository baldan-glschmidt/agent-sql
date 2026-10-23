# R350ASO

## Descrição

S-2220 - eSocial - Monitoramento da Saúde do Trabalhador

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqAso | Number(009,0) | Não | Sequência |
| CodAte | Number(006,0) | Não | Código do Atendente |
| NumAte | Number(009,0) | Não | Número do Atestado Médico |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Tipo de inscrição do empregador |
| NumIns | Number(014,0) | Sim | Número de inscrição do empregador - Obsoleto |
| CfjIns | String(014) | Sim | Número de inscrição do empregador |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (Obsoleto) |
| NumMat | String(255) | Sim | Matrícula atribuída ao trabalhador pela empresa |
| CatEso | Number(004,0) | Sim | Código da categoria do trabalhador |
| TipASO | Number(002,0) | Sim | Tipo do exame médico ocupacional |
| DatASO | Date | Sim | Data de emissão do ASO |
| ResASO | Number(001,0) | Sim | Resultado do ASO |
| CpfMed | Number(011,0) | Sim | CPF do médico emitente do ASO (Obsoleto) |
| NisMed | Number(011,0) | Sim | Número de Identificação Social do médico emitente do ASO (Obsoleto) |
| NomMed | String(070) | Sim | Nome do médico emitente do ASO |
| NrCrmM | String(010) | Sim | Número de inscrição do médico emitente do ASO no Conselho Regional de Medicina |
| UfCrmM | String(002) | Sim | Sigla da UF de expedição do CRM do médico emitente do ASO |
| CpfRsp | Number(011,0) | Sim | Número do CPF do médico responsável/coordenador do PCMSO |
| NomRsp | String(070) | Sim | Nome do médico responsável/coordenador do PCMSO |
| NumCon | String(010) | Sim | Número de inscrição do médico responsável/coordenador do PCMSO no CRM |
| EstCon | String(002) | Sim | Sigla da UF de expedição do CRM do médico responsável/coordenador do PCMSO |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Envio Válido |
| EnvExc | String(001) | Sim | Envio Excluído |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqAso

---

## Índices

### R350ASOIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
