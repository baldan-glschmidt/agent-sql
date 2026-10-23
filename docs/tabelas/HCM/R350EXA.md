# R350EXA

## Descrição

S-2220 - eSocial - Monitoramento da Saúde do Trabalhador - Exames

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| SeqAso | Number(009,0) | Não | Sequência |
| SeqExa | Number(009,0) | Não | Sequência |
| DatExa | Date | Sim | Data do exame realizado |
| ProRea | Number(004,0) | Sim | Código do procedimento diagnóstico constante da Tabela 27 |
| ObsPro | String(999) | Sim | Observação sobre o procedimento diagnóstico realizado |
| OrdExa | Number(001,0) | Sim | Ordem do exame |
| IndRes | Number(001,0) | Sim | Indicação dos resultados |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |

---

## Chave Primária

- NumEmp
- FilEmp
- TipCol
- NumCad
- SeqAso
- SeqExa

---

## Índices

### R350EXAIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
