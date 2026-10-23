# R077HBP

## Descrição

Habilidades Técnicas - Processos

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
| CodHte | String(006) | Não | Código da Habilidade Técnica |
| DatPrh | Date | Não | Data do Processo |
| CodPrh | String(011) | Não | Código do Processo da Habilidade Técnica |

---

## Chave Primária

- CodHte
- DatPrh
- CodPrh

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R077HBP_000

**Tabela:** R077HTE

| Origem | Destino |
|--------|---------|
| CodHte | CodHte |

### IR_R077HBP_002

**Tabela:** R077PRO

| Origem | Destino |
|--------|---------|
| CodPrh | CodPrh |

