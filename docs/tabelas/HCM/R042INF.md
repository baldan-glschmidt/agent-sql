# R042INF

## Descrição

Rescisão - Informações Adicionais

---

## Resumo

- Campos: 28
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| For13s | Number(001,0) | Sim | Forma de Cálculo Médias 13° Salário |
| Bas13s | Number(001,0) | Sim | Apuração Cálculo 13° Salário |
| Qtd13s | Number(002,0) | Sim | Quantidade Meses 13° Salário |
| Mai13s | Number(002,0) | Sim | Maiores Meses 13° Salário |
| ForFer | Number(001,0) | Sim | Forma de Cálculo Médias Férias |
| BasFer | Number(001,0) | Sim | Apuração de Cálculo Férias |
| QtdFer | Number(002,0) | Sim | Quantidade de Meses Férias |
| MaiFer | Number(002,0) | Sim | Maiores Meses Férias |
| ForAvi | Number(001,0) | Sim | Forma de Cálculo  Aviso Prévio |
| QtdAvi | Number(002,0) | Sim | Quantidade Meses Aviso Prévio |
| MaiAvi | Number(002,0) | Sim | Maiores Meses Aviso Prévio |
| DiaAvi | Number(005,2) | Sim | Quantidade de Dias de Aviso Prévio |
| DiaRea | Number(005,2) | Sim | Quantidade de Dias de Aviso Reavido |
| DepIrf | Number(002,0) | Sim | Dependentes IRRF |
| DepSaf | Number(002,0) | Sim | Dependentes Sal. Família |
| QtdDsr | Number(002,0) | Sim | DSR no Mês de Afastamento exceto última semana |
| FalDsr | Number(002,0) | Sim | Faltas Injustificadas no Mês da Rescisão Mais DSR |
| VlrIrf | Number(011,2) | Sim | Valor IR Antes Rescisão |
| AvoInd | Number(002,0) | Sim | Aviso Prévio Indenizado |
| DiaInd | Number(005,2) | Sim | Dias Indenizados |
| Prp13s | Number(002,0) | Sim | Avos 13° Salário Prop |
| TclRcs | Number(002,0) | Sim | Tipo do Evento Férias Proporcionais |
| DsiMen | Number(011,2) | Sim | Dedução IR Simplificado Mensal |
| Dsim13 | Number(011,2) | Sim | Dedução IR Simplificado 13º Salário |
| DsiFer | Number(011,2) | Sim | Dedução IR Simplificado Férias |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042INF_002

**Tabela:** R042RCM

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

