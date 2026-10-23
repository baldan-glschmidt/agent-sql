# R005TES

## Descrição

Testemunhas do Acidente

---

## Resumo

- Campos: 14
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAci | Number(005,0) | Não | Código do Acidente |
| CodSeq | Number(002,0) | Não | Código da Sequência |
| NomTes | String(040) | Sim | Nome da Testemunha |
| EndTes | String(040) | Sim | Endereço Residencial da Testemunha |
| TelTes | String(020) | Sim | Telefone Residencial da Testemunha |
| EndCom | String(040) | Sim | Endereço Comercial da Testemunha |
| TelCom | String(020) | Sim | Telefone Comercial da Testemunha |
| CepCom | Number(008,0) | Sim | CEP Comercial da Testemunha |
| PonRef | String(040) | Sim | Ponto de Referência |
| ParTes | String(2500) | Sim | Parecer da Testemunha |
| DddTes | Number(003,0) | Sim | Código DDD residencial da Testemunha |
| DddCom | Number(003,0) | Sim | Código DDD comercial da Testemunha |
| DdiTes | Number(003,0) | Sim | Código DDI residencial da Testemunha |
| DdiCom | Number(003,0) | Sim | Código DDI comercial da Testemunha |

---

## Chave Primária

- CodAci
- CodSeq

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R005TES_000

**Tabela:** R005ACI

| Origem | Destino |
|--------|---------|
| CodAci | CodAci |

