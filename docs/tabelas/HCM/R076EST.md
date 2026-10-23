# R076EST

## Descrição

Estrutura Tabela Salários

---

## Resumo

- Campos: 11
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEst | Number(004,0) | Não | Código da Estrutura |
| TipEst | Number(001,0) | Não | Tipo da Estrutura |
| DatAlt | Date | Não | Data da Alteração da Estrutura |
| CodMot | Number(003,0) | Sim | Motivo da Alteração Salarial |
| ValEst | Number(011,2) | Sim | Valor do Índice (TipInf = 5) |
| ArrMes | Number(001,0) | Sim | Arredonda Mensalistas |
| ArrHor | Number(001,0) | Sim | Arredonda Horistas |
| AnoEst | String(250) | Sim | Anotações |
| PerRea | Number(008,5) | Sim | % de Reajuste efetuado na Estrutura Salarial |
| ValBas | Number(011,2) | Sim | Valor Base para Estrutura com Tipo Formação 4 |
| DatExt | Date | Sim | Data de Extinção da Estrutura Salarial |

---

## Chave Primária

- CodEst
- TipEst
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R076EST_000

**Tabela:** R076DES

| Origem | Destino |
|--------|---------|
| CodEst | CodEst |

### IR_R076EST_003

**Tabela:** R076MOT

| Origem | Destino |
|--------|---------|
| CodMot | CodMot |

