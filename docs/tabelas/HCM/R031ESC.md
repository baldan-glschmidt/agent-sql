# R031ESC

## Descrição

Geração de Escalas - Escalas em Definição

---

## Resumo

- Campos: 22
- Chave Primária: 7 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEqp | Number(004,0) | Não | Código da Equipe |
| CodTur | Number(001,0) | Não | Código do Turno |
| CodCat | Number(003,0) | Não | Código da Categoria |
| DatCmp | Date | Não | Data Competência |
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| LisSib | String(125) | Sim | Lista de Símbolos |
| ColReg | String(010) | Sim | Regime de Trabalho |
| PrvFPM | Number(002,0) | Sim | Previsto - Quantidade de Folgas no Mês |
| PrvTPM | Number(002,0) | Sim | Previsto - Quantidade de Trabalhos no Mês |
| PrvPAC | Number(002,0) | Sim | Previsto - Mínimo Preferências Atendidas Dia Útil |
| PrvFSF | Number(002,0) | Sim | Previsto - Número Mínimo Finais Semana Folga |
| PrvDFo | Number(002,0) | Sim | Previsto - Número Mínimo de Domingos de Folga |
| PrvFFe | Number(002,0) | Sim | Previsto - Número Mínimo de Folgas em Feriados |
| ReaFPM | Number(002,0) | Sim | Realizado - Quantidade de Folgas no Mês |
| ReaTPM | Number(002,0) | Sim | Realizado - Quantidade de Trabalhos no Mês |
| ReaPAC | Number(002,0) | Sim | Realizado - Mínimo Preferências Atendidas Dia Útil |
| ReaFSF | Number(002,0) | Sim | Realizado - Número Mínimo Finais Semana Folga |
| ReaDFo | Number(002,0) | Sim | Realizado - Número Mínimo de Domingos de Folga |
| ReaFFe | Number(002,0) | Sim | Realizado - Número Mínimo de Folgas em Feriados |
| ColObs | String(030) | Sim | Observação |

---

## Chave Primária

- CodEqp
- CodTur
- CodCat
- DatCmp
- NumEmp
- TipCol
- NumCad

---

## Índices

### R031ESCIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad
- DatCmp

---

## Relacionamentos

### IR_R031ESC_000

**Tabela:** R031EQP

| Origem | Destino |
|--------|---------|
| CodEqp | CodEqp |

### IR_R031ESC_002

**Tabela:** R031CAT

| Origem | Destino |
|--------|---------|
| CodCat | CodCat |

