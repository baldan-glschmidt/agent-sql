# R024ERL

## Descrição

Exceções de Requisitos de Cargo por Local

---

## Resumo

- Campos: 19
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TabOrg | Number(004,0) | Não | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Não | Local do Organograma |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| BloHte | String(004) | Sim | Bloco de Habilidades Técnicas |
| BloHpe | String(004) | Sim | Bloco de Habilidades Pessoais |
| NomArq | String(250) | Sim | Arquivo |
| DesSum | String(5000) | Sim | Descrição Sumária do Cargo |
| USU_DesDet | String(8000) | Sim | Detalhamento das Atividades do Cargo |
| USU_HabPes | String(4000) | Sim | Habilidades e Caracteristicas Pessoais do Cargo |
| USU_ResCar | String(2000) | Sim | Responsabilidades do Cargo |
| USU_CplCar | String(2000) | Sim | Complexidade do Cargo |
| USU_SupIme | String(024) | Sim | Codigo Superior Imediato |
| USU_DatRev | Date | Sim | Data de Revis?o do Cargo |
| USU_UsuRqu | Number(010,0) | Sim | Codigo do usuario que cadastrou a descric?o |
| USU_AnoEsf | String(2000) | Sim | Anotac?es (Esforco: Fisico, Intelectual, Visual) |
| USU_EsfFis | String(001) | Sim | Esforco Fisico |
| USU_EsfInt | String(001) | Sim | Esforco Intelectual |
| USU_EsfVis | String(001) | Sim | Esforco Visual |

---

## Chave Primária

- TabOrg
- NumLoc
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024ERL_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

