# R073HCH_AUX

## Descrição

Histórico de Crachá de Alunos - TRIGGERS

---

## Resumo

- Campos: 11
- Chave Primária: 0 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipCra | Number(001,0) | Sim | Tipo de Crachá |
| NumMat | String(015) | Sim | Matrícula do Aluno |
| DatIni | Date | Sim | Data Inicial do Histórico do Crachá |
| HorIni | Number(005,0) | Sim | Hora Inicial do Histórico de Crachá |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatFim | Date | Sim | Data Final do Histórico de Crachá |
| HorFim | Number(005,0) | Sim | Hora Final do Histórico de Crachá |
| StaAtu | Number(001,0) | Sim | Status do Histórico |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou o Crachá |
| TipOpe | Number(001,0) | Sim | Tipo de Operação (1,2,3,4) |
| CraOld | Number(012,0) | Sim | Crachá Anterior |

---

## Chave Primária

Não possui.

---

## Índices

### R073HCH_AUXIndice2

**Tipo:** Não unico

Campos:
- TipCra
- NumMat
- DatIni
- HorIni

---

## Relacionamentos

Nenhum relacionamento cadastrado.
