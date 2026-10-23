# R050GER

## Descrição

Compromissos - Def. Geração

---

## Resumo

- Campos: 13
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCom | Number(004,0) | Não | Código do Compromisso |
| TipCal | Number(002,0) | Não | Tipo do Cálculo |
| TipGer | Number(001,0) | Sim | Tipo de Geração |
| DefDI1 | Number(001,0) | Sim | Definição para o Dia Inicial |
| DefDI2 | Number(001,0) | Sim | Definição para o Dia Inicial |
| SmaIni | Number(001,0) | Sim | Dia Inicial (semana) |
| DiaIni | Number(003,0) | Sim | Dia Inicial |
| MesIni | Number(002,0) | Sim | Mês Inicial |
| SmeIni | Number(001,0) | Sim | Mês Inicial no Semestre |
| SmaFim | Number(001,0) | Sim | Dia Final (semana) |
| DiaFim | Number(003,0) | Sim | Dia Final |
| MesFim | Number(002,0) | Sim | Mês Final |
| SmeFim | Number(001,0) | Sim | Mês Final no Semestre |

---

## Chave Primária

- CodCom
- TipCal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R050GER_000

**Tabela:** R050COM

| Origem | Destino |
|--------|---------|
| CodCom | CodCom |

