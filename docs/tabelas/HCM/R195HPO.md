# R195HPO

## Descrição

Cenário - Histórico Posto de Trabalho

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TipCol | Number(001,0) | Não | Tipo de colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| IniAtu | Date | Não | Início da atuação do colaborador no posto de trabalho |
| TerAtu | Date | Sim | Término da atuação do colaborador no posto de trabalho |
| CodTap | Number(003,0) | Sim | Tipo de atuação que o colaborador exercerá no posto |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Sim | Posto de trabalho onde o colaborador atua |
| MotAlt | Number(003,0) | Sim | Motivo de alteração do posto de trabalho |
| GerCol | String(001) | Sim | Origem da geração do histórico de posto |

---

## Chave Primária

- NumEmp
- CodCen
- TipCol
- NumCad
- IniAtu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R195HPO_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R195HPO_006

**Tabela:** R017TAP

| Origem | Destino |
|--------|---------|
| CodTap | CodTap |

### IR_R195HPO_008

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

### IR_R195HPO_009

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| MotAlt | CodMot |

