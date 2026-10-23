# R034PPP

## Descrição

PPP Rubi - Colaborador

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
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatIni | Date | Não | Data do início da atividade do colaborador |
| DatFim | Date | Sim | Data final da atuação do colaborador |
| NomLoc | String(060) | Sim | Descrição do Local |
| TitCar | String(100) | Sim | Título do  Cargo |
| DesReq | String(300) | Sim | Descrição do requisito |
| CodCbo | String(005) | Sim | Cbo do Cargo |
| CodCb2 | String(006) | Sim | Cbo 2002 do Cargo |
| CodGfi | Number(002,0) | Sim | Código de GFIP |
| LocFun | String(030) | Sim | Local onde é exercido cargo de comando |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
