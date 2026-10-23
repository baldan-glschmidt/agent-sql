# R350BET

## Descrição

S-2420 - Cadastro de Benefício - Entes Públicos - Término

---

## Resumo

- Campos: 25
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
| SeqBet | Number(009,0) | Não | Sequência |
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
| DatTer | Date | Sim | Data de término do benefício. |
| MtvTer | Number(002,0) | Sim | Motivo da cessação do benefício |
| CNPJDs | Number(014,0) | Sim | Informar o CNPJ do órgão público sucessor |
| CfjDes | String(014) | Sim | Informar o CNPJ do órgão público sucessor |
| NovCPF | Number(011,0) | Sim | CPF do trabalhador |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| EnvExc | String(001) | Sim | Exclusão realizada |
| EnvVal | String(001) | Sim | Determina se envio é válido |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqBet

---

## Índices

### R350BETIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
