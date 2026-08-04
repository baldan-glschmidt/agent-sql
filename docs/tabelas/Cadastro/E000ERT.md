# E000ERT

## Descrição

Tabelas - Integrações autenticador externo - Cancelamento de renegociacao

---

## Resumo

- Campos: 12
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqReg | Number(009,0) | Não | Número sequencial dos registros de integração |
| CodEmp | Number(004,0) | Não | Código da empresa |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| SitExp | String(001) | Sim | Situação do processamento da pendência de integração |
| ChvLot | String(024) | Sim | Chave do lote de baixa |
| DatExp | Date | Sim | Data da exportação |
| HorExp | Number(005,0) | Sim | Hora da exportacao do registro |
| CodFil | Number(005,0) | Não | Código da filial |
| NumTit | String(015) | Não | Número do título a receber |
| CodTpt | String(003) | Não | Código do tipo de título a receber |
| CodCli | Number(009,0) | Não | Código do cliente |

---

## Chave Primária

- SeqReg

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
