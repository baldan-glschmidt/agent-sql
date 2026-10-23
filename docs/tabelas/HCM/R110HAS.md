# R110HAS

## Descrição

Ficha Médica - Subnormalidades - Acompanhamento

---

## Resumo

- Campos: 9
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código Empresa |
| CodFic | Number(009,0) | Não | Código da Ficha Médica |
| DatIni | Date | Não | Data início da subnormalidade |
| CodSun | Number(006,0) | Não | Código da subnormalidade |
| DatAco | Date | Não | Data do último acompanhamento |
| ObsSun | String(500) | Sim | Observação sobre a subnormalidade |
| CodPar | Number(003,0) | Sim | Código do Parecer |
| CodCon | Number(002,0) | Sim | Código da tabela de controle do nível de atenção |
| NivAte | Number(002,0) | Sim | Código do nível de atenção |

---

## Chave Primária

- NumEmp
- CodFic
- DatIni
- CodSun
- DatAco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R110HAS_003

**Tabela:** R110HSN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFic | CodFic |
| DatIni | DatIni |
| CodSun | CodSun |

