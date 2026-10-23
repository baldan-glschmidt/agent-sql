# R350FEC

## Descrição

S-1299 - eSocial - Eventos Periódicos - Fechamento

---

## Resumo

- Campos: 29
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
| SeqFec | Number(009,0) | Não | Sequência |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| NomRes | String(070) | Sim | Nome do Responsável pelas informações |
| CpfRes | Number(011,0) | Sim | CPF do Responsável pelas informações |
| TelRes | String(013) | Sim | Telefone do Responsável pelas informações |
| EmaRes | String(060) | Sim | Endereço eletrônico do Responsável pelas informações |
| EvtRem | String(001) | Sim | Possui informações de folha de pagamentos no período de apuração? |
| EvtPgt | String(001) | Sim | Possui pagamentos de rendimentos do trabalho no período de apuração? |
| EvtAPr | String(001) | Sim | Possui informações sobre a aquisição de produto rural pessoa físicas? |
| EvtCPr | String(001) | Sim | Possui informações de comercialização de produção? |
| EvtPor | String(001) | Sim | Contratou por intermédio de sindicato, serviços de trab. avulsos não portuário? |
| EvtCom | String(001) | Sim | Possui inf. de Desoneração de Folha ou Atividades concomitantes? |
| IndExc | String(001) | Sim | Indicativo exclusão de apuração das aquisições de produção rural S-1250. |
| DctWeb | String(001) | Sim | Solicitação de transmissão imediata da DCTFWeb |
| ValFec | String(001) | Sim | Não realizar as validações das regras do fechamento? |
| CmpSMo | Date | Sim | Primeira competência a partir da qual não Houve movimento |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- IndApu
- SeqFec

---

## Índices

### R350FECIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
