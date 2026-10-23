# R940END

## Descrição

Dicionário de tradução de enumerações

---

## Resumo

- Campos: 7
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| LngKey | Number(005,0) | Não | Chave do idioma |
| EnmNam | String(032) | Não | Nome da enumeração |
| EnmKey | String(100) | Não | Chave da enumeração |
| NatVal | String(499) | Sim | Valor nativo da enumeração |
| EnmVal | String(500) | Sim | Valor da enumeração |
| TrnKey | String(100) | Sim | Tradução da chave |
| TrnChn | Number(001,0) | Sim | Tradução alterada |

---

## Chave Primária

- LngKey
- EnmNam
- EnmKey

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
