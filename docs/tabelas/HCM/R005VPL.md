# R005VPL

## Descrição

Viagens com Problemas

---

## Resumo

- Campos: 22
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa da Linha |
| CodLin | Number(004,0) | Não | Linha de ônibus |
| DatVia | Date | Não | Data da Viagem |
| HorVia | Number(005,0) | Não | Hora Viagem |
| VeiVia | String(010) | Sim | Inutilizado |
| NumVeP | Number(006,0) | Sim | Número do Veículo Previsto |
| DirVia | Number(001,0) | Sim | Direção da Viagem |
| SupVia | String(030) | Sim | Supervisor |
| ResAno | String(030) | Sim | Responsável pela anotação |
| ViaRea | String(001) | Sim | Viagem Realizada |
| VeiSub | String(010) | Sim | Inutilizado |
| NumVeS | Number(006,0) | Sim | Número do Veículo do Substituto |
| EmpSub | Number(004,0) | Sim | Empresa Substituto |
| TipSub | Number(001,0) | Sim | Tipo Substituto |
| CadSub | Number(009,0) | Sim | Cadastro Substituto |
| HorFim | Number(005,0) | Sim | Hora Término |
| NumNRe | Number(002,0) | Sim | Número Não Realizadas |
| MotPrb | String(2500) | Sim | Motivo Problema |
| EmpMot | Number(004,0) | Sim | Empresa Motorista |
| TipMot | Number(001,0) | Sim | Tipo Motorista |
| CadMot | Number(009,0) | Sim | Cadastro Motorista |
| EncPar | String(030) | Sim | Encaminhar Para |

---

## Chave Primária

- NumEmp
- CodLin
- DatVia
- HorVia

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
