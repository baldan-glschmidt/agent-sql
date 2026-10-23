# R124HEC

## Descrição

Colaborador - Emprego Anterior(Cargos)

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo de Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqAdm | Number(002,0) | Não | Sequência da Admissão na Data |
| DatCar | Date | Não | Data Alteração do Cargo |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo |
| TitCar | String(100) | Sim | Título do Cargo |
| ComCar | String(2000) | Sim | Comentário |
| TpoCar | Number(003,0) | Sim | Tempo de Ocupação do Cargo, em meses |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqAdm
- DatCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124HEC_003

**Tabela:** R124HEA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| SeqAdm | SeqAdm |

### IR_R124HEC_006

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

