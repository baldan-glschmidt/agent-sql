# R110HDO

## Descrição

Ficha Médica - Histórico de Doação de Sangue

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodFic | Number(009,0) | Não | Código da Ficha Médica |
| DatDoa | Date | Não | Data Doação |

---

## Chave Primária

- NumEmp
- CodFic
- DatDoa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110HDO_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

