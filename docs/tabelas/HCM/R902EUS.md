# R902EUS

## Descrição

Estatísticas de uso do sistema

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ACTDAT | Date | Não | Data da ação |
| SYSMOD | String(050) | Não | Sistema e módulo que executou a ação no sistema(número_do_systema.modulo) |
| ACTTYP | Number(001,0) | Não | Tipo do objeto |
| OBJNAM | String(100) | Não | Nome do objeto que sofreu a ação |
| ACTCTX | String(200) | Não | Contexto da Ação(CS,BA,WA,WS,WE) |
| ACTCNT | Number(009,0) | Sim | Quantidade de vezes que esta ação foi executada no dia |

---

## Chave Primária

- ACTDAT
- SYSMOD
- ACTTYP
- OBJNAM
- ACTCTX

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
