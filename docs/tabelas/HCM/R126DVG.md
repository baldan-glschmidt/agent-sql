# R126DVG

## Descrição

Anúncios - Período de divulgação por público-alvo

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodVag | String(010) | Não | Código da Vaga usado na publicação do anúncio |
| PubAlv | Number(001,0) | Não | Público alvo do anúncio |
| CodPer | Number(003,0) | Não | Código do perfil |
| DatIni | Date | Não | Data de início do período de divulgação |
| DatFim | Date | Sim | Data de término do período de divulgação |

---

## Chave Primária

- CodVag
- PubAlv
- CodPer
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R126DVG_000

**Tabela:** R126ANU

| Origem | Destino |
|--------|---------|
| CodVag | CodVag |

