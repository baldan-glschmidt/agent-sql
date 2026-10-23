# R083FGL

## Descrição

PPRA - Fontes Geradoras

---

## Resumo

- Campos: 13
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 4

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpPpa | Date | Não | Competência do PPRA |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodGru | Number(007,0) | Não | Grupo de Atividades |
| CodAgt | Number(006,0) | Não | Código do Perigo/Fator de Risco |
| CodFgl | Number(006,0) | Não | Código da Fonte Geradora de Lesão |
| CodCau | Number(003,0) | Não | Causa da Exposição |
| MeiPpg | String(100) | Sim | Meio de Propagação |
| TemExp | String(020) | Sim | Tempo de Exposição |
| JorTra | String(040) | Sim | Jornada de Trabalho (semanal) |
| ForExp | Number(001,0) | Sim | Forma de exposição |
| LocFgl | String(050) | Sim | Localização da fonte geradora |

---

## Chave Primária

- NumEmp
- CmpPpa
- TabOrg
- NumLoc
- CodGru
- CodAgt
- CodFgl
- CodCau

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R083FGL_004

**Tabela:** R083ATV

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodGru | CodAtv |

### IR_R083FGL_005

**Tabela:** R083AGT

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CmpPpa | CmpPpa |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| CodGru | CodGru |
| CodAgt | CodAgt |

### IR_R083FGL_006

**Tabela:** R086FGL

| Origem | Destino |
|--------|---------|
| CodFgl | CodFgl |

### IR_R083FGL_007

**Tabela:** R086CAU

| Origem | Destino |
|--------|---------|
| CodCau | CodCau |

