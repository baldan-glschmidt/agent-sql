# R176DLO

## Descrição

Def. Contas p/ Local

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| FilCtb | Number(006,0) | Sim | Filial Contábil |
| OutEmp | Number(004,0) | Sim | Código da Outra Empresa |
| OutTab | Number(004,0) | Sim | Tabela de Organograma |
| OutLoc | Number(009,0) | Sim | Código Outro Local Org. |
| TipCta | String(001) | Sim | Tipos de Contas (P,O) |
| LocTxt | String(010) | Sim | Local Exp.Arq.Texto |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R176DLO_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R176DLO_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

