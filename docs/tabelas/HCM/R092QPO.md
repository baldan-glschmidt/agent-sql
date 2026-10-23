# R092QPO

## Descrição

Quadro Lotação p/ Posto de Trabalho

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| CodPlv | Number(004,0) | Não | Código do Plano de Vagas |
| PosTra | String(024) | Não | Posto de Trabalho |
| DatQpo | Date | Não | Data de Alteração do Quadro de Vagas |
| QtdQpo | Number(004,0) | Sim | Quantidade de Vagas no Posto de Trabalho |
| ObsQpo | String(999) | Sim | Descontinuado |
| CodUsu | Number(009,0) | Sim | Usuário que realizou a última alteração no Quadro de Vagas |
| DthAlt | Number(014,6) | Sim | Data/Hora da última alteração do Quadro de Vagas |
| OriQpo | Number(001,0) | Sim | Origem do Quadro |
| QtTpPo | Number(004,0) | Sim | Quantidade de Vagas Temporárias no Posto de Trabalho |

---

## Chave Primária

- EstPos
- CodPlv
- PosTra
- DatQpo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R092QPO_000

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

### IR_R092QPO_001

**Tabela:** R017PLV

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| CodPlv | CodPlv |

