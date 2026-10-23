# R030ANU

## Descrição

Anuidades Pagas p/ Empresa

---

## Resumo

- Campos: 4
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| NumAnu | Number(002,0) | Não | Número Anuidade |
| TetAnu | Number(005,2) | Sim | Percentual máximo pago de anuidade |
| TetVal | Number(008,2) | Sim | Valor máximo pago de anuidade |

---

## Chave Primária

- NumEmp
- NumAnu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030ANU_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

