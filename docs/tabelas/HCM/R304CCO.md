# R304CCO

## Descrição

e-Sfinge Online - Convocação do Concurso

---

## Resumo

- Campos: 5
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| DatCon | Date | Não | Data da Convocação |
| SeqReg | Number(009,0) | Não | Sequência |
| PidSta | String(030) | Sim | Pid Status |

---

## Chave Primária

- NumEmp
- NumEdi
- DatCon
- SeqReg

---

## Índices

### R304CCOIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
