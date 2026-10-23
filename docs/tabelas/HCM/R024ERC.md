# R024ERC

## Descrição

Exceções de Requisitos Conhecimento de Cargo por Local

---

## Resumo

- Campos: 22
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| DatRqu | Date | Não | Data do Requisito do Cargo |
| FamCnc | String(004) | Não | Código da Família de Conhecimentos |
| CodCnc | String(005) | Não | Código do Conhecimento |
| PesCnc | Number(002,0) | Sim | OBSOLETO - Peso do Conhecimento |
| ConRec | String(001) | Sim | Considera este requisito para recrutamento |
| ConPpp | String(001) | Sim | Considera requisito p/perfil profissiográfico previdenciário |
| ExiRqu | String(001) | Sim | Exigência do requisito(D-Desejável/N-Necessário) |
| CodPro | Number(003,0) | Sim | Código da Tabela de Proficiência - OBSOLETO |
| DatPro | Date | Sim | Data da Tabela de Níveis de Proficiência - OBSOLETO |
| CodNiv | Number(002,0) | Sim | Código do Nível da Proficiência - OBSOLETO |
| ConAut | String(001) | Sim | Considera conhecimento na autoavaliação |
| ConSup | String(001) | Sim | Considera conhecimento na avaliação com foco no superior |
| ConSub | String(001) | Sim | Considera conhecimento na avaliação com foco no subordinado |
| ConPar | String(001) | Sim | Considera conhecimento na avaliação com foco no cargo par |
| ConCli | String(001) | Sim | Considera conhecimento na avaliação com foco no cliente |
| ConFor | String(001) | Sim | Considera conhecimento na avaliação com foco no fornecedor |
| ConIns | String(001) | Sim | Considera conhecimento na avaliação com foco no instrutor |
| ConCon | String(001) | Sim | Considera conhecimento na avaliação de consenso |

---

## Chave Primária

- TabOrg
- NumLoc
- EstCar
- CodCar
- DatRqu
- FamCnc
- CodCnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024ERC_003

**Tabela:** R024ERL

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| EstCar | EstCar |
| CodCar | CodCar |

### IR_R024ERC_005

**Tabela:** R125FAM

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |

### IR_R024ERC_006

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

