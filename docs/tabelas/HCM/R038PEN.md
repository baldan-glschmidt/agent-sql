# R038PEN

## Descrição

Pendências de Transferências

---

## Resumo

- Campos: 16
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| DatTrf | Date | Não | Data Transferência |
| AltEmp | String(001) | Sim | Alterou Empresa |
| AltFil | String(001) | Sim | Alterou Filial |
| AltLoc | String(001) | Sim | Alterou Local |
| AltCcu | String(001) | Sim | Alterou C.Custo |
| AltCar | String(001) | Sim | Alterou Cargo |
| AltEsc | String(001) | Sim | Alterou Escala |
| AltDes | String(001) | Sim | Decorrente Desligamento |
| SitChe | Number(001,0) | Sim | Situação do cadastro do chefe |
| SitUsu | Number(001,0) | Sim | Situação das permissões e abrangência do usuário |
| NesRev | String(001) | Sim | Necessita Revisão |
| EmpAtu | Number(004,0) | Sim | Código da Nova Empresa |
| CadAtu | Number(009,0) | Sim | Código do Novo Cadastro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatTrf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
