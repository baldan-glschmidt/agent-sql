# R005VIT

## Descrição

Vítimas do Acidente

---

## Resumo

- Campos: 17
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAci | Number(005,0) | Não | Código do Acidente |
| CodSeq | Number(002,0) | Não | Código da Sequência |
| NomVit | String(040) | Sim | Nome da Vítima |
| SexVit | String(001) | Sim | Sexo da Vítima |
| IdaVit | Number(003,0) | Sim | Idade da Vítima |
| EndVit | String(040) | Sim | Endereço da Vítima |
| TelVit | String(020) | Sim | Telefone da Vítima |
| LocTra | String(040) | Sim | Empresa em que Trabalha |
| EstCiv | Number(001,0) | Sim | Estado Civil da Vítima |
| VitFat | String(001) | Sim | Vítima Fatal |
| FilMai | Number(002,0) | Sim | Quantidade de Filhos Maiores de 18 anos |
| FilMen | Number(002,0) | Sim | Quantidade de Filhos Menores de 18 anos |
| NomCon | String(040) | Sim | Nome do Cônjuge |
| LocCon | String(040) | Sim | Empresa em que o Cônjuge Trabalha |
| IdaCon | Number(003,0) | Sim | Idade do Cônjuge |
| DddVit | Number(003,0) | Sim | Código DDD da vítima |
| DdiVit | Number(003,0) | Sim | Código DDI da vítima |

---

## Chave Primária

- CodAci
- CodSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005VIT_000

**Tabela:** R005ACI

| Origem | Destino |
|--------|---------|
| CodAci | CodAci |

