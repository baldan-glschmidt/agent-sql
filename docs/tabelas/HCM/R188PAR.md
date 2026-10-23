# R188PAR

## Descrição

PLR - Paradas

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodMaq | Number(004,0) | Não | Código da Máquina |
| CodPrd | Number(004,0) | Não | Código do Produto |
| DatPar | Date | Não | Data Parada |
| HorPar | Number(005,0) | Não | Hora Parada |
| DatFim | Date | Sim | Data de Término da Parada |
| HorFim | Number(005,0) | Sim | Hora de Término da Parada |
| CodMpa | Number(006,0) | Sim | Motivo da Parada |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CodMaq
- CodPrd
- DatPar
- HorPar

---

## Índices

### R188PARIndice2

**Tipo:** Não unico

Campos:
- NumLoc

---

## Relacionamentos

### IR_R188PAR_003

**Tabela:** R188MAQ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| CodMaq | CodMaq |

### IR_R188PAR_004

**Tabela:** R188PRD

| Origem | Destino |
|--------|---------|
| CodPrd | CodPrd |

