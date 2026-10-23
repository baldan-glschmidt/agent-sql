# R124CSL

## Descrição

Colaborador - Solicitação Vaga

---

## Resumo

- Campos: 15
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Candidato |
| NumCad | Number(009,0) | Não | Cadastro do Candidato |
| DatSol | Date | Não | Data da Solicitação |
| CodSol | Number(003,0) | Não | Tipo da Solicitação |
| AbrFil | String(025) | Sim | Abrangência de filial |
| AbrLoc | String(1500) | Sim | Abrangência de local |
| AbrTur | String(015) | Sim | Abrangência de turno |
| SisCar | Number(002,0) | Sim | Sistema de Cargo |
| CodHie | Number(003,0) | Sim | Hierarquia pretendida |
| DatVal | Date | Sim | Data de validade da solicitação |
| SitSol | Number(001,0) | Sim | Situação da solicitação |
| CodJus | Number(003,0) | Sim | Código da justificativa para eliminação/desistência candidato. |
| DatJus | Date | Sim | Data de conclusão da solicitação |
| CodRqu | Number(009,0) | Sim | Código da requisição que atendeu a solicitação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatSol
- CodSol

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124CSL_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R124CSL_004

**Tabela:** R114SLC

| Origem | Destino |
|--------|---------|
| CodSol | CodSlc |

