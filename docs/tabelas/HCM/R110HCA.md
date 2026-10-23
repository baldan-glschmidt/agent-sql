# R110HCA

## Descrição

Histórico de Calibragem dos Audiômetros

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
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodAud | Number(003,0) | Não | Código do Audiômetro |
| DatCal | Date | Não | Data da Calibragem do Audiômetro |

---

## Chave Primária

- NumEmp
- CodAud
- DatCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110HCA_001

**Tabela:** R110AUD

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodAud | CodAud |

