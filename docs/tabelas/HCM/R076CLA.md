# R076CLA

## Descrição

Classes Salariais Tabela Salar

---

## Resumo

- Campos: 9
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEst | Number(004,0) | Não | Código da Estrutura |
| TipEst | Number(001,0) | Não | Tipo Estrutura |
| DatAlt | Date | Não | Data Alteração da Estrutura |
| SeqCla | Number(004,0) | Não | Sequência da Classe |
| ClaSal | String(005) | Sim | Classe Salarial |
| TipSis | Number(002,0) | Sim | Tipo do Sistema |
| PonCla | Number(004,0) | Sim | Número de Pontos da Classe Salarial |
| ModSal | String(001) | Sim | Modalidade da Classe Salarial |
| IndCla | Number(007,5) | Sim | Índice de Formação da Classe |

---

## Chave Primária

- CodEst
- TipEst
- DatAlt
- SeqCla

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R076CLA_000

**Tabela:** R076DES

| Origem | Destino |
|--------|---------|
| CodEst | CodEst |

