# E000LBS

## Descrição

Tabelas - Gerais - Limpeza de base Saldos

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodAss | String(003) | Não | Assunto da limpeza de base |
| SeqLbd | Number(009,0) | Não | Sequência da limpeza de base |
| SeqLbs | Number(009,0) | Não | Sequência dos saldos da limpeza de base |
| NomLbs | String(010) | Sim | Nome livre para o assunto da limpeza |
| CodLbs | String(030) | Sim | Código livre para o assunto da limpeza |
| VlrSl1 | Number(014,5) | Sim | Valor do saldo 1 |
| VlrSl2 | Number(014,5) | Sim | Valor do saldo 2 |
| DesSl1 | String(250) | Sim | Descrição 1 |
| DesSl2 | String(250) | Sim | Descrição 2 |

---

## Chave Primária

- CodAss
- SeqLbd
- SeqLbs

---

## Índices

### E000LBSIndice2

**Tipo:** Não unico

Campos:
- CodAss
- SeqLbd
- NomLbs
- CodLbs

---

## Relacionamentos

### IR_E000LBS_001

**Tabela:** E000LBD

| Origem | Destino |
|--------|---------|
| CodAss | CodAss |
| SeqLbd | SeqLbd |

