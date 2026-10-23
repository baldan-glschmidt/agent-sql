# R034USU

## Descrição

Usuários dos Colaboradores

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| CodUsu | Number(010,0) | Não | Código do Usuário para o Colaborador |
| CriUsu | Number(001,0) | Sim | Criar Usuário Colaborador no Sistema |
| TipDoc | Number(001,0) | Sim | Tipo do Documento do Visitante |
| NumDoc | String(020) | Sim | Número do Documento do Visitante |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodUsu

---

## Índices

### R034USUIndice2

**Tipo:** Não unico

Campos:
- CodUsu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
