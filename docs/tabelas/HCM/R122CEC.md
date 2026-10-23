# R122CEC

## Descrição

Candidatos Externos - Empregos Anteriores (Cargos)

---

## Resumo

- Campos: 11
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro Candidato |
| DatAdm | Date | Não | Data Admissão |
| SeqAdm | Number(002,0) | Não | Sequência da Admissão na Data |
| DatCar | Date | Não | Data Alteração do Cargo |
| CodOem | Number(008,0) | Sim | Empresa Anterior |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código Cargo |
| TitCar | String(100) | Sim | Título do Cargo |
| ComCar | String(2000) | Sim | Comentário |
| TpoCar | Number(003,0) | Sim | Tempo de Ocupação do Cargo, em meses |
| USU_NomCar | String(060) | Sim | OUTROS CARGOS |

---

## Chave Primária

- NumCan
- DatAdm
- SeqAdm
- DatCar

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R122CEC_002

**Tabela:** R122CEA

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |
| DatAdm | DatAdm |
| SeqAdm | SeqAdm |

### IR_R122CEC_006

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

