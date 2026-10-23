# R036PJU

## Descrição

Pensão Judicial

---

## Resumo

- Campos: 45
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo do Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodDep | Number(002,0) | Não | Código do Dependente |
| TipLgr | String(005) | Sim | Tipo de Logradouro |
| RuaDep | String(040) | Sim | Rua Endereço do Dependente |
| CodCid | Number(007,0) | Sim | Cidade do Dependente |
| CodBai | Number(004,0) | Sim | Bairro do Dependente |
| CodCep | Number(008,0) | Sim | Código do Cep do Dependente |
| NumTel | String(020) | Sim | Telefone do Dependente |
| ModPag | String(001) | Sim | Modo Pagto do Líquido |
| CodBan | Number(004,0) | Sim | Código do Banco |
| CodAge | Number(005,0) | Sim | Código da Agência |
| ConBan | Number(012,0) | Sim | Conta Bancária |
| DigBan | String(003) | Sim | Dígito Conta Banco |
| BasPju | String(001) | Sim | Tipo Base Cálculo (F,R) |
| PerPen | Number(005,2) | Sim | %  Pensão Judicial |
| ValIni | Number(011,2) | Sim | Valor Fixo Inicial |
| DatIni | Date | Sim | Data Competência Inicial |
| CodIdm | Number(003,0) | Sim | Código Tabela Índices Correção |
| DiaInd | Number(002,0) | Sim | Dia Índice Correção |
| PerCor | Number(002,0) | Sim | Periodicidade da Correção |
| CotSaf | Number(001,0) | Sim | Cotas Salário Família |
| Pag13s | String(001) | Sim | Pensão Judicial 13° Salário qdo tipo=F |
| TipFGT | String(001) | Sim | Tipo Pensão FGTS(N, V, P) |
| CciCom | Number(007,0) | Sim | Cidade da Comarca |
| CodCon | String(030) | Sim | Código da Conta Contábil |
| CodRed | Number(008,0) | Sim | Código da Conta Contábil Reduzida |
| IniPen | Date | Sim | Data de Início da Concessão |
| FimPen | Date | Sim | Data de Fim da Concessão |
| Per13s | Number(005,2) | Sim | %  Pensão 13° Salário |
| PerFer | Number(005,2) | Sim | %  Pensão nas férias |
| PerPlr | Number(005,2) | Sim | %  Pensão no PLR |
| TpCtBa | Number(001,0) | Sim | Tipo Conta |
| TipEmb | Number(001,0) | Sim | Tipo de Embargo Judicial |
| PenTer | Number(001,0) | Sim | Determina como será o desconto de pensão para terceiros. |
| TetPen | Number(011,2) | Sim | Valor máximo de pensão a ser descontado dos terceiros |
| DddTel | Number(003,0) | Sim | Código DDD do telefone |
| DdiTel | Number(003,0) | Sim | Código DDI do telefone |
| PerFgt | Number(005,2) | Sim | % Pensão FGTS |
| VlrMin | Number(011,2) | Sim | Valor mínimo pensão judicial |
| BasPen | Number(011,2) | Sim | Base de cálculo |
| ValPen | Number(011,2) | Sim | Valor calculado |
| TpcPix | Number(002,0) | Sim | Tipo de Chave Pix - Pagamento Instantâneo |
| ChvPix | String(100) | Sim | Chave Pix - Pagamento Instantâneo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R036PJU_003

**Tabela:** R036DEP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodDep | CodDep |

