# R090HCG

## Descrição

Histórico de Crachás de Grupos de Visitantes

---

## Resumo

- Campos: 13
- Chave Primária: 5 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatEnt | Date | Não | Data de Entrada |
| HorEnt | Number(005,0) | Não | Hora de Entrada |
| SeqEnt | Number(002,0) | Não | Sequência do Registro |
| GruVis | Number(003,0) | Não | Código do Grupo de Visitantes |
| SeqVis | Number(003,0) | Não | Sequência do Visitante Segundo o Grupo |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante do Grupo |
| NumDoc | String(020) | Sim | Número do Documento do Visitante do Grupo |
| NomVis | String(040) | Sim | Nome do Visitante do Grupo |
| NumCra | Number(012,0) | Sim | Número do Crachá do Vistante |
| DatSai | Date | Sim | Data da Saída do Grupo na Portaria |
| HorSai | Number(005,0) | Sim | Hora da Saída do Grupo na Portaria |
| DatSLo | Date | Sim | Data da Saída do Local Visitado na Empresa |
| HorSLo | Number(005,0) | Sim | Hora da Saída do Local Visitado na Empresa |

---

## Chave Primária

- DatEnt
- HorEnt
- SeqEnt
- GruVis
- SeqVis

---

## Índices

### R090HCGIndice2

**Tipo:** Não unico

Campos:
- GruVis

### R090HCGIndice3

**Tipo:** Não unico

Campos:
- NumCra
- DatSai

---

## Relacionamentos

### IR_R090HCG_003

**Tabela:** R090GRV

| Origem | Destino |
|--------|---------|
| GruVis | GruVis |

