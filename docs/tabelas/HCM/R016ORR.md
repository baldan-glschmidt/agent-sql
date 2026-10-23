# R016ORR

## Descrição

Coletores/Funções Rateio Local

---

## Resumo

- Campos: 5
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodPlt | Number(005,0) | Não | Código do Site |
| CodRlg | Number(005,0) | Não | Código do Coletor p/Rateio |
| CodFnc | Number(002,0) | Não | Código da Função p/Rateio |

---

## Chave Primária

- TabOrg
- NumLoc
- CodPlt
- CodRlg
- CodFnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016ORR_001

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

