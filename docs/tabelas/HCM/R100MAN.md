# R100MAN

## Descrição

Mandatos

---

## Resumo

- Campos: 36
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodMan | Number(004,0) | Não | Código do Mandato |
| DesMan | String(050) | Sim | Descrição do Mandato |
| DatIni | Date | Sim | Data Inicial Mandato |
| DatFim | Date | Sim | Data Final Mandato |
| QtdCip | Number(003,0) | Sim | Quantidade de Cipeiros Necessários |
| QtdSup | Number(003,0) | Sim | Quantidade de Suplentes Necessários |
| DatEle | Date | Sim | Data de Início da Eleição (Obsoleto) |
| NroEdi | Number(004,0) | Sim | Nº Edital Convocação da Eleição (Obsoleto) |
| HorIni | Number(005,0) | Sim | Hora Início da Apuração Votos (Obsoleto) |
| HorTer | Number(005,0) | Sim | Hora Término da Apuração Votos (Obsoleto) |
| QtdVot | Number(005,0) | Sim | Quantidade de Votantes na Eleição (Obsoleto) |
| OcoEle | String(4000) | Sim | Ocorrências durante a Eleição (Obsoleto) |
| DatPos | Date | Sim | Data da Posse (Obsoleto) |
| HorPos | Number(005,0) | Sim | Hora da Posse (Obsoleto) |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local da Posse |
| LocPos | String(060) | Sim | Descrição do local da posse (Obsoleto) |
| VotBra | Number(004,0) | Sim | Quantidade de votos em branco (Obsoleto) |
| VotNul | Number(004,0) | Sim | Quantidade de votos nulos (Obsoleto) |
| DatCon | Date | Sim | Data da convocação (Obsoleto) |
| DatIIn | Date | Sim | Data de início da inscrição (Obsoleto) |
| HorIIn | Number(005,0) | Sim | Hora do início da inscrição (Obsoleto) |
| DatTIn | Date | Sim | Data de término da inscrição (Obsoleto) |
| HorTIn | Number(005,0) | Sim | Hora do término da inscrição (Obsoleto) |
| HorInE | Number(005,0) | Sim | Hora do início da eleição (Obsoleto) |
| HorTeE | Number(005,0) | Sim | Hora do término da eleição (Obsoleto) |
| DatApu | Date | Sim | Data de início da apuração (Obsoleto) |
| LocApu | String(060) | Sim | Descrição do local da apuração (Obsoleto) |
| TipCip | Number(001,0) | Sim | Tipo de mandato da CIPA |
| LocEle | String(060) | Sim | Descrição do local da eleição (Obsoleto) |
| LocIns | String(060) | Sim | Descrição do local da inscrição (Obsoleto) |
| DatExt | Date | Sim | Data Extinção |
| FimEle | Date | Sim | Data Final da Eleição (Obsoleto) |
| FimApu | Date | Sim | Data final da apuração (Obsoleto) |

---

## Chave Primária

- NumEmp
- CodFil
- CodMan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R100MAN_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

