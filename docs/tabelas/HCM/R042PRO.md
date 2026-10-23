# R042PRO

## Descrição

HomologNet - Outros Proventos

---

## Resumo

- Campos: 17
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
| ValPro | Number(011,2) | Sim | Valor do Provento (Outros) |
| IncPro | Number(003,0) | Sim | Incidência |
| IncFGT | String(001) | Sim | Incide FGTS |
| IncINS | String(001) | Sim | Incide INSS |
| IncIRF | String(001) | Sim | Incide IRRF |
| RepBas | Number(003,0) | Sim | Integração de Base de Cálculo |
| RepFer | String(001) | Sim | Indica se a rubrica repercute no cálculo das Férias |
| Rep13s | String(001) | Sim | Indica se a rubrica repercute no cálculo do 13º Salário |
| RepRcs | String(001) | Sim | Indica se a rubrica repercute no cálculo do aviso prévio |
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

### IR_R042PRO_003

**Tabela:** R042SAL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| MesAno | MesAno |

