# R197PCO

## Descrição

Cenário - Promoções Coletivas - Colaboradores

---

## Resumo

- Campos: 12
- Chave Primária: 9 campo(s)
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
| SeqPro | Number(003,0) | Não | Sequência dos registros de promoções |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| OriPro | Number(001,0) | Sim | Origem da promoção |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| CarDes | String(024) | Sim | Código do cargo de destino |

---

## Chave Primária

- NumEmp
- CodCen
- CodCcu
- EstCar
- CodCar
- CmpQua
- SeqPro
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R197PCO_001

**Tabela:** R195CEN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCen | CodCen |

### IR_R197PCO_002

**Tabela:** R018CCU

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodCcu | CodCcu |

### IR_R197PCO_004

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

