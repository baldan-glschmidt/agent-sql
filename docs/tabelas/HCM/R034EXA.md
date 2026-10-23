# R034EXA

## Descrição

PPP Rubi -  Exames do Colaborador

---

## Resumo

- Campos: 14
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| DatExa | Date | Não | Data exame |
| SeqExa | Number(002,0) | Não | Sequência de exame |
| TipExa | String(050) | Sim | Tipo do exame |
| DesExa | String(200) | Sim | Descrição do parecer do exame |
| ExaAud | String(001) | Sim | Identifica os exames de audiometria |
| TipAud | String(001) | Sim | Tipo de Audiometria |
| NorAlt | String(001) | Sim | Resultado do exame(N-Normal/A-Alterado) |
| EvoRes | String(001) | Sim | Evolução resultado(E-Estável/A-Agravamento) |
| SitRes | String(001) | Sim | Situação do resultado(O-Ocupacional/N-Não Ocupacional) |
| NatExa | String(050) | Sim | Natureza do exame |
| DatAso | Date | Sim | Data ASO |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatExa
- SeqExa

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
