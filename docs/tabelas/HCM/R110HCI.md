# R110HCI

## Descrição

Histórico de Calibração dos Impedanciômetros

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
| CodImp | Number(003,0) | Não | Código do Impedanciômetro |
| DatCal | Date | Não | Data da Calibração do Impedanciômetro |

---

## Chave Primária

- NumEmp
- CodImp
- DatCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110HCI_001

**Tabela:** R110IMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodImp | CodImp |

