# R042RUB

## Descrição

HomologNet - Rubricas

---

## Resumo

- Campos: 14
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| MesAno | Date | Não | Mes/Ano do Salário |
| RubHom | Number(003,0) | Não | Rubrica HomologNet |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(005,0) | Não | Código do Evento |
| SeqPro | String(020) | Sim | Código Sequencial do Produto |
| ValRub | Number(011,2) | Sim | Valor da Rubrica |
| BasCal | Number(011,2) | Sim | Base de Cálculo |
| QtdPro | Number(009,2) | Sim | Quantidade de Produtos Produzidos, Remuneração Por Produção |
| PerRub | Number(005,2) | Sim | Percentual Rubrica |
| DiaHor | Number(011,2) | Sim | Quantidade de Dias ou Horas |
| CodHom | Number(003,0) | Sim | Código HomologNet |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MesAno
- RubHom
- TabEve
- CodEve

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042RUB_003

**Tabela:** R042SAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| MesAno | MesAno |

