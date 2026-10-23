# R073FOT

## Descrição

Foto do Aluno

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumMat | String(015) | Não | Matrícula do Aluno |
| FotAlu | Image | Sim | Foto do Aluno |
| DatFot | Date | Sim | Data da Foto |
| HorFot | Number(005,0) | Sim | Hora da Foto |

---

## Chave Primária

- NumMat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R073FOT_000

**Tabela:** R073ALU

| Origem | Destino |
|--------|---------|
| NumMat | NumMat |

