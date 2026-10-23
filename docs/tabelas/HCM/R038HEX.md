# R038HEX

## Descrição

Histórico Exames Toxicológicos

---

## Resumo

- Campos: 21
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
| DatAlt | Date | Não | Data da solicitação do exame toxicológico |
| DatExm | Date | Sim | Data da realização do exame |
| NumExa | String(017) | Sim | Código do exame toxicológico |
| CodLab | Number(008,0) | Sim | Laboratório responsável pela realização do exame |
| NumCgc | Number(015,0) | Sim | CNPJ do laboratório responsável pela realização do exame - Obsoleto |
| CfjIns | String(014) | Sim | CNPJ do laboratório responsável pela realização do exame |
| CodAte | Number(006,0) | Sim | Código do Atendente |
| RegCon | String(020) | Sim | Registro no Conselho Profissional |
| EstCon | String(004) | Sim | UF do Conselho Profissional |
| RecExa | String(001) | Sim | Colaborador recusou-se a fazer o exame toxicológico no desligamento |
| TipExm | Number(001,0) | Sim | Tipo do exame toxicológico |
| NomMed | String(070) | Sim | Nome do Médico |
| DiaVal | Number(003,0) | Sim | Quantidade de dias de validade do exame |
| EnvEso | String(001) | Sim | Informar se deseja que o Ex. Toxicológico seja enviado através do evento S-2221 |
| CodEso | String(011) | Sim | Código do exame toxicológico no eSocial |
| ResExa | String(001) | Sim | Resultado do Exame Toxicológico |
| SorTea | Number(001,0) | Sim | Resultado do sorteio realizado pelo laboratório |
| DatSor | Date | Sim | Data do Sorteio realizado pelo Laboratório |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
