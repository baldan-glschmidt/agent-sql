# R600KEY

## Descrição

Tabela de Alterações nas Chaves do Smart Card

---

## Resumo

- Campos: 5
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DatAlt | Date | Não | Data da Última Alteração |
| SeqAlt | Number(002,0) | Não | Sequência da Alteração da Chave |
| OldKey | String(018) | Sim | Antiga Chave para Acesso ao Smart Card |
| NewKey | String(018) | Sim | Nova Chave para Acesso ao Smart Card |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou o Agendamento |

---

## Chave Primária

- DatAlt
- SeqAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
