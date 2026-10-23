# R146PRM

## Descrição

Provisão - Mestre

---

## Resumo

- Campos: 15
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| MesAno | Date | Não | Competência Provisões |
| TipPrv | Number(004,0) | Não | Tipo de Provisão |
| SeqPrv | Number(001,0) | Não | Sequência Para Saldo Transferido |
| OriPrv | String(001) | Sim | Origem dos Valores da Provisão |
| CodCcu | String(018) | Sim | Código Centro Custo Contábil |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| EmpAnt | Number(004,0) | Sim | Código da Empresa Antes da Transferência |
| CadAnt | Number(009,0) | Sim | Cadastro do Colaborador Antes da Transferência |
| TipTrf | Number(001,0) | Sim | Tipo da Transferência |
| MatMes | Number(005,0) | Sim | Dias em auxílio maternidade no mês |
| MatAno | Number(005,0) | Sim | Dias em auxílio maternidade no ano |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- MesAno
- TipPrv
- SeqPrv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R146PRM_004

**Tabela:** R146DEF

| Origem | Destino |
|--------|---------|
| TipPrv | TipPrv |

