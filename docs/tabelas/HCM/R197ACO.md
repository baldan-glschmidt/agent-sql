# R197ACO

## Descrição

Cenário - Admissões Coletivas - Colaboradores

---

## Resumo

- Campos: 13
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodCen | Number(004,0) | Não | Código do cenário |
| CodCcu | String(018) | Não | Código do Centro de Custo |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| CmpQua | Date | Não | Data do Quadro |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| TipCon | Number(002,0) | Sim | Tipo de Contrato padrão para admissões coletivas |
| CodEsc | Number(009,0) | Sim | Código padrão da escala para admissões |
| FilAdm | Number(006,0) | Sim | Código da filial padrão para admissões coletivas do cenário |
| ValSal | Number(013,4) | Sim | Salário de admissão utilizado nas admissões coletivas do cenário |
| CodMot | Number(003,0) | Sim | Motivo da admissão do colaborador no cenário |

---

## Chave Primária

- NumEmp
- CodCen
- CodCcu
- EstCar
- CodCar
- CmpQua
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R197ACO_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R197ACO_002

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R197ACO_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

