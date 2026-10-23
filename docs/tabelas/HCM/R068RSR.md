# R068RSR

## Descrição

Reserva Refeição

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
| RlgRes | Number(005,0) | Não | Código do Coletor na Reserva |
| FncRes | Number(002,0) | Não | Código da Funçao na Reserva |
| IniRes | Number(005,0) | Não | Hora de Início da Reserva |
| FimRes | Number(005,0) | Não | Hora Fim da Reserva |

---

## Chave Primária

- NumEmp
- CodRef
- CodPlt
- RlgRes
- FncRes
- IniRes
- FimRes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R068RSR_001

**Tabela:** R068TRF

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodRef | CodRef |

### IR_R068RSR_002

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

