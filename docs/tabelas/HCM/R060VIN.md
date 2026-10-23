# R060VIN

## Descrição

Vínculos - Horários e Afastamentos

---

## Resumo

- Campos: 7
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodVin | Number(005,0) | Não | Código do Vínculo |
| DesVin | String(060) | Não | Descrição do Vínculo da Legenda e Horário |
| TipSit | Number(002,0) | Sim | Tipo da Situação de Afastamento |
| CodHor | Number(004,0) | Sim | Código do Horário |
| CodLeg | Number(005,0) | Não | Código da Legenda |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| CodFil | Number(006,0) | Sim | Código da Filial |

---

## Chave Primária

- CodVin

---

## Índices

### R060VINIndice1

**Tipo:** Unico

Campos:
- TipSit
- CodHor
- NumEmp
- CodFil

---

## Relacionamentos

### IR_R060VIN_003

**Tabela:** R004HOR

| Origem | Destino |
|--------|---------|
| CodHor | CodHor |

### IR_R060VIN_004

**Tabela:** R060LEG

| Origem | Destino |
|--------|---------|
| CodLeg | CodLeg |

