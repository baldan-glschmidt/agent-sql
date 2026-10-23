# R176CLO

## Descrição

Contas Local

---

## Resumo

- Campos: 7
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodClc | Number(004,0) | Não | Código do CLC |
| HisPad | Number(004,0) | Sim | Código Histórico Padrão |
| GerGer | String(001) | Sim | Gerar Gerencial |

---

## Chave Primária

- NumEmp
- TabOrg
- NumLoc
- TabEve
- CodClc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R176CLO_004

**Tabela:** R048CLC

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodClc | CodClc |

