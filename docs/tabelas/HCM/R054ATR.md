# R054ATR

## Descrição

Atrasos Carnê

---

## Resumo

- Campos: 12
- Chave Primária: 5 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| AtrOri | Number(001,0) | Não | Origem do Atraso |
| AtrIni | Date | Não | Competência Inicial do Atraso |
| AtrFim | Date | Sim | Competência Final do Atraso |
| ComPag | Date | Sim | Competência de Pagamento |
| FaiAtr | Number(002,0) | Sim | Faixa do Atraso |
| TipAtr | String(001) | Sim | Tipo do Atraso |
| PerMul | Number(005,2) | Sim | Percentual de Multa |
| AtrBas | Number(010,2) | Sim | Valor da Base do Atraso |
| AtrVal | Number(010,2) | Sim | Valor Contribuição Atraso |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- AtrOri
- AtrIni

---

## Índices

### R054ATRIndice2

**Tipo:** Unico

Campos:
- NumEmp
- AtrOri
- TipCol
- NumCad
- AtrIni

---

## Relacionamentos

### IR_R054ATR_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

