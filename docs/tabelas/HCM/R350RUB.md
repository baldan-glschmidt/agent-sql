# R350RUB

## Descrição

S-1010 - eSocial - Tabela de Rubricas

---

## Resumo

- Campos: 33
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| RubEso | String(030) | Não | Código da rubrica eSocial |
| SeqRub | Number(009,0) | Não | Sequência |
| CodRub | Number(009,0) | Sim | Código da Rubrica |
| VerLei | String(011) | Sim | Código da versão do leiaute |
| IdeEve | String(044) | Sim | Identificador que representa unicamente o evento dentro do lote de envio |
| TipAmb | Number(001,0) | Sim | Identificação do ambiente |
| ProEmi | Number(001,0) | Sim | Processo de emissão do evento |
| VerPro | String(020) | Sim | Versão do processo de emissão do evento |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição do contribuinte |
| CfjIns | String(014) | Sim | Número de inscrição do contribuinte |
| IniVal | Date | Sim | Data de início da validade das informações prestadas no evento |
| FimVal | Date | Sim | Data final da validade das informações |
| NoInVa | Date | Sim | Data de início da nova validade das informações prestadas no evento |
| NoFiVa | Date | Sim | Data final da nova validade das informações |
| DesRub | String(100) | Sim | Descrição (nome) da rubrica no sistema |
| NatRub | Number(004,0) | Sim | Código de classificação da rubrica de acordo com a natureza |
| TipRub | Number(001,0) | Sim | Indicativo do tipo de rubrica |
| IncPre | Number(002,0) | Sim | Código de incidência tributária da rubrica para a Previdência Social |
| IncIrr | Number(004,0) | Sim | Código de incidência tributária da rubrica para o IRRF |
| IncFgt | Number(002,0) | Sim | Código de incidência tributária da rubrica para o FGTS |
| IncSin | Number(002,0) | Sim | Código de incidência tributária da rubrica para a Contribuição Sindical Laboral |
| InCPRP | Number(002,0) | Sim | Código da incidência tributária para o regime próprio da previdência |
| TetRem | String(001) | Sim | Informar se a rubrica compõe o teto remuneratório específico (art. 37, XI, da CF/1988) |
| ObsRub | String(255) | Sim | Observações relacionadas à rubrica ou à sua utilização |
| TabRub | String(008) | Sim | Tabela de Rubrica |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| TipOpe | Number(001,0) | Sim | Tipo operação do leiaute. |
| LayOut | String(006) | Sim | Leiaute |
| EnvVal | String(001) | Sim | Envio Válido |
| IncPis | Number(002,0) | Sim | Incidência PIS |

---

## Chave Primária

- NumEmp
- FilEmp
- RubEso
- SeqRub

---

## Índices

### R350RUBIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
