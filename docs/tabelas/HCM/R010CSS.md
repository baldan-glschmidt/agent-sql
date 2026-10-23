# R010CSS

## Descrição

Base de Cálculo do Saldo de Situações

---

## Resumo

- Campos: 6
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodSal | Number(002,0) | Não | Código do Saldo |
| CodSit | Number(003,0) | Não | Código da Situação |
| SinSit | String(001) | Não | Sinal da Situação |
| UsoSit | Number(001,0) | Não | Uso Situação |
| MaiMen | String(001) | Sim | Maior/Menor que o Limite |
| LimHor | Number(010,0) | Sim | Limite de Horas da Situação |

---

## Chave Primária

- CodSal
- CodSit
- SinSit
- UsoSit

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R010CSS_000

**Tabela:** R010CSA

| Origem | Destino |
|--------|---------|
| CodSal | CodSal |

### IR_R010CSS_001

**Tabela:** R010SIT

| Origem | Destino |
|--------|---------|
| CodSit | CodSit |

