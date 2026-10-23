# R998LNF

## Descrição

Tabela dos campos que fazem parte de um link do usuário

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
| TblLnk | String(032) | Não | Tabela proprietária do campo que contém o link |
| FldLnk | String(032) | Não | Nome do campo proprietáio do link |
| FldSrc | String(032) | Não | Nome do campo origem |
| FldTrg | String(032) | Não | Nome do campo destino |
| FldOrd | Number(005,0) | Sim | Ordem dos campo para a ligação |
| ObjSis | String(001) | Sim | Identifica se o campo é de sistema ou usuário |

---

## Chave Primária

- TblLnk
- FldLnk
- FldSrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
