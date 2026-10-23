# R304ECO

## Descrição

e-Sfinge Online - Edital do Concurso/Processo Seletivo

---

## Resumo

- Campos: 10
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| SeqReg | Number(009,0) | Não | Sequência |
| TipEdi | Number(002,0) | Sim | Tipo de edital |
| DatVal | Date | Sim | Data da validade do concurso |
| DatPub | Date | Sim | Data da publicação do edital |
| NumCon | String(016) | Sim | Número do contrato do concurso/processo seletivo |
| UniPra | Number(001,0) | Sim | Unidade de medida utilizada para expressar o prazo de validade |
| PraVal | Number(002,0) | Sim | Tempo de vigência do concurso/processo seletivo |
| PidSta | String(030) | Sim | Pid Status |

---

## Chave Primária

- NumEmp
- NumEdi
- SeqReg

---

## Índices

### R304ECOIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
