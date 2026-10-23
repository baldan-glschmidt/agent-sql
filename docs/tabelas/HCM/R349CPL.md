# R349CPL

## Descrição

S-5002 - eSocial - Informações complementares

---

## Resumo

- Campos: 10
- Chave Primária: 6 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa |
| FilEmp | Number(006,0) | Não | Código da Filial Empregadora |
| PerApu | Date | Não | Período Apuração |
| CpfTra | Number(011,0) | Não | CPF do trabalhador |
| SeqTab | Number(009,0) | Não | Sequência |
| SeqCpl | Number(009,0) | Não | Sequência |
| DatLau | Date | Sim | Data da moléstia grave atribuída pelo laudo |
| PidExc | String(050) | Sim | Identificador da execução da pendência para consultar retorno recibo |
| PerAju | Date | Não | perApur do S-1210 cujo infoIRComplem será alterado |
| NrReOr | String(023) | Sim | Recibo do S-1210 original cujas informações de infoIRComplem serão alteradas |

---

## Chave Primária

- NumEmp
- FilEmp
- PerApu
- CpfTra
- SeqTab
- SeqCpl

---

## Índices

### R349CPLIndice1

**Tipo:** Não unico

Campos:
- PidExc

---

## Relacionamentos

Nenhum relacionamento cadastrado.
