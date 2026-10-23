# R196MOV

## Descrição

BS - Movimento Tarefeiros

---

## Resumo

- Campos: 18
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Colaborador |
| DatMov | Date | Não | Data Movimento |
| CodTar | Number(004,0) | Não | Código da Tarefa |
| SeqMov | Number(002,0) | Não | Sequência |
| CodNuc | Number(004,0) | Sim | Código do Núcleo |
| HorIni | Number(005,0) | Sim | Hora Início |
| HorFim | Number(005,0) | Sim | Hora Final |
| CodFaz | Number(008,0) | Sim | Código da Fazenda |
| CodGle | Number(005,0) | Sim | Código da Gleba |
| CodTal | Number(004,0) | Sim | Talhão |
| CodTta | Number(003,0) | Sim | Código da Turma |
| QtdTar | Number(011,2) | Sim | Quantidade |
| VlrInf | Number(011,4) | Sim | Valor Informado da Tarefa |
| VlrTot | Number(011,4) | Sim | Valor Total da Tarefa |
| CodFis | Number(006,0) | Sim | Código do Fiscal |
| OriMov | String(001) | Sim | Origem do Movimento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatMov
- CodTar
- SeqMov

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R196MOV_004

**Tabela:** R194TAR

| Origem | Destino |
|--------|---------|
| CodTar | CodTar |

