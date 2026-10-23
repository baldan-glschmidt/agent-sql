# R016RCO

## Descrição

Requisitos por Local - Conhecimento

---

## Resumo

- Campos: 13
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número Empresa |
| DatRqu | Date | Não | Data do Requisito do Cargo |
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| FamCnc | String(004) | Não | Código da Família de Conhecimentos |
| CodCnc | String(005) | Não | Código do Conhecimento |
| PesCnc | Number(002,0) | Sim | OBSOLETO - Peso do Conhecimento |
| ConRec | String(001) | Sim | Considera este requisito para recrutamento |
| ConPpp | String(001) | Sim | Considera requisito p/perfil profissiográfico previdenciário |
| ExiRqu | String(001) | Sim | Exigência do requisito(D-Desejável/N-Necessário) |
| CodPro | Number(003,0) | Sim | Código da Tabela de Proficiência - OBSOLETO |
| DatPro | Date | Sim | Data da Tabela de Níveis de Proficiência - OBSOLETO |
| CodNiv | Number(002,0) | Sim | Código do Nível da Proficiência - OBSOLETO |

---

## Chave Primária

- NumEmp
- DatRqu
- TabOrg
- NumLoc
- FamCnc
- CodCnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R016RCO_004

**Tabela:** R125FAM

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |

### IR_R016RCO_005

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

