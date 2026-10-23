# R067CMD

## Descrição

Lista de Comandos de Acesso

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCmd | Number(003,0) | Não | Código do Comando |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor |
| DatChe | Date | Sim | Data de Chegada do Comando |
| HorChe | Number(005,0) | Sim | Hora de Chegada do Comando |
| NumTen | Number(001,0) | Sim | Número de Tentativas |
| StaCmd | Number(001,0) | Sim | Status do Comando |

---

## Chave Primária

- CodCmd
- CodPlt
- CodRlg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R067CMD_001

**Tabela:** R058PLT

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |

### IR_R067CMD_002

**Tabela:** R058RLG

| Origem | Destino |
|--------|---------|
| CodPlt | CodPlt |
| CodRlg | CodRlg |

