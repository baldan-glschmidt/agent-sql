# R016HIE

## Descrição

Hierarquia dos Locais no Organograma

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
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| DatIni | Date | Não | Primeiro Dia do Período |
| DatFim | Date | Sim | Último Dia do Período |
| PosLoc | String(072) | Sim | Posição do Local Dentro da Arvore |
| CodLoc | String(150) | Sim | Código do Local do Organograma |

---

## Chave Primária

- TabOrg
- NumLoc
- DatIni

---

## Índices

### R016HIEIndice2

**Tipo:** Não unico

Campos:
- NumLoc
- DatIni
- DatFim

### R016HIEIndice3

**Tipo:** Não unico

Campos:
- TabOrg
- PosLoc
- DatIni
- DatFim

### R016HIEIndice4

**Tipo:** Não unico

Campos:
- TabOrg
- CodLoc
- DatIni
- DatFim

---

## Relacionamentos

### IR_R016HIE_000

**Tabela:** R016ORE

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |

