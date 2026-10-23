# R206QLO

## Descrição

PLR Paquetá - Quesitos Atingidos p/ Loja

---

## Resumo

- Campos: 6
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CmpRef | Date | Não | Competência de Referência |
| CodQst | Number(004,0) | Não | Código do Quesito |
| QstAtg | String(001) | Sim | Indicador de Quesito Atingido (S,N) |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- CmpRef
- CodQst

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R206QLO_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R206QLO_002

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

### IR_R206QLO_004

**Tabela:** R206QST

| Origem | Destino |
|--------|---------|
| CodQst | CodQst |

