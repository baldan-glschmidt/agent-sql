# R350ETM

## Descrição

S-2221 - eSocial - Exame Toxicológico do Motorista Profissional

---

## Resumo

- Campos: 31
- Chave Primária: 6 campo(s)
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
| DatExm | Date | Não | Data da solicitação do exame toxicológico |
| SeqEtm | Number(009,0) | Não | Sequência |
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
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| NumMat | String(255) | Sim | Matrícula atribuída ao trabalhador pela empresa |
| CatEso | Number(004,0) | Sim | Código da categoria do trabalhador |
| DatRel | Date | Não | Data da Realização do exame toxicológico |
| NumLab | Number(014,0) | Sim | CNPJ do laboratório responsável pela realização do exame - Obsoleto |
| CfjLab | String(014) | Sim | CNPJ do laboratório responsável pela realização do exame |
| CodExm | String(011) | Sim | Código do exame toxicológico |
| NomMed | String(070) | Sim | Nome do médico |
| NrCrmM | String(010) | Sim | Número de inscrição do médico no CRM |
| UfCrmM | String(002) | Sim | Sigla da UF de expedição do CRM |
| IndRec | String(001) | Sim | Trabalhador se recusou a realizar o exame toxicológico no desligamento |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Envio Válido |
| EnvExc | String(001) | Sim | Envio Excluído |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- DatExm
- SeqEtm

---

## Índices

### R350ETMIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
