# R195CND

## Descrição

Cenário - Contas Contábeis por Natureza Despesa

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| NatDes | Number(003,0) | Não | Natureza de despesa |
| IteOrc | Number(003,0) | Não | Código do Item |
| CodCon | String(030) | Sim | Código da conta contábil |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| CodCen | Number(004,0) | Sim | Código do cenário |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- NatDes
- IteOrc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
