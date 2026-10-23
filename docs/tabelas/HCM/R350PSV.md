# R350PSV

## Descrição

S-2399 - eSocial - Trabalhador Sem Vínculo de Emprego/Estatutário - Término - Pagamentos

---

## Resumo

- Campos: 16
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| SeqRsv | Number(009,0) | Não | Sequência |
| SeqPsv | Number(009,0) | Não | Sequência |
| SeqOcs | String(010) | Sim | Seq. Outros Contratos |
| IdePag | String(030) | Sim | Identificador do pagamento |
| IndRRA | Number(001,0) | Sim | Indicativo RRA |
| TipRRA | Number(001,0) | Sim | Tipo Processo RRA |
| ProRRA | String(021) | Sim | Número Processo RRA |
| DesRRA | String(050) | Sim | Descrição Rendimentos Recebidos Acumuladamente - RRA |
| QmeRRA | Number(004,0) | Sim | Número meses relativo aos Rendimentos Recebidos Acumuladamente - RRA |
| ValCus | Number(014,2) | Sim | Valor das despesas com custas judiciais |
| ValAdv | Number(014,2) | Sim | Valor total das despesas com advogado(s) |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqRsv
- SeqPsv

---

## Índices

### R350PSVIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
