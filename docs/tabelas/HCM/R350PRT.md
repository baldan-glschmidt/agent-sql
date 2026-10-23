# R350PRT

## Descrição

S-1210 - eSocial - Pagamentos de Rendimentos do Trabalho

---

## Resumo

- Campos: 20
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| IndGui | Number(001,0) | Sim | Indicativo do tipo de Guia |
| SeqPrt | Number(009,0) | Não | Sequência |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IndRet | Number(001,0) | Sim | Indica se o arquivo é um arquivo de retificação |
| NroRec | String(040) | Sim | Número do recibo do arquivo a ser retificado |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjIns | String(014) | Sim | CNPJ Alfanumérico |
| CpfTra | Number(011,0) | Sim | CPF do trabalhador |
| ValDep | Number(014,2) | Sim | Valor Dedução base de cálculo do IRRF relativo aos dependentes |
| DatMol | Date | Sim | Esse campo foi descontinuado, agora é utilizado o campo R350INF.DatLau |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqPrt

---

## Índices

### R350PRTIndice1

**Tipo:** Não unico

Campos:
- PidExc

### R350PRTIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- FilEmp
- PerApu
- IndApu
- NroRec

---

## Relacionamentos

Nenhum relacionamento cadastrado.
