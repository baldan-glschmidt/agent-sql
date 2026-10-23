# R092OBS

## Descrição

Quadro Lotação p/ Posto de Trabalho - Observação

---

## Resumo

- Campos: 5
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
| ObsQpo | String(999) | Sim | Observação das Vagas do Posto de Trabalho |

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

### IR_R092OBS_000

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

### IR_R092OBS_001

**Tabela:** R017PLV

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| CodPlv | CodPlv |

