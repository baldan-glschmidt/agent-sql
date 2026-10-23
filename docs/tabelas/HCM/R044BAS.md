# R044BAS

## Descrição

Bases de Cálculo

---

## Resumo

- Campos: 33
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CmpBas | Date | Não | Competência das Bases |
| SeqBas | Number(002,0) | Não | Sequência |
| BmeIns | Number(011,2) | Sim | Base do INSS Mensal |
| VmeIns | Number(011,2) | Sim | Valor do INSS Mensal |
| B13Ins | Number(011,2) | Sim | Base do INSS 13° Salário |
| V13Ins | Number(011,2) | Sim | Valor do INSS 13° Salário |
| BmeIrf | Number(011,2) | Sim | Base do IR Mensal |
| VmeIrf | Number(011,2) | Sim | Valor do IR Mensal |
| BfeIrf | Number(011,2) | Sim | Base do IR Férias |
| VfeIrf | Number(011,2) | Sim | Valor do IR Férias |
| B13Irf | Number(011,2) | Sim | Base do IR 13° Salário |
| V13Irf | Number(011,2) | Sim | Valor do IR 13° Salário |
| BplIrf | Number(011,2) | Sim | Base do IR Part.Lucros |
| VplIrf | Number(011,2) | Sim | Valor do IR Part.Lucros |
| BmeIpe | Number(011,2) | Sim | Base do IPE Mensal |
| VmeIpe | Number(011,2) | Sim | Valor do IPE Mensal |
| BfeIpe | Number(011,2) | Sim | Base do IPE de Férias |
| VfeIpe | Number(011,2) | Sim | Valor do IPE de Férias |
| B13Ipe | Number(011,2) | Sim | Base do IPE 13° Salário |
| V13Ipe | Number(011,2) | Sim | Valor do IPE de 13° Salário |
| ConInd | String(001) | Sim | Contribuinte Individual |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição |
| NumIns | Number(015,0) | Sim | Número Inscrição |
| CfjIns | String(014) | Sim | Número Inscrição |
| NomOem | String(060) | Sim | Nome da outra empresa |
| ConDes | String(001) | Sim | Primeira Contribuição Descontada |
| CateSo | Number(004,0) | Sim | Código da categoria eSocial |
| DmenSi | Number(011,2) | Sim | Deduções IR Simplificado Mês |
| D13Sim | Number(011,2) | Sim | Deduções IR Simplificado 13º Salário |
| DferSi | Number(011,2) | Sim | Deduções IR Simplificado Férias |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpBas
- SeqBas

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044BAS_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

