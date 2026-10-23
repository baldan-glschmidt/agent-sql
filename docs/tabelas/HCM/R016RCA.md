# R016RCA

## Descrição

Requisitos por Local - Aperfeiçoamento - Conhecimentos Adquiridos

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número Empresa |
| DatRqu | Date | Não | Data do Requisito do Cargo |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| CodCua | Number(009,0) | Não | Código do Curso de Aperfeiçoamento |
| FamCnc | String(004) | Não | Código da Família de Conhecimentos |
| CodCnc | String(005) | Não | Código do Conhecimento |
| NumRev | Number(006,0) | Sim | Revisão |
| SelCon | String(001) | Sim | Selecionar |
| HerCur | String(001) | Sim | Herdado do Curso |

---

## Chave Primária

- NumEmp
- DatRqu
- TabOrg
- NumLoc
- CodCua
- FamCnc
- CodCnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016RCA_004

**Tabela:** R128CUA

| Origem | Destino |
|--------|---------|
| CodCua | CodCua |

### IR_R016RCA_005

**Tabela:** R125FAM

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |

### IR_R016RCA_006

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

