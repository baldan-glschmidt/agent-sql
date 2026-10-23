# R068CAN

## Descrição

Cancelamento da Reserva

---

## Resumo

- Campos: 7
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodRef | Number(003,0) | Não | Código da Refeição |
| CodPlt | Number(005,0) | Não | Código do Site |
| RlgCan | Number(005,0) | Não | Código do Coletor na Reserva |
| FncCan | Number(002,0) | Não | Código da Função na Reserva |
| IniCan | Number(005,0) | Não | Faixa Início Cancelamento Reserva |
| FimCan | Number(005,0) | Não | Faixa Fim Cancelamento Reserva |

---

## Chave Primária

- NumEmp
- CodRef
- CodPlt
- RlgCan
- FncCan
- IniCan
- FimCan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R068CAN_001

**Tabela:** R068TRF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodRef | CodRef |

### IR_R068CAN_002

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

