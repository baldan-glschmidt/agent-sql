# R005FOT

## Descrição

Fotos do Acidente

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
| CodAci | Number(005,0) | Não | Código do Acidente |
| CodSeq | Number(002,0) | Não | Código da Sequência |
| ObsFot | String(2500) | Sim | Descrição da Foto |
| FotAci | Image | Sim | Foto do Acidente |

---

## Chave Primária

- CodAci
- CodSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005FOT_000

**Tabela:** R005ACI

| Origem | Destino |
|--------|---------|
| CodAci | CodAci |

