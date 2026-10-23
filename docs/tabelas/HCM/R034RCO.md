# R034RCO

## Descrição

Requisitos Colaborador - Conhecimentos

---

## Resumo

- Campos: 14
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatRqu | Date | Não | Data de início do requisito |
| FamCnc | String(004) | Não | Código da Família de Conhecimentos |
| CodCnc | String(005) | Não | Código do Conhecimento |
| IdiLei | String(001) | Sim | Nível Conhecimento Leitura |
| IdiEsc | String(001) | Sim | Nível Conhecimento Escrita |
| IdiCon | String(001) | Sim | Nível Conhecimento Conversação |
| ExiRqu | String(001) | Sim | Exigência do requisito(D-Desejável/N-Necessário) |
| DatTer | Date | Sim | Data de término do requisito |
| CodPro | Number(003,0) | Sim | Código da Tabela de Proficiência - OBSOLETO |
| DatPro | Date | Sim | Data da Tabela de Níveis de Proficiência - OBSOLETO |
| CodNiv | Number(002,0) | Sim | Código do Nível da Proficiência - OBSOLETO |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatRqu
- FamCnc
- CodCnc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R034RCO_004

**Tabela:** R125FAM

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |

### IR_R034RCO_005

**Tabela:** R125CNC

| Origem | Destino |
|--------|---------|
| FamCnc | FamCnc |
| CodCnc | CodCnc |

