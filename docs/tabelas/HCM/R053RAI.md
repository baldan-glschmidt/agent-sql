# R053RAI

## Descrição

RAIS - Registro Filial

---

## Resumo

- Campos: 28
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EmpArq | Number(004,0) | Não | Código da Empresa no Arquivo |
| AnoBas | Number(004,0) | Não | Ano Base da Rais |
| FilArq | Number(006,0) | Não | Código da Filial no Arquivo |
| NumCgc | Number(015,0) | Sim | Número da Inscrição |
| CfjNum | String(014) | Sim | Número da Inscrição |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição da Filial (CNPJ/CEI/CPF/INCRA) |
| DatBas | Number(002,0) | Sim | Data Base |
| RaiNeg | Number(001,0) | Sim | Rais com Empregados |
| CeiVin | Number(012,0) | Sim | Matrícula CEI/CNO Vinculada a uma inscrição CNPJ |
| PorEmp | Number(001,0) | Sim | Indicador de Porte da Empresa |
| OptSim | Number(001,0) | Sim | Indicador de Optante pelo Simples |
| EmpPat | Number(001,0) | Sim | Indicador de Participação no PAT |
| NViA5s | Number(006,0) | Sim | Vinculos que Recebem até 5 Salários |
| NViM5s | Number(006,0) | Sim | Vinculos que Recebem Mais de 5 Salários |
| PerMo1 | Number(003,0) | Sim | Porcentagem de Serviço Proprio |
| PerMo2 | Number(003,0) | Sim | Porcentagem de Administração Cozinha |
| PerMo3 | Number(003,0) | Sim | Porcentagem de Refeição Convênio |
| PerMo4 | Number(003,0) | Sim | Porcentagem de Refeição Transportada |
| PerMo5 | Number(003,0) | Sim | Porcentagem de Cesta Alimento |
| PerMo6 | Number(003,0) | Sim | Porcentagem de Alimentação Convênio |
| EncAtv | Number(001,0) | Sim | Indicador de Encerramento das Atividades |
| OriMov | String(001) | Sim | Origem do Registro |
| ExeAtv | Number(001,0) | Sim | Exerceu Atividades |
| CgcCsi | Number(015,0) | Sim | CNPJ Centralizadora Contribuição Sindical |
| CfjCsi | String(014) | Sim | CNPJ Centralizadora Contribuição Sindical |
| FilSin | Number(001,0) | Sim | Indicador de Filial Sindicalizada |
| SisPon | Number(002,0) | Sim | Tipo de Sistema de Controle de Ponto |
| TipAux | Number(005,0) | Sim | Uso Exclusivo da Senior |

---

## Chave Primária

- EmpArq
- AnoBas
- FilArq

---

## Índices

### R053RAIIndice2

**Tipo:** Não unico

Campos:
- AnoBas
- OriMov

---

## Relacionamentos

### IR_R053RAI_002

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| EmpArq | NumEmp |
| FilArq | CodFil |

