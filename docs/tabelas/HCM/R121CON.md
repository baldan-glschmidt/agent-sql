# R121CON

## Descrição

Concurso - Definição

---

## Resumo

- Campos: 26
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| AnoCon | Number(004,0) | Não | Ano para controle de identificação do concurso |
| NumCon | Number(006,0) | Não | Número do Concurso |
| DatIni | Date | Sim | Data de início para inscrições |
| DatFim | Date | Sim | Data para encerramento das inscrições |
| HorIni | Number(005,0) | Sim | Hora de início para as inscrições |
| HorFim | Number(005,0) | Sim | Hora de encerramento para as inscrições |
| LocIns | String(420) | Sim | Definição dos locais para inscrições |
| ValIns | Number(013,4) | Sim | Valor da inscrição |
| ValCon | Number(003,0) | Sim | Validade do concurso(em meses) |
| NumEmp | Number(004,0) | Sim | Empresa do colaborador aprovador |
| TipCol | Number(001,0) | Sim | Tipo do colaborador aprovador |
| NumCad | Number(009,0) | Sim | Cadastro do colaborador aprovador |
| DatApr | Date | Sim | Data da aprovação do concurso |
| TabOrg | Number(004,0) | Sim | Código do organograma do local responsável |
| NumLoc | Number(009,0) | Sim | Local responsável pela gestão do concurso |
| TipCon | String(001) | Sim | Tipo do concurso(I-Interno/E-Externo) |
| IndVga | String(001) | Sim | Indicador de existência de vaga |
| CodSit | Number(002,0) | Sim | Código da situação do concurso |
| QtdBan | Number(003,0) | Sim | Quantidade de componentes da banca |
| ObsCon | String(1400) | Sim | Observações do Concurso |
| DatCan | Date | Sim | Data de cancelamento |
| NumEdi | String(010) | Sim | Identificação do Edital |
| DatEdi | Date | Sim | Data de publicação do Edital |
| DatCad | Date | Sim | Data de cadastramento do concurso |
| NomArq | String(250) | Sim | Link para o arquivo do edital do concurso |
| ArqPub | String(250) | Sim | Link para o arquivo da publicação do edital |

---

## Chave Primária

- AnoCon
- NumCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R121CON_017

**Tabela:** R121SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

