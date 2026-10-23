# R017SAL

## Descrição

Postos de Trabalho - Salários

---

## Resumo

- Campos: 20
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstPos | Number(003,0) | Não | Código da estrutura de postos de trabalho |
| PosTra | String(024) | Não | Código do Posto de Trabalho |
| DatAlt | Date | Não | Data da alteração da estrutura salarial por posto |
| EstSal | Number(004,0) | Sim | Estrutura salarial |
| ClaIni | String(005) | Sim | Classe/Nível Inicial do Posto |
| NivIni | String(005) | Sim | Nível inicial |
| ClaFim | String(005) | Sim | Classe/Nível Final do Posto |
| NivFim | String(005) | Sim | Nível final |
| ClaIns | String(005) | Sim | Classe/Nível Instrução do Posto |
| NivIns | String(005) | Sim | Nível Final Instrução |
| TipSal | Number(001,0) | Sim | Tipo de Salário |
| PerIns | Number(005,2) | Sim | % Insalubridade |
| PerPer | Number(005,2) | Sim | % Periculosidade |
| FatTph | Number(004,2) | Sim | Fator Tempo Serviço p/ Homens |
| FatTpm | Number(004,2) | Sim | Fator Tempo Serviço p/ Mulheres |
| ApoEsp | Number(002,0) | Sim | Número de Anos p/ Aposentadoria Especial |
| GraIns | Number(002,0) | Sim | Grau de Instrução |
| TipExp | String(001) | Sim | Tipo Experiência (anos/meses) |
| ExpCar | Number(002,0) | Sim | Experiência |
| QtdPto | Number(004,0) | Sim | Quantidade de pontos |

---

## Chave Primária

- EstPos
- PosTra
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R017SAL_000

**Tabela:** R017EST

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |

### IR_R017SAL_001

**Tabela:** R017POS

| Origem | Destino |
|--------|---------|
| EstPos | EstPos |
| PosTra | PosTra |

