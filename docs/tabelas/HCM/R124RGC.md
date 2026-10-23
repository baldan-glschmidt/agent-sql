# R124RGC

## Descrição

Colaborador - Resultado de Cálculo Cargo

---

## Resumo

- Campos: 11
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo de colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatSol | Date | Não | Data da solicitação do cálculo do cargo |
| EstCar | Number(004,0) | Não | Código da estrutura de cargos |
| CodCar | String(024) | Não | Código do cargo |
| CodUsu | Number(010,0) | Sim | Código do usuário que solicitou o teste |
| DatCal | Date | Sim | Data do cálculo do cargo |
| CodTes | Number(015,0) | Sim | Código do teste |
| NotCal | Number(007,2) | Sim | Nota final do cálculo do cargo |
| OriTes | String(001) | Sim | Origem da informação(D-Digitado, I-Integração, M-Modificado) |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatSol
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R124RGC_005

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

