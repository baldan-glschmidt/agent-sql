# R199QPO

## Descrição

Cenário - Quadro Lotação p/ Posto de Trabalho

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Posto de Trabalho |
| DatQpo | Date | Não | Data de Alteração do Quadro de Vagas |
| QtdQpo | Number(004,0) | Sim | Quantidade de Vagas no Posto de Trabalho |
| ObsQpo | String(999) | Sim | Observação das Vagas do Posto de Trabalho |
| QtTpPo | Number(004,0) | Sim | Quantidade de Vagas Temporárias no Posto de Trabalho |

---

## Chave Primária

- NumEmp
- CodCen
- EstPos
- PosTra
- DatQpo

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R199QPO_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R199QPO_002

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

### IR_R199QPO_003

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

