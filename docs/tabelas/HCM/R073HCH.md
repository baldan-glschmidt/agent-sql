# R073HCH

## Descrição

Histórico de Crachá de Alunos

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 3
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| TipCra | Number(001,0) | Não | Tipo de Crachá |
| NumMat | String(015) | Não | Matrícula do Aluno |
| DatIni | Date | Não | Data Inicial do Histórico do Crachá |
| HorIni | Number(005,0) | Não | Hora Inicial do Histórico de Crachá |
| NumCra | Number(012,0) | Sim | Número do Crachá |
| DatFim | Date | Sim | Data Final do Histórico de Crachá |
| HorFim | Number(005,0) | Sim | Hora Final do Histórico de Crachá |
| StaAtu | Number(001,0) | Sim | Status do Histórico |
| CodUsu | Number(010,0) | Sim | Código do Usuário que Cadastrou o Crachá |
| CraEnt | String(001) | Sim | Crachá provisório entregue |

---

## Chave Primária

- TipCra
- NumMat
- DatIni
- HorIni

---

## Índices

### R073HCHIndice2

**Tipo:** Não unico

Campos:
- NumCra
- DatFim

### R073HCHIndice3

**Tipo:** Não unico

Campos:
- NumCra
- DatIni

### R073HCHIndice4

**Tipo:** Não unico

Campos:
- TipCra
- NumMat
- DatIni
- HorIni
- NumCra

---

## Relacionamentos

### IR_R073HCH_001

**Tabela:** R073ALU

| Origem | Destino |
|--------|---------|
| NumMat | NumMat |

