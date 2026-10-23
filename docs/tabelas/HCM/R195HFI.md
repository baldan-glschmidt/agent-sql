# R195HFI

## Descrição

Cenário - Histórico Filial

---

## Resumo

- Campos: 25
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAlt | Date | Não | Data da Alteração do Cargo |
| EmpAtu | Number(004,0) | Sim | Código da Nova Empresa |
| CodFil | Number(006,0) | Sim | Código da Nova Filial |
| CadAtu | Number(009,0) | Sim | Código do Novo Cadastro |
| CodCcu | String(018) | Sim | Código do Novo Centro de Custo |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Novo Cargo |
| CarVag | String(024) | Sim | Código do novo cargo para ocupação da vaga |
| CodMot | Number(003,0) | Sim | Motivo da Alteração do Cargo |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma da Nova Empresa |
| NumLoc | Number(009,0) | Sim | Local do Organograma da Nova Empresa |
| AtuQvO | String(001) | Sim | Atualiza Quadro de vagas no cenário de origem (S/N) |
| AtuQvD | String(001) | Sim | Atualiza Quadro de vagas no destino (S/N) |
| CenAtu | Number(004,0) | Sim | Código do cenário |
| CauDem | Number(002,0) | Sim | Causa Demissão do Colaborador |
| GerCol | String(001) | Sim | Origem da geração do histórico |
| TipTrf | Number(001,0) | Sim | Para transferência de empresa, indica se haverá cálculo de rescisão |
| CodTap | Number(003,0) | Sim | Tipo de atuação que o colaborador exercerá no posto |
| EstPos | Number(003,0) | Sim | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Sim | Código do posto de trabalho onde o colaborador atua |
| MotAlt | Number(003,0) | Sim | Motivo de alteração do posto de trabalho |

---

## Chave Primária

- NumEmp
- CodCen
- TipCol
- NumCad
- DatAlt

---

## Índices

### R195HFIIndice2

**Tipo:** Não unico

Campos:
- EmpAtu
- CodFil
- CadAtu

---

## Relacionamentos

Nenhum relacionamento cadastrado.
