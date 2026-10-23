# R076NIV

## Descrição

Níveis da Tabela de Classe Salarial

---

## Resumo

- Campos: 21
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEst | Number(004,0) | Não | Estrutura Salarial |
| TipEst | Number(001,0) | Não | Tipo da Estrutura |
| DatAlt | Date | Não | Data de Alteração da Tabela |
| SeqCla | Number(004,0) | Não | Sequência da Classe Salarial |
| SeqNiv | Number(004,0) | Não | Sequência do Nível Salarial |
| NivSal | String(005) | Sim | Nível Salarial |
| SisNiv | Number(002,0) | Sim | Sistema do Nível |
| PonNiv | Number(004,0) | Sim | Pontuação mínima de desempenho p/estar neste Nível |
| ValSal | Number(013,4) | Sim | Salário no Nível |
| CplSal | Number(013,4) | Sim | Complemento Salário |
| NroMes | Number(002,0) | Sim | Número de Meses |
| IndNiv | Number(007,5) | Sim | Índice de Formação do Nível |
| EstBas | Number(004,0) | Sim | Estrutura Salarial Base |
| TipEBa | Number(001,0) | Sim | Tipo da Estrutura Base |
| DatEBa | Date | Sim | Data da Estrutura Base |
| SeqClB | Number(003,0) | Sim | Sequência da Classe Base |
| SeqNiB | Number(003,0) | Sim | Sequência do Nível Salarial Base |
| NivBas | String(005) | Sim | Nível Salarial Base |
| PerBas | Number(008,5) | Sim | Percentual da Est/Cla/Niv Base |
| OriSal | String(001) | Sim | Origem do Salário |
| ValSim | Number(011,2) | Sim | Sal.simulado a ser considerado no aumento/redução quadro |

---

## Chave Primária

- CodEst
- TipEst
- DatAlt
- SeqCla
- SeqNiv

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R076NIV_003

**Tabela:** R076CLA

| Origem | Destino |
|--------|---------|
| CodEst | CodEst |
| TipEst | TipEst |
| DatAlt | DatAlt |
| SeqCla | SeqCla |

