# R240EHA

## Descrição

Configurações Analytics Absenteísmo - Eventos de horas de ausência

---

## Resumo

- Campos: 4
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabEve | Number(003,0) | Não | Código Tabela de Eventos |
| CodEve | Number(004,0) | Não | Código do Evento |
| CodTip | Number(003,0) | Não | Código do Tipo de Ausência |

---

## Chave Primária

- NumEmp
- CodTip
- TabEve
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R240EHA_003

**Tabela:** R240TPA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodTip | CodTip |

