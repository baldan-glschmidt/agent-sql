# R124HRA

## Descrição

Colaborador - Resultado Avaliações

---

## Resumo

- Campos: 9
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 3

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
| CodIta | Number(006,0) | Não | Código do Item de Avaliação |
| CodRsp | Number(003,0) | Sim | Código do Resultado |
| AnoRsp | String(2000) | Sim | Anotações da Resposta |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- EstCar
- CodGav
- DatGra
- CodIta

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124HRA_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

### IR_R124HRA_006

**Tabela:** R116GAI

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodGav | CodGav |
| CodIta | CodIta |

### IR_R124HRA_007

**Tabela:** R116ITR

| Origem | Destino |
|--------|---------|
| CodIta | CodIta |
| CodRsp | CodRsp |

