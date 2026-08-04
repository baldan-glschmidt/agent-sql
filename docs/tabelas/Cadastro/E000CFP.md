# E000CFP

## Descrição

Tabelas - Parâmetros - Campos por forma de pagamento

---

## Resumo

- Campos: 6
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqCfp | Number(009,0) | Não | Número sequencial do registro de configuração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| CodFpg | Number(002,0) | Não | Código da forma de pagamento |
| NomCpo | String(050) | Não | Nome do Campo |
| DesCpo | String(100) | Não | Descrição do Campo |
| IndObr | String(001) | Não | Indicativo se o campo é obrigatório |

---

## Chave Primária

- SeqCfp

---

## Índices

### E000CFPIndice1

**Tipo:** Não unico

Campos:
- CodEmp
- CodFpg
- NomCpo

---

## Relacionamentos

### IR_E000CFP_001

**Tabela:** E070EMP

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |

### IR_E000CFP_002

**Tabela:** E066FPG

| Origem | Destino |
|--------|---------|
| CodEmp | CodEmp |
| CodFpg | CodFpg |

