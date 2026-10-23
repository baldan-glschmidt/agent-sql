# R184PLO

## Descrição

PLR - Pontuação do Local

---

## Resumo

- Campos: 11
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| DatPon | Date | Não | Data Pontuação |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodObj | Number(004,0) | Não | Código do Objetivo |
| DatIni | Date | Sim | Data Início da Pontuação |
| DatFim | Date | Sim | Data Final da Pontuação |
| ResObj | Number(011,2) | Sim | Resultado do Objetivo |
| PonObj | Number(011,2) | Sim | Pontuação Conquistada |
| TotObj | Number(011,2) | Sim | Total do Objetivo (Pontos * Peso) |
| ExpCal | String(030) | Sim | Expressão Utilizada no Cálculo |

---

## Chave Primária

- NumEmp
- DatPon
- TabOrg
- NumLoc
- CodObj

---

## Índices

### R184PLOIndice2

**Tipo:** Não unico

Campos:
- NumLoc

---

## Relacionamentos

### IR_R184PLO_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R184PLO_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R184PLO_004

**Tabela:** R182OBJ

| Origem | Destino |
|--------|---------|
| CodObj | CodObj |

