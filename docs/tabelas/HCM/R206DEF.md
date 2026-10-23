# R206DEF

## Descrição

PLR Paquetá - Definições

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CmpPlr | Date | Não | Competência do PLR |
| CodCal | Number(005,0) | Sim | Código do Cálculo |
| CmpIni | Date | Sim | Competência de Início da Apuração do PLR |
| CmpFim | Date | Sim | Competência Final da Apuração do PLR |
| TabEve | Number(003,0) | Sim | Código da Tabela de Eventos |
| CodEve | Number(004,0) | Sim | Código do Evento do PLR na Folha |
| NivLoc | Number(002,0) | Sim | Nível da Loja no Local |

---

## Chave Primária

- NumEmp
- CmpPlr

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R206DEF_002

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

### IR_R206DEF_006

**Tabela:** R008EVC

| Origem | Destino |
|--------|---------|
| TabEve | CodTab |
| CodEve | CodEve |

