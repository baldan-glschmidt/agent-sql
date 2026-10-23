# R073FOR

## Descrição

Foto do Responsável do Aluno

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipDoc | Number(001,0) | Não | Tipo do Documento do Responsável |
| NumDoc | String(020) | Não | Número do Documento do Responsável |
| FotRes | Image | Sim | Foto do Responsável do Aluno |
| DatFot | Date | Sim | Data da Foto |
| HorFot | Number(005,0) | Sim | Hora da Foto |

---

## Chave Primária

- TipDoc
- NumDoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R073FOR_001

**Tabela:** R073RES

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

