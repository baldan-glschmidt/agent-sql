# R350AVI

## Descrição

S-2250 - eSocial - Aviso Prévio

---

## Resumo

- Campos: 28
- Chave Primária: 6 campo(s)
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
| DatAvi | Date | Não | Data em que o trabalhador ou o empregador recebeu o aviso de desligamento |
| SeqAvi | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| NisTra | Number(011,0) | Sim | Número de inscrição do segurado (PIS, PASEP ou NIT) |
| NumMat | String(030) | Sim | Matrícula atribuída ao trabalhador pela empresa |
| DatPre | Date | Sim | Data prevista para o desligamento |
| TipAvi | Number(001,0) | Sim | Tipo de Aviso Prévio |
| ObsAvi | String(255) | Sim | Observações |
| DatCan | Date | Sim | Data Cancelamento |
| MotCan | Number(001,0) | Sim | Motivo Cancelamento |
| ObsCan | String(255) | Sim | Observação Cancelamento |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvVal | String(001) | Sim | Determina se envio é válido |
| EnvExc | String(001) | Sim | Envio Excluído |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- DatAvi
- SeqAvi

---

## Índices

### R350AVIIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
