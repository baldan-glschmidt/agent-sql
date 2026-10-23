# R350CON

## Descrição

S-2240 - eSocial - Condições Ambientais do Trabalho - Agentes Nocivos

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
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data em que o trabalhador iniciou as atividades no ambiente de trabalho |
| SeqCon | Number(009,0) | Não | Sequência |
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
| CodCat | Number(004,0) | Sim | Código da categoria do trabalhador |
| LocAmb | Number(001,0) | Sim | Tipo de estabelecimento do ambiente de trabalho |
| DscSet | String(100) | Sim | Descrição do lugar administrativo onde o trabalhador exerce suas atividades |
| TpInAm | Number(001,0) | Sim | Código correspondente ao tipo de inscrição do ambiente |
| NrInAm | Number(015,0) | Sim | Número de inscrição onde está localizado o ambiente - Obsoleto |
| CfjAmb | String(014) | Sim | Número de inscrição onde está localizado o ambiente |
| DscAtv | String(15000) | Sim | Descrição das atividades, físicas ou mentais, realizadas pelo trabalhador |
| MetErg | String(999) | Sim | Descrição da metodologia utilizada para o levantamento dos riscos ergonômicos (Obsoleto) |
| ObsCon | String(999) | Sim | Observações complementares referentes a registros ambientais |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Envio Válido |
| EnvExc | String(001) | Sim | Envio Excluído |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- DatIni
- SeqCon

---

## Índices

### R350CONIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
