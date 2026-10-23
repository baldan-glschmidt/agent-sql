# R035EXA

## Descrição

PPP - Exames médicos

---

## Resumo

- Campos: 14
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqReg | Number(004,0) | Não | Sequência do registro |
| DatExa | Date | Sim | Data do Exame |
| OriExa | String(015) | Sim | Tipo do Exame |
| NatExa | String(070) | Sim | Descrição da Natureza do Exame |
| TipExa | String(001) | Sim | Tipo do Exame (Referencial/Sequêncial) |
| NorAlt | String(001) | Sim | Resultado do exame(N-Normal/A-Alterado) |
| EvoRes | String(001) | Sim | Evolução resultado(E-Estável/A-Agravamento) |
| SitRes | String(001) | Sim | Situação do resultado(O-Ocupacional/N-Não Ocupacional) |
| SitRPP | Number(001,0) | Sim | Situação do Registro |
| IgnReg | String(001) | Sim | Define se o registro será ignorado na emissão do PPP |
| IndCon | String(001) | Sim | Apresenta se o registro está em conflito com outro |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
