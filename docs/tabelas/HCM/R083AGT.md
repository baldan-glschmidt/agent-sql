# R083AGT

## Descrição

PPRA - Perigos/Fatores Risco

---

## Resumo

- Campos: 19
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpPpa | Date | Não | Competência do PPRA |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodGru | Number(007,0) | Não | Grupo de Atividades |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| OutCon | String(700) | Sim | Outras Medidas Controle (existentes) |
| ObsAgt | String(1200) | Sim | Observação do Perigo/Fator de Risco |
| SitAgt | String(001) | Sim | Situação do perigo/fator de risco em relação Plano de Ação |
| ConEfi | String(001) | Sim | Identifica se os EPI´s são eficazes |
| EPCEfi | String(001) | Sim | Identifica se os EPC´s são eficazes |
| EmiPPP | String(001) | Sim | Considera este PPRA na emissão do PPP e LTCAT |
| MedPro | String(001) | Sim | Medidas de proteção |
| ConFun | String(001) | Sim | Condições de funcionamento |
| PraVal | String(001) | Sim | Prazo de validade |
| PerTro | String(001) | Sim | Periocidade de troca |
| ObsHig | String(001) | Sim | Higienização |
| ConIns | String(001) | Sim | Considera insalubridade |
| ConPer | String(001) | Sim | Considera periculosidade |

---

## Chave Primária

- NumEmp
- CmpPpa
- TabOrg
- NumLoc
- CodGru
- CodAgt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R083AGT_003

**Tabela:** R083ARI

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CmpPpa | CmpPpa |
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R083AGT_004

**Tabela:** R083ATV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodGru | CodAtv |

### IR_R083AGT_005

**Tabela:** R082AGT

| Origem | Destino |
|--------|---------|
| CodAgt | CodAgt |

