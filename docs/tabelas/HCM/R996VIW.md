# R996VIW

## Descrição

Views do usuário

---

## Resumo

- Campos: 10
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| VIWNAM | String(032) | Não | Nome da view |
| VIWSEQ | Number(005,0) | Não | Sequência do SQL da view |
| VIWSQL | String(3999) | Não | SQL da view |
| VRSSQL | Number(003,0) | Não | Linguagem SQL |
| VIWDSC | String(100) | Sim | Descrição da view |
| ORINAM | String(032) | Sim | Nome original da view |
| CODUSU | Number(010,0) | Sim | Código do usuário |
| LASUPD | Date | Sim | Última utilização |
| ObjSis | String(001) | Sim | Identifica se a view é de sistema ou usuário |
| IDTFLD | String(032) | Sim | Identificator Field. |

---

## Chave Primária

- VIWNAM
- VIWSEQ

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
