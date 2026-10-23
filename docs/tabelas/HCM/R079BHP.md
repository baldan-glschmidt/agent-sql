# R079BHP

## Descrição

Bloco - Habilidades Pessoais

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| BloHpe | String(004) | Não | Bloco de Habilidades Pessoais |
| DatHpe | Date | Não | Data Habilidade Pessoal |
| CodHpe | String(004) | Não | Código da Habilidade Pessoal |
| PesHpe | Number(002,0) | Sim | Peso da Habilidade |
| ConAut | String(001) | Sim | Considera habilidade na autoavaliação |
| ConSup | String(001) | Sim | Considera habilidade na avaliação com foco no superior |
| ConSub | String(001) | Sim | Considera habilidade na avaliação com foco no subordinado |
| ConPar | String(001) | Sim | Considera habilidade na avaliação com foco no cargo par |
| ConCli | String(001) | Sim | Considera habilidade na avaliação com foco no cliente |
| ConFor | String(001) | Sim | Considera habilidade na avaliação com foco no fornecedor |
| ConIns | String(001) | Sim | Considera habilidade na avaliação com foco no instrutor |
| ConCon | String(001) | Sim | Considera habilidade na avaliação de consenso |

---

## Chave Primária

- BloHpe
- DatHpe
- CodHpe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R079BHP_000

**Tabela:** R079BLO

| Origem | Destino |
|--------|---------|
| BloHpe | BloHpe |

### IR_R079BHP_002

**Tabela:** R079HPE

| Origem | Destino |
|--------|---------|
| CodHpe | CodHpe |

