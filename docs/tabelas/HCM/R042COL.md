# R042COL

## Descrição

HomologNet - Informações Gerais

---

## Resumo

- Campos: 49
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| JorSem | Number(001,0) | Sim | Cumpriu Jornada na Semana  da Rescisão |
| SabCom | Number(001,0) | Sim | Sábado Compensado Semana Rescisão |
| For13s | Number(001,0) | Sim | Forma de Cálculo Médias 13° Salário |
| Bas13s | Number(001,0) | Sim | Apuração Cálculo 13° Salário |
| Qtd13s | Number(002,0) | Sim | Quantidade Meses 13° Salário |
| Mai13s | Number(002,0) | Sim | Maiores Meses 13° Salário |
| ForFer | Number(001,0) | Sim | Forma de Cálculo Médias Férias |
| BasFer | Number(001,0) | Sim | Apuração de Cálculo Férias |
| QtdFer | Number(002,0) | Sim | Quantidade de Meses Férias |
| MaiFer | Number(002,0) | Sim | Maiores Meses Férias |
| ForAvi | Number(001,0) | Sim | Forma de Cálculo  Aviso Prévio |
| QtdAvi | Number(002,0) | Sim | Quantidade Meses Aviso Prévio |
| DiaAvi | Number(002,0) | Sim | Quantidade de Dias de Aviso Prévio |
| MaiAvi | Number(002,0) | Sim | Maiores Meses Aviso Prévio |
| OriInf | String(001) | Sim | Origem das Informações |
| CodFil | Number(006,0) | Sim | Código da Filial |
| SinEmp | Number(015,0) | Sim | Número do CNPJ Sindicato Patronal (CEES/MTE) |
| CFJSIN | String(014) | Sim | Número do CNPJ Sindicato Patronal (CEES/MTE) |
| EntEmp | Number(012,0) | Sim | Código da Entidade Sindical Patronal |
| TipIns | Number(001,0) | Sim | Tipo de Inscrição Tomador/Obra |
| CgcCei | Number(014,0) | Sim | Número CNPJ/CEI  Tomador/Obra |
| CFJCEI | String(014) | Sim | Número CNPJ/CEI  Tomador/Obra |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | Código do Cargo do Colaborador |
| CodSin | Number(004,0) | Sim | Código do Sindicato do Colaborador |
| MesDis | Number(004,0) | Sim | Mês Data Base Sindicato (MM/DD) |
| DatAdm | Date | Sim | Data de Admissão |
| HorSem | Number(002,0) | Sim | Jornada de Trabalho Semanal em Horas |
| DatAvi | Date | Sim | Data do Aviso Prévio |
| DatDem | Date | Sim | Data da Demissão |
| DatPag | Date | Sim | Data Pagto da Rescisão |
| CauDem | String(003) | Sim | Causa da Demissão |
| TipCon | Number(001,0) | Sim | Tipo de Contrato |
| PerAvi | Number(001,0) | Sim | Perde Aviso Prévio |
| DisAvi | Number(001,0) | Sim | Dispensado do Aviso Prévio |
| PerPen | Number(004,2) | Sim | Pensão Alimentícia % - TRCT |
| PerFgt | Number(004,2) | Sim | Pensão Alimentícia  % - FGTS |
| CatEmp | Number(002,0) | Sim | Categoria do Trabalhador |
| DepIrf | Number(003,0) | Sim | Dependentes IRRF |
| DepSaf | Number(003,0) | Sim | Dependentes Sal. Família |
| FimCtt | Date | Sim | Data Fim Contrato Trabalho |
| CttPar | Number(001,0) | Sim | Contrato Tempo Parcial |
| QtdDsr | Number(001,0) | Sim | DSR no Mês de Afastamento Exceto Última Semana. |
| SalAnt | Number(011,2) | Sim | Sálario Mês Anterior Rescisão |
| TipTra | Number(001,0) | Sim | Tipo Trabalhador |
| VlrPen | Number(011,2) | Sim | Valor Pensão Alimentícia TRCT |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
