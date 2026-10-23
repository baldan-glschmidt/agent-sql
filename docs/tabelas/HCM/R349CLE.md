# R349CLE

## Descrição

S-5011 - eSocial - Identificação da lotação tributária

---

## Resumo

- Campos: 31
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| IndApu | Number(001,0) | Não | Indicativo de período de apuração |
| PerApu | Date | Não | Período Apuração |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCeo | Number(009,0) | Não | Sequência |
| SeqCle | Number(009,0) | Não | Sequência |
| CodLot | String(030) | Sim | Código atribuído pela empresa para a lotação |
| CodFpa | Number(003,0) | Sim | Código relativo ao FPAS |
| CodTer | Number(004,0) | Sim | Código de terceiros |
| CodCom | Number(004,0) | Sim | Código Combinado Terceiros com suspensão devido a processo judicial |
| TpInCo | Number(001,0) | Sim | Tipo de inscrição do contratante |
| InsCon | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjCon | String(014) | Sim | CNPJ Alfanumérico |
| TpInPr | Number(001,0) | Sim | Tipo de inscrição do propietário do CNO |
| InsPro | Number(014,0) | Sim | Número de inscrição (CNPJ/CPF) - Obsoleto |
| CfjPro | String(014) | Sim | CNPJ Alfanumérico |
| CnoObr | Number(012,0) | Sim | Número do CNO da Obra |
| OpCnpj | Number(014,0) | Sim | CNPJ do Operador Portuário |
| CfjOpe | String(014) | Sim | CNPJ do Operador Portuário |
| OpAlRa | Number(001,0) | Sim | Alíquota Definida no Decreto 3.048/99  Para a Atividade (CNAE) Predominante |
| OpFFap | Number(005,4) | Sim | Fator Acidentário de Prevenção |
| OpAjRa | Number(005,4) | Sim | Alíquota após ajustar pelo FAP |
| BcCp00 | Number(014,2) | Sim | {vrBcCp00} do evento S-1270 |
| BcCp15 | Number(014,2) | Sim | {vrBcCp15} do evento S-1270 |
| BcCp20 | Number(014,2) | Sim | {vrBcCp20} do evento S-1270 |
| BcCp25 | Number(014,2) | Sim | {vrBcCp25} do evento S-1270 |
| BcCp13 | Number(014,2) | Sim | {vrBcCp13} do evento S-1270 |
| BcFgts | Number(014,2) | Sim | {vrBcFGTS} do evento S-1270 |
| DescCP | Number(014,2) | Sim | {vrDescCP} do evento S-1270 |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- IndApu
- PerApu
- SeqTab
- SeqCeo
- SeqCle

---

## Índices

### R349CLEIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
