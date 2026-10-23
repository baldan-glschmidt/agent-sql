# R136IMP

## Descrição

Testes turma - Imagem das perguntas

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
| CodTst | String(005) | Não | Código do teste |
| CodPer | String(003) | Não | Código da pergunta |
| SeqImg | Number(003,0) | Não | Sequência da imagem |
| DesImg | String(255) | Sim | Descrição da imagem |
| Imagem | Image | Sim | Imagem da pergunta |

---

## Chave Primária

- CodTst
- CodPer
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R136IMP_000

**Tabela:** R136TES

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |

### IR_R136IMP_001

**Tabela:** R136PER

| Origem | Destino |
|--------|---------|
| CodTst | CodTst |
| CodPer | CodPer |

