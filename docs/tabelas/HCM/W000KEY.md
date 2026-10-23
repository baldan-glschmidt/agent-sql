# W000KEY

## Descrição

Mantém chaves associadas à instâncias de processos

---

## Resumo

- Campos: 3
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| PRCIID | Number(010,0) | Não | Identificador da instância do processo |
| PROCID | Number(005,0) | Sim | Identificador do processo |
| PRIKEY | String(030) | Sim | Chave inst. do proc. |

---

## Chave Primária

- PRCIID

---

## Índices

### W000KEYindiceUnico

**Tipo:** Unico

Campos:
- PROCID
- PRIKEY

---

## Relacionamentos

Nenhum relacionamento cadastrado.
