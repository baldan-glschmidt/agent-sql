# R202IMP

## Descrição

Teste Certificação - Imagem das Perguntas

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GruPer | Number(005,0) | Não | Código do teste |
| CodPer | Number(003,0) | Não | Código da Pergunta |
| SeqImg | Number(003,0) | Não | Sequência da Imagem |
| DesImg | String(255) | Sim | Descrição da Imagem |
| Imagem | Image | Sim | Imagem da Pergunta |

---

## Chave Primária

- GruPer
- CodPer
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R202IMP_000

**Tabela:** R202GRU

| Origem | Destino |
|--------|---------|
| GruPer | GruPer |

### IR_R202IMP_001

**Tabela:** R202PER

| Origem | Destino |
|--------|---------|
| GruPer | GruPer |
| CodPer | CodPer |

