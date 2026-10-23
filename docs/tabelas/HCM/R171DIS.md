# R171DIS

## Descrição

Professores - Tabela de Disciplinas

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodDpf | Number(007,0) | Não | Código da Disciplina |
| DesDpf | String(040) | Sim | Descrição da Disciplina |
| CodApf | Number(004,0) | Sim | Código da Atividade Correspondente |
| IniDpf | Date | Sim | Data de Início de Validade da Disciplina |
| FimDpf | Date | Sim | Data de Fim da Validade da Disciplina |

---

## Chave Primária

- CodDpf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R171DIS_002

**Tabela:** R171ATI

| Origem | Destino |
|--------|---------|
| CodApf | CodApf |

