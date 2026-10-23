# R122FOT

## Descrição

Candidatos Externos - Foto

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
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| FotCan | Image | Sim | Foto do Candidato |
| DatFot | Date | Sim | Data da Foto |
| HorFot | Number(005,0) | Sim | Hora da Foto |

---

## Chave Primária

- NumCan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122FOT_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

