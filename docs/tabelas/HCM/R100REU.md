# R100REU

## Descrição

Reuniões Cipa

---

## Resumo

- Campos: 15
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| CodMan | Number(004,0) | Não | Código do Mandato |
| DatReu | Date | Não | Data da Reunião |
| HorReu | Number(005,0) | Não | Hora da Reunião |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| TipReu | String(001) | Sim | Tipo da Reunião |
| SitReu | String(001) | Sim | Situação da Reunião |
| HorTer | Number(005,0) | Sim | Hora do Término da Reunião |
| AssReu | String(12001) | Sim | Assunto da Reunião |
| NumReu | Number(005,0) | Sim | Número de Ordem da Reunião |
| LocPos | String(060) | Sim | Descrição do local da reunião |
| NomArq | String(250) | Sim | Arquivo |
| SeqEle | Number(002,0) | Sim | Sequência da eleição |

---

## Chave Primária

- NumEmp
- CodFil
- CodMan
- DatReu
- HorReu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
