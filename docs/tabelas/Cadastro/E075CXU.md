# E075CXU

## Descrição

Tabelas - Ligações - Categorias de Produto x Usuários

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
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodUsu | Number(010,0) | Não | Código do usuário |
| IdeCat | String(050) | Não | Identificador único da Categoria de Produtos |
| CodCat | String(010) | Sim | Código da Categoria vinculada a um produto |
| DesCat | String(040) | Não | Descrição usual da categoria |
| NomUsu | String(255) | Sim | Nome do usuário |
| SitReg | String(001) | Não | Situação do registro |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAlt | Number(010,0) | Sim | Usuário responsável pela última alteração do registro |
| DatAlt | Date | Sim | Data da última alteração do registro |
| HorAlt | Number(005,0) | Sim | Hora da última alteração do registro |

---

## Chave Primária

- CodEmp
- CodUsu
- IdeCat

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
