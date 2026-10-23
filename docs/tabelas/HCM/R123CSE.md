# R123CSE

## Descrição

Selecionados Triagem - Candidato - Nova

---

## Resumo

- Campos: 8
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRqu | Number(009,0) | Não | Código Requisição |
| EstCar | Number(004,0) | Não | Código da Estrutura de Cargos |
| CodCar | String(024) | Não | Cargo Requisitado |
| NumCan | Number(007,0) | Não | Número do Candidato |
| MotEli | Number(002,0) | Não | Motivo da Eliminação |
| SitCan | Number(002,0) | Sim | Situação do Candidato |
| OriSel | Number(001,0) | Sim | Origem Seleção |
| CodJus | Number(003,0) | Sim | Código da justificativa para eliminação/desistência candidato |

---

## Chave Primária

- CodRqu
- EstCar
- CodCar
- NumCan
- MotEli

---

## Índices

### R123CSEIndice2

**Tipo:** Não unico

Campos:
- CodRqu
- EstCar
- CodCar
- MotEli

---

## Relacionamentos

### IR_R123CSE_003

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

