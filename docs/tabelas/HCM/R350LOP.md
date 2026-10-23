# R350LOP

## Descrição

S-1020 - eSocial - Tabela de Lotações - Processo Judicial

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PidExc | String(050) | Não | Identificador da execução da pendência para consultar retorno recibo |
| SeqLop | Number(009,0) | Não | Sequência |
| NumPro | String(021) | Sim | Número do Processo |
| CodSus | Number(014,0) | Sim | Código Suspensão |
| CodTer | Number(004,0) | Sim | Código de Terceiros |

---

## Chave Primária

- PidExc
- SeqLop

---

## Índices

### R350LOPIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
