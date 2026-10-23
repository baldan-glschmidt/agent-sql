# R126ANX

## Descrição

Anúncios - Anexos

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
| CodVag | String(010) | Não | Código da Vaga usado na publicação do anúncio |
| SeqAne | Number(002,0) | Não | Sequência do anexo |
| NomAne | String(250) | Sim | Nome do arquivo anexo |
| ArqAne | Image | Sim | Arquivo anexo |

---

## Chave Primária

- CodVag
- SeqAne

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126ANX_000

**Tabela:** R126ANU

| Origem | Destino |
|--------|---------|
| CodVag | CodVag |

