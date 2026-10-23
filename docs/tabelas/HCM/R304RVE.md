# R304RVE

## Descrição

e-Sfinge Online - Reserva de Vagas Especiais do Concurso/Processo Seletivo

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumEdi | String(016) | Não | Número do edital de concurso |
| TipRes | Number(002,0) | Não | Tipo de reserva de vaga |
| SeqReg | Number(009,0) | Não | Sequência |
| PerRes | Number(005,2) | Sim | Percentual de vagas reservadas |
| PidSta | String(030) | Sim | Pid status |

---

## Chave Primária

- NumEmp
- NumEdi
- TipRes
- SeqReg

---

## Índices

### R304RVEIndice1

**Tipo:** Não unico

Campos:
- PidSta

---

## Relacionamentos

Nenhum relacionamento cadastrado.
