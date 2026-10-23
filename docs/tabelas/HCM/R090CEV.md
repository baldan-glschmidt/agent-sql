# R090CEV

## Descrição

Crachás Extraviados Visitantes

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipDoc | Number(001,0) | Não | Tipo do Documento do Visitante |
| NumDoc | String(020) | Não | Número do Documento do Visitante |
| NumCra | Number(012,0) | Não | Número do Crachá Extraviado pelo Visitante |

---

## Chave Primária

- TipDoc
- NumDoc
- NumCra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R090CEV_001

**Tabela:** R090VIS

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

### IR_R090CEV_002

**Tabela:** R090CEX

| Origem | Destino |
|--------|---------|
| NumCra | NumCra |

