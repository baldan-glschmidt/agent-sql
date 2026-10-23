# R024HIS

## Descrição

Histórico de Informações Salariais do Cargo

---

## Resumo

- Campos: 21
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Código do Cargo |
| DatIni | Date | Não | Data de Início do Histórico Informações do Cargo |
| EstSal | Number(004,0) | Sim | Estrutura salarial |
| ClaIni | String(005) | Sim | Classe/Nível Inicial do Cargo |
| NivIni | String(005) | Sim | Nível inicial |
| ClaFim | String(005) | Sim | Classe/Nível Final do Cargo |
| NivFim | String(005) | Sim | Nível final |
| ClaIns | String(005) | Sim | Classe/Nível  Instrução do Cargo |
| NivIns | String(005) | Sim | Nível Limite Instrução |
| TipSal | Number(001,0) | Sim | Tipo de Salário |
| GraIns | Number(002,0) | Sim | Grau de Instrução |
| TipExp | String(001) | Sim | Tipo Experiência (anos/meses) |
| ExpCar | Number(002,0) | Sim | Experiência |
| QtdPon | Number(004,0) | Sim | Quantidade de Pontos |
| USU_CarProII | String(024) | Sim | Cargo Progressão II |
| USU_CarProI | String(024) | Sim | Cargo Progressão I |
| USU_CarGen | String(060) | Sim | Cargo Genérico |
| USU_OrdCar | String(060) | Sim | Ordenação |
| USU_ClaInt | String(005) | Sim | Classe Intermediario |
| USU_NivInt | String(005) | Sim | Nivel Intermediario |

---

## Chave Primária

- EstCar
- CodCar
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024HIS_000

**Tabela:** R024EST

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |

### IR_R024HIS_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

