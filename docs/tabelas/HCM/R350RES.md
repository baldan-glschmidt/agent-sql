# R350RES

## Descrição

S-1280 - eSocial - Desoneração da Folha e/ou Simples Concomitante (Inf.Comp.Eventos Periódicos)

---

## Resumo

- Campos: 24
- Chave Primária: 5 campo(s)
- Índices: 1
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
| SeqRes | Number(009,0) | Não | Sequência |
| SeqAnp | Number(009,0) | Sim | Sequência |
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
| IndSub | Number(001,0) | Sim | Indicativo de substituição patronal |
| PerRed | Number(005,2) | Sim | Percentual de redução |
| FatMes | Number(005,2) | Sim | Fator cálculo da contribuição patronal do mês |
| Fat13s | Number(005,2) | Sim | Fator cálc. da contrib. patronal do décimo terceiro |
| InfCon | String(001) | Sim | Atividades Concomitantes |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| PerTra | Number(001,0) | Sim | Informe o percentual de contribuição social devida |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqRes

---

## Índices

### R350RESIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
