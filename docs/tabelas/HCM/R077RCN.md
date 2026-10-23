# R077RCN

## Descrição

Hab. Técnica - Req. Conhecimentos

---

## Resumo

- Campos: 16
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodHte | String(006) | Não | Código da Habilidade Técnica |
| FamCnc | String(004) | Não | Código da Família de Conhecimentos |
| CodCnc | String(005) | Não | Código do Conhecimento |
| PesCnc | Number(002,0) | Sim | Peso do Conhecimento |
| ExiRqu | String(001) | Sim | Exigência do requisito(D-Desejável/N-Necessário) |
| ConAut | String(001) | Sim | Considera conhecimento na autoavaliação |
| ConSup | String(001) | Sim | Considera conhecimento na avaliação com foco no superior |
| ConSub | String(001) | Sim | Considera conhecimento na avaliação com foco no subordinado |
| ConPar | String(001) | Sim | Considera conhecimento na avaliação com foco no cargo par |
| ConCli | String(001) | Sim | Considera conhecimento na avaliação com foco no cliente |
| ConFor | String(001) | Sim | Considera conhecimento na avaliação com foco no fornecedor |
| ConIns | String(001) | Sim | Considera conhecimento na avaliação com foco no instrutor |
| ConCon | String(001) | Sim | Considera conhecimento na avaliação de consenso |
| CodPro | Number(003,0) | Sim | Código da Tabela de Proficiência - OBSOLETO |
| DatPro | Date | Sim | Data da Tabela de Níveis de Proficiência - OBSOLETO |
| CodNiv | Number(002,0) | Sim | Código do Nível da Proficiência - OBSOLETO |

---

## Chave Primária

- CodHte
- FamCnc
- CodCnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077RCN_000

**Tabela:** R077HTE

| Origem | Destino |
|--------|---------|
| CodHte | CodHte |

### IR_R077RCN_001

**Tabela:** R125FAM

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |

### IR_R077RCN_002

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

