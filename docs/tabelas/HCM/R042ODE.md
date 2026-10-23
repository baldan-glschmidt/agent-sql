# R042ODE

## Descrição

HomologNet - Outros Descontos

---

## Resumo

- Campos: 12
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro Empregado |
| TabEve | Number(003,0) | Não | Código da Tabela de Eventos |
| CodEve | Number(005,0) | Não | Código do Evento |
| CodDes | Number(003,0) | Não | Código da Rubrica |
| ValDes | Number(011,2) | Sim | Valor do Desconto (Outros) |
| IncDes | Number(003,0) | Sim | Incidência |
| IncFGT | String(001) | Sim | Incide FGTS |
| IncINS | String(001) | Sim | Incide INSS |
| IncIRF | String(001) | Sim | Incide IRRF |
| CodHom | Number(003,0) | Sim | Código HomologNet |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- TabEve
- CodEve
- CodDes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R042ODE_002

**Tabela:** R042DES

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

