# R058PLA

## Descrição

Plano de Ambientes da Planta

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPlt | Number(005,0) | Não | Código do Site |
| NumAmb | Number(009,0) | Não | Ambiente da Planta |
| DatIni | Date | Não | Primeiro Dia do Período |
| DatFim | Date | Sim | Último Dia do Período |
| PosAmb | String(024) | Sim | Posição do Ambiente dentro da Planta |
| CodAmb | String(032) | Sim | Código do Ambiente na Planta |

---

## Chave Primária

- CodPlt
- NumAmb
- DatIni

---

## Índices

### R058PLAIndice2

**Tipo:** Não unico

Campos:
- NumAmb
- DatIni
- DatFim

### R058PLAIndice3

**Tipo:** Não unico

Campos:
- CodPlt
- PosAmb
- DatIni
- DatFim

### R058PLAIndice4

**Tipo:** Não unico

Campos:
- CodPlt
- CodAmb
- DatIni
- DatFim

---

## Relacionamentos

### IR_R058PLA_000

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

