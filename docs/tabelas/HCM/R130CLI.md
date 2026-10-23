# R130CLI

## Descrição

Custos do Orçamento - Item de Custo - Por Local

---

## Resumo

- Campos: 8
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodCua | Number(009,0) | Não | Código do Curso |
| CmpCus | Date | Não | Competência de Custos |
| SeqCus | Number(002,0) | Não | Sequência de Custos |
| CodTcu | Number(004,0) | Não | Código do Item de Custo |
| ValCus | Number(011,2) | Sim | Valor do Item de Custo |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CodCua
- CmpCus
- SeqCus
- CodTcu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R130CLI_005

**Tabela:** R130CLO

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TabOrg | TabOrg |
| NumLoc | NumLoc |
| CodCua | CodCua |
| CmpCus | CmpCus |
| SeqCus | SeqCus |

### IR_R130CLI_006

**Tabela:** R130TCU

| Origem | Destino |
|--------|---------|
| CodTcu | CodTcu |

