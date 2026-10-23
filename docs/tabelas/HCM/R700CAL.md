# R700CAL

## Descrição

Controle de Usuários por Código de Cálculo

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCal | Number(005,0) | Não | Código do Cálculo |
| DatSeq | Number(005,0) | Não | Sequência do Dado |
| DatOne | String(254) | Sim | Dado Um (Criptografado) |
| DatTwo | String(254) | Sim | Dado Dois (Criptografado) |

---

## Chave Primária

- NumEmp
- CodCal
- DatSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R700CAL_001

**Tabela:** R044CAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCal | CodCal |

