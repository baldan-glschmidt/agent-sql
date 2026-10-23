# R078TBP

## Descrição

Times - Blocos de Habilidades Pessoais - OBSOLETA

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodTim | String(008) | Não | Código do Time |
| DatHab | Date | Não | Data da Última Revisão das Habilidades do Time |
| BloHpe | String(004) | Não | Bloco de Habilidades Pessoais |

---

## Chave Primária

- CodTim
- DatHab
- BloHpe

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R078TBP_000

**Tabela:** R078TIM

| Origem | Destino |
|--------|---------|
| CodTim | CodTim |

