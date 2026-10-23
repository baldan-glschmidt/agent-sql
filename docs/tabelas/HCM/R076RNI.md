# R076RNI

## Descrição

Requisitos dos Níveis

---

## Resumo

- Campos: 17
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodEst | Number(004,0) | Não | Código da Estrutura |
| TipSis | Number(002,0) | Não | Tipo do Sistema |
| ClaSal | String(005) | Não | Classe Salarial |
| NivSal | String(005) | Não | Nível Salarial |
| PerMht | Number(005,2) | Sim | % Multihabilidade Time |
| PerPft | Number(005,2) | Sim | % Performance Time |
| PerExt | Number(005,2) | Sim | % Excelência Time |
| PerApt | Number(005,2) | Sim | % Aperfeiçoamento Time |
| PerFmt | Number(005,2) | Sim | % Formação Time |
| PerCnt | Number(005,2) | Sim | % Conhecimento Time |
| PerMhc | Number(005,2) | Sim | % Multihabilidade Carreira |
| PerPfc | Number(005,2) | Sim | % Performance Carreira |
| PerExc | Number(005,2) | Sim | % Excelência Carreira |
| PerApc | Number(005,2) | Sim | % Aperfeiçoamento Carreira |
| PerFmc | Number(005,2) | Sim | % Formação Carreira |
| PerCnc | Number(005,2) | Sim | % Conhecimento Carreira |

---

## Chave Primária

- NumEmp
- CodEst
- TipSis
- ClaSal
- NivSal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R076RNI_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R076RNI_001

**Tabela:** R076DES

| Origem | Destino |
|--------|---------|
| CodEst | CodEst |

