# R210IMP

## Descrição

Questionário - Imagens da Pergunta

---

## Resumo

- Campos: 5
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodQue | Number(003,0) | Não | Código do Questionário |
| CodPer | Number(003,0) | Não | Código da Pergunta |
| SeqImg | Number(003,0) | Não | Sequência da Imagem |
| DesImg | String(255) | Sim | Descrição da Imagem |
| Imagem | Image | Sim | Imagem da Pergunta |

---

## Chave Primária

- CodQue
- CodPer
- SeqImg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R210IMP_001

**Tabela:** R210PER

| Origem | Destino |
|--------|---------|
| CodQue | CodQue |
| CodPer | CodPer |

