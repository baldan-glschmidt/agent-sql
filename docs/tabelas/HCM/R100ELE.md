# R100ELE

## Descrição

Mandatos - Eleições

---

## Resumo

- Campos: 28
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodMan | Number(004,0) | Não | Código do Mandato |
| SeqEle | Number(002,0) | Não | Sequência da eleição |
| DatEle | Date | Sim | Data de início da eleição |
| HorInE | Number(005,0) | Sim | Hora de início da eleição |
| FimEle | Date | Sim | Data de término da eleição |
| HorTeE | Number(005,0) | Sim | Hora de término da eleição |
| LocEle | String(060) | Sim | Descrição do local da eleição |
| NroEdi | Number(004,0) | Sim | Nº do edital de convocação da eleição |
| DatApu | Date | Sim | Data de início da apuração dos votos |
| HorIni | Number(005,0) | Sim | Hora de início da apuração dos votos |
| FimApu | Date | Sim | Data de término da apuração dos votos |
| HorTer | Number(005,0) | Sim | Hora de término da apuração dos votos |
| LocApu | String(060) | Sim | Descrição do local da apuração |
| DatCon | Date | Sim | Data da convocação |
| DatIIn | Date | Sim | Data de início da inscrição |
| HorIIn | Number(005,0) | Sim | Hora de início da inscrição |
| DatTIn | Date | Sim | Data de término da inscrição |
| HorTIn | Number(005,0) | Sim | Hora do término da inscrição |
| LocIns | String(060) | Sim | Descrição do local da inscrição |
| QtdVot | Number(005,0) | Sim | Quantidade de votantes na eleição |
| VotBra | Number(004,0) | Sim | Quantidade de votos em branco |
| VotNul | Number(004,0) | Sim | Quantidade de votos nulos |
| OcoEle | String(4000) | Sim | Ocorrências durante a eleição |
| DatPos | Date | Sim | Data da posse |
| HorPos | Number(005,0) | Sim | Hora da posse |
| LocPos | String(060) | Sim | Descrição do local da posse |

---

## Chave Primária

- NumEmp
- CodFil
- CodMan
- SeqEle

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R100ELE_002

**Tabela:** R100MAN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |
| CodMan | CodMan |

