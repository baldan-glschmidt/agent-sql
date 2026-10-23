# R103GPS

## Descrição

PSS - Grupo

---

## Resumo

- Campos: 6
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodPss | Number(003,0) | Não | Código do grupo de PSS |
| DesPSS | String(050) | Sim | Descrição do Grupo |
| TurPss | Number(001,0) | Sim | Turno de Trabalho |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |

---

## Chave Primária

- NumEmp
- CodPss

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R103GPS_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R103GPS_005

**Tabela:** R016ORN

| Origem | Destino |
|--------|---------|
| TabOrg | TabOrg |
| NumLoc | NumLoc |

