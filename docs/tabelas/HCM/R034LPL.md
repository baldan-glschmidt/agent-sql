# R034LPL

## Descrição

Log de permissão por local físico

---

## Resumo

- Campos: 6
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdtPes | String(023) | Não | Identificador da Pessoa |
| CodDsp | Number(009,0) | Não | Código do Dispositivo |
| DatAlt | Date | Não | Data da alteração |
| TipOpe | String(001) | Sim | Tipo da operação (I/E) Inclusão/Exclusão |
| ObsAco | String(080) | Sim | Observação da permissão |
| CodUsu | Number(010,0) | Sim | Código do usuário que realizou a permissão |

---

## Chave Primária

- IdtPes
- CodDsp
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
