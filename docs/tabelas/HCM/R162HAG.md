# R162HAG

## Descrição

BS - Histórico Assinalamento Vale Gerado

---

## Resumo

- Campos: 17
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Número do Colaborador |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodVal | Number(004,0) | Não | Código do Tipo do Vale |
| DatSoc | Date | Não | Data Solicitação do Vale |
| DatVal | Date | Sim | Data Validade da Solicitação |
| VlrVal | Number(011,2) | Sim | Valor Fixo do Vale |
| PerSub | Number(007,4) | Sim | Percentual de Subsídio |
| QtdVal | Number(006,2) | Sim | Quantidade de Vales |
| QtdUti | Number(005,2) | Sim | Quantidade de Vales Dia Util |
| QtdSab | Number(005,2) | Sim | Quantidade de Vales Sábado |
| QtdDom | Number(005,2) | Sim | Quantidade de Vales Domingo |
| QtdFer | Number(005,2) | Sim | Quantidade de Vales Feriado |
| IniAtu | Date | Sim | Início da atuação do Colaborador no Posto de trabalho |
| SeqHis | Number(002,0) | Sim | Sequência do Histórico |
| IncExc | String(001) | Sim | Tipo de operação do registro na troca de posto de trabalho |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TabEve
- CodVal
- DatSoc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R162HAG_004

**Tabela:** R044TVL

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodVal | CodVal |

