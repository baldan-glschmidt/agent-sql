# R005VEI

## Descrição

Veículos das Linhas de ônibus

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodLin | Number(004,0) | Não | Linha de ônibus |
| NumVei | Number(006,0) | Não | Número do Veículo |
| PlaVei | String(010) | Sim | Inutilizado |

---

## Chave Primária

- NumEmp
- CodLin
- NumVei

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005VEI_001

**Tabela:** R005LIN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodLin | CodLin |

