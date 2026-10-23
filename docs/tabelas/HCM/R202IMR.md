# R202IMR

## Descrição

Teste Certificação - Imagens da Resposta

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| GruPer | Number(005,0) | Não | Código do teste |
| CodPer | Number(003,0) | Não | Código da Pergunta |
| CodRes | Number(002,0) | Não | Código da Resposta |
| SeqImg | Number(003,0) | Não | Sequência da Imagem |
| DesImg | String(255) | Sim | Descrição da Imagem |
| Imagem | Image | Sim | Imagem |

---

## Chave Primária

- GruPer
- CodPer
- CodRes
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R202IMR_000

**Tabela:** R202GRU

| Origem | Destino |
|--------|---------|
| GruPer | GruPer |

### IR_R202IMR_001

**Tabela:** R202PER

| Origem | Destino |
|--------|---------|
| GruPer | GruPer |
| CodPer | CodPer |

### IR_R202IMR_002

**Tabela:** R202RES

| Origem | Destino |
|--------|---------|
| GruPer | GruPer |
| CodPer | CodPer |
| CodRes | CodRes |

