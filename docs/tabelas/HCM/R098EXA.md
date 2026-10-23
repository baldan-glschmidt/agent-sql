# R098EXA

## Descrição

Exames do Equipamento

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipEqp | Number(003,0) | Não | Código Tipo de Equipamento |
| CodEqp | Number(006,0) | Não | Código do Equipamento |
| CodExa | Number(004,0) | Não | Código Exame |
| ValExa | Number(003,0) | Sim | Validade do Exame em Meses |

---

## Chave Primária

- NumEmp
- TipEqp
- CodEqp
- CodExa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R098EXA_001

**Tabela:** R098TEQ

| Origem | Destino |
|--------|---------|
| TipEqp | TipEqp |

### IR_R098EXA_002

**Tabela:** R098EQP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipEqp | TipEqp |
| CodEqp | CodEqp |

### IR_R098EXA_003

**Tabela:** R108EXA

| Origem | Destino |
|--------|---------|
| CodExa | CodExa |

