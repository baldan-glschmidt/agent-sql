# R044DIS

## Descrição

Cálculo de Dissídios

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
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCal | Number(005,0) | Não | Código de Cálculo |
| CodDis | Number(005,0) | Não | Código de Dissídio |

---

## Chave Primária

- NumEmp
- CodCal
- CodDis

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R044DIS_001

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

