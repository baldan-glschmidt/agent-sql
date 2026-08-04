# E000EMS

## Descrição

Tabelas - Ext. Dados - Log de tentativa de acesso por módulo

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| ModSis | String(008) | Não | Módulo que o usuário tentou acessar |
| DatExe | Date | Não | Data em que o usuário tentou acessar o menu |
| QtdLog | Number(004,0) | Sim | Quantidade de acessos realizado com sucesso no dia |
| QtdTen | Number(004,0) | Sim | Quantidade de tentativas de acessos realizadas no dia |

---

## Chave Primária

- IdeUni

---

## Índices

### E000EMSIndice1

**Tipo:** Unico

Campos:
- ModSis
- DatExe

---

## Relacionamentos

Nenhum relacionamento cadastrado.
