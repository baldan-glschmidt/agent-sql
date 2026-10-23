# R076PCA

## Descrição

Proposta de Alteração Cargo

---

## Resumo

- Campos: 26
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Cadastro |
| DatAlt | Date | Não | Data da Proposta |
| CodMot | Number(003,0) | Sim | Motivo da Proposta |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo Proposto |
| SitPrp | Number(001,0) | Sim | Situação da Proposta |
| OriPrp | Number(001,0) | Sim | Origem da Proposta |
| DatEfe | Date | Sim | Data da Efetivação da Proposta |
| ObsPca | String(1000) | Sim | Observação Proposta de Cargo |
| CodCrr | Number(003,0) | Sim | Código da Carreira |
| NumLot | Number(009,0) | Sim | Número do lote de geração |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| EmpRsp | Number(004,0) | Sim | Código da Empresa do Responsável |
| TipRsp | Number(001,0) | Sim | Tipo de Colaborador Responsável |
| CadRsp | Number(009,0) | Sim | Cadastro do Colaborador Responsável |
| USU_CodMot | Number(003,0) | Sim | Código do Motivo da Proposta |
| USU_EstPos | Number(003,0) | Sim | Código da Estrutura de Postos de Trabalho |
| USU_PosTra | String(024) | Sim | Código do Posto de Trabalho |
| USU_CodCcu | String(018) | Sim | Código Centro Custo Contábil |
| USU_TipDir | Number(001,0) | Sim | Tipo Diretor |
| USU_CadDir | Number(009,0) | Sim | Diretor Responsável |
| USU_RetAfa | Date | Sim | Retorno do Afastamento |
| USU_SitAfa | Number(003,0) | Sim | Situação de Afastamento |
| USU_Setor | String(030) | Sim | Setor |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R076PCA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R076PCA_004

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

### IR_R076PCA_006

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

