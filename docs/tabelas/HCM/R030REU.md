# R030REU

## Descrição

Comissão de Representação - Reunião

---

## Resumo

- Campos: 12
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodMan | Number(004,0) | Não | Código do Mandato |
| DatReu | Date | Não | Data da Reunião |
| HorReu | Number(005,0) | Não | Hora de Início da Reunião |
| NumReu | Number(004,0) | Sim | Número da Reunião |
| SitReu | String(001) | Sim | Situação da Reunião |
| HorTer | Number(005,0) | Sim | Horário de Término da Reunião |
| LocReu | String(060) | Sim | Descrição do local da reunião |
| ArqAta | String(250) | Sim | Arquivo da Ata |
| AssReu | String(5000) | Sim | Assuntos da Reunião |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |

---

## Chave Primária

- NumEmp
- CodMan
- DatReu
- HorReu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
