# R040ACU

## Descrição

Períodos de Férias - Acumulados

---

## Resumo

- Campos: 8
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Colaborador |
| IniPer | Date | Não | Início Período Aquisitivo de Férias |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodTot | Number(004,0) | Não | Totalizador |
| ValTot | Number(011,2) | Sim | Quantidade / Referência / Valor |
| ValAnt | Number(011,2) | Sim | Quantidade / Referência / Valor (Anterior) |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- IniPer
- TabEve
- CodTot

---

## Índices

### R040ACUIndice2

**Tipo:** Não unico

Campos:
- TabEve
- CodTot

---

## Relacionamentos

### IR_R040ACU_003

**Tabela:** R040PER

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| IniPer | IniPer |

### IR_R040ACU_005

**Tabela:** R040TOT

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodTot | CodTot |

