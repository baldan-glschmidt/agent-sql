# R109EXA

## Descrição

PCMSO - Exames do Local e Cargo

---

## Resumo

- Campos: 35
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodPcm | Number(004,0) | Não | Código de identificação do PCMSO |
| TabOrg | Number(004,0) | Não | Código da tabela de organograma do local |
| NumLoc | Number(009,0) | Não | Local do organograma |
| EstCar | Number(004,0) | Não | Código da estrutura de cargos |
| CodCar | String(024) | Não | Código do cargo |
| DatIni | Date | Não | Data de início do exame periódico |
| CodExa | Number(004,0) | Não | Código do Exame |
| DatTer | Date | Sim | Data de término do exame periódico |
| UsaAdm | String(001) | Sim | Gerar Solicitação Exame p/ Admissional |
| UsaRet | String(001) | Sim | Gerar Solicitação Exame p/ Retorno do Afastamento |
| UsaTlo | String(001) | Sim | Gerar Solicitação Exame p/ Transferência Local |
| UsaTca | String(001) | Sim | Gerar Solicitação Exame p/ Transferência Cargo |
| UsaTfu | String(001) | Sim | Gerar Solicitação Exame p/ Transferência Função |
| UsaTAt | String(001) | Sim | Gerar Solicitação Exame p/ Transferência Atividade |
| UsaDem | String(001) | Sim | Gerar Solicitação Exame p/ Demissional |
| UsaAco | String(001) | Sim | Gerar Solicitação Exame p/ Acompanhamento Demitidos |
| UsaNor | String(001) | Sim | Gerar Solicitação Exame p/ Periódico |
| CodReg | Number(003,0) | Sim | Código da Regra para Exame |
| PerDet | String(001) | Sim | Define se a periodicidade está detalhada neste registro |
| PriNor | Number(003,0) | Sim | Meses do Primeiro Exame Normal |
| MesNor | Number(003,0) | Sim | Meses Exame Normal |
| PriIns | Number(003,0) | Sim | Meses Primeiro Exame Insalubridade |
| MesIns | Number(003,0) | Sim | Meses Exame de Insalubridade |
| PriPer | Number(003,0) | Sim | Meses Primeiro Exame de Periculosidade |
| MesPer | Number(003,0) | Sim | Meses Exame de Periculosidade |
| PriMen | Number(003,0) | Sim | Meses Primeiro Exame Menor Faixa Etária |
| MesMen | Number(003,0) | Sim | Meses Exame Menor Faixa Etária |
| PriMai | Number(003,0) | Sim | Período Primeiro Exame Maior Faixa Etária |
| MesMai | Number(003,0) | Sim | Meses Exame Maior Faixa Etária |
| DurAcp | Number(003,0) | Sim | Duração do Acompanhamento Demitidos |
| PriAcp | Number(003,0) | Sim | Meses do Primeiro Exame de Acompanhamento de Demitidos |
| MesAcp | Number(003,0) | Sim | Meses Acompanhamento Demitidos |
| UsaTPo | String(001) | Sim | Gerar Solicitação Exame p/ Transferência de Posto de Trabalho |
| UsaTGH | String(001) | Sim | Gerar Solicitação Exame p/ Transferência de GHE |

---

## Chave Primária

- NumEmp
- CodPcm
- TabOrg
- NumLoc
- EstCar
- CodCar
- DatIni
- CodExa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R109EXA_001

**Tabela:** R109PCM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPcm | CodPcm |

### IR_R109EXA_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R109EXA_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R109EXA_007

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

