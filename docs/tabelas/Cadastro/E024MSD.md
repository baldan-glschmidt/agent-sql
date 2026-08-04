# E024MSD

## Descrição

Tabelas - Mensagens para Nota Fiscal de Saída e Contrato de Venda - Campos dinâmicos

---

## Resumo

- Campos: 5
- Chave Primária: 1 campo(s)
- Índices: 1
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SeqMsd | Number(009,0) | Não | Sequência |
| CodMsg | Number(004,0) | Não | Código da mensagem especial para nota fiscal de saída e contrato |
| CmpRes | String(255) | Sim | Campo resultante |
| VlrSim | String(255) | Sim | Valor simulado |
| InfMsg | String(999) | Sim | Informações de compilação da mensagem |

---

## Chave Primária

- SeqMsd

---

## Índices

### E024MSDMensagem

**Tipo:** Não unico

Campos:
- CodMsg

---

## Relacionamentos

Nenhum relacionamento cadastrado.
