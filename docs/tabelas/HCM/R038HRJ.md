# R038HRJ

## Descrição

Histórico Redução Jornada

---

## Resumo

- Campos: 18
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data Início |
| PerRed | Number(002,0) | Sim | Percentual Redução |
| PerAco | Number(003,0) | Sim | Percentual Acordo |
| DurMes | Number(003,0) | Sim | Dias Duração |
| DatFim | Date | Sim | Data Final |
| DesTpj | String(100) | Sim | Descrição do Tipo de Jornada |
| CmpAu1 | Number(011,2) | Sim | Campo Auxiliar 1 |
| CmpAu2 | Number(011,2) | Sim | Campo Auxiliar 2 |
| CmpAu3 | Number(009,0) | Sim | Campo Auxiliar 3 |
| CmpAu4 | Number(003,0) | Sim | Campo Auxiliar 4 |
| CmpAu5 | Date | Sim | Campo Auxiliar 5 |
| CmpAu6 | Date | Sim | Campo Auxiliar 6 |
| CmpAu7 | String(001) | Sim | Campo Auxiliar 7 |
| CmpAu8 | String(300) | Sim | Campo Auxiliar 8 |
| CmpAu9 | String(100) | Sim | Campo Auxiliar 9 |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R038HRJ_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

