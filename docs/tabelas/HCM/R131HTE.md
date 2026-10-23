# R131HTE

## Descrição

Histórico Testes - Habilidades

---

## Resumo

- Campos: 18
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatIni | Date | Não | Data de Início do Teste |
| HorIni | Number(005,0) | Não | Hora de Início do Teste |
| DatTer | Date | Sim | Data de Término do Teste |
| HorTer | Number(005,0) | Sim | Hora de Término do Teste |
| AmpTes | String(001) | Sim | OBSOLETO 5.4.1.39 - Amplitude do Teste |
| CodHte | String(006) | Sim | Código da Habilidade Técnica |
| CodTim | String(008) | Sim | OBSOLETO 5.4.1.39 - Código do Time |
| EstCar | Number(004,0) | Sim | OBSOLETO 5.4.1.39 - Código da Estrutura de Cargos |
| CodCar | String(024) | Sim | OBSOLETO 5.4.1.39 - Código do Cargo |
| TipAva | Number(001,0) | Sim | Tipo do Colaborador Avaliador |
| CadAva | Number(009,0) | Sim | Cadastro do Avaliador |
| NotDom | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - Nota do Domínio |
| PerDom | Number(005,2) | Sim | OBSOLETO 5.4.1.39 - Percentual de Domínio |
| NotTes | Number(005,2) | Sim | Nota do Teste |
| PerTes | Number(005,2) | Sim | Percentual de Teste |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- DatIni
- HorIni

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R131HTE_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

