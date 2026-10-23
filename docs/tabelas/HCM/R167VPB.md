# R167VPB

## Descrição

BS - Pacote de Benefícios - Vales

---

## Resumo

- Campos: 13
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodPac | Number(004,0) | Não | Código do Pacote de Benefícios |
| DatIni | Date | Não | Data de início do vale |
| TabEve | Number(003,0) | Não | Código Tabela de Eventos |
| CodVal | Number(004,0) | Não | Código do Vale |
| BenCom | String(001) | Sim | Indicar se o benefício é obrigatório |
| QtdUti | Number(005,2) | Sim | Quantidade de Vales Dia Útil |
| QtdSab | Number(005,2) | Sim | Quantidade de Vales Sábado |
| QtdDom | Number(005,2) | Sim | Quantidade de Vales Domingo |
| QtdFer | Number(005,2) | Sim | Quantidade de Vales Feriado |
| PerVal | Number(005,2) | Sim | Percentual sobre o Salário |
| VlrVal | Number(011,2) | Sim | Valor Fixo do Vale |
| PerSub | Number(007,4) | Sim | Percentual de Subsídio |
| QtdVal | Number(006,2) | Sim | Quantidade de Vales |

---

## Chave Primária

- CodPac
- DatIni
- TabEve
- CodVal

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R167VPB_000

**Tabela:** R167CPB

| Origem | Destino |
|--------|---------|
| CodPac | CodPac |

### IR_R167VPB_003

**Tabela:** R044TVL

| Origem | Destino |
|--------|---------|
| TabEve | TabEve |
| CodVal | CodVal |

