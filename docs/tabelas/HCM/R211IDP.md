# R211IDP

## Descrição

Pesquisa - Definição - Identificadores dos participantes

---

## Resumo

- Campos: 22
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPsq | Number(006,0) | Não | Código da Pesquisa |
| SeqPsq | Number(002,0) | Não | Sequência da pesquisa |
| SeqIde | Number(005,0) | Não | Sequência da identificação |
| IdePar | String(024) | Sim | Identificação do Participante na pesquisa |
| DatRes | Date | Sim | Data da Resposta do participante |
| QueCon | String(001) | Sim | Indica a situação do questionário do participante |
| NumEmp | Number(004,0) | Sim | Código da Empresa do questionado |
| TipCol | Number(001,0) | Sim | Tipo do questionado |
| CodFil | Number(006,0) | Sim | Código da Filial do Questionado |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do questionado |
| NumLoc | Number(009,0) | Sim | Local do questionado |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos do questionado |
| CodCar | String(024) | Sim | Código do Cargo do questionado |
| CodTur | Number(001,0) | Sim | Turno do questionado |
| CodCcu | String(018) | Sim | Código do Centro de Custo do questionado |
| CodHie | Number(003,0) | Sim | Código da Hierarquia do questionado |
| CodSin | Number(004,0) | Sim | Código do Sindicato do questionado |
| TipSex | String(001) | Sim | Sexo do questionado |
| PerLid | Number(005,2) | Sim | % atingido na pesquisa sobre atendimento das necessidades dos liderados |
| GraIns | Number(002,0) | Sim | Grau de Instrução |
| TabCla | Number(003,0) | Sim | Código da tabela de classificação dos participantes da pesquisa |
| IteCla | Number(003,0) | Sim | Código do item de classificação dos participantes da pesquisa |

---

## Chave Primária

- CodPsq
- SeqPsq
- SeqIde

---

## Índices

### R211IDPIndice2

**Tipo:** Não unico

Campos:
- IdePar

---

## Relacionamentos

### IR_R211IDP_001

**Tabela:** R211DEF

| Origem | Destino |
|--------|---------|
| CodPsq | CodPsq |
| SeqPsq | SeqPsq |

