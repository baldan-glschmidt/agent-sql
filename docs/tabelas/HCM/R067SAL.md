# R067SAL

## Descrição

Log Processamentos de Histórico Salarial

---

## Resumo

- Campos: 38
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| DtHLog | Number(014,6) | Não | Data/Hora do Log do Processamento |
| CnxUsu | Number(005,0) | Não | Número da Conexão do Usuário |
| SeqLog | Number(004,0) | Não | Sequência do Log |
| CodUsu | Number(010,0) | Sim | Código do Usuário do Processamento |
| OpeSal | Number(001,0) | Sim | Operação efetuada(1-Inclusão |
| NumEmp | Number(004,0) | Sim | Código da Empresa |
| TipCol | Number(001,0) | Sim | Tipo Colaborador |
| NumCad | Number(009,0) | Sim | Cadastro do colaborador |
| DatAlt | Date | Sim | Data da Alteração |
| SeqAlt | Number(002,0) | Sim | Sequência do reajuste |
| CodMot | Number(003,0) | Sim | Motivo da Alteração |
| CodEst | Number(004,0) | Sim | Código da Estrutura Salarial |
| ValSal | Number(013,4) | Sim | Salário Atual |
| CplSal | Number(013,4) | Sim | Valor Complementar ao Salário |
| TipSal | Number(001,0) | Sim | Tipo do Salário |
| TipEst | Number(001,0) | Sim | Tipo de Estrutura |
| ClaSal | String(005) | Sim | Classe Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| PerDes | Number(005,2) | Sim | Percentual Desempenho |
| PerRea | Number(008,5) | Sim | % de Reajuste Concedido |
| StaHis | Number(001,0) | Sim | Status do Histórico |
| CodIdm | Number(003,0) | Sim | Código da Tabela de Índices |
| SalEst | Number(013,4) | Sim | Salário atual em moeda estrangeira |
| CplEst | Number(013,4) | Sim | Valor Complementar ao Salário em moeda estrangeira |
| MotAnt | Number(003,0) | Sim | Motivo da Alteração - Anterior |
| EstAnt | Number(004,0) | Sim | Código da Estrutura Salarial Anterior |
| SalAnt | Number(013,4) | Sim | Salário Anterior |
| CplAnt | Number(013,4) | Sim | Valor Complementar ao Salário - Anterior |
| TipAnt | Number(001,0) | Sim | Tipo do Salário Anterior |
| TEsAnt | Number(001,0) | Sim | Tipo de Estrutura Anterior |
| ClaAnt | String(005) | Sim | Classe Salarial Anterior |
| NivAnt | String(005) | Sim | Nível Salarial Anterior |
| PDeAnt | Number(005,2) | Sim | Percentual Desempenho Anterior |
| PReAnt | Number(008,5) | Sim | % de Reajuste Concedido - Anterior |
| StaAnt | Number(001,0) | Sim | Status do Histórico Anterior |
| IdmAnt | Number(003,0) | Sim | Código da Tabela de Índices Ant |
| SEsAnt | Number(013,4) | Sim | Salário atual em moeda estrangeira - Anterior |
| CEsAnt | Number(013,4) | Sim | Valor Complementar ao Salário em moeda estrangeira - Anterior |

---

## Chave Primária

- DtHLog
- CnxUsu
- SeqLog

---

## Índices

### R067SALIndice2

**Tipo:** Não unico

Campos:
- NumEmp
- TipCol
- NumCad

---

## Relacionamentos

Nenhum relacionamento cadastrado.
