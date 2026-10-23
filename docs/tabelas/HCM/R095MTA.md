# R095MTA

## Descrição

Materiais por Aluno

---

## Resumo

- Campos: 3
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumMat | String(015) | Não | Matrícula do Aluno |
| CodMat | String(008) | Não | Código do Material |
| ObsMat | String(080) | Sim | Observação |

---

## Chave Primária

- NumMat
- CodMat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R095MTA_000

**Tabela:** R073ALU

| Origem | Destino |
|--------|---------|
| NumMat | NumMat |

### IR_R095MTA_001

**Tabela:** R095MAT

| Origem | Destino |
|--------|---------|
| CodMat | CodMat |

