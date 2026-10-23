# R348VRM

## Descrição

eSocial - GRFGTS - Visão Remuneração - Resultado - obsoleta

---

## Resumo

- Campos: 27
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdePen | String(040) | Não | Identificador da solicitação |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| FilEmp | Number(006,0) | Sim | Código da Filial Empregadora |
| TipIns | Number(001,0) | Sim | Código correspondente ao tipo de inscrição |
| NumIns | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CmpRef | Date | Sim | Competência |
| DatVen | Date | Sim | Data de vencimento |
| TraACR | Number(008,0) | Sim | Trab. ativos com remuneração |
| TraAfa | Number(008,0) | Sim | Trab. afastados |
| TraDem | Number(008,0) | Sim | Trab. desligados |
| QtdTom | Number(008,0) | Sim | Tomadores |
| TraASR | Number(008,0) | Sim | Trab. ativos sem remuneração |
| TotRem | Number(014,2) | Sim | Total remuneração |
| FgtDCa | Number(014,2) | Sim | Tot. depósito FGTS calculado |
| FgtDRe | Number(014,2) | Sim | Tot. depósito FGTS recolhido |
| FgtDRM | Number(014,2) | Sim | Tot. depósito FGTS recolhido a maior |
| TotEnc | Number(014,2) | Sim | Total encargos |
| FgtRec | Number(014,2) | Sim | FGTS a recolher |
| ValMes | Number(014,2) | Sim | Valor mensal |
| Val13s | Number(014,2) | Sim | Valor 13º salário |
| ValDis | Number(014,2) | Sim | Valor dissídio |
| Val13d | Number(014,2) | Sim | Valor 13º dissídio |
| ValAci | Number(014,2) | Sim | Valor conversão acidente de trabalho |
| ValMul | Number(014,2) | Sim | Multa |
| ValJur | Number(014,2) | Sim | Juros |
| ValMon | Number(014,2) | Sim | Atualização monetária |
| CfjIns | String(014) | Sim | CNPJ Alfanumérico |

---

## Chave Primária

- IdePen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
