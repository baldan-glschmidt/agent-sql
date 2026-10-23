# R017ADI

## Descrição

Postos de Trabalho - Salários

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| DatAlt | Date | Não | Data da alteração dos adicionais por posto |
| PerIns | Number(005,2) | Sim | % Insalubridade |
| PerPer | Number(005,2) | Sim | % Periculosidade |
| FatTph | Number(004,2) | Sim | Fator Tempo Serviço p/ Homens |
| FatTpm | Number(004,2) | Sim | Fator Tempo Serviço p/ Mulheres |
| ApoEsp | Number(002,0) | Sim | Número de Anos p/ Aposentadoria Especial |
| CmpTer | Date | Sim | Competência Término do Adicional |

---

## Chave Primária

- EstPos
- PosTra
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017ADI_000

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

### IR_R017ADI_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

