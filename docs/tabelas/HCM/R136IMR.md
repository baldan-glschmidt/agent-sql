# R136IMR

## Descrição

Testes turma - Imagem das respostas

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
| CodTst | String(005) | Não | Código do teste |
| CodPer | String(003) | Não | Código da pergunta |
| CodRes | String(002) | Não | Código da resposta |
| SeqImg | Number(003,0) | Não | Sequência da imagem |
| DesImg | String(255) | Sim | Descrição da imagem |
| Imagem | Image | Sim | Imagem da resposta |

---

## Chave Primária

- CodTst
- CodPer
- CodRes
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R136IMR_000

**Tabela:** R136TES

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |

### IR_R136IMR_001

**Tabela:** R136PER

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |
| CodPer | CodPer |

### IR_R136IMR_002

**Tabela:** R136RES

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |
| CodPer | CodPer |
| CodRes | CodRes |

