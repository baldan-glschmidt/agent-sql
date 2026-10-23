# R998TBL

## Descrição

Tabelas do usuário

---

## Resumo

- Campos: 8
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TBLNAM | String(032) | Não | Nome da Tabela |
| DESTBL | String(255) | Sim | Descrição |
| ORINAM | String(032) | Sim | Nome Original da tabela, no caso de renomear |
| CodUsu | Number(010,0) | Sim | Código do último usuário que alterou a tabela |
| LasUpd | Date | Sim | Data da última alteração |
| PKFLDS | String(1999) | Sim | Campos que fazerm parte da chave primária |
| TblOrd | Number(005,0) | Sim | Ordem da tabela no TBS |
| ObjSis | String(001) | Sim | Identifica se a tabela é de sistema ou usuário |

---

## Chave Primária

- TBLNAM

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
