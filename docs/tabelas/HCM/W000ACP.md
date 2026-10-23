# W000ACP

## Descrição

Tabela para manutenção de processos de workflow ativos

---

## Resumo

- Campos: 4
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PROCID | Number(005,0) | Não | Identificador único do processo de workflow |
| CURVER | Number(005,0) | Sim | Versão corrente, ou seja, versão ativa do processo |
| PRCNAM | String(255) | Sim | Nome do processo de workflow |
| ACTIVE | Number(001,0) | Sim | Indica se o processo está ativo |

---

## Chave Primária

- PROCID

---

## Índices

### W000ACPPRCNAM

**Tipo:** Não unico

Campos:
- PRCNAM

---

## Relacionamentos

Nenhum relacionamento cadastrado.
