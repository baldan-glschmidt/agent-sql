# R083ARI

## Descrição

PPRA - Ambiente de Risco

---

## Resumo

- Campos: 7
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número Empresa |
| CmpPpa | Date | Não | Competência do PPRA |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| DesAri | String(3000) | Sim | Descrição do Ambiente de Risco |
| AtiRis | String(700) | Sim | Descrição das Atividades de Risco |
| ConAmb | String(3000) | Sim | Condições ambientais de trabalho |

---

## Chave Primária

- NumEmp
- CmpPpa
- TabOrg
- NumLoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R083ARI_003

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

