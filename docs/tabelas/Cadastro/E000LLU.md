# E000LLU

## Descrição

Tabelas - Ext. Dados - Log de tentativa de acesso por módulo e usuário

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| IdeUni | Number(009,0) | Não | Identificador de registro |
| IdeEms | Number(009,0) | Não | Identificador de registro |
| CodUsu | Number(010,0) | Não | Usuário responsável pela geração do registro |
| UsuLog | String(001) | Não | Usuário conseguiu acessar determinado módulo naquela data |
| UsuTlo | String(001) | Não | Usuário tentou acessar determinado módulo naquela data |

---

## Chave Primária

- IdeUni

---

## Índices

### E000LLUIndice1

**Tipo:** Unico

Campos:
- IdeEms
- CodUsu

---

## Relacionamentos

### IR_E000LLU_001

**Tabela:** E000EMS

| Origem | Destino |
|--------|---------|
| IdeEms | IdeUni |

