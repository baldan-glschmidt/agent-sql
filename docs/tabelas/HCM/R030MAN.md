# R030MAN

## Descrição

Comissão de Empregados - Mandatos

---

## Resumo

- Campos: 26
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodMan | Number(004,0) | Não | Código do Mandato |
| DesMan | String(080) | Sim | Descrição do Mandato |
| DatIni | Date | Sim | Data de Início do Mandato |
| DatTer | Date | Sim | Data de Término do Mandato |
| QtdMem | Number(003,0) | Sim | Quantidade de Membros |
| EdiCon | Number(004,0) | Sim | Número do Edital de Convocação |
| DatCon | Date | Sim | Data de Convocação |
| DtInIn | Date | Sim | Data de Início das Inscrições |
| HrInIn | Number(005,0) | Sim | Horário de Início das Inscrições |
| DtTeIn | Date | Sim | Data de Término das Inscrições |
| HrTeIn | Number(005,0) | Sim | Horário de Término das Inscrições |
| LocIns | String(100) | Sim | Local das Inscrições |
| DtInEl | Date | Sim | Data de Início da Eleição |
| HrInEl | Number(005,0) | Sim | Horário de Início da Eleição |
| DtTeEl | Date | Sim | Data de Término da Eleição |
| HrTeEl | Number(005,0) | Sim | Horário de Término da Eleição |
| LocEle | String(060) | Sim | Local da Eleição |
| ObsEle | String(1000) | Sim | Observações da Eleição |
| DatPos | Date | Sim | Data da Posse |
| HorPos | Number(005,0) | Sim | Hora da Posse |
| LocPos | String(100) | Sim | Local da Posse |
| ObsPos | String(1000) | Sim | Observações da Posse |
| QtdVot | Number(005,0) | Sim | Quantidade de votantes na eleição |
| VotBra | Number(004,0) | Sim | Quantidade de votos em branco |
| VotNul | Number(004,0) | Sim | Quantidade de votos nulos |

---

## Chave Primária

- NumEmp
- CodMan

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
