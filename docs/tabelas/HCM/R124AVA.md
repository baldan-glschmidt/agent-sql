# R124AVA

## Descrição

Colaborador - Aprovação Avaliação

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador Candidato |
| NumCad | Number(009,0) | Não | Cadastro do Candidato |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodGav | Number(003,0) | Não | Código do Grupo de Avaliação |
| DatGra | Date | Não | Data Resultado Avaliação |
| CodUsu | Number(010,0) | Sim | Código do usuário responsável pelo registro |
| UsuApr | Number(010,0) | Sim | Código do usuário aprovador |
| DatApr | Date | Sim | Data da aprovação da avaliação |
| HorApr | Number(005,0) | Sim | Hora da aprovação |
| ObsApr | String(1000) | Sim | Observações sobre aprovação |
| IndApr | Number(001,0) | Sim | Indica a situação da avaliação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- EstCar
- CodGav
- DatGra

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
