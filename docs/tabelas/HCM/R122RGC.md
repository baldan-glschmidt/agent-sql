# R122RGC

## Descrição

Candidato- Resultado de Cálculo Cargo

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
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

- NumCan
- DatSol
- EstCar
- CodCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122RGC_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122RGC_003

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

