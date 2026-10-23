# R110HSN

## Descrição

Ficha Médica - Subnormalidades

---

## Resumo

- Campos: 10
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodFic | Number(009,0) | Não | Código da Ficha Médica |
| DatIni | Date | Não | Data início da subnormalidade |
| CodSun | Number(006,0) | Não | Código da subnormalidade |
| DatTer | Date | Sim | Data término(encerramento) da subnormalidade |
| ObsSun | String(500) | Sim | Observação sobre a subnormalidade |
| CodPar | Number(003,0) | Sim | Código do Parecer |
| DatAco | Date | Sim | Data do último acompanhamento |
| CodCon | Number(002,0) | Sim | Código da tabela de controle do nível de atenção |
| NivAte | Number(002,0) | Sim | Código do nível de atenção |

---

## Chave Primária

- NumEmp
- CodFic
- DatIni
- CodSun

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110HSN_001

**Tabela:** R110FIC

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |

### IR_R110HSN_003

**Tabela:** R110SUN

| Origem | Destino |
|--------|---------|
| CodSun | CodSun |

