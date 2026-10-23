# R100PLN

## Descrição

Reuniões Cipa - Plano de Ação

---

## Resumo

- Campos: 6
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodMan | Number(004,0) | Não | Código do Mandato |
| DatReu | Date | Não | Data da Reunião |
| HorReu | Number(005,0) | Não | Hora da Reunião |
| CodPln | Number(009,0) | Não | Código do Plano de Ação |

---

## Chave Primária

- NumEmp
- CodFil
- CodMan
- DatReu
- HorReu
- CodPln

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R100PLN_004

**Tabela:** R100REU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |
| DatReu | DatReu |
| HorReu | HorReu |

### IR_R100PLN_005

**Tabela:** R084PLN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPln | CodPln |

