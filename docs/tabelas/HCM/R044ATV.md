# R044ATV

## Descrição

Códigos de Cálculo - Períodos de apuração por tipo de vale

---

## Resumo

- Campos: 8
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| CodVal | Number(004,0) | Não | Código do Vale |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| IniApu | Date | Sim | Data Início Período Apuração por Tipo de Vale |
| FimApu | Date | Sim | Data Final Período Apuração por Tipo de Vale |
| IniFal | Date | Sim | Data Início Período de Faltas por Tipo de Vale |
| FimFal | Date | Sim | Data Final Período de Faltas por Tipo de Vale |

---

## Chave Primária

- NumEmp
- CodCal
- CodVal
- TabEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044ATV_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

