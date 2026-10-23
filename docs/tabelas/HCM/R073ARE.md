# R073ARE

## Descrição

Aluno / Responsável

---

## Resumo

- Campos: 4
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipDoc | Number(001,0) | Não | Tipo do Documento do Responsável |
| NumDoc | String(020) | Não | Número do Documento do Responsável |
| NumMat | String(015) | Não | Matrícula do Aluno |
| ParAlu | Number(001,0) | Sim | Parentesco do Responsável com Aluno |

---

## Chave Primária

- NumMat
- TipDoc
- NumDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R073ARE_001

**Tabela:** R073RES

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

### IR_R073ARE_002

**Tabela:** R073ALU

| Origem | Destino |
|--------|---------|
| NumMat | NumMat |

