# R077BHT

## Descrição

Bloco - Habilidades Técnicas

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| BloHte | String(004) | Não | Bloco de Habilidades Genéricas |
| DatHte | Date | Não | Data Habilidade Técnica |
| CodHte | String(006) | Não | Código da Habilidade Técnica |
| PesHte | Number(002,0) | Sim | Peso da Habilidade |
| ConAut | String(001) | Sim | Considera habilidade na autoavaliação |
| ConSup | String(001) | Sim | Considera habilidade na avaliação com foco no superior |
| ConSub | String(001) | Sim | Considera habilidade na avaliação com foco no subordinado |
| ConPar | String(001) | Sim | Considera habilidade na avaliação com foco no cargo par |
| ConCli | String(001) | Sim | Considera habilidade na avaliação com foco no cliente |
| ConFor | String(001) | Sim | Considera habilidade na avaliação com foco no fornecedor |
| ConIns | String(001) | Sim | Considera habilidade na avaliação com foco no instrutor |
| ConCon | String(001) | Sim | Considera habilidade na avaliação de consenso |
| TipHab | Number(001,0) | Sim | Indica se a habilidade é Essencial ou Complementar |

---

## Chave Primária

- BloHte
- DatHte
- CodHte

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077BHT_000

**Tabela:** R077BLO

| Origem | Destino |
|--------|---------|
| BloHte | BloHte |

### IR_R077BHT_002

**Tabela:** R077HTE

| Origem | Destino |
|--------|---------|
| CodHte | CodHte |

