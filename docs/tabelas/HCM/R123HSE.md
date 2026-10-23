# R123HSE

## Descrição

Selecionados Triagem - Colaborador - Nova

---

## Resumo

- Campos: 10
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código Requisição |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Cargo Requisitado |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Colaborador |
| MotEli | Number(002,0) | Não | Motivo da Eliminação |
| SitCan | Number(002,0) | Sim | Situação do Candidato |
| OriSel | Number(001,0) | Sim | Origem Seleção |
| CodJus | Number(003,0) | Sim | Código da justificativa para eliminação/desistência candidato |

---

## Chave Primária

- CodRqu
- EstCar
- CodCar
- NumEmp
- TipCol
- NumCad
- MotEli

---

## Índices

### R123HSEIndice2

**Tipo:** Não unico

Campos:
- CodRqu
- EstCar
- CodCar
- MotEli

---

## Relacionamentos

Nenhum relacionamento cadastrado.
