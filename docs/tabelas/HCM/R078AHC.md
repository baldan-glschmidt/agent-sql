# R078AHC

## Descrição

Resultado das Avaliações - Cargo

---

## Resumo

- Campos: 21
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Código do Colaborador |
| CmpAva | Date | Não | Competência da Avaliação |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| MedExc | Number(005,2) | Sim | Média da Avaliação de Excelência |
| PerExc | Number(005,2) | Sim | % atingido na avaliação de Excelência |
| MedPrf | Number(005,2) | Sim | Média da Avaliação de Performance |
| PerPrf | Number(005,2) | Sim | % atingido na avaliação de Performance |
| MedCnc | Number(005,2) | Sim | Média da Avaliação de Conhecimentos |
| PerCnc | Number(005,2) | Sim | % atingido na avaliação de Conhecimento |
| MedDom | Number(005,2) | Sim | OBSOLETO - Média de Domínio |
| PerDom | Number(005,2) | Sim | OBSOLETO - % Médio de Domínio |
| PerApf | Number(005,2) | Sim | % de Aperfeiçoamento da Habilidade Técnica |
| PerFor | Number(005,2) | Sim | % de Formação da Habilidade Técnica |
| PerFin | Number(005,2) | Sim | % Final atingido entre Performance, Conhecimento e Excelência |
| LotRes | Number(009,0) | Sim | Número do lote em que foi gerado o Resultado |
| CodCic | Number(003,0) | Sim | Código do ciclo de avaliação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpAva
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R078AHC_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R078AHC_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

