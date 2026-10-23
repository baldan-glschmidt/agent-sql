# R042GER

## Descrição

Informações Gerais

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipRcs | Number(001,0) | Não | Tipo Rescisão |
| PagRcs | Date | Não | Data de pagamento da rescisão |
| ChaMov | String(030) | Sim | Chave de movimentação |
| OpcPre | Number(001,0) | Sim | Opção para determinar o tipo do presposto |
| EmpPre | Number(004,0) | Sim | Código da empresa do preposto responsável |
| TipPre | Number(001,0) | Sim | Tipo do preposto responsável |
| CadPre | Number(009,0) | Sim | Cadastro do preposto responsável |
| NomPre | String(040) | Sim | Nome do preposto responsável |
| DocPre | String(025) | Sim | Número do documento do preposto |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TipRcs
- PagRcs

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
