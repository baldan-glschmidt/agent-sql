# R999MEN

## Descrição

Menus personalizados pelo usuário

---

## Resumo

- Campos: 13
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodUsu | Number(010,0) | Não | Código do usuário |
| ModID | Number(005,0) | Não | Módulo |
| NamMen | String(100) | Não | Nome do menu |
| NamPar | String(100) | Sim | Pai do menu |
| SeqMen | Number(005,0) | Sim | Sequência do menu dentro do pai |
| DesMen | String(255) | Sim | Título do menu |
| Visibl | String(001) | Sim | Visível |
| RefMen | String(100) | Sim | Menu de referência |
| NomAnt | String(100) | Sim | Nome do menu anterior |
| RefExt | String(255) | Sim | Referência externa. Programa referenciado pelo menu |
| RefPar | String(255) | Sim | Parâmetro para a referência externa |
| RelMod | String(020) | Sim | Nome do modelo de relatório de referência |
| HotKey | String(050) | Sim | Tecla de atalho do menu |

---

## Chave Primária

- CodUsu
- ModID
- NamMen

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
