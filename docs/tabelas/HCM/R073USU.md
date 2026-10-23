# R073USU

## Descrição

Usuários de responsável de aluno

---

## Resumo

- Campos: 3
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipDoc | Number(001,0) | Não | Tipo do Documento do Responsável |
| NumDoc | String(020) | Não | Número do Documento do Responsável |
| CodUsu | Number(010,0) | Não | Código do Usuário para o responsável |

---

## Chave Primária

- TipDoc
- NumDoc
- CodUsu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R073USU_001

**Tabela:** R073RES

| Origem | Destino |
|--------|---------|
| TipDoc | TipDoc |
| NumDoc | NumDoc |

