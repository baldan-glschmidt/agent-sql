# R122CRA

## Descrição

Candidatos Externos - Resultado Avaliações

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 3

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Código do Candidato |
| EstCar | Number(004,0) | Não | Código da Estrutura do Cargo |
| CodGav | Number(003,0) | Não | Código do Grupo de Avaliação |
| DatGra | Date | Não | Data da Avaliação do Grupo |
| CodIta | Number(006,0) | Não | Código do Item de Avaliação |
| CodRsp | Number(003,0) | Sim | Código do Resultado |
| CodOem | Number(008,0) | Sim | Código do Cliente da Agência de Empregos |
| AnoRsp | String(2000) | Sim | Anotações da Resposta |

---

## Chave Primária

- NumCan
- EstCar
- CodGav
- DatGra
- CodIta

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CRA_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

### IR_R122CRA_004

**Tabela:** R116GAI

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodGav | CodGav |
| CodIta | CodIta |

### IR_R122CRA_005

**Tabela:** R116ITR

| Origem | Destino |
|--------|---------|
| CodIta | CodIta |
| CodRsp | CodRsp |

